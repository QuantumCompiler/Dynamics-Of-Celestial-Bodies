#pragma once
#include <algorithm>
#include <chrono>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <glob.h>
#include <iomanip>
#include <limits>
#include <map>
#include <memory>
#include <numeric>
#include <random>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <nlohmann/json.hpp>
#include <torch/torch.h>
#include "constants.h"
#include "models.h"
#include "solvers.h"
#include "celestial_bodies.h"
#include "utilities.h"

using json = nlohmann::json;

// -----------------------------
// Types / DTOs
// -----------------------------

// MLP implementation class (required before TORCH_MODULE macro)
struct SingleBodyMLPImpl : torch::nn::Module {
    torch::nn::Linear fc1{nullptr}, fc2{nullptr}, fc3{nullptr};

    SingleBodyMLPImpl() = default;
    SingleBodyMLPImpl(int64_t in_dim, int64_t out_dim);
    torch::Tensor forward(torch::Tensor x);
};

TORCH_MODULE(SingleBodyMLP);

struct SingleBodyStandardizer {
    torch::Tensor mean;
    torch::Tensor std;

    SingleBodyStandardizer() = default;
    SingleBodyStandardizer(torch::Tensor m, torch::Tensor s) : mean(std::move(m)), std(std::move(s)) {}

    torch::Tensor transform(const torch::Tensor& x) const;
    torch::Tensor inverse(const torch::Tensor& x) const;
};

struct SingleBodyTrajectoryData {
    std::vector<double> times;
    std::vector<double> positions;
    std::vector<double> velocities;

    double bodyMass = 0.0;
    double bodyRadius = 0.0;

    double initPosition = 0.0;
    double initVelocity = 0.0;
    double simTime = 0.0;
    double timeStep = 0.0;

    std::string csvPath;
};

struct SingleBodySplitGlobs {
    std::string trainGlob;
    std::string valGlob;
    std::string testGlob;
};

struct SingleBodySplitTrajectories {
    std::vector<std::unique_ptr<SingleBodyTrajectoryData>> trainTrajs;
    std::vector<std::unique_ptr<SingleBodyTrajectoryData>> valTrajs;
    std::vector<std::unique_ptr<SingleBodyTrajectoryData>> testTrajs;
};

struct SingleBodySplitTensors {
    torch::Tensor X_train, Y_train;
    torch::Tensor X_val,   Y_val;
    torch::Tensor X_test,  Y_test;
};

struct SingleBodyStandardizedTensors {
    torch::Tensor Xtr, Ytr;
    torch::Tensor Xva, Yva;

    SingleBodyStandardizer xStd;
    SingleBodyStandardizer yStd;

    bool scalersLoadedFromDisk = false;
};

struct SingleBodyTrainingModel {
    SingleBodyMLP model;
    std::string modelPath;
    std::string scalerPath;
};

struct SingleBodyTrainedModel {
    SingleBodyMLP model;

    int bestEpoch = -1;
    double bestTrainMse = 0.0;

    double bestValMseScaled = 0.0;
    double bestValMaeScaled = 0.0;

    double bestValMseReal = 0.0;
    double bestValMaeReal = 0.0;
};

struct SingleBodyTestResults {
    double meanRmse = 0.0;
    double stdRmse = 0.0;
    size_t numTrajectories = 0;
};

// Controls for training/eval without threading config everywhere.
struct SingleBodyTrainConfig {
    bool resumeTraining = true;
    int epochs = 25;

    bool runTestEval = false;
    bool runRolloutEval = false;

    int batchSize = 4096;

    // Optional knobs you’ve been toggling
    bool useRolloutLoss = true;
    bool computeValRolloutMetric = true;  // On by default so we catch rollout drift early
    int rolloutK = 50;  // Default eval horizon (keep modest for speed); increase to 500+ when validating final quality

    // PINN Residual Configuration
    // NN learns accel_residual; final accel = accel_physics + accel_residual
    bool useResidualPINN = true;  // Enable residual PINN mode
    float lambdaRes = 1e-4f;       // L2 regularization on residual to keep it small
    float resCap = 0.3f;           // Clamp residual as fraction of |accel_phys| (safety)
    float resCapMin = 1e-2f;       // Minimum absolute cap for residual (when accel_phys is tiny)
    float resCapFloorMin = 1e-3f;  // Absolute floor for res_cap to prevent collapse to zero

    // Gradient clipping for training stability
    float maxGradNorm = 1.0f;      // Tighter clipping improves stability with large batches

    // Learning rate (lower for rollout training)
    float learningRate = 3e-4f;    // Safer default for AdamW on large batches; can tune up if stable
};

// Single body data IO from CSV files
class SingleBodyDataIO {
    public:
        explicit SingleBodyDataIO(const std::string& bodyName = "");
        SingleBodySplitGlobs getSplitGlobs() const;
        SingleBodySplitTrajectories loadSplitTrajectories(const SingleBodySplitGlobs& globs) const;
        std::unique_ptr<SingleBodyTrajectoryData> loadTrajectory(const std::string& csvPath) const;
        std::string extractBodyNameFromPath(const std::string& csvPath) const;
        void setBodyName(const std::string& bodyName) { bodyName_ = bodyName; }
        std::string getBodyName() const { return bodyName_; }

    private:
        std::vector<std::string> globPaths(const std::string& pattern) const;
        std::string findColumn(const std::vector<std::string>& headers,
                            const std::vector<std::string>& candidates) const;
        std::filesystem::path execDir_;
        std::string bodyName_;
};

// Single body dataset building (tensors from trajectories)
// PINN-style: NN learns acceleration only; kinematics integrates state.
class SingleBodyDatasetBuilder {
    public:
        explicit SingleBodyDatasetBuilder(torch::Device device);
        std::pair<torch::Tensor, torch::Tensor> trajectoryToPairs(const SingleBodyTrajectoryData& traj,
                                                                bool useParams = true) const;
        std::pair<torch::Tensor, torch::Tensor> buildArrays(
            const std::vector<std::unique_ptr<SingleBodyTrajectoryData>>& trajs) const;
        SingleBodySplitTensors buildSplitTensors(const SingleBodySplitTrajectories& split) const;
        int64_t featureDim(bool useParams = true) const;
        int64_t targetDim() const;  // Returns 1 (acceleration only)
    private:
        torch::Device device_;
};

// Single body scaler management (fit/load/save standardizers)
class SingleBodyScalerManager {
    public:
        explicit SingleBodyScalerManager(torch::Device device);
        SingleBodyStandardizer fitStandardizer(const torch::Tensor& data) const;
        void saveScalers(const std::string& path,
                        const SingleBodyStandardizer& xStd,
                        const SingleBodyStandardizer& yStd) const;
        void loadScalers(const std::string& path,
                        SingleBodyStandardizer& xStd,
                        SingleBodyStandardizer& yStd) const;
        SingleBodyStandardizedTensors fitOrLoadAndStandardize(const SingleBodySplitTensors& splitTensors,
                                                            const std::string& scalerPath,
                                                            bool resumeTraining) const;
        bool runScalerSanityCheck(const SingleBodySplitTensors& splitTensors,
                                const SingleBodyStandardizer& xStd,
                                const SingleBodyStandardizer& yStd) const;
    private:
        torch::Device device_;
};

// Single body model trainer
// PINN-style: NN learns acceleration (or residual correction); kinematics integrates state.
class SingleBodyTrainer {
    public:
        explicit SingleBodyTrainer(torch::Device device);
        SingleBodyTrainingModel initializeModel(const SingleBodyStandardizedTensors& stdTensors,
                                            const std::string& modelPath,
                                            const std::string& scalerPath,
                                            bool resumeTraining) const;
        SingleBodyTrainedModel runTrainingLoop(SingleBodyTrainingModel& trainingModel,
                                            const SingleBodyTrainConfig& cfg,
                                            const SingleBodyStandardizedTensors& stdTensors,
                                            const SingleBodySplitTensors& splitTensors,
                                            const SingleBodySplitTrajectories& splitTrajs) const;
        
        // Compute physics-based acceleration -G*M/(R+pos)^2 using torch tensors (differentiable)
        // Used by residual PINN: accel_hat = accel_phys + accel_residual
        static torch::Tensor computePhysicsAccelTensor(const torch::Tensor& pos,
                                                        const torch::Tensor& mass,
                                                        const torch::Tensor& radius);
    protected:
        torch::Tensor multiStepRolloutLoss(SingleBodyMLP& model,
                                        const SingleBodyTrajectoryData& traj,
                                        const SingleBodyStandardizer& xStd,
                                        const SingleBodyStandardizer& yStd,
                                        const SingleBodyTrainConfig& cfg) const;
        void runTeacherForcedDebug(SingleBodyMLP& model,
                                const SingleBodyTrajectoryData& traj,
                                const SingleBodyStandardizer& xStd,
                                const SingleBodyStandardizer& yStd,
                                const SingleBodyTrainConfig& cfg) const;

        // Compute acceleration using canonical Models::singleBodySystem (CPU, for reference)
        static double computeAccelFromModels(double bodyMass, double bodyRadius, double pos, double vel);
    private:
        torch::Device device_;
};

// Single body model evaluator
// PINN-style: uses kinematics to integrate state from learned acceleration.
class SingleBodyEvaluator {
    public:
        explicit SingleBodyEvaluator(torch::Device device);
        // Rollout trajectory using kinematics: NN outputs accel (or accel_res), state updated via physics
        std::pair<torch::Tensor, torch::Tensor> rolloutTrajectory(SingleBodyMLP& model,
                                                                const SingleBodyTrajectoryData& traj,
                                                                const SingleBodyStandardizer& xStd,
                                                                const SingleBodyStandardizer& yStd,
                                                                bool useResidualPINN = true) const;
        double computeValRolloutMse(SingleBodyMLP& model,
                                    const std::vector<std::unique_ptr<SingleBodyTrajectoryData>>& valTrajs,
                                    const SingleBodyStandardizer& xStd,
                                    const SingleBodyStandardizer& yStd,
                                    int numTrajs,
                                    int K,
                                    bool useResidualPINN = true) const;
        bool evaluateTestRollouts(SingleBodyMLP& model,
                                const std::vector<std::unique_ptr<SingleBodyTrajectoryData>>& testTrajs,
                                const SingleBodyStandardizer& xStd,
                                const SingleBodyStandardizer& yStd,
                                bool useResidualPINN = true) const;
    private:
        torch::Device device_;
};

// Single body data generator
class SingleBodyDataGenerator {
    public:
        explicit SingleBodyDataGenerator(const std::string& bodyName = "");
        void generateSingleBodyData(bool generateTrain, int perTrain, int perVal, int perTest, uint32_t seed);
        void generateTrainData(int perTrain, uint32_t seed);
        void generateValData(int perVal, uint32_t seed);
        void generateTestData(int perTest, uint32_t seed);
        void generateValTestDataDisjoint(int perVal, int perTest, uint32_t seed);
        void generateTrainValTestDataDisjoint(int perTrain, int perVal, int perTest, uint32_t seed);
        void setBodyName(const std::string& bodyName) { bodyName_ = bodyName; }
        std::string getBodyName() const { return bodyName_; }
    protected:
        static std::pair<int,int> chooseGridBins(int n);
    private:
        std::string bodyName_;
        std::vector<Body> getBodiesToGenerate() const;
};

// Main single body torch model class
class SingleBodyTorchModel {
    public:
        explicit SingleBodyTorchModel(const std::string& bodyName = "");
        void train(bool resumeTraining = true);
        SingleBodySolution predict(SingleBodyIC initialConditions);
        std::string getBodyName() const { return bodyName_; }
    private:
        std::string modelPath() const;
        std::string scalerPath() const;
        std::string summaryPath() const;
        void saveTrainingSummary(const std::string& summaryPath,
                                const std::string& modelPath,
                                const std::string& scalerPath,
                                const SingleBodySplitGlobs& globs,
                                int trainCount,
                                int valCount,
                                int testCount,
                                const SingleBodyTrainConfig& cfg,
                                int best_epoch,
                                const std::map<std::string, double>& metrics) const;
        std::string bodyName_;
        torch::Device device_;
        SingleBodyDataIO dataIO_;
        SingleBodyDatasetBuilder datasetBuilder_;
        SingleBodyScalerManager scalerMgr_;
        SingleBodyTrainer trainer_;
        SingleBodyEvaluator evaluator_;
        SingleBodyDataGenerator dataGen_;
};
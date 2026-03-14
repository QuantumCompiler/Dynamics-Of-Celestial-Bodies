#include "single_body_torch.h"
#include <algorithm>
#include <chrono>
#include <filesystem>
#include <glob.h>
#include <iostream>
#include <map>
#include <random>

// Reference : https://github.com/maciejczarnacki/PINNs-projectile-motion

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
//                                                                               SingleBodyStandardizer
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

torch::Tensor SingleBodyStandardizer::transform(const torch::Tensor& x) const {
    return (x - mean) / std;
}

torch::Tensor SingleBodyStandardizer::inverse(const torch::Tensor& x) const {
    return x * std + mean;
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
//                                                                               SingleBodyMLPImpl
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PUBLIC METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

SingleBodyMLPImpl::SingleBodyMLPImpl(int64_t in_dim, int64_t out_dim) {
    fc1 = register_module("fc1", torch::nn::Linear(in_dim, 256));
    fc2 = register_module("fc2", torch::nn::Linear(256, 256));
    fc3 = register_module("fc3", torch::nn::Linear(256, out_dim));
}

torch::Tensor SingleBodyMLPImpl::forward(torch::Tensor x) {
    x = torch::relu(fc1->forward(x));
    x = torch::relu(fc2->forward(x));
    x = fc3->forward(x);
    return x;
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
//                                                                               SingleBodyDataIO
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PUBLIC METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Constructor
SingleBodyDataIO::SingleBodyDataIO(const std::string& bodyName) 
    : bodyName_(bodyName) {
    execDir_ = SystemUtilities::getExecutableDir();
}

// Get split globs for train/val/test directories
SingleBodySplitGlobs SingleBodyDataIO::getSplitGlobs() const {
    SingleBodySplitGlobs globs;
    
    // Use body-specific directories if a body name is set
    if (!bodyName_.empty()) {
        std::cout << "Using body-specific data for: " << bodyName_ << std::endl;
        globs.trainGlob = (execDir_ / UniversalConstants::getSingleBodyTrainDir(bodyName_) / "*.csv").string();
        globs.valGlob = (execDir_ / UniversalConstants::getSingleBodyValDir(bodyName_) / "*.csv").string();
        globs.testGlob = (execDir_ / UniversalConstants::getSingleBodyTestDir(bodyName_) / "*.csv").string();
    } else {
        globs.trainGlob = (execDir_ / UniversalConstants::singleBodyTrainDir / "*.csv").string();
        globs.valGlob = (execDir_ / UniversalConstants::singleBodyValDir / "*.csv").string();
        globs.testGlob = (execDir_ / UniversalConstants::singleBodyTestDir / "*.csv").string();
    }

    std::cout << "TRAIN glob: " << globs.trainGlob << std::endl;
    std::cout << "VAL   glob: " << globs.valGlob << std::endl;
    std::cout << "TEST  glob: " << globs.testGlob << std::endl;

    return globs;
}

// Load trajectories from train/val/test splits
SingleBodySplitTrajectories SingleBodyDataIO::loadSplitTrajectories(const SingleBodySplitGlobs& globs) const {
    // Get paths for each split
    auto trainPaths = globPaths(globs.trainGlob);
    auto valPaths = globPaths(globs.valGlob);
    auto testPaths = globPaths(globs.testGlob);

    std::cout << "Found " << trainPaths.size() << " TRAIN CSV files" << std::endl;
    std::cout << "Found " << valPaths.size() << " VAL CSV files" << std::endl;
    std::cout << "Found " << testPaths.size() << " TEST CSV files" << std::endl;

    // Helper to load trajectories from paths
    auto loadFromPaths = [&](const std::vector<std::string>& paths) {
        std::vector<std::unique_ptr<SingleBodyTrajectoryData>> out;
        out.reserve(paths.size());
        for (const auto& path : paths) {
            auto traj = loadTrajectory(path);
            if (traj) {
                out.push_back(std::move(traj));
            }
        }
        return out;
    };

    SingleBodySplitTrajectories split;
    split.trainTrajs = loadFromPaths(trainPaths);
    split.valTrajs = loadFromPaths(valPaths);
    split.testTrajs = loadFromPaths(testPaths);

    return split;
}

// Load a single trajectory from a CSV file
std::unique_ptr<SingleBodyTrajectoryData> SingleBodyDataIO::loadTrajectory(const std::string& csvPath) const {
    // Use existing CSV utilities
    SingleBodyIC initialConditions;
    SingleBodySolution rk4Solution;

    if (!CSVUtilities::readSingleBodySimDataCSV(csvPath, initialConditions, rk4Solution)) {
        return nullptr;
    }

    // Check if we have valid data
    if (rk4Solution.times.size() < 2) {
        return nullptr;
    }

    // Convert to SingleBodyTrajectoryData
    auto traj = std::make_unique<SingleBodyTrajectoryData>();
    traj->csvPath = csvPath;
    traj->times = rk4Solution.times;
    traj->positions = rk4Solution.positions;
    traj->velocities = rk4Solution.velocities;
    traj->bodyMass = initialConditions.bodyMass;
    traj->bodyRadius = initialConditions.bodyRadius;
    traj->initPosition = initialConditions.initialPosition;
    traj->initVelocity = initialConditions.initialVelocity;
    traj->simTime = initialConditions.timeSpan;
    traj->timeStep = initialConditions.timeStep;

    return traj;
}

// Extract body name from CSV path
std::string SingleBodyDataIO::extractBodyNameFromPath(const std::string& csvPath) const {
    // Try to extract body name from CSV path
    // Expected patterns: .../Mercury/... or filename contains body name
    std::vector<std::string> bodies = {
        "Sun", "Mercury", "Venus", "Earth", "Mars",
        "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"
    };

    for (const auto& body : bodies) {
        if (csvPath.find(body) != std::string::npos) {
            return body;
        }
    }

    return "Unknown";
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PRIVATE METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Get paths matching a glob pattern
std::vector<std::string> SingleBodyDataIO::globPaths(const std::string& pattern) const {
    glob_t globbuf;
    std::vector<std::string> paths;
    if (glob(pattern.c_str(), 0, nullptr, &globbuf) == 0) {
        for (size_t i = 0; i < globbuf.gl_pathc; ++i) {
            paths.push_back(globbuf.gl_pathv[i]);
        }
        globfree(&globbuf);
    }
    std::sort(paths.begin(), paths.end());
    return paths;
}

// Find a column in headers by matching against candidates
std::string SingleBodyDataIO::findColumn(const std::vector<std::string>& headers,
                                        const std::vector<std::string>& candidates) const {
    // Create lowercase map
    std::map<std::string, std::string> headerMap;
    for (const auto& h : headers) {
        std::string lower = h;
        std::transform(lower.begin(), lower.end(), lower.begin(), ::tolower);
        headerMap[lower] = h;
    }

    // Search for candidates
    for (const auto& cand : candidates) {
        std::string lower = cand;
        std::transform(lower.begin(), lower.end(), lower.begin(), ::tolower);
        if (headerMap.count(lower)) {
            return headerMap[lower];
        }
    }
    return "";
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
//                                                                               SingleBodyDatasetBuilder
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PUBLIC METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Constructor
SingleBodyDatasetBuilder::SingleBodyDatasetBuilder(torch::Device device)
    : device_(device) {}

// Return feature dimension based on whether params are included
int64_t SingleBodyDatasetBuilder::featureDim(bool useParams) const {
    // Base features: [pos_t, vel_t, t_norm, dt] = 4
    // With params: + [bodyMass, bodyRadius, initPosition, initVelocity, simTime] = 5
    // Total with params: 9
    int64_t dim = 4;
    if (useParams) {
        dim += 5;
    }
    return dim;
}

// Return target dimension (acceleration only - PINN-style)
// NN learns acceleration; kinematics integrates state.
int64_t SingleBodyDatasetBuilder::targetDim() const {
    return 1;  // [accel] - single value
}

// Convert a single trajectory to (X, Y) training pairs
std::pair<torch::Tensor, torch::Tensor> SingleBodyDatasetBuilder::trajectoryToPairs(
    const SingleBodyTrajectoryData& traj,
    bool useParams) const {
    
    int n = static_cast<int>(traj.times.size()) - 1;
    
    // Handle edge case: not enough data points
    if (n < 1) {
        auto opts = torch::TensorOptions().dtype(torch::kFloat32).device(device_);
        return {torch::empty({0, featureDim(useParams)}, opts),
                torch::empty({0, targetDim()}, opts)};
    }

    // Calculate dt array
    std::vector<float> dts(n);
    for (int i = 0; i < n; ++i) {
        dts[i] = static_cast<float>(traj.times[i + 1] - traj.times[i]);
    }

    // Prepare feature dimensions
    // Features per step:
    //   [pos_t, vel_t, t_norm, dt, bodyMass, bodyRadius, initPosition, initVelocity, simTime]
    int featDim = 4; // pos, vel, t_norm, dt
    if (useParams) {
        featDim += 5; // + mass, radius, initPosition, initVelocity, simTime
    }

    // Create data vectors
    // PINN-style: Y is acceleration only (1-D), not [dpos, dvel]
    std::vector<float> X_data;
    std::vector<float> Y_data;
    X_data.reserve(n * featDim);
    Y_data.reserve(n);  // 1 value per sample (acceleration)

    for (int i = 0; i < n; ++i) {
        // Input features per step:
        // [pos_t, vel_t, t_norm, dt, bodyMass, bodyRadius, initPosition, initVelocity, simTime]
        const float simTime = static_cast<float>(traj.simTime);
        const float tNorm = (simTime > 0.0f) ? (static_cast<float>(traj.times[i]) / simTime) : 0.0f;

        X_data.push_back(static_cast<float>(traj.positions[i]));
        X_data.push_back(static_cast<float>(traj.velocities[i]));
        X_data.push_back(tNorm);
        X_data.push_back(dts[i]);

        if (useParams) {
            X_data.push_back(static_cast<float>(traj.bodyMass));
            X_data.push_back(static_cast<float>(traj.bodyRadius));
            X_data.push_back(static_cast<float>(traj.initPosition));
            X_data.push_back(static_cast<float>(traj.initVelocity));
            X_data.push_back(simTime);
        }

        // PINN-style output: acceleration = dvel / dt
        // NN learns acceleration; kinematics integrates state.
        float dvel = static_cast<float>(traj.velocities[i + 1] - traj.velocities[i]);
        float dt = dts[i];
        float accel = (dt > 0.0f) ? (dvel / dt) : 0.0f;
        Y_data.push_back(accel);
    }

    // Create tensors from data vectors
    auto X = torch::from_blob(X_data.data(), {n, featDim}, torch::kFloat32).clone().to(device_);
    auto Y = torch::from_blob(Y_data.data(), {n, 1}, torch::kFloat32).clone().to(device_);

    return {X, Y};
}

// Build concatenated (X, Y) arrays from multiple trajectories
std::pair<torch::Tensor, torch::Tensor> SingleBodyDatasetBuilder::buildArrays(
    const std::vector<std::unique_ptr<SingleBodyTrajectoryData>>& trajs) const {
    
    // Handle empty trajectory list
    if (trajs.empty()) {
        auto opts = torch::TensorOptions().dtype(torch::kFloat32).device(device_);
        return {torch::empty({0, featureDim(true)}, opts),
                torch::empty({0, targetDim()}, opts)};
    }

    std::vector<torch::Tensor> Xs, Ys;
    Xs.reserve(trajs.size());
    Ys.reserve(trajs.size());

    for (const auto& traj : trajs) {
        auto [X, Y] = trajectoryToPairs(*traj, true);
        if (X.size(0) > 0) { // Only add non-empty tensors
            Xs.push_back(X);
            Ys.push_back(Y);
        }
    }

    // Handle case where all trajectories were invalid
    if (Xs.empty()) {
        auto opts = torch::TensorOptions().dtype(torch::kFloat32).device(device_);
        return {torch::empty({0, featureDim(true)}, opts),
                torch::empty({0, targetDim()}, opts)};
    }

    return {torch::cat(Xs, 0), torch::cat(Ys, 0)};
}

// Build split tensors for train/val/test
SingleBodySplitTensors SingleBodyDatasetBuilder::buildSplitTensors(const SingleBodySplitTrajectories& split) const {
    SingleBodySplitTensors out;
    auto opts = torch::TensorOptions().dtype(torch::kFloat32).device(device_);

    // TRAIN
    if (!split.trainTrajs.empty()) {
        auto [X_train, Y_train] = buildArrays(split.trainTrajs);
        out.X_train = X_train;
        out.Y_train = Y_train;
    } else {
        out.X_train = torch::empty({0}, opts);
        out.Y_train = torch::empty({0}, opts);
    }

    // VAL
    if (!split.valTrajs.empty()) {
        auto [X_val, Y_val] = buildArrays(split.valTrajs);
        out.X_val = X_val;
        out.Y_val = Y_val;
    } else {
        out.X_val = torch::empty({0}, opts);
        out.Y_val = torch::empty({0}, opts);
    }

    // TEST
    if (!split.testTrajs.empty()) {
        auto [X_test, Y_test] = buildArrays(split.testTrajs);
        out.X_test = X_test;
        out.Y_test = Y_test;
    } else {
        out.X_test = torch::empty({0}, opts);
        out.Y_test = torch::empty({0}, opts);
    }

    return out;
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
//                                                                               SingleBodyScalerManager
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PUBLIC METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Constructor
SingleBodyScalerManager::SingleBodyScalerManager(torch::Device device)
    : device_(device) {}

// Fit standardizer on data tensor
SingleBodyStandardizer SingleBodyScalerManager::fitStandardizer(const torch::Tensor& data) const {
    // Move to CPU and use float64 for numerical stability with large astronomical values
    auto data_cpu = data.to(torch::kCPU).to(torch::kFloat64);
    
    // Compute mean per feature
    auto mean_f64 = data_cpu.mean(0);
    
    // Compute variance then sqrt for std (more stable than direct std)
    auto variance = data_cpu.var(0, /*unbiased=*/true);
    auto std_f64 = torch::sqrt(variance);
    
    // Replace any NaN/Inf in mean with 0
    auto mean_finite = torch::isfinite(mean_f64);
    mean_f64 = torch::where(mean_finite, mean_f64, torch::zeros_like(mean_f64));
    
    // Replace any NaN/Inf in std with 1, and clamp small values to epsilon
    constexpr double eps = 1e-8;
    auto std_finite = torch::isfinite(std_f64);
    std_f64 = torch::where(std_finite, std_f64, torch::ones_like(std_f64));
    std_f64 = torch::clamp(std_f64, eps);
    
    // Convert back to float32 for model compatibility
    auto mean_f32 = mean_f64.to(torch::kFloat32);
    auto std_f32 = std_f64.to(torch::kFloat32);
    
    // Final safety check - replace any remaining NaN/Inf
    mean_f32 = torch::where(torch::isfinite(mean_f32), mean_f32, torch::zeros_like(mean_f32));
    std_f32 = torch::where(torch::isfinite(std_f32), std_f32, torch::ones_like(std_f32));
    std_f32 = torch::clamp(std_f32, static_cast<float>(eps));
    
    return SingleBodyStandardizer(mean_f32, std_f32);
}

// Save scalers to JSON file
void SingleBodyScalerManager::saveScalers(const std::string& path,
                                        const SingleBodyStandardizer& xStd,
                                        const SingleBodyStandardizer& yStd) const {
    // Ensure directory exists
    std::filesystem::path filePath(path);
    if (filePath.has_parent_path()) {
        std::filesystem::create_directories(filePath.parent_path());
    }

    json j;

    // X scaler
    std::vector<float> x_mean, x_std_vec;
    for (int i = 0; i < xStd.mean.size(0); ++i) {
        x_mean.push_back(xStd.mean[i].item<float>());
        x_std_vec.push_back(xStd.std[i].item<float>());
    }
    j["x_mean"] = x_mean;
    j["x_std"] = x_std_vec;
    j["x_dim"] = static_cast<int>(xStd.mean.size(0));

    // Y scaler
    std::vector<float> y_mean, y_std_vec;
    for (int i = 0; i < yStd.mean.size(0); ++i) {
        y_mean.push_back(yStd.mean[i].item<float>());
        y_std_vec.push_back(yStd.std[i].item<float>());
    }
    j["y_mean"] = y_mean;
    j["y_std"] = y_std_vec;
    j["y_dim"] = static_cast<int>(yStd.mean.size(0));

    std::ofstream file(path);
    file << j.dump(2);
}

// Load scalers from JSON file
void SingleBodyScalerManager::loadScalers(const std::string& path,
                                        SingleBodyStandardizer& xStd,
                                        SingleBodyStandardizer& yStd) const {
    std::ifstream file(path);
    if (!file.is_open()) {
        throw std::runtime_error("Could not open scaler file: " + path);
    }

    json j;
    file >> j;

    // X scaler
    auto x_mean_vec = j["x_mean"].get<std::vector<float>>();
    auto x_std_vec = j["x_std"].get<std::vector<float>>();
    xStd.mean = torch::from_blob(x_mean_vec.data(), {static_cast<int64_t>(x_mean_vec.size())}, torch::kFloat32).clone();
    xStd.std = torch::from_blob(x_std_vec.data(), {static_cast<int64_t>(x_std_vec.size())}, torch::kFloat32).clone();

    // Y scaler
    auto y_mean_vec = j["y_mean"].get<std::vector<float>>();
    auto y_std_vec = j["y_std"].get<std::vector<float>>();
    yStd.mean = torch::from_blob(y_mean_vec.data(), {static_cast<int64_t>(y_mean_vec.size())}, torch::kFloat32).clone();
    yStd.std = torch::from_blob(y_std_vec.data(), {static_cast<int64_t>(y_std_vec.size())}, torch::kFloat32).clone();
}

// Fit or load scalers and standardize tensors
SingleBodyStandardizedTensors SingleBodyScalerManager::fitOrLoadAndStandardize(
    const SingleBodySplitTensors& splitTensors,
    const std::string& scalerPath,
    bool resumeTraining) const {

    SingleBodyStandardizer xStd, yStd;
    bool loadedFromDisk = false;

    if (resumeTraining && SystemUtilities::fileExists(scalerPath)) {
        std::cout << "Loading existing scalers: " << scalerPath << std::endl;
        loadScalers(scalerPath, xStd, yStd);
        loadedFromDisk = true;
    } else {
        std::cout << "Fitting scalers on TRAIN..." << std::endl;
        xStd = fitStandardizer(splitTensors.X_train);
        yStd = fitStandardizer(splitTensors.Y_train);
        loadedFromDisk = false;
    }

    // Print dims
    std::cout << "Scaler dims | x=" << xStd.mean.size(0) << " y=" << yStd.mean.size(0) << std::endl;

    // Move scaler parameters to match data device for transform operations
    auto dataDevice = splitTensors.X_train.device();
    SingleBodyStandardizer xStd_device, yStd_device;
    xStd_device.mean = xStd.mean.to(dataDevice);
    xStd_device.std = xStd.std.to(dataDevice);
    yStd_device.mean = yStd.mean.to(dataDevice);
    yStd_device.std = yStd.std.to(dataDevice);

    // Standardize all splits using device-matched scalers
    SingleBodyStandardizedTensors result;
    result.Xtr = xStd_device.transform(splitTensors.X_train);
    result.Ytr = yStd_device.transform(splitTensors.Y_train);
    result.Xva = xStd_device.transform(splitTensors.X_val);
    result.Yva = yStd_device.transform(splitTensors.Y_val);
    
    // Store CPU scalers for saving/loading compatibility
    result.xStd = xStd;
    result.yStd = yStd;
    result.scalersLoadedFromDisk = loadedFromDisk;

    return result;
}

// Scaler sanity check: verify inverse(transform(x)) ≈ x
bool SingleBodyScalerManager::runScalerSanityCheck(
    const SingleBodySplitTensors& splitTensors,
    const SingleBodyStandardizer& xStd,
    const SingleBodyStandardizer& yStd) const {

    std::cout << "\n=== Scaler Sanity Check ===" << std::endl;

    // Check for NaN/Inf in scaler parameters
    auto checkFinite = [](const torch::Tensor& t, const std::string& name) -> bool {
        if (!torch::isfinite(t).all().item<bool>()) {
            std::cerr << "ERROR: " << name << " contains NaN or Inf!" << std::endl;
            return false;
        }
        return true;
    };

    if (!checkFinite(xStd.mean, "xStd.mean") || !checkFinite(xStd.std, "xStd.std") ||
        !checkFinite(yStd.mean, "yStd.mean") || !checkFinite(yStd.std, "yStd.std")) {
        return false;
    }

    // Check for zero std (after clamp, should not happen, but be safe)
    if ((xStd.std.abs() < 1e-12).any().item<bool>()) {
        std::cerr << "ERROR: xStd.std contains near-zero values!" << std::endl;
        return false;
    }
    if ((yStd.std.abs() < 1e-12).any().item<bool>()) {
        std::cerr << "ERROR: yStd.std contains near-zero values!" << std::endl;
        return false;
    }

    // Take a small slice of raw data and convert to CPU float64 for precision
    int64_t n_check = std::min(static_cast<int64_t>(1024), splitTensors.X_train.size(0));
    auto X_slice = splitTensors.X_train.slice(0, 0, n_check).cpu().to(torch::kFloat64);
    auto Y_slice = splitTensors.Y_train.slice(0, 0, n_check).cpu().to(torch::kFloat64);

    // Convert scaler params to CPU float64
    auto xMean = xStd.mean.cpu().to(torch::kFloat64);
    auto xStdDev = xStd.std.cpu().to(torch::kFloat64);
    auto yMean = yStd.mean.cpu().to(torch::kFloat64);
    auto yStdDev = yStd.std.cpu().to(torch::kFloat64);

    // Compute transform and inverse manually in float64
    auto X_transformed = (X_slice - xMean) / xStdDev;
    auto X_recovered = X_transformed * xStdDev + xMean;
    auto X_diff = (X_slice - X_recovered).abs();
    double X_abs_err = X_diff.max().item<double>();
    double X_max_val = X_slice.abs().max().item<double>();
    double X_rel_err = X_abs_err / std::max(X_max_val, 1.0);

    auto Y_transformed = (Y_slice - yMean) / yStdDev;
    auto Y_recovered = Y_transformed * yStdDev + yMean;
    auto Y_diff = (Y_slice - Y_recovered).abs();
    double Y_abs_err = Y_diff.max().item<double>();
    double Y_max_val = Y_slice.abs().max().item<double>();
    double Y_rel_err = Y_abs_err / std::max(Y_max_val, 1.0);

    std::cout << "  X scaler: abs_err=" << std::scientific << X_abs_err 
            << ", rel_err=" << X_rel_err << std::endl;
    std::cout << "  Y scaler: abs_err=" << std::scientific << Y_abs_err 
            << ", rel_err=" << Y_rel_err << std::endl;

    // Tolerances
    const double atol_X = 1e-3;
    const double atol_Y = 1e-6;
    const double rtol = 1e-6;
    const double critical_atol = 1e-2;  // Truly broken threshold

    // Check for truly broken scalers (hard abort)
    if (X_abs_err > critical_atol || Y_abs_err > critical_atol) {
        std::cerr << "ERROR: Scaler inversion error critically large (>" << critical_atol << ")! Aborting." << std::endl;
        return false;
    }

    // Check for NaN/Inf in recovered values
    if (!torch::isfinite(X_recovered).all().item<bool>() || !torch::isfinite(Y_recovered).all().item<bool>()) {
        std::cerr << "ERROR: Scaler inversion produced NaN/Inf! Aborting." << std::endl;
        return false;
    }

    // Warning for elevated but acceptable errors
    bool X_warn = (X_abs_err > atol_X) && (X_rel_err > rtol);
    bool Y_warn = (Y_abs_err > atol_Y) && (Y_rel_err > rtol);

    if (X_warn) {
        std::cout << "  [WARNING] X scaler abs_err > " << atol_X << " AND rel_err > " << rtol 
                << ". This may be float32 precision noise from large feature values." << std::endl;
    }
    if (Y_warn) {
        std::cout << "  [WARNING] Y scaler abs_err > " << atol_Y << " AND rel_err > " << rtol << std::endl;
    }

    if (X_warn || Y_warn) {
        std::cout << "  [CONTINUE] Proceeding with training despite warnings." << std::endl;
    } else {
        std::cout << "  [OK] Scaler sanity check passed." << std::endl;
    }

    return true;
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
//                                                                               SingleBodyTrainer
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PUBLIC METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Constructor
SingleBodyTrainer::SingleBodyTrainer(torch::Device device) : device_(device) {}

// Compute physics-based acceleration: -G*M/(R+pos)^2
// This is differentiable and runs on device (GPU or CPU).
// Used by residual PINN: accel_hat = accel_phys + accel_residual
torch::Tensor SingleBodyTrainer::computePhysicsAccelTensor(const torch::Tensor& pos,
                                                            const torch::Tensor& mass,
                                                            const torch::Tensor& radius) {
    // Gravitational constant (matching models.h)
    constexpr double G = 6.67430e-11;
    
    // r = radius + pos (distance from center of mass)
    auto r = radius + pos;
    
    // Clamp r to avoid division by zero near surface
    auto r_safe = torch::clamp(r.abs(), 1.0);  // Minimum 1 meter
    
    // accel = -G * M / r^2 (negative because gravity pulls inward)
    auto accel = -G * mass / (r_safe * r_safe);
    
    // Handle sign: if pos is negative (inside body), physics may diverge
    // For safety, keep sign consistent with original r sign
    auto sign_r = torch::sign(r);
    accel = accel * sign_r.abs();  // Ensure accel is always negative (toward body)
    
    return accel;
}

// Initialize model (create or resume from checkpoint)
// PINN-style: output dimension is 1 (acceleration only)
SingleBodyTrainingModel SingleBodyTrainer::initializeModel(
    const SingleBodyStandardizedTensors& stdTensors,
    const std::string& modelPath,
    const std::string& scalerPath,
    bool resumeTraining) const {
    
    // Determine dims from standardized tensors
    int64_t in_dim = stdTensors.Xtr.size(1);
    // PINN-style: NN outputs acceleration (or acceleration residual), always 1-D
    int64_t out_dim = 1;
    
    // Create model
    auto model = SingleBodyMLP(in_dim, out_dim);
    model->to(device_);
    
    // Load existing model if resuming
    if (resumeTraining && SystemUtilities::fileExists(modelPath)) {
        try {
            torch::load(model, modelPath);
            std::cout << "Resuming training from existing model: " << modelPath << std::endl;
        } catch (const std::exception& e) {
            std::cout << "Could not load existing model, starting fresh: " << e.what() << std::endl;
        }
    } else {
        std::cout << "Starting fresh training" << std::endl;
    }
    
    std::cout << "Model: " << in_dim << " inputs -> " << out_dim << " outputs" << std::endl;
    std::cout << "Training on " << device_ << "..." << std::endl;
    
    return SingleBodyTrainingModel{model, modelPath, scalerPath};
}

// Run the training loop
SingleBodyTrainedModel SingleBodyTrainer::runTrainingLoop(
    SingleBodyTrainingModel& trainingModel,
    const SingleBodyTrainConfig& cfg,
    const SingleBodyStandardizedTensors& stdTensors,
    const SingleBodySplitTensors& splitTensors,
    const SingleBodySplitTrajectories& splitTrajs) const {
    
    // ===== TIMING HELPERS =====
    auto now = []() { return std::chrono::steady_clock::now(); };
    auto sec = [](std::chrono::steady_clock::time_point t0) {
        return std::chrono::duration<double>(std::chrono::steady_clock::now() - t0).count();
    };
    
    // ===== SCALER SANITY CHECK =====
    SingleBodyScalerManager scalerMgr(device_);
    if (!scalerMgr.runScalerSanityCheck(splitTensors, stdTensors.xStd, stdTensors.yStd)) {
        std::cerr << "Scaler sanity check failed! Aborting training." << std::endl;
        SingleBodyTrainedModel result;
        result.model = trainingModel.model;
        result.bestEpoch = -1;
        result.bestTrainMse = std::numeric_limits<double>::infinity();
        result.bestValMseScaled = std::numeric_limits<double>::infinity();
        result.bestValMaeScaled = std::numeric_limits<double>::infinity();
        result.bestValMseReal = std::numeric_limits<double>::infinity();
        result.bestValMaeReal = std::numeric_limits<double>::infinity();
        return result;
    }
    
    // ===== MOVE SCALERS TO DEVICE =====
    SingleBodyStandardizer xStd_device, yStd_device;
    xStd_device.mean = stdTensors.xStd.mean.to(device_);
    xStd_device.std = stdTensors.xStd.std.to(device_);
    yStd_device.mean = stdTensors.yStd.mean.to(device_);
    yStd_device.std = stdTensors.yStd.std.to(device_);
    
    // ===== TEACHER-FORCED DEBUG =====
    if (!splitTrajs.trainTrajs.empty()) {
        runTeacherForcedDebug(trainingModel.model, *splitTrajs.trainTrajs[0], xStd_device, yStd_device, cfg);
    } else if (!splitTrajs.valTrajs.empty()) {
        runTeacherForcedDebug(trainingModel.model, *splitTrajs.valTrajs[0], xStd_device, yStd_device, cfg);
    }
    
    // ===== TRAINING SETUP =====
    // Use learning rate from config (lower for rollout training stability)
    torch::optim::AdamW optimizer(trainingModel.model->parameters(), 
                                torch::optim::AdamWOptions(cfg.learningRate).weight_decay(1e-3));
    
    // Extract actual optimizer settings for accurate logging
    auto& opt_defaults = static_cast<torch::optim::AdamWOptions&>(optimizer.defaults());
    const double optimizer_lr = opt_defaults.lr();
    const double optimizer_wd = opt_defaults.weight_decay();
    
    // Best model tracking
    double best_val_mse = std::numeric_limits<double>::infinity();
    int best_epoch = 0;
    double best_train_mse = 0.0;
    double best_val_mae_scaled = 0.0;
    double best_val_mse_real = 0.0;
    double best_val_mae_real = 0.0;
    std::stringstream best_state_stream;
    
    // Batch config
    int64_t batch_size = cfg.batchSize;
    int64_t n_train = stdTensors.Xtr.size(0);
    int64_t n_val = stdTensors.Xva.size(0);
    int64_t steps_per_epoch = (n_train + batch_size - 1) / batch_size;
    
    // Rollout config
    int rollout_K = cfg.rolloutK;
    int rollout_trajs_per_batch = 4;
    int rollout_every_n_batches = 25;
    float rollout_lambda = 0.1f;
    const int64_t print_every = 25;
    
    // PINN Residual config (NN learns acceleration; kinematics integrates state)
    bool use_residual_pinn = cfg.useResidualPINN;
    float lambda_res = cfg.lambdaRes;  // L2 regularization on residual
    
    // Warning rate-limiting counters (per epoch)
    int nan_warn_count = 0;
    const int max_nan_warns_per_epoch = 3;
    
    // ===== SANITY CHECKS (fail fast on silent no-learning issues) =====
    auto params = trainingModel.model->parameters();
    if (params.size() == 0) {
        std::cerr << "ERROR: Model has no trainable parameters!" << std::endl;
        throw std::runtime_error("Model has no parameters - training would be a no-op");
    }
    if (cfg.learningRate <= 0) {
        std::cerr << "ERROR: learningRate=" << cfg.learningRate << " is non-positive! Training would be a no-op." << std::endl;
        throw std::runtime_error("learningRate must be > 0");
    }
    float effective_max_grad_norm = cfg.maxGradNorm;
    if (effective_max_grad_norm <= 1e-6f) {
        std::cerr << "WARNING: maxGradNorm=" << cfg.maxGradNorm << " is too small, setting to 1.0" << std::endl;
        effective_max_grad_norm = 1.0f;
    }
    
    // ===== PRINT TRAINING CONFIGURATION =====
    std::cout << "\n=== Training Configuration (PINN-style) ===" << std::endl;
    std::cout << "  NN output: acceleration " << (use_residual_pinn ? "(residual correction)" : "(direct)") << std::endl;
    std::cout << "  n_train=" << n_train << ", n_val=" << n_val << ", batch_size=" << batch_size << std::endl;
    std::cout << "  steps_per_epoch=" << steps_per_epoch << ", epochs=" << cfg.epochs << std::endl;
    
    // LR + optimizer truth
    std::cout << "  cfg.learningRate=" << cfg.learningRate
            << " | optimizer_lr=" << optimizer_lr
            << " | optimizer_weight_decay=" << optimizer_wd << std::endl;
    
    // Grad clipping truth
    std::cout << "  cfg.maxGradNorm=" << cfg.maxGradNorm
            << " | effective_max_grad_norm=" << effective_max_grad_norm << std::endl;
    
    // Rollout settings
    std::cout << "  use_rollout_loss=" << (cfg.useRolloutLoss ? "true" : "false");
    if (cfg.useRolloutLoss) {
        std::cout << " | lambda=" << rollout_lambda
                << " | K=" << rollout_K
                << " | every_n_batches=" << rollout_every_n_batches
                << " | trajs_per_batch=" << rollout_trajs_per_batch;
    }
    std::cout << std::endl;
    
    std::cout << "  compute_val_rollout_metric=" << (cfg.computeValRolloutMetric ? "true" : "false");
    if (cfg.computeValRolloutMetric) {
        std::cout << " | val_rollout_K=" << rollout_K
                << " | num_val_trajs<=5";
    }
    std::cout << std::endl;
    
    // Residual PINN knobs
    std::cout << "  useResidualPINN=" << (cfg.useResidualPINN ? "true" : "false");
    if (cfg.useResidualPINN) {
        std::cout << " | lambdaRes=" << cfg.lambdaRes
                << " | resCap=" << cfg.resCap
                << " | resCapMin=" << cfg.resCapMin
                << " | resCapFloorMin=" << cfg.resCapFloorMin;
    }
    std::cout << std::endl;
    // Print trainable parameter count
    int64_t total_params = 0;
    for (const auto& p : params) {
        total_params += p.numel();
    }
    std::cout << "  trainable_params=" << total_params << std::endl;
    
    // Representative parameter for tracking changes (first scalar of first tensor)
    float repr_param_prev = params[0].flatten()[0].item<float>();
    std::cout << "  repr_param_initial=" << std::scientific << std::setprecision(6) << repr_param_prev << std::endl;
    
    // ===== EPOCH LOOP =====
    for (int epoch = 1; epoch <= cfg.epochs; ++epoch) {
        auto epoch_start = now();
        
        // Reset per-epoch warning counter
        nan_warn_count = 0;
        
        // Per-epoch instrumentation counters
        int64_t updates_this_epoch = 0;
        int64_t skipped_nan_pred = 0;
        int64_t skipped_nan_loss = 0;
        double grad_norm_sum = 0.0;
        int64_t grad_norm_count = 0;
        bool first_batch_of_epoch = true;
        
        // PINN residual debug (first batch stats)
        double first_batch_mean_accel_phys = 0.0;
        double first_batch_mean_res_cap = 0.0;
        double first_batch_mean_res_before = 0.0;
        double first_batch_mean_res_after = 0.0;
        
        // ----- TRAINING PHASE -----
        trainingModel.model->train();
        double train_loss_sum = 0.0;
        double train_rollout_loss_sum = 0.0;
        double train_res_loss_sum = 0.0;  // Residual L2 regularization loss
        int64_t train_count = 0;
        int rollout_count = 0;
        int res_count = 0;
        
        for (int64_t step = 0; step < steps_per_epoch; ++step) {
            int64_t cur_bs = std::min(batch_size, n_train);
            // Create batch indices on same device as data for index_select compatibility
            auto batch_indices = torch::randint(0, n_train, {cur_bs}, 
                torch::TensorOptions().dtype(torch::kLong).device(stdTensors.Xtr.device()));
            
            auto xb = stdTensors.Xtr.index_select(0, batch_indices);
            auto yb = stdTensors.Ytr.index_select(0, batch_indices);  // yb is accel_true [B,1]
            
            optimizer.zero_grad();
            
            // PINN-style: NN outputs acceleration (or residual correction)
            // pred is accel_res_scaled [B,1] in residual mode, or accel_scaled [B,1] otherwise
            auto pred = trainingModel.model->forward(xb);
            
            // Check for NaN/Inf in predictions (rate-limited warning)
            if (!torch::isfinite(pred).all().item<bool>()) {
                skipped_nan_pred++;
                if (skipped_nan_pred == 1) {
                    std::cerr << "  [WARNING] NaN/Inf in predictions at step " << step << ", skipping batch" << std::endl;
                }
                continue;
            }
            
            // Compute supervised loss on acceleration
            torch::Tensor one_step_loss;
            torch::Tensor res_loss = torch::zeros({1}, torch::TensorOptions().device(device_));
            
            if (use_residual_pinn) {
                // Residual PINN: NN learns accel_residual, final accel = accel_phys + accel_res
                // Convert to real units to compute physics-based acceleration
                auto xb_real = xStd_device.inverse(xb);
                
                // Extract pos, mass, radius from xb_real (feature indices 0, 4, 5)
                auto pos_real = xb_real.index({torch::indexing::Slice(), 0}).unsqueeze(1);    // [B,1]
                auto mass_real = xb_real.index({torch::indexing::Slice(), 4}).unsqueeze(1);   // [B,1]
                auto radius_real = xb_real.index({torch::indexing::Slice(), 5}).unsqueeze(1); // [B,1]
                
                // Compute physics-based acceleration (differentiable, on device)
                auto accel_phys = computePhysicsAccelTensor(pos_real, mass_real, radius_real);  // [B,1]
                
                // Convert NN output (residual) to real units
                auto accel_res_real = yStd_device.inverse(pred);  // [B,1]
                
                // Clamp residual to prevent instability: |res| <= resCap * |accel_phys| + resCapMin
                // Apply floor to prevent res_cap from collapsing to zero
                auto res_cap = cfg.resCap * accel_phys.abs() + cfg.resCapMin;
                res_cap = torch::clamp(res_cap, cfg.resCapFloorMin);  // floor to prevent near-zero cap
                
                // First batch debug: track residual PINN stats before/after clamp
                if (first_batch_of_epoch) {
                    first_batch_mean_accel_phys = accel_phys.abs().mean().item<double>();
                    first_batch_mean_res_cap = res_cap.mean().item<double>();
                    first_batch_mean_res_before = accel_res_real.abs().mean().item<double>();
                }
                
                accel_res_real = torch::tanh(accel_res_real / (res_cap + 1e-8)) * res_cap;
                
                // First batch: record residual after clamp
                if (first_batch_of_epoch) {
                    first_batch_mean_res_after = accel_res_real.abs().mean().item<double>();
                }
                
                // Final acceleration: physics + learned residual
                auto accel_hat_real = accel_phys + accel_res_real;  // [B,1]
                
                // Get ground truth acceleration in real units
                auto accel_true_real = yStd_device.inverse(yb);  // [B,1]
                
                // Supervised loss: MSE between accel_hat and accel_true (in real units)
                one_step_loss = torch::mse_loss(accel_hat_real, accel_true_real);
                
                // L2 regularization on residual (keep it small, let physics do the work)
                res_loss = lambda_res * (accel_res_real.pow(2)).mean();
                train_res_loss_sum += res_loss.item<double>();
                res_count++;
            } else {
                // Direct mode: NN directly outputs acceleration
                // Simple MSE loss in standardized space
                one_step_loss = torch::mse_loss(pred, yb);
            }
            
            // Multi-step rollout loss (conditional, uses kinematics)
            auto rollout_loss = torch::zeros({1}, torch::TensorOptions().device(device_));
            bool compute_rollout_this_batch = cfg.useRolloutLoss && 
                                            !splitTrajs.trainTrajs.empty() && 
                                            (step % rollout_every_n_batches == 0);
            
            if (compute_rollout_this_batch) {
                int n_trajs = static_cast<int>(splitTrajs.trainTrajs.size());
                int trajs_to_sample = std::min(rollout_trajs_per_batch, n_trajs);
                
                for (int t = 0; t < trajs_to_sample; ++t) {
                    int traj_idx = (static_cast<int>(epoch * step) + t) % n_trajs;
                    auto traj_loss = multiStepRolloutLoss(
                        trainingModel.model,
                        *splitTrajs.trainTrajs[traj_idx],
                        xStd_device,
                        yStd_device,
                        cfg);  // Pass full config for PINN settings
                    rollout_loss = rollout_loss + traj_loss;
                }
                rollout_loss = rollout_loss / static_cast<float>(trajs_to_sample);
            }
            
            // Total loss = accel_loss + residual_reg + rollout_loss
            auto total_loss = one_step_loss + res_loss + rollout_lambda * rollout_loss;
            
            // Check for NaN/Inf in loss (track count, skip batch)
            if (!torch::isfinite(total_loss).item<bool>()) {
                skipped_nan_loss++;
                if (skipped_nan_loss == 1) {
                    std::cerr << "  [WARNING] NaN/Inf in loss at step " << step << ", skipping batch" << std::endl;
                }
                continue;
            }
            
            total_loss.backward();
            
            // Compute gradient norm before clipping
            double grad_norm_before = 0.0;
            for (const auto& p : trainingModel.model->parameters()) {
                if (p.grad().defined()) {
                    grad_norm_before += p.grad().norm().item<double>() * p.grad().norm().item<double>();
                }
            }
            grad_norm_before = std::sqrt(grad_norm_before);
            
            // Gradient clipping for training stability (only if effective_max_grad_norm > 0)
            double grad_norm_after = grad_norm_before;
            if (effective_max_grad_norm > 0) {
                torch::nn::utils::clip_grad_norm_(trainingModel.model->parameters(), effective_max_grad_norm);
                // Recompute grad norm after clipping
                grad_norm_after = 0.0;
                for (const auto& p : trainingModel.model->parameters()) {
                    if (p.grad().defined()) {
                        grad_norm_after += p.grad().norm().item<double>() * p.grad().norm().item<double>();
                    }
                }
                grad_norm_after = std::sqrt(grad_norm_after);
            }
            
            // First batch: print grad norms before/after clipping
            if (first_batch_of_epoch) {
                std::cout << "  [Epoch " << epoch << " batch 0] grad_norm_before_clip=" << std::scientific 
                          << std::setprecision(3) << grad_norm_before 
                          << ", grad_norm_after_clip=" << grad_norm_after << std::endl;
            }
            
            // Track grad norm statistics
            grad_norm_sum += grad_norm_after;
            grad_norm_count++;
            
            // Track representative parameter before step
            float repr_param_before_step = params[0].flatten()[0].item<float>();
            
            optimizer.step();
            
            // Track representative parameter after step
            float repr_param_after_step = params[0].flatten()[0].item<float>();
            
            // First batch: print param delta
            if (first_batch_of_epoch) {
                float param_delta = repr_param_after_step - repr_param_before_step;
                std::cout << "  [Epoch " << epoch << " batch 0] param_delta=" << std::scientific 
                          << std::setprecision(6) << param_delta << std::endl;
            }
            
            updates_this_epoch++;
            first_batch_of_epoch = false;
            
            double step_loss = one_step_loss.item<double>();
            double step_rollout = rollout_loss.item<double>();
            double step_res = res_loss.item<double>();
            
            train_loss_sum += step_loss * xb.size(0);
            train_count += xb.size(0);
            if (compute_rollout_this_batch) {
                train_rollout_loss_sum += step_rollout;
                rollout_count++;
            }
            
            // Progress print
            if ((step + 1) % print_every == 0 || step == 0) {
                std::cout << "\rEpoch " << epoch << " step " << (step + 1) << "/" << steps_per_epoch
                        << " | loss=" << std::fixed << std::setprecision(4) << step_loss
                        << " | res=" << step_res
                        << " | rollout=" << step_rollout << "          " << std::flush;
            }
        }
        
        double train_mse = (train_count > 0) ? train_loss_sum / train_count : 0.0;
        double avg_rollout_loss = (rollout_count > 0) ? train_rollout_loss_sum / rollout_count : 0.0;
        double avg_res_loss = (res_count > 0) ? train_res_loss_sum / res_count : 0.0;
        double mean_grad_norm = (grad_norm_count > 0) ? grad_norm_sum / grad_norm_count : 0.0;
        
        // ===== TRAINING PHASE DIAGNOSTICS =====
        std::cout << "\r" << std::string(80, ' ') << "\r";  // Clear progress line
        
        // Print instrumentation summary
        std::cout << "  [Diag] updates=" << updates_this_epoch 
                  << ", skipped_nan_pred=" << skipped_nan_pred 
                  << ", skipped_nan_loss=" << skipped_nan_loss
                  << ", mean_grad_norm=" << std::scientific << std::setprecision(3) << mean_grad_norm << std::endl;
        
        // Print residual PINN debug info (first batch stats)
        if (use_residual_pinn) {
            std::cout << "  [PINN] mean|accel_phys|=" << std::scientific << std::setprecision(3) << first_batch_mean_accel_phys
                      << ", mean_res_cap=" << first_batch_mean_res_cap
                      << ", mean|res_before|=" << first_batch_mean_res_before
                      << ", mean|res_after|=" << first_batch_mean_res_after << std::endl;
            // Warn if res_cap is very small
            if (first_batch_mean_res_cap < 1e-6) {
                std::cerr << "  [WARNING] res_cap is near zero - residual is effectively locked to zero!" << std::endl;
            }
        }
        
        // Check for excessive skipping
        int64_t total_skipped = skipped_nan_pred + skipped_nan_loss;
        double skip_fraction = (steps_per_epoch > 0) ? static_cast<double>(total_skipped) / steps_per_epoch : 0.0;
        if (skip_fraction > 0.1) {
            std::cerr << "  [WARNING] " << (skip_fraction * 100) << "% of batches skipped due to NaN/Inf - consider lowering learning rate" << std::endl;
        }
        
        // Critical: check if any updates happened
        if (updates_this_epoch == 0) {
            std::cerr << "\n=== CRITICAL ERROR: No optimizer updates this epoch! ===" << std::endl;
            std::cerr << "All batches were skipped due to NaN/Inf. Training is not progressing." << std::endl;
            std::cerr << "Possible causes: learning rate too high, bad data, or numerical instability." << std::endl;
            std::cerr << "Aborting training early." << std::endl;
            break;  // Exit epoch loop
        }
        
        // Track representative parameter across epochs
        float repr_param_now = params[0].flatten()[0].item<float>();
        float param_change_epoch = repr_param_now - repr_param_prev;
        if (std::abs(param_change_epoch) < 1e-12f && epoch > 1) {
            std::cerr << "  [WARNING] repr_param unchanged across epoch " << epoch << " - model may not be learning!" << std::endl;
        }
        repr_param_prev = repr_param_now;
        
        // ----- VALIDATION PHASE -----
        trainingModel.model->eval();
        torch::NoGradGuard no_grad;
        
        double val_mse_scaled_sum = 0.0;
        double val_mae_scaled_sum = 0.0;
        double val_mse_real_sum = 0.0;
        double val_mae_real_sum = 0.0;
        int64_t val_count = 0;
        
        for (int64_t i = 0; i < n_val; i += batch_size) {
            int64_t batch_end = std::min(i + batch_size, n_val);
            auto xb = stdTensors.Xva.slice(0, i, batch_end).to(device_);
            auto yb = stdTensors.Yva.slice(0, i, batch_end).to(device_);
            
            auto pred_scaled = trainingModel.model->forward(xb);
            
            // Check for NaN/Inf in predictions (rate-limited)
            if (!torch::isfinite(pred_scaled).all().item<bool>()) {
                if (nan_warn_count < max_nan_warns_per_epoch) {
                    std::cerr << "  [WARNING] NaN/Inf in val predictions, skipping batch" << std::endl;
                    nan_warn_count++;
                }
                continue;
            }
            
            // For residual PINN: compute accel_hat = accel_phys + accel_res
            torch::Tensor pred_accel_scaled;
            if (use_residual_pinn) {
                auto xb_real = xStd_device.inverse(xb);
                auto pos_real = xb_real.index({torch::indexing::Slice(), 0}).unsqueeze(1);
                auto mass_real = xb_real.index({torch::indexing::Slice(), 4}).unsqueeze(1);
                auto radius_real = xb_real.index({torch::indexing::Slice(), 5}).unsqueeze(1);
                
                auto accel_phys = computePhysicsAccelTensor(pos_real, mass_real, radius_real);
                auto accel_res_real = yStd_device.inverse(pred_scaled);
                auto res_cap = cfg.resCap * accel_phys.abs() + cfg.resCapMin;
                res_cap = torch::clamp(res_cap, cfg.resCapFloorMin);  // floor to prevent near-zero cap
                accel_res_real = torch::tanh(accel_res_real / (res_cap + 1e-8)) * res_cap;
                auto accel_hat_real = accel_phys + accel_res_real;
                // Convert back to scaled space for consistency
                pred_accel_scaled = yStd_device.transform(accel_hat_real);
            } else {
                pred_accel_scaled = pred_scaled;
            }
            
            // Scaled space metrics (comparing final acceleration, whether residual or direct)
            auto mse_scaled = (pred_accel_scaled - yb).pow(2).sum(1);
            auto mae_scaled = (pred_accel_scaled - yb).abs().sum(1);
            
            val_mse_scaled_sum += mse_scaled.sum().item<double>();
            val_mae_scaled_sum += mae_scaled.sum().item<double>();
            
            // Real space metrics (inverse transform)
            auto pred_real = yStd_device.inverse(pred_scaled).cpu().to(torch::kFloat64);
            auto y_real = yStd_device.inverse(yb).cpu().to(torch::kFloat64);
            
            // Check for NaN/Inf in real space (rate-limited)
            if (!torch::isfinite(pred_real).all().item<bool>() || 
                !torch::isfinite(y_real).all().item<bool>()) {
                if (nan_warn_count < max_nan_warns_per_epoch) {
                    std::cerr << "  [WARNING] NaN/Inf in inverse transform, skipping real metrics for batch" << std::endl;
                    nan_warn_count++;
                }
                val_count += xb.size(0);
                continue;
            }
            
            auto mse_real = (pred_real - y_real).pow(2).sum(1);
            auto mae_real = (pred_real - y_real).abs().sum(1);
            
            val_mse_real_sum += mse_real.sum().item<double>();
            val_mae_real_sum += mae_real.sum().item<double>();
            
            val_count += xb.size(0);
        }
        
        double val_mse_scaled = (val_count > 0) ? val_mse_scaled_sum / val_count : 0.0;
        double val_mae_scaled = (val_count > 0) ? val_mae_scaled_sum / val_count : 0.0;
        double val_mse_real = (val_count > 0) ? val_mse_real_sum / val_count : 0.0;
        double val_mae_real = (val_count > 0) ? val_mae_real_sum / val_count : 0.0;
        
        // ----- OPTIONAL VALIDATION ROLLOUT METRIC -----
        std::string val_rollout_str = "SKIP";
        if (cfg.computeValRolloutMetric && !splitTrajs.valTrajs.empty()) {
            double val_rollout_mse = 0.0;
            int num_val_trajs = std::min(5, static_cast<int>(splitTrajs.valTrajs.size()));
            int rollout_count_val = 0;
            
            for (int t = 0; t < num_val_trajs; ++t) {
                const auto& traj = *splitTrajs.valTrajs[t];
                int traj_len = static_cast<int>(traj.times.size());
                if (traj_len < rollout_K + 2) continue;
                
                auto traj_loss = multiStepRolloutLoss(trainingModel.model, traj, xStd_device, yStd_device, cfg);
                double loss_val = traj_loss.item<double>();
                if (std::isfinite(loss_val)) {
                    val_rollout_mse += loss_val;
                    rollout_count_val++;
                }
            }
            if (rollout_count_val > 0) {
                val_rollout_mse /= rollout_count_val;
                std::ostringstream oss;
                oss << std::fixed << std::setprecision(4) << val_rollout_mse;
                val_rollout_str = oss.str();
            }
        }
        
        double epoch_time = sec(epoch_start);
        
        // ----- PRINT EPOCH SUMMARY -----
        std::cout << "\r" << std::string(80, ' ') << "\r";  // Clear line
        std::cout << "Epoch " << std::setw(2) << epoch
                << " | train_mse=" << std::fixed << std::setprecision(6) << train_mse;
        if (cfg.useRolloutLoss) {
            std::cout << " | rollout=" << std::setprecision(4) << avg_rollout_loss;
        }
        std::cout << " | val_mse=" << std::setprecision(6) << val_mse_scaled
                << " | val_rollout=" << val_rollout_str
                << " | " << std::setprecision(1) << epoch_time << "s" << std::endl;
        
        // ----- TRACK BEST MODEL -----
        if (val_mse_scaled < best_val_mse) {
            best_val_mse = val_mse_scaled;
            best_epoch = epoch;
            best_train_mse = train_mse;
            best_val_mae_scaled = val_mae_scaled;
            best_val_mse_real = val_mse_real;
            best_val_mae_real = val_mae_real;
            
            // Save best model to in-memory stream
            best_state_stream.str("");
            best_state_stream.clear();
            torch::save(trainingModel.model, best_state_stream);
        }
    }
    
    // ===== RELOAD BEST MODEL =====
    if (best_epoch > 0) {
        best_state_stream.seekg(0);
        torch::load(trainingModel.model, best_state_stream);
    }
    
    // ===== SAVE MODEL TO DISK =====
    torch::save(trainingModel.model, trainingModel.modelPath);
    std::cout << "\nModel saved to: " << trainingModel.modelPath << std::endl;
    
    // ===== DISPLAY BEST MODEL METRICS =====
    std::cout << "\n=== Best Model (Epoch " << best_epoch << ") ===" << std::endl;
    std::cout << "  train_mse (scaled): " << std::fixed << std::setprecision(6) << best_train_mse << std::endl;
    std::cout << "  val_mse_scaled:     " << best_val_mse << std::endl;
    std::cout << "  val_mae_scaled:     " << best_val_mae_scaled << std::endl;
    std::cout << "  val_mse_real:       " << best_val_mse_real << std::endl;
    std::cout << "  val_mae_real:       " << best_val_mae_real << std::endl;
    
    // ===== RETURN TRAINED MODEL =====
    SingleBodyTrainedModel result;
    result.model = trainingModel.model;
    result.bestEpoch = best_epoch;
    result.bestTrainMse = best_train_mse;
    result.bestValMseScaled = best_val_mse;
    result.bestValMaeScaled = best_val_mae_scaled;
    result.bestValMseReal = best_val_mse_real;
    result.bestValMaeReal = best_val_mae_real;
    
    return result;
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PROTECTED METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Multi-step rollout loss (differentiable, for training)
// PINN-style: NN outputs acceleration, kinematics integrates state
// v_next = v + accel * dt
// x_next = x + v * dt + 0.5 * accel * dt^2
torch::Tensor SingleBodyTrainer::multiStepRolloutLoss(
    SingleBodyMLP& model,
    const SingleBodyTrajectoryData& traj,
    const SingleBodyStandardizer& xStd,
    const SingleBodyStandardizer& yStd,
    const SingleBodyTrainConfig& cfg) const {
    
    int K = cfg.rolloutK;
    int traj_len = static_cast<int>(traj.times.size());
    if (traj_len < K + 2) {
        // Not enough steps, return zero loss
        return torch::zeros({1}, torch::TensorOptions().device(device_).requires_grad(true));
    }
    
    // Random start index
    static std::mt19937 rng(42);
    std::uniform_int_distribution<int> dist(0, traj_len - K - 1);
    int s = dist(rng);
    
    // Prepare trajectory constants
    float mass_f = static_cast<float>(traj.bodyMass);
    float radius_f = static_cast<float>(traj.bodyRadius);
    float initPos_f = static_cast<float>(traj.initPosition);
    float initVel_f = static_cast<float>(traj.initVelocity);
    float simTime_f = static_cast<float>(traj.simTime);
    
    // Initialize pos and vel as tensors (differentiable)
    auto pos = torch::tensor({static_cast<float>(traj.positions[s])},
                            torch::TensorOptions().dtype(torch::kFloat32).device(device_).requires_grad(false));
    auto vel = torch::tensor({static_cast<float>(traj.velocities[s])},
                            torch::TensorOptions().dtype(torch::kFloat32).device(device_).requires_grad(false));
    
    // Accumulate loss over K steps using SmoothL1Loss (Huber) for stability
    auto total_loss = torch::zeros({1}, torch::TensorOptions().device(device_));
    
    for (int j = 0; j < K; ++j) {
        int idx = s + j;
        float dt_val = traj.times[idx + 1] - traj.times[idx];
        float tNorm = (simTime_f > 0.0f) ? (static_cast<float>(traj.times[idx]) / simTime_f) : 0.0f;
        
        // Build feature tensor: [pos, vel, tNorm, dt, mass, radius, initPos, initVel, simTime]
        auto tNorm_t = torch::tensor({tNorm}, torch::TensorOptions().dtype(torch::kFloat32).device(device_));
        auto dt_t = torch::tensor({dt_val}, torch::TensorOptions().dtype(torch::kFloat32).device(device_));
        auto mass_t = torch::tensor({mass_f}, torch::TensorOptions().dtype(torch::kFloat32).device(device_));
        auto radius_t = torch::tensor({radius_f}, torch::TensorOptions().dtype(torch::kFloat32).device(device_));
        auto initPos_t = torch::tensor({initPos_f}, torch::TensorOptions().dtype(torch::kFloat32).device(device_));
        auto initVel_t = torch::tensor({initVel_f}, torch::TensorOptions().dtype(torch::kFloat32).device(device_));
        auto simTime_t = torch::tensor({simTime_f}, torch::TensorOptions().dtype(torch::kFloat32).device(device_));
        
        auto feat = torch::cat({pos, vel, tNorm_t, dt_t, mass_t, radius_t, initPos_t, initVel_t, simTime_t}, 0).unsqueeze(0);
        
        // Transform and predict acceleration (or residual)
        auto feat_scaled = xStd.transform(feat);
        auto accel_out_scaled = model->forward(feat_scaled);  // [1,1]
        
        // Get acceleration in real units
        torch::Tensor accel_real;
        if (cfg.useResidualPINN) {
            // Residual PINN: accel_hat = accel_phys + accel_res
            auto accel_phys = computePhysicsAccelTensor(pos.unsqueeze(1), mass_t.unsqueeze(1), radius_t.unsqueeze(1));
            auto accel_res_real = yStd.inverse(accel_out_scaled);  // [1,1]
            // Clamp residual with floor
            auto res_cap = cfg.resCap * accel_phys.abs() + cfg.resCapMin;
            res_cap = torch::clamp(res_cap, cfg.resCapFloorMin);  // floor to prevent near-zero cap
            accel_res_real = torch::tanh(accel_res_real / (res_cap + 1e-8)) * res_cap;
            accel_real = (accel_phys + accel_res_real).squeeze();  // scalar
        } else {
            accel_real = yStd.inverse(accel_out_scaled).squeeze();  // scalar
        }
        
        // Check for NaN/Inf in predictions
        if (!torch::isfinite(accel_real).all().item<bool>()) {
            // Return a large finite loss instead of NaN
            return torch::tensor({1e3}, torch::TensorOptions().device(device_).requires_grad(true));
        }
        
        // Kinematics update: compute next state using physics equations
        // Store current velocity before update
        auto vel_prev = vel.clone();
        
        // v_next = v + accel * dt
        vel = vel + accel_real * dt_val;
        
        // x_next = x + v_prev * dt + 0.5 * accel * dt^2 (using velocity at start of interval)
        pos = pos + vel_prev * dt_val + 0.5f * accel_real * dt_val * dt_val;
        
        // Ground truth at next step
        float gt_pos = static_cast<float>(traj.positions[idx + 1]);
        float gt_vel = static_cast<float>(traj.velocities[idx + 1]);
        
        // State error using SmoothL1Loss (Huber loss) for stability
        auto pos_err = torch::smooth_l1_loss(pos, torch::tensor({gt_pos}, pos.options()), 
                                              torch::Reduction::Mean, 1.0);
        auto vel_err = torch::smooth_l1_loss(vel, torch::tensor({gt_vel}, vel.options()),
                                              torch::Reduction::Mean, 1.0);
        total_loss = total_loss + pos_err + vel_err;
    }
    
    return total_loss / static_cast<float>(K);
}

// Compute acceleration using the canonical Models::singleBodySystem
// This ensures physics loss matches RK4 data generation exactly (used for reference/debugging)
double SingleBodyTrainer::computeAccelFromModels(double bodyMass, double bodyRadius, double pos, double vel) {
    Models models;
    SingleBodyDiffyEqs eom;
    eom.time = 0.0;  // Time not used in acceleration computation
    eom.bodyMass = bodyMass;
    eom.bodyRadius = bodyRadius;
    eom.position = pos;
    eom.velocity = vel;
    
    auto result = models.singleBodySystem(eom);
    // result.equations[0] = velocity, result.equations[1] = acceleration
    return result.equations[1];
}

// Teacher-forced one-step debug: compare predicted acceleration to ground truth
// PINN-style: NN outputs acceleration, kinematics integrates state
void SingleBodyTrainer::runTeacherForcedDebug(
    SingleBodyMLP& model,
    const SingleBodyTrajectoryData& traj,
    const SingleBodyStandardizer& xStd,
    const SingleBodyStandardizer& yStd,
    const SingleBodyTrainConfig& cfg) const {
    
    std::cout << "\n=== Teacher-Forced One-Step Debug (PINN-style) ===" << std::endl;
    std::cout << "  Model outputs: acceleration " << (cfg.useResidualPINN ? "(residual)" : "(direct)") << std::endl;
    
    model->eval();
    torch::NoGradGuard no_grad;
    
    int n_steps = std::min(100, static_cast<int>(traj.times.size()) - 1);
    if (n_steps < 1) {
        std::cout << "  [SKIP] Trajectory too short for debug." << std::endl;
        return;
    }
    
    double sum_gt_accel = 0.0;
    double sum_pred_accel = 0.0;
    int sign_agree = 0;
    
    // Move scalers to device
    auto xStd_mean = xStd.mean.to(device_);
    auto xStd_std = xStd.std.to(device_);
    auto yStd_mean = yStd.mean.to(device_);
    auto yStd_std = yStd.std.to(device_);
    
    for (int i = 0; i < n_steps; ++i) {
        // Ground truth acceleration = dvel / dt
        float dt = traj.times[i + 1] - traj.times[i];
        float gt_dvel = traj.velocities[i + 1] - traj.velocities[i];
        float gt_accel = (dt > 0.0f) ? (gt_dvel / dt) : 0.0f;
        
        // Build feature from TRUE state (teacher forcing)
        float simTime = static_cast<float>(traj.simTime);
        float tNorm = (simTime > 0.0f) ? (static_cast<float>(traj.times[i]) / simTime) : 0.0f;
        float mass_f = static_cast<float>(traj.bodyMass);
        float radius_f = static_cast<float>(traj.bodyRadius);
        float pos_f = static_cast<float>(traj.positions[i]);
        
        std::vector<float> feat = {
            pos_f,
            static_cast<float>(traj.velocities[i]),
            tNorm,
            dt,
            mass_f,
            radius_f,
            static_cast<float>(traj.initPosition),
            static_cast<float>(traj.initVelocity),
            simTime
        };
        
        auto feat_t = torch::from_blob(feat.data(), {1, 9}, torch::kFloat32).clone().to(device_);
        
        // Standardize and predict
        auto feat_scaled = (feat_t - xStd_mean) / xStd_std;
        auto accel_out_scaled = model->forward(feat_scaled);  // [1,1]
        
        // Get predicted acceleration
        float pred_accel;
        if (cfg.useResidualPINN) {
            // Compute physics acceleration
            float accel_phys = static_cast<float>(computeAccelFromModels(traj.bodyMass, traj.bodyRadius, traj.positions[i], traj.velocities[i]));
            // Get residual from NN
            auto accel_res_scaled = accel_out_scaled.cpu();
            float accel_res = (accel_res_scaled[0][0].item<float>() * yStd_std[0].item<float>()) + yStd_mean[0].item<float>();
            // Clamp residual with floor
            float res_cap = cfg.resCap * std::abs(accel_phys) + cfg.resCapMin;
            res_cap = std::max(res_cap, cfg.resCapFloorMin);  // floor to prevent near-zero cap
            accel_res = std::clamp(accel_res, -res_cap, res_cap);
            pred_accel = accel_phys + accel_res;
        } else {
            auto accel_scaled_cpu = accel_out_scaled.cpu();
            pred_accel = (accel_scaled_cpu[0][0].item<float>() * yStd_std[0].item<float>()) + yStd_mean[0].item<float>();
        }
        
        sum_gt_accel += gt_accel;
        sum_pred_accel += pred_accel;
        
        // Sign agreement for acceleration (should be negative for gravity)
        if ((gt_accel >= 0 && pred_accel >= 0) || (gt_accel < 0 && pred_accel < 0)) {
            sign_agree++;
        }
    }
    
    double mean_gt_accel = sum_gt_accel / n_steps;
    double mean_pred_accel = sum_pred_accel / n_steps;
    double sign_pct = 100.0 * sign_agree / n_steps;
    
    std::cout << "  mean_gt_accel:   " << std::fixed << std::setprecision(8) << mean_gt_accel << std::endl;
    std::cout << "  mean_pred_accel: " << mean_pred_accel << std::endl;
    std::cout << "  sign_agreement:  " << std::setprecision(1) << sign_pct << "%" << std::endl;
    
    if (sign_pct < 60.0) {
        std::cout << "  [WARN] Sign agreement < 60%! Possible output order/sign mismatch." << std::endl;
    } else {
        std::cout << "  [OK] Sign agreement looks reasonable." << std::endl;
    }
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
//                                                                               SingleBodyEvaluator
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PUBLIC METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Constructor
SingleBodyEvaluator::SingleBodyEvaluator(torch::Device device) : device_(device) {}

// Rollout trajectory and return (x_true, x_pred) in REAL units
// PINN-style: NN outputs acceleration, kinematics integrates state
std::pair<torch::Tensor, torch::Tensor> SingleBodyEvaluator::rolloutTrajectory(
    SingleBodyMLP& model,
    const SingleBodyTrajectoryData& traj,
    const SingleBodyStandardizer& xStd,
    const SingleBodyStandardizer& yStd,
    bool useResidualPINN) const {
    
    model->eval();
    torch::NoGradGuard no_grad;
    
    int n = static_cast<int>(traj.times.size());
    if (n < 1) {
        // Return empty tensors
        return {torch::empty({0, 2}, torch::kFloat64), torch::empty({0, 2}, torch::kFloat64)};
    }
    
    // Create tensors for predictions and ground truth (CPU float64 for stable metrics)
    auto x_pred = torch::zeros({n, 2}, torch::kFloat64);
    auto x_true = torch::zeros({n, 2}, torch::kFloat64);
    
    // Initialize state from initial conditions (matching predict() semantics)
    float pos = static_cast<float>(traj.initPosition);
    float vel = static_cast<float>(traj.initVelocity);
    
    // Store first prediction (at t=0, pred matches initial state)
    x_pred[0][0] = static_cast<double>(pos);
    x_pred[0][1] = static_cast<double>(vel);
    
    // Store first ground truth
    x_true[0][0] = traj.positions[0];
    x_true[0][1] = traj.velocities[0];
    
    // Trajectory constants
    float mass_f = static_cast<float>(traj.bodyMass);
    float radius_f = static_cast<float>(traj.bodyRadius);
    float initPos_f = static_cast<float>(traj.initPosition);
    float initVel_f = static_cast<float>(traj.initVelocity);
    float simTime_f = static_cast<float>(traj.simTime);
    
    // PINN residual config (default values)
    constexpr float resCap = 0.3f;
    constexpr float resCapMin = 1e-2f;
    constexpr float resCapFloorMin = 1e-3f;  // floor to prevent near-zero cap
    
    // Rollout from step 0 to step n-1 using kinematics
    for (int k = 0; k < n - 1; ++k) {
        float dt = static_cast<float>(traj.times[k + 1] - traj.times[k]);
        float tNorm = (simTime_f > 0.0f) ? (static_cast<float>(traj.times[k]) / simTime_f) : 0.0f;
        
        // Build feature vector matching training layout EXACTLY:
        // [pos_t, vel_t, t_norm, dt, bodyMass, bodyRadius, initPosition, initVelocity, simTime]
        std::vector<float> feat = {
            pos,
            vel,
            tNorm,
            dt,
            mass_f,
            radius_f,
            initPos_f,
            initVel_f,
            simTime_f
        };
        
        auto feat_t = torch::from_blob(feat.data(), {1, 9}, torch::kFloat32).clone().to(device_);
        auto feat_scaled = xStd.transform(feat_t);
        auto accel_out_scaled = model->forward(feat_scaled);  // [1,1]
        
        // Get acceleration in real units
        float accel;
        if (useResidualPINN) {
            // Compute physics-based acceleration: -G*M/(R+pos)^2
            constexpr double G = 6.67430e-11;
            double r = static_cast<double>(radius_f + pos);
            r = std::max(std::abs(r), 1.0);  // Clamp to minimum 1 meter
            float accel_phys = static_cast<float>(-G * mass_f / (r * r));
            
            // Get residual from NN
            auto accel_res_real = yStd.inverse(accel_out_scaled).cpu();
            float accel_res = accel_res_real[0][0].item<float>();
            
            // Clamp residual with floor
            float cap = resCap * std::abs(accel_phys) + resCapMin;
            cap = std::max(cap, resCapFloorMin);  // floor to prevent near-zero cap
            accel_res = std::clamp(accel_res, -cap, cap);
            
            accel = accel_phys + accel_res;
        } else {
            auto accel_real = yStd.inverse(accel_out_scaled).cpu();
            accel = accel_real[0][0].item<float>();
        }
        
        // Check for NaN/Inf in acceleration
        if (!std::isfinite(accel)) {
            std::cerr << "  [WARNING] NaN/Inf in rollout at step " << k << ", stopping early." << std::endl;
            // Pad remaining with last finite state
            for (int j = k + 1; j < n; ++j) {
                x_pred[j][0] = static_cast<double>(pos);
                x_pred[j][1] = static_cast<double>(vel);
                x_true[j][0] = traj.positions[j];
                x_true[j][1] = traj.velocities[j];
            }
            break;
        }
        
        // Kinematics update: compute next state using physics equations
        // Store current velocity before update
        float vel_prev = vel;
        
        // v_next = v + accel * dt
        vel = vel + accel * dt;
        
        // x_next = x + v_prev * dt + 0.5 * accel * dt^2
        pos = pos + vel_prev * dt + 0.5f * accel * dt * dt;
        
        // Store prediction for next step
        x_pred[k + 1][0] = static_cast<double>(pos);
        x_pred[k + 1][1] = static_cast<double>(vel);
        
        // Store ground truth for next step
        x_true[k + 1][0] = traj.positions[k + 1];
        x_true[k + 1][1] = traj.velocities[k + 1];
    }
    
    return {x_true, x_pred};
}

// Compute validation rollout MSE on a subset of trajectories (fast path)
// PINN-style: NN outputs acceleration, kinematics integrates state
double SingleBodyEvaluator::computeValRolloutMse(
    SingleBodyMLP& model,
    const std::vector<std::unique_ptr<SingleBodyTrajectoryData>>& valTrajs,
    const SingleBodyStandardizer& xStd,
    const SingleBodyStandardizer& yStd,
    int numTrajs,
    int K,
    bool useResidualPINN) const {
    
    if (valTrajs.empty()) {
        std::cerr << "  [WARNING] No validation trajectories for rollout MSE." << std::endl;
        return 0.0;
    }
    
    model->eval();
    torch::NoGradGuard no_grad;
    
    int n_to_eval = std::min(numTrajs, static_cast<int>(valTrajs.size()));
    double total_mse = 0.0;
    int valid_count = 0;
    
    // PINN residual config
    constexpr float resCap = 0.3f;
    constexpr float resCapMin = 1e-2f;
    constexpr float resCapFloorMin = 1e-3f;  // floor to prevent near-zero cap
    constexpr double G = 6.67430e-11;
    
    for (int t = 0; t < n_to_eval; ++t) {
        const auto& traj = *valTrajs[t];
        int traj_len = static_cast<int>(traj.times.size());
        if (traj_len < 2) continue;
        
        int steps = std::min(K, traj_len - 1);
        
        // Initialize state from initial conditions
        float pos = static_cast<float>(traj.initPosition);
        float vel = static_cast<float>(traj.initVelocity);
        
        // Trajectory constants
        float mass_f = static_cast<float>(traj.bodyMass);
        float radius_f = static_cast<float>(traj.bodyRadius);
        float initPos_f = static_cast<float>(traj.initPosition);
        float initVel_f = static_cast<float>(traj.initVelocity);
        float simTime_f = static_cast<float>(traj.simTime);
        
        double traj_mse = 0.0;
        bool valid_traj = true;
        
        for (int k = 0; k < steps && valid_traj; ++k) {
            float dt = static_cast<float>(traj.times[k + 1] - traj.times[k]);
            float tNorm = (simTime_f > 0.0f) ? (static_cast<float>(traj.times[k]) / simTime_f) : 0.0f;
            
            // Build feature vector matching training layout EXACTLY:
            // [pos_t, vel_t, t_norm, dt, bodyMass, bodyRadius, initPosition, initVelocity, simTime]
            std::vector<float> feat = {
                pos,
                vel,
                tNorm,
                dt,
                mass_f,
                radius_f,
                initPos_f,
                initVel_f,
                simTime_f
            };
            
            auto feat_t = torch::from_blob(feat.data(), {1, 9}, torch::kFloat32).clone().to(device_);
            auto feat_scaled = xStd.transform(feat_t);
            auto accel_out_scaled = model->forward(feat_scaled);  // [1,1]
            
            // Get acceleration in real units
            float accel;
            if (useResidualPINN) {
                // Compute physics-based acceleration: -G*M/(R+pos)^2
                double r = static_cast<double>(radius_f + pos);
                r = std::max(std::abs(r), 1.0);
                float accel_phys = static_cast<float>(-G * mass_f / (r * r));
                
                auto accel_res_real = yStd.inverse(accel_out_scaled).cpu();
                float accel_res = accel_res_real[0][0].item<float>();
                float cap = resCap * std::abs(accel_phys) + resCapMin;
                cap = std::max(cap, resCapFloorMin);  // floor to prevent near-zero cap
                accel_res = std::clamp(accel_res, -cap, cap);
                accel = accel_phys + accel_res;
            } else {
                auto accel_real = yStd.inverse(accel_out_scaled).cpu();
                accel = accel_real[0][0].item<float>();
            }
            
            // Check for NaN/Inf
            if (!std::isfinite(accel)) {
                valid_traj = false;
                break;
            }
            
            // Kinematics update
            float vel_prev = vel;
            vel = vel + accel * dt;
            pos = pos + vel_prev * dt + 0.5f * accel * dt * dt;
            
            // Ground truth at next step
            float gt_pos = static_cast<float>(traj.positions[k + 1]);
            float gt_vel = static_cast<float>(traj.velocities[k + 1]);
            
            // Accumulate squared error
            float pos_err = pos - gt_pos;
            float vel_err = vel - gt_vel;
            traj_mse += static_cast<double>(pos_err * pos_err + vel_err * vel_err);
        }
        
        if (valid_traj && steps > 0) {
            traj_mse /= static_cast<double>(steps);
            total_mse += traj_mse;
            valid_count++;
        }
    }
    
    if (valid_count == 0) {
        std::cerr << "  [WARNING] All validation rollouts produced NaN/Inf." << std::endl;
        return 0.0;
    }
    
    return total_mse / static_cast<double>(valid_count);
}

// Evaluate test set rollouts and print summary
// PINN-style: NN outputs acceleration, kinematics integrates state
bool SingleBodyEvaluator::evaluateTestRollouts(
    SingleBodyMLP& model,
    const std::vector<std::unique_ptr<SingleBodyTrajectoryData>>& testTrajs,
    const SingleBodyStandardizer& xStd,
    const SingleBodyStandardizer& yStd,
    bool useResidualPINN) const {
    
    if (testTrajs.empty()) {
        std::cout << "\nNo TEST trajectories; skipping rollout evaluation." << std::endl;
        return false;
    }
    
    std::vector<double> pos_rmse, vel_rmse;
    pos_rmse.reserve(testTrajs.size());
    vel_rmse.reserve(testTrajs.size());
    
    std::cout << "\nEvaluating on " << testTrajs.size() << " test trajectories (PINN-style kinematics)..." << std::endl;
    
    // Move standardizers to device for rollout
    SingleBodyStandardizer xStd_device, yStd_device;
    xStd_device.mean = xStd.mean.to(device_);
    xStd_device.std = xStd.std.to(device_);
    yStd_device.mean = yStd.mean.to(device_);
    yStd_device.std = yStd.std.to(device_);
    
    for (size_t i = 0; i < testTrajs.size(); ++i) {
        auto [x_true, x_pred] = rolloutTrajectory(model, *testTrajs[i], xStd_device, yStd_device, useResidualPINN);
        
        // Check for empty tensors
        if (x_true.size(0) == 0 || x_pred.size(0) == 0) {
            std::cout << "\r  [WARNING] Trajectory " << (i + 1) << " produced empty rollout, skipping.          " << std::endl;
            continue;
        }
        
        // Compute error (both are shape [T, 2]: [pos, vel])
        auto err = x_true - x_pred;
        
        // Check for NaN/Inf in error tensor
        if (!torch::isfinite(err).all().item<bool>()) {
            std::cout << "\r  [WARNING] Trajectory " << (i + 1) << " produced NaN/Inf errors, skipping.          " << std::endl;
            continue;
        }
        
        // RMSE for position (column 0)
        double rmse_pos = std::sqrt(torch::mean(err.index({torch::indexing::Slice(), 0}).pow(2)).item<double>());
        
        // RMSE for velocity (column 1)
        double rmse_vel = std::sqrt(torch::mean(err.index({torch::indexing::Slice(), 1}).pow(2)).item<double>());
        
        // Only add if finite
        if (std::isfinite(rmse_pos) && std::isfinite(rmse_vel)) {
            pos_rmse.push_back(rmse_pos);
            vel_rmse.push_back(rmse_vel);
        }
        
        std::cout << "\rEvaluating trajectory " << (i + 1) << " / " << testTrajs.size() << "          " << std::flush;
    }
    std::cout << std::endl;
    
    if (pos_rmse.empty()) {
        std::cout << "\n  [WARNING] No valid test trajectories for RMSE computation." << std::endl;
        return false;
    }
    
    // Helper to compute mean and std
    auto meanStd = [](const std::vector<double>& v) -> std::pair<double, double> {
        if (v.empty()) return {0.0, 0.0};
        
        double mean = 0.0;
        for (double x : v) mean += x;
        mean /= static_cast<double>(v.size());
        
        double var = 0.0;
        for (double x : v) var += (x - mean) * (x - mean);
        var /= static_cast<double>(v.size());
        
        return {mean, std::sqrt(var)};
    };
    
    auto [meanPos, stdPos] = meanStd(pos_rmse);
    auto [meanVel, stdVel] = meanStd(vel_rmse);
    
    // Find max (worst case) for debugging
    double maxPos = *std::max_element(pos_rmse.begin(), pos_rmse.end());
    double maxVel = *std::max_element(vel_rmse.begin(), vel_rmse.end());
    
    std::cout << "\n=== Test Set Rollout RMSE ===" << std::endl;
    std::cout << "Position (m)   | mean: " << std::fixed << std::setprecision(6) << meanPos 
            << "  std: " << stdPos << "  max: " << maxPos << std::endl;
    std::cout << "Velocity (m/s) | mean: " << std::fixed << std::setprecision(6) << meanVel 
            << "  std: " << stdVel << "  max: " << maxVel << std::endl;
    
    std::cout << "Evaluated " << pos_rmse.size() << " / " << testTrajs.size() << " trajectories successfully." << std::endl;
    
    return true;
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
//                                                                               SingleBodyDataGenerator
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// CONSTRUCTOR
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

SingleBodyDataGenerator::SingleBodyDataGenerator(const std::string& bodyName)
    : bodyName_(bodyName) {
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PRIVATE METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Get the bodies to generate data for (single body if bodyName_ is set, otherwise all common bodies)
std::vector<Body> SingleBodyDataGenerator::getBodiesToGenerate() const {
    if (!bodyName_.empty()) {
        // Find the specific body
        if (bodyName_ == "Sun") return {CelestialBody::sun};
        if (bodyName_ == "Mercury") return {CelestialBody::mercury};
        if (bodyName_ == "Venus") return {CelestialBody::venus};
        if (bodyName_ == "Earth") return {CelestialBody::earth};
        if (bodyName_ == "Mars") return {CelestialBody::mars};
        if (bodyName_ == "Jupiter") return {CelestialBody::jupiter};
        if (bodyName_ == "Saturn") return {CelestialBody::saturn};
        if (bodyName_ == "Uranus") return {CelestialBody::uranus};
        if (bodyName_ == "Neptune") return {CelestialBody::neptune};
        if (bodyName_ == "Pluto") return {CelestialBody::pluto};
        // If not found, fallback to common bodies
        std::cerr << "Warning: Unknown body name '" << bodyName_ << "', using common bodies" << std::endl;
    }
    // Return all common bodies as a vector
    std::vector<Body> bodies;
    for (const auto& body : CelestialBody::commonBodies) {
        bodies.push_back(body);
    }
    return bodies;
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PROTECTED METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Choose grid bins such that a*b >= n, preferring near-square grids
std::pair<int, int> SingleBodyDataGenerator::chooseGridBins(int n) {
    if (n <= 0) {
        return {1, 1};
    }
    
    int a = static_cast<int>(std::floor(std::sqrt(static_cast<double>(n))));
    if (a < 1) {
        a = 1;
    }
    
    int b = (n + a - 1) / a;  // ceil(n / a)
    if (b < 1) {
        b = 1;
    }
    
    return {a, b};
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PUBLIC METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Main entry point for generating single body data
void SingleBodyDataGenerator::generateSingleBodyData(bool generateTrain, int perTrain, int perVal, int perTest, uint32_t seed) {
    if (!bodyName_.empty()) {
        std::cout << "Generating single body data for " << bodyName_ << " (train/val/test)..." << std::endl;
    } else {
        std::cout << "Generating single body data for all bodies (train/val/test)..." << std::endl;
    }
    
    // Validate inputs: clamp negatives to 0
    if (perTrain < 0) perTrain = 0;
    if (perVal < 0) perVal = 0;
    if (perTest < 0) perTest = 0;
    
    const int totalPerSet = perTrain + perVal + perTest;
    if (totalPerSet == 0) {
        std::cout << "No data to generate." << std::endl;
        return;
    }
    
    // Determine directories based on whether we have a specific body
    std::string trainDir, valDir, testDir;
    if (!bodyName_.empty()) {
        trainDir = UniversalConstants::getSingleBodyTrainDir(bodyName_);
        valDir = UniversalConstants::getSingleBodyValDir(bodyName_);
        testDir = UniversalConstants::getSingleBodyTestDir(bodyName_);
    } else {
        trainDir = UniversalConstants::singleBodyTrainDir;
        valDir = UniversalConstants::singleBodyValDir;
        testDir = UniversalConstants::singleBodyTestDir;
    }
    
    // Ensure directories exist
    SystemUtilities::createDirectory(trainDir);
    SystemUtilities::createDirectory(valDir);
    SystemUtilities::createDirectory(testDir);
    
    // Check which directories are empty
    bool trainDirEmpty = CSVUtilities::checkForEmptyDirectory(trainDir);
    bool valDirEmpty = CSVUtilities::checkForEmptyDirectory(valDir);
    bool testDirEmpty = CSVUtilities::checkForEmptyDirectory(testDir);
    
    // Prevent freezing an empty benchmark by accident
    if (valDirEmpty && perVal == 0) {
        std::cerr << "VAL directory is empty but perVal==0; cannot create a validation set." << std::endl;
        return;
    }
    if (testDirEmpty && perTest == 0) {
        std::cerr << "TEST directory is empty but perTest==0; cannot create a test set." << std::endl;
        return;
    }
    
    // If both VAL and TEST are missing, prefer generating ALL THREE splits disjoint.
    // This guarantees TRAIN/VAL/TEST have no overlap (per body) for this dataset version.
    if (valDirEmpty && testDirEmpty) {
        if (trainDirEmpty || generateTrain) {
            generateTrainValTestDataDisjoint(perTrain, perVal, perTest, seed);
        } else {
            // TRAIN already exists; we can still generate VAL/TEST disjoint from each other,
            // but they may overlap with the existing TRAIN set.
            generateValTestDataDisjoint(perVal, perTest, seed);
        }
    } else {
        // Normal behavior: keep existing VAL/TEST fixed; only generate missing splits.
        if (trainDirEmpty || generateTrain) {
            generateTrainData(perTrain, seed);
        }
        if (valDirEmpty) {
            generateValData(perVal, seed);
        }
        if (testDirEmpty) {
            generateTestData(perTest, seed);
        }
    }
}

// Generate training data (simple, non-disjoint)
void SingleBodyDataGenerator::generateTrainData(int perTrain, uint32_t seed) {
    std::cout << "Generating single body training data..." << std::endl;
    
    std::vector<Body> bodiesToGenerate = getBodiesToGenerate();
    const int perBodyTrajectories = std::max(0, perTrain);
    
    if (perBodyTrajectories == 0) {
        std::cout << "perTrain is 0; no training trajectories to generate." << std::endl;
        return;
    }
    
    // Choose bin counts such that (posBins * velBins) >= perBodyTrajectories
    auto [posBins, velBins] = chooseGridBins(perBodyTrajectories);
    auto [spanBins, stepBins] = chooseGridBins(perBodyTrajectories);
    
    std::cout << "Per-body trajectories: " << perBodyTrajectories
            << " | IC bins: " << posBins << "x" << velBins
            << " | NumMethod bins: " << spanBins << "x" << stepBins
            << std::endl;
    
    // Reuse one solver instance for all trajectories
    Solvers solver_instance;
    
    for (size_t bodyIndex = 0; bodyIndex < bodiesToGenerate.size(); ++bodyIndex) {
        Body body = bodiesToGenerate[bodyIndex];
        
        // Get body-specific directory
        std::string trainDir = UniversalConstants::getSingleBodyTrainDir(body.name);
        SystemUtilities::createDirectory(trainDir);
        
        // Generate in deterministic bin order; shuffle deterministically using seed
        auto projectileICs = CelestialBody::generateUniformSingleBodyProjectileIC(posBins, velBins, false);
        auto numParams = CelestialBody::generateUniformSingleBodyNumMethodParams(spanBins, stepBins, false);
        
        const int poolN = std::min(
            static_cast<int>(projectileICs.size()),
            static_cast<int>(numParams.size()));
        const int N = std::min(poolN, perBodyTrajectories);
        
        if (N <= 0) {
            std::cout << "No usable IC/num-method pairs for body: " << body.name << std::endl;
            continue;
        }
        
        // Deterministic shuffle of indices so the dataset is reproducible for a given seed
        std::vector<int> order(poolN);
        std::iota(order.begin(), order.end(), 0);
        
        // Mix seed with bodyIndex so each body gets a different (but repeatable) ordering
        std::mt19937 rng(seed ^ (0x9E3779B9u + static_cast<uint32_t>(bodyIndex)));
        std::shuffle(order.begin(), order.end(), rng);
        
        for (int i = 0; i < N; ++i) {
            const int idx = order[i];
            
            auto [pos0, vel0] = projectileICs[idx];
            auto [timeSpan, timeStep] = numParams[idx];
            
            SingleBodyIC initialConditions = {
                pos0,
                vel0,
                body.name,
                body.mass,
                body.radius,
                0.0,
                timeSpan,
                timeStep
            };
            
            SingleBodySolution solution = solver_instance.RK4SingleBody(initialConditions);
            
            CSVUtilities::writeSingleBodySimDataCSV(
                initialConditions,
                solution,
                trainDir);
            
            std::cout << "\rGenerated TRAIN trajectory " << (i + 1) << " / " << N
                    << " for body: " << body.name << "          " << std::flush;
        }
        
        std::cout << std::endl;
    }
}

// Generate validation data (simple, non-disjoint)
void SingleBodyDataGenerator::generateValData(int perVal, uint32_t seed) {
    std::cout << "Generating single body validation data..." << std::endl;
    
    std::vector<Body> bodiesToGenerate = getBodiesToGenerate();
    const int perBodyTrajectories = std::max(0, perVal);
    
    if (perBodyTrajectories == 0) {
        std::cout << "perVal is 0; no validation trajectories to generate." << std::endl;
        return;
    }
    
    // Pick bins so we have at least perBodyTrajectories combinations available
    auto [posBins, velBins] = chooseGridBins(perBodyTrajectories);
    auto [spanBins, stepBins] = chooseGridBins(perBodyTrajectories);
    
    std::cout << "Per-body trajectories: " << perBodyTrajectories
            << " | IC bins: " << posBins << "x" << velBins
            << " | NumMethod bins: " << spanBins << "x" << stepBins
            << std::endl;
    
    Solvers solver_instance;
    
    for (size_t bodyIndex = 0; bodyIndex < bodiesToGenerate.size(); ++bodyIndex) {
        Body body = bodiesToGenerate[bodyIndex];
        
        // Get body-specific directory
        std::string valDir = UniversalConstants::getSingleBodyValDir(body.name);
        SystemUtilities::createDirectory(valDir);
        
        // Deterministic bin order; we shuffle deterministically below with seed
        auto projectileICs = CelestialBody::generateUniformSingleBodyProjectileIC(posBins, velBins, false);
        auto numParams = CelestialBody::generateUniformSingleBodyNumMethodParams(spanBins, stepBins, false);
        
        const int poolN = std::min(
            static_cast<int>(projectileICs.size()),
            static_cast<int>(numParams.size()));
        const int N = std::min(poolN, perBodyTrajectories);
        
        if (N <= 0) {
            std::cout << "No usable IC/num-method pairs for body: " << body.name << std::endl;
            continue;
        }
        
        // IMPORTANT: use a different seed mix than training so val doesn't mirror train
        std::vector<int> order(poolN);
        std::iota(order.begin(), order.end(), 0);
        
        // Mix in a constant unique to VAL so it produces a different permutation than TRAIN
        std::mt19937 rng(seed ^ 0xA5A5A5A5u ^ (0x9E3779B9u + static_cast<uint32_t>(bodyIndex)));
        std::shuffle(order.begin(), order.end(), rng);
        
        for (int i = 0; i < N; ++i) {
            const int idx = order[i];
            
            auto [pos0, vel0] = projectileICs[idx];
            auto [timeSpan, timeStep] = numParams[idx];
            
            SingleBodyIC initialConditions = {
                pos0,
                vel0,
                body.name,
                body.mass,
                body.radius,
                0.0,
                timeSpan,
                timeStep
            };
            
            SingleBodySolution solution = solver_instance.RK4SingleBody(initialConditions);
            
            CSVUtilities::writeSingleBodySimDataCSV(
                initialConditions,
                solution,
                valDir);
            
            std::cout << "\rGenerated VAL trajectory " << (i + 1) << " / " << N
                    << " for body: " << body.name << "          " << std::flush;
        }
        
        std::cout << std::endl;
    }
}

// Generate test data (simple, non-disjoint)
void SingleBodyDataGenerator::generateTestData(int perTest, uint32_t seed) {
    std::cout << "Generating single body test data..." << std::endl;
    
    std::vector<Body> bodiesToGenerate = getBodiesToGenerate();
    const int perBodyTrajectories = std::max(0, perTest);
    
    if (perBodyTrajectories == 0) {
        std::cout << "perTest is 0; no test trajectories to generate." << std::endl;
        return;
    }
    
    auto [posBins, velBins] = chooseGridBins(perBodyTrajectories);
    auto [spanBins, stepBins] = chooseGridBins(perBodyTrajectories);
    
    std::cout << "Per-body trajectories: " << perBodyTrajectories
            << " | IC bins: " << posBins << "x" << velBins
            << " | NumMethod bins: " << spanBins << "x" << stepBins
            << std::endl;
    
    Solvers solver_instance;
    
    for (size_t bodyIndex = 0; bodyIndex < bodiesToGenerate.size(); ++bodyIndex) {
        Body body = bodiesToGenerate[bodyIndex];
        
        // Generate in deterministic bin order; shuffle deterministically using seed
        auto projectileICs = CelestialBody::generateUniformSingleBodyProjectileIC(posBins, velBins, false);
        auto numParams = CelestialBody::generateUniformSingleBodyNumMethodParams(spanBins, stepBins, false);
        
        const int poolN = std::min(
            static_cast<int>(projectileICs.size()),
            static_cast<int>(numParams.size()));
        const int N = std::min(poolN, perBodyTrajectories);
        
        if (N <= 0) {
            std::cout << "No usable IC/num-method pairs for body: " << body.name << std::endl;
            continue;
        }
        
        // Get body-specific directory
        std::string testDir = UniversalConstants::getSingleBodyTestDir(body.name);
        SystemUtilities::createDirectory(testDir);
        
        // IMPORTANT: use a different seed mix than training/val so test doesn't mirror them
        std::vector<int> order(poolN);
        std::iota(order.begin(), order.end(), 0);
        
        // Mix in a constant unique to TEST so it produces a different permutation than TRAIN/VAL
        std::mt19937 rng(seed ^ 0x5A5A5A5Au ^ (0x9E3779B9u + static_cast<uint32_t>(bodyIndex)));
        std::shuffle(order.begin(), order.end(), rng);
        
        for (int i = 0; i < N; ++i) {
            const int idx = order[i];
            
            auto [pos0, vel0] = projectileICs[idx];
            auto [timeSpan, timeStep] = numParams[idx];
            
            SingleBodyIC initialConditions = {
                pos0,
                vel0,
                body.name,
                body.mass,
                body.radius,
                0.0,
                timeSpan,
                timeStep
            };
            
            SingleBodySolution solution = solver_instance.RK4SingleBody(initialConditions);
            
            CSVUtilities::writeSingleBodySimDataCSV(
                initialConditions,
                solution,
                testDir);
            
            std::cout << "\rGenerated TEST trajectory " << (i + 1) << " / " << N
                    << " for body: " << body.name << "          " << std::flush;
        }
        
        std::cout << std::endl;
    }
}

// Generate disjoint validation and test data (per-body no overlap)
void SingleBodyDataGenerator::generateValTestDataDisjoint(int perVal, int perTest, uint32_t seed) {
    std::cout << "Generating single body validation + test data (disjoint)..." << std::endl;
    
    std::vector<Body> bodiesToGenerate = getBodiesToGenerate();
    const int perBodyVal = std::max(0, perVal);
    const int perBodyTest = std::max(0, perTest);
    const int perBodyTotal = perBodyVal + perBodyTest;
    
    if (perBodyTotal == 0) {
        std::cout << "perVal and perTest are 0; no validation/test trajectories to generate." << std::endl;
        return;
    }
    
    // Bins sized to cover BOTH val + test
    auto [posBins, velBins] = chooseGridBins(perBodyTotal);
    auto [spanBins, stepBins] = chooseGridBins(perBodyTotal);
    
    std::cout << "Per-body val/test: " << perBodyVal << "/" << perBodyTest
            << " | IC bins: " << posBins << "x" << velBins
            << " | NumMethod bins: " << spanBins << "x" << stepBins
            << std::endl;
    
    Solvers solver_instance;
    
    for (size_t bodyIndex = 0; bodyIndex < bodiesToGenerate.size(); ++bodyIndex) {
        Body body = bodiesToGenerate[bodyIndex];
        
        // Get body-specific directories
        std::string valDir = UniversalConstants::getSingleBodyValDir(body.name);
        std::string testDir = UniversalConstants::getSingleBodyTestDir(body.name);
        SystemUtilities::createDirectory(valDir);
        SystemUtilities::createDirectory(testDir);
        
        auto projectileICs = CelestialBody::generateUniformSingleBodyProjectileIC(posBins, velBins, false);
        auto numParams = CelestialBody::generateUniformSingleBodyNumMethodParams(spanBins, stepBins, false);
        
        const int poolN = std::min(static_cast<int>(projectileICs.size()), static_cast<int>(numParams.size()));
        const int N = std::min(poolN, perBodyTotal);
        
        if (N <= 0) {
            std::cout << "No usable IC/num-method pairs for body: " << body.name << std::endl;
            continue;
        }
        
        // ONE order per body, ONE seed, then slice
        std::vector<int> order(poolN);
        std::iota(order.begin(), order.end(), 0);
        
        std::mt19937 rng(seed ^ 0xC0FFEE01u ^ (0x9E3779B9u + static_cast<uint32_t>(bodyIndex)));
        std::shuffle(order.begin(), order.end(), rng);
        
        // --- VAL slice ---
        const int valN = std::min(perBodyVal, N);
        for (int i = 0; i < valN; ++i) {
            int idx = order[i];
            auto [pos0, vel0] = projectileICs[idx];
            auto [timeSpan, timeStep] = numParams[idx];
            
            SingleBodyIC ic = {pos0, vel0, body.name, body.mass, body.radius, 0.0, timeSpan, timeStep};
            auto sol = solver_instance.RK4SingleBody(ic);
            
            CSVUtilities::writeSingleBodySimDataCSV(ic, sol, valDir);
            
            std::cout << "\rGenerated VAL trajectory " << (i + 1) << " / " << valN
                    << " for body: " << body.name << "          " << std::flush;
        }
        std::cout << std::endl;
        
        // --- TEST slice ---
        const int testStart = valN;
        const int testAvail = std::max(0, N - testStart);
        const int testN = std::min(perBodyTest, testAvail);
        
        for (int i = 0; i < testN; ++i) {
            int idx = order[testStart + i];
            auto [pos0, vel0] = projectileICs[idx];
            auto [timeSpan, timeStep] = numParams[idx];
            
            SingleBodyIC ic = {pos0, vel0, body.name, body.mass, body.radius, 0.0, timeSpan, timeStep};
            auto sol = solver_instance.RK4SingleBody(ic);
            
            CSVUtilities::writeSingleBodySimDataCSV(ic, sol, testDir);
            
            std::cout << "\rGenerated TEST trajectory " << (i + 1) << " / " << testN
                    << " for body: " << body.name << "          " << std::flush;
        }
        std::cout << std::endl;
    }
}

// Generate disjoint train, validation, and test data (per-body no overlap)
void SingleBodyDataGenerator::generateTrainValTestDataDisjoint(int perTrain, int perVal, int perTest, uint32_t seed) {
    std::cout << "Generating single body training + validation + test data (disjoint)..." << std::endl;
    
    std::vector<Body> bodiesToGenerate = getBodiesToGenerate();
    const int perBodyTrain = std::max(0, perTrain);
    const int perBodyVal = std::max(0, perVal);
    const int perBodyTest = std::max(0, perTest);
    const int perBodyTotal = perBodyTrain + perBodyVal + perBodyTest;
    
    if (perBodyTotal == 0) {
        std::cout << "perTrain/perVal/perTest are 0; no trajectories to generate." << std::endl;
        return;
    }
    
    // Choose bins so we have at least (train + val + test) combos available
    auto [posBins, velBins] = chooseGridBins(perBodyTotal);
    auto [spanBins, stepBins] = chooseGridBins(perBodyTotal);
    
    std::cout << "Per-body split (train/val/test): "
            << perBodyTrain << "/" << perBodyVal << "/" << perBodyTest
            << " | IC bins: " << posBins << "x" << velBins
            << " | NumMethod bins: " << spanBins << "x" << stepBins
            << std::endl;
    
    Solvers solver_instance;
    
    for (size_t bodyIndex = 0; bodyIndex < bodiesToGenerate.size(); ++bodyIndex) {
        Body body = bodiesToGenerate[bodyIndex];
        
        // Get body-specific directories
        std::string trainDir = UniversalConstants::getSingleBodyTrainDir(body.name);
        std::string valDir = UniversalConstants::getSingleBodyValDir(body.name);
        std::string testDir = UniversalConstants::getSingleBodyTestDir(body.name);
        SystemUtilities::createDirectory(trainDir);
        SystemUtilities::createDirectory(valDir);
        SystemUtilities::createDirectory(testDir);
        
        // Deterministic bin order; shuffle deterministically below with seed
        auto projectileICs = CelestialBody::generateUniformSingleBodyProjectileIC(posBins, velBins, false);
        auto numParams = CelestialBody::generateUniformSingleBodyNumMethodParams(spanBins, stepBins, false);
        
        const int poolN = std::min(static_cast<int>(projectileICs.size()), static_cast<int>(numParams.size()));
        const int N = std::min(poolN, perBodyTotal);
        
        if (N <= 0) {
            std::cout << "No usable IC/num-method pairs for body: " << body.name << std::endl;
            continue;
        }
        
        // ONE order per body, ONE seed, then slice TRAIN -> VAL -> TEST
        std::vector<int> order(poolN);
        std::iota(order.begin(), order.end(), 0);
        
        // Unique salt so this pool is not identical to your other generators
        std::mt19937 rng(seed ^ 0xD15C0DEu ^ (0x9E3779B9u + static_cast<uint32_t>(bodyIndex)));
        std::shuffle(order.begin(), order.end(), rng);
        
        const int trainN = std::min(perBodyTrain, N);
        const int valN = std::min(perBodyVal, std::max(0, N - trainN));
        const int testN = std::min(perBodyTest, std::max(0, N - trainN - valN));
        
        // --- TRAIN slice ---
        for (int i = 0; i < trainN; ++i) {
            const int idx = order[i];
            auto [pos0, vel0] = projectileICs[idx];
            auto [timeSpan, timeStep] = numParams[idx];
            
            SingleBodyIC ic = {pos0, vel0, body.name, body.mass, body.radius, 0.0, timeSpan, timeStep};
            auto sol = solver_instance.RK4SingleBody(ic);
            
            CSVUtilities::writeSingleBodySimDataCSV(ic, sol, trainDir);
            
            std::cout << "\rGenerated TRAIN trajectory " << (i + 1) << " / " << trainN
                    << " for body: " << body.name << "          " << std::flush;
        }
        std::cout << std::endl;
        
        // --- VAL slice ---
        const int valStart = trainN;
        for (int i = 0; i < valN; ++i) {
            const int idx = order[valStart + i];
            auto [pos0, vel0] = projectileICs[idx];
            auto [timeSpan, timeStep] = numParams[idx];
            
            SingleBodyIC ic = {pos0, vel0, body.name, body.mass, body.radius, 0.0, timeSpan, timeStep};
            auto sol = solver_instance.RK4SingleBody(ic);
            
            CSVUtilities::writeSingleBodySimDataCSV(ic, sol, valDir);
            
            std::cout << "\rGenerated VAL trajectory " << (i + 1) << " / " << valN
                    << " for body: " << body.name << "          " << std::flush;
        }
        std::cout << std::endl;
        
        // --- TEST slice ---
        const int testStart = trainN + valN;
        for (int i = 0; i < testN; ++i) {
            const int idx = order[testStart + i];
            auto [pos0, vel0] = projectileICs[idx];
            auto [timeSpan, timeStep] = numParams[idx];
            
            SingleBodyIC ic = {pos0, vel0, body.name, body.mass, body.radius, 0.0, timeSpan, timeStep};
            auto sol = solver_instance.RK4SingleBody(ic);
            
            CSVUtilities::writeSingleBodySimDataCSV(ic, sol, testDir);
            
            std::cout << "\rGenerated TEST trajectory " << (i + 1) << " / " << testN
                    << " for body: " << body.name << "          " << std::flush;
        }
        std::cout << std::endl;
    }
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
//                                                                               SingleBodyTorchModel
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PUBLIC METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Constructor
SingleBodyTorchModel::SingleBodyTorchModel(const std::string& bodyName)
    : bodyName_(bodyName),
        device_(torch::kCPU),
        dataIO_(bodyName),
        datasetBuilder_(torch::kCPU),
        scalerMgr_(torch::kCPU),
        trainer_(torch::kCPU),
        evaluator_(torch::kCPU),
        dataGen_(bodyName) {
    
    // Set device (prefer MPS on macOS, then CUDA, then CPU)
    if (torch::mps::is_available()) {
        device_ = torch::Device(torch::kMPS);
        std::cout << "Using MPS (Apple Silicon GPU) device" << std::endl;
    } else if (torch::cuda::is_available()) {
        device_ = torch::Device(torch::kCUDA);
        std::cout << "Using CUDA device" << std::endl;
    } else {
        std::cout << "Using CPU device" << std::endl;
    }
    
    // Re-initialize micro-classes with the correct device
    datasetBuilder_ = SingleBodyDatasetBuilder(device_);
    scalerMgr_ = SingleBodyScalerManager(device_);
    trainer_ = SingleBodyTrainer(device_);
    evaluator_ = SingleBodyEvaluator(device_);
    
    if (!bodyName_.empty()) {
        std::cout << "SingleBodyTorchModel initialized for body: " << bodyName_ << std::endl;
    }
}

// Train the model
void SingleBodyTorchModel::train(bool resumeTraining) {
    std::cout << "\n=== LibTorch Single Body Model Training ===" << std::endl;
    if (!bodyName_.empty()) {
        std::cout << "Training model for body: " << bodyName_ << std::endl;
    } else {
        std::cout << "Training generic model (no specific body)" << std::endl;
    }
    
    // ----- DATA GENERATION CONFIG -----
    // Easy to tweak development parameters
    int perTrain = 800;
    int perVal = 100;
    int perTest = 100;
    uint32_t seed = 1337;
    
    // Ensure output directories exist
    if (!bodyName_.empty()) {
        SystemUtilities::createDirectory(UniversalConstants::getSingleBodyModelPath(bodyName_));
    } else {
        SystemUtilities::createDirectory(UniversalConstants::singleBodyModelsPath);
    }
    
    // ----- STEP 1: Generate data (disjoint splits) -----
    dataGen_.generateSingleBodyData(true, perTrain, perVal, perTest, seed);
    
    // ----- STEP 2: Get globs and load trajectories -----
    auto globs = dataIO_.getSplitGlobs();
    auto splitTrajs = dataIO_.loadSplitTrajectories(globs);
    
    // Check we have data
    if (splitTrajs.trainTrajs.empty()) {
        std::cerr << "ERROR: No training trajectories found. Aborting." << std::endl;
        return;
    }
    if (splitTrajs.valTrajs.empty()) {
        std::cerr << "ERROR: No validation trajectories found. Aborting." << std::endl;
        return;
    }
    
    // ----- STEP 3: Build tensors -----
    auto splitTensors = datasetBuilder_.buildSplitTensors(splitTrajs);
    
    std::cout << "Dataset sizes: train=" << splitTensors.X_train.size(0)
                << ", val=" << splitTensors.X_val.size(0)
                << ", test=" << splitTensors.X_test.size(0) << std::endl;
    
    // ----- STEP 4: Fit/load scalers and standardize -----
    auto sp = scalerPath();
    auto stdTensors = scalerMgr_.fitOrLoadAndStandardize(splitTensors, sp, resumeTraining);
    
    // Run scaler sanity check
    if (!scalerMgr_.runScalerSanityCheck(splitTensors, stdTensors.xStd, stdTensors.yStd)) {
        std::cerr << "Scaler sanity check failed! Aborting training." << std::endl;
        
        // Save failure summary
        std::map<std::string, double> failMetrics;
        failMetrics["scaler_sanity_check_failed"] = 1.0;
        SingleBodyTrainConfig failCfg;
        failCfg.epochs = 30;
        failCfg.resumeTraining = resumeTraining;
        saveTrainingSummary(summaryPath(), modelPath(), sp, globs,
                            static_cast<int>(splitTensors.X_train.size(0)),
                            static_cast<int>(splitTensors.X_val.size(0)),
                            static_cast<int>(splitTensors.X_test.size(0)),
                            failCfg, -1, failMetrics);
        return;
    }
    
    // ----- STEP 5: Initialize model -----
    auto mp = modelPath();
    auto trainingModel = trainer_.initializeModel(stdTensors, mp, sp, resumeTraining);
    
    // ----- STEP 6: Build training config -----
    SingleBodyTrainConfig cfg;
    
    // ----- STEP 7: Run training loop -----
    auto trained = trainer_.runTrainingLoop(trainingModel, cfg, stdTensors, splitTensors, splitTrajs);
    
    // ----- STEP 8: Model is saved by trainer, but ensure it's at the right path -----
    // (trainer already saves to trainingModel.modelPath in runTrainingLoop)
    
    // ----- STEP 9: Save scalers (only if we fit new ones) -----
    if (stdTensors.scalersLoadedFromDisk) {
        std::cout << "[dev] Scalers were loaded from disk; skipping overwrite." << std::endl;
    } else {
        scalerMgr_.saveScalers(sp, stdTensors.xStd, stdTensors.yStd);
        std::cout << "Scalers saved to: " << sp << std::endl;
    }
    
    // ----- STEP 10: Optional evaluations -----
    // Move standardizers to device for evaluation
    SingleBodyStandardizer xStd_device, yStd_device;
    xStd_device.mean = stdTensors.xStd.mean.to(device_);
    xStd_device.std = stdTensors.xStd.std.to(device_);
    yStd_device.mean = stdTensors.yStd.mean.to(device_);
    yStd_device.std = stdTensors.yStd.std.to(device_);
    
    if (cfg.runTestEval) {
        evaluator_.evaluateTestRollouts(trained.model, splitTrajs.testTrajs, xStd_device, yStd_device);
    } else {
        std::cout << "[dev] Skipping TEST set metrics." << std::endl;
    }
    
    if (cfg.runRolloutEval) {
        double valRolloutMse = evaluator_.computeValRolloutMse(
            trained.model, splitTrajs.valTrajs, xStd_device, yStd_device, 5, cfg.rolloutK);
        std::cout << "Validation rollout MSE: " << std::fixed << std::setprecision(6) << valRolloutMse << std::endl;
    } else {
        std::cout << "[dev] Skipping rollout RMSE evaluation." << std::endl;
    }
    
    // ----- STEP 11: Save training summary -----
    std::map<std::string, double> metrics;
    metrics["train_mse"] = trained.bestTrainMse;
    metrics["val_mse_scaled"] = trained.bestValMseScaled;
    metrics["val_mae_scaled"] = trained.bestValMaeScaled;
    metrics["val_mse_real"] = trained.bestValMseReal;
    metrics["val_mae_real"] = trained.bestValMaeReal;
    
    saveTrainingSummary(summaryPath(), mp, sp, globs,
                        static_cast<int>(splitTensors.X_train.size(0)),
                        static_cast<int>(splitTensors.X_val.size(0)),
                        static_cast<int>(splitTensors.X_test.size(0)),
                        cfg, trained.bestEpoch, metrics);
    
    std::cout << "\nTraining complete!" << std::endl;
}

// Predict trajectory using trained model
// PINN-style: NN outputs acceleration (or residual), kinematics integrates state
SingleBodySolution SingleBodyTorchModel::predict(SingleBodyIC initialConditions) {
    // Construct full paths from executable directory
    auto mp = modelPath();
    auto sp = scalerPath();
    
    // Check if model file exists
    if (!SystemUtilities::fileExists(mp)) {
        std::cerr << "ERROR: Model file not found: " << mp << std::endl;
        std::cerr << "Falling back to RK4 solution." << std::endl;
        Solvers solver;
        return solver.RK4SingleBody(initialConditions);
    }
    
    // Check if scaler file exists
    if (!SystemUtilities::fileExists(sp)) {
        std::cerr << "ERROR: Scaler file not found: " << sp << std::endl;
        std::cerr << "Falling back to RK4 solution." << std::endl;
        Solvers solver;
        return solver.RK4SingleBody(initialConditions);
    }
    
    try {
        // Load scalers
        SingleBodyStandardizer xStd, yStd;
        scalerMgr_.loadScalers(sp, xStd, yStd);
        
        // Move scalers to device
        xStd.mean = xStd.mean.to(device_);
        xStd.std = xStd.std.to(device_);
        yStd.mean = yStd.mean.to(device_);
        yStd.std = yStd.std.to(device_);
        
        // Create model with correct dimensions (PINN-style: out_dim=1 for acceleration)
        int64_t in_dim = datasetBuilder_.featureDim(true);  // 9
        int64_t out_dim = 1;  // acceleration only
        auto model = SingleBodyMLP(in_dim, out_dim);
        
        // Load model weights
        torch::load(model, mp);
        model->to(device_);
        model->eval();
        
        // Generate time array
        int num_steps = static_cast<int>(std::round(initialConditions.timeSpan / initialConditions.timeStep));
        if (num_steps < 1) num_steps = 1;
        
        std::vector<double> times(num_steps + 1);
        for (int i = 0; i <= num_steps; ++i) {
            times[i] = i * initialConditions.timeStep;
        }
        // Clamp the final time to the requested simTime to avoid accumulated rounding drift
        times.back() = initialConditions.timeSpan;
        
        // Initialize trajectory
        std::vector<double> positions(num_steps + 1);
        std::vector<double> velocities(num_steps + 1);
        positions[0] = initialConditions.initialPosition;
        velocities[0] = initialConditions.initialVelocity;
        
        // PINN residual config (use default settings)
        constexpr bool useResidualPINN = true;
        constexpr float resCap = 0.3f;
        constexpr float resCapMin = 1e-2f;
        constexpr float resCapFloorMin = 1e-3f;  // floor to prevent near-zero cap
        constexpr double G = 6.67430e-11;
        
        // Rollout using kinematics
        torch::NoGradGuard no_grad;
        float mass_f = static_cast<float>(initialConditions.bodyMass);
        float radius_f = static_cast<float>(initialConditions.bodyRadius);
        float initPos_f = static_cast<float>(initialConditions.initialPosition);
        float initVel_f = static_cast<float>(initialConditions.initialVelocity);
        float simTime_f = static_cast<float>(initialConditions.timeSpan);
        
        for (int k = 0; k < num_steps; ++k) {
            float tNorm = (simTime_f > 0.0f) ? (static_cast<float>(times[k]) / simTime_f) : 0.0f;
            float dt = static_cast<float>(initialConditions.timeStep);
            float pos_f = static_cast<float>(positions[k]);
            float vel_f = static_cast<float>(velocities[k]);
            
            // Build feature vector matching training layout EXACTLY:
            // [pos_t, vel_t, t_norm, dt, bodyMass, bodyRadius, initPosition, initVelocity, simTime]
            std::vector<float> feat = {
                pos_f,
                vel_f,
                tNorm,
                dt,
                mass_f,
                radius_f,
                initPos_f,
                initVel_f,
                simTime_f
            };
            
            auto feat_t = torch::from_blob(feat.data(), {1, 9}, torch::kFloat32).clone().to(device_);
            auto feat_scaled = xStd.transform(feat_t);
            auto accel_out_scaled = model->forward(feat_scaled);  // [1,1]
            
            // Get acceleration in real units
            float accel;
            if (useResidualPINN) {
                // Compute physics-based acceleration: -G*M/(R+pos)^2
                double r = static_cast<double>(radius_f + pos_f);
                r = std::max(std::abs(r), 1.0);  // Clamp to minimum 1 meter
                float accel_phys = static_cast<float>(-G * mass_f / (r * r));
                
                // Get residual from NN
                auto accel_res_real = yStd.inverse(accel_out_scaled).cpu();
                float accel_res = accel_res_real[0][0].item<float>();
                
                // Clamp residual with floor
                float cap = resCap * std::abs(accel_phys) + resCapMin;
                cap = std::max(cap, resCapFloorMin);  // floor to prevent near-zero cap
                accel_res = std::clamp(accel_res, -cap, cap);
                
                accel = accel_phys + accel_res;
            } else {
                auto accel_real = yStd.inverse(accel_out_scaled).cpu();
                accel = accel_real[0][0].item<float>();
            }
            
            // Check for NaN/Inf
            if (!std::isfinite(accel)) {
                std::cerr << "WARNING: NaN/Inf in prediction at step " << k << ", stopping early." << std::endl;
                // Pad remaining with last state
                for (int j = k + 1; j <= num_steps; ++j) {
                    positions[j] = positions[k];
                    velocities[j] = velocities[k];
                }
                break;
            }
            
            // Kinematics update: compute next state using physics equations
            // v_next = v + accel * dt
            // x_next = x + v * dt + 0.5 * accel * dt^2
            velocities[k + 1] = velocities[k] + static_cast<double>(accel * dt);
            positions[k + 1] = positions[k] + velocities[k] * dt + 0.5 * static_cast<double>(accel * dt * dt);
        }
        
        return {positions, velocities, times};
        
    } catch (const std::exception& e) {
        std::cerr << "ERROR: Failed to load model or predict: " << e.what() << std::endl;
        std::cerr << "Falling back to RK4 solution." << std::endl;
        Solvers solver;
        return solver.RK4SingleBody(initialConditions);
    }
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PRIVATE METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Get path to model file
std::string SingleBodyTorchModel::modelPath() const {
    std::filesystem::path execDir = SystemUtilities::getExecutableDir();
    if (!bodyName_.empty()) {
        return (execDir / UniversalConstants::getSingleBodyModelFilePath(bodyName_)).string();
    }
    std::filesystem::path fullOutDir = execDir / UniversalConstants::singleBodyModelsPath;
    return (fullOutDir / UniversalConstants::singleBodyModelName).string();
}

// Get path to scaler file
std::string SingleBodyTorchModel::scalerPath() const {
    std::filesystem::path execDir = SystemUtilities::getExecutableDir();
    if (!bodyName_.empty()) {
        return (execDir / UniversalConstants::getSingleBodyScalersFilePath(bodyName_)).string();
    }
    std::filesystem::path fullOutDir = execDir / UniversalConstants::singleBodyModelsPath;
    return (fullOutDir / UniversalConstants::singleBodyModelScalers).string();
}

// Get path to summary file
std::string SingleBodyTorchModel::summaryPath() const {
    std::filesystem::path execDir = SystemUtilities::getExecutableDir();
    if (!bodyName_.empty()) {
        return (execDir / UniversalConstants::getSingleBodySummaryFilePath(bodyName_)).string();
    }
    std::filesystem::path fullOutDir = execDir / UniversalConstants::singleBodyModelsPath;
    return (fullOutDir / UniversalConstants::singleBodyModelSummary).string();
}

// Save training summary to JSON
void SingleBodyTorchModel::saveTrainingSummary(
    const std::string& summaryPathArg,
    const std::string& modelPathArg,
    const std::string& scalerPathArg,
    const SingleBodySplitGlobs& globs,
    int trainCount,
    int valCount,
    int testCount,
    const SingleBodyTrainConfig& cfg,
    int best_epoch,
    const std::map<std::string, double>& metrics) const {
    
    try {
        // Ensure parent directory exists
        std::filesystem::path summaryDir = std::filesystem::path(summaryPathArg).parent_path();
        SystemUtilities::createDirectory(summaryDir.string());
        
        json j;
        
        // Timestamp
        auto now = std::chrono::system_clock::now();
        auto time_t = std::chrono::system_clock::to_time_t(now);
        std::stringstream ss;
        ss << std::put_time(std::localtime(&time_t), "%Y-%m-%dT%H:%M:%S");
        j["timestamp"] = ss.str();
        
        // Device
        std::string device_str = "cpu";
        if (device_.type() == torch::kMPS) device_str = "mps";
        else if (device_.type() == torch::kCUDA) device_str = "cuda";
        j["device"] = device_str;
        
        // Paths
        j["paths"]["model"] = modelPathArg;
        j["paths"]["scalers"] = scalerPathArg;
        j["paths"]["train_glob"] = globs.trainGlob;
        j["paths"]["val_glob"] = globs.valGlob;
        j["paths"]["test_glob"] = globs.testGlob;
        
        // Dataset counts
        j["dataset"]["train_count"] = trainCount;
        j["dataset"]["val_count"] = valCount;
        j["dataset"]["test_count"] = testCount;
        
        // Model config
        j["model"]["input_dim"] = 9;
        j["model"]["output_dim"] = 2;
        j["model"]["hidden_sizes"] = {256, 256};
        
        // Training config
        j["training"]["epochs"] = cfg.epochs;
        j["training"]["batch_size"] = cfg.batchSize;
        j["training"]["resume_training"] = cfg.resumeTraining;
        j["training"]["run_test_eval"] = cfg.runTestEval;
        j["training"]["run_rollout_eval"] = cfg.runRolloutEval;
        j["training"]["use_rollout_loss"] = cfg.useRolloutLoss;
        j["training"]["compute_val_rollout_metric"] = cfg.computeValRolloutMetric;
        j["training"]["rollout_k"] = cfg.rolloutK;
        j["training"]["learning_rate"] = 1e-3;
        j["training"]["weight_decay"] = 1e-4;
        j["training"]["optimizer"] = "AdamW";
        j["training"]["loss"] = "MSE";
        j["training"]["best_epoch"] = best_epoch;
        
        // Metrics
        j["metrics"] = metrics;
        
        // Write to file
        std::ofstream file(summaryPathArg);
        if (!file.is_open()) {
            std::cerr << "ERROR: Could not open summary file for writing: " << summaryPathArg << std::endl;
            return;
        }
        file << j.dump(2);
        file.close();
        
        std::cout << "\nTraining summary saved to: " << summaryPathArg << std::endl;
        
    } catch (const std::exception& e) {
        std::cerr << "ERROR: Failed to save training summary: " << e.what() << std::endl;
    }
}

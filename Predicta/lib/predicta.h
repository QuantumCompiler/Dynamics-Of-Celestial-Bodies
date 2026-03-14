#pragma once
#include "celestial_bodies.h"
#include "constants.h"
#include "machine_learning.h"
#include "plotters.h"
#include "solvers.h"
#include "utilities.h"

class Predicta {
    public:
        // Generation Methods
        static Body autoBodyGenerator();
        static std::array<double, 2> autoSingleBodyNumMethodGenerator();
        static std::array<double, 2> autoSingleBodyProjectileICGenerator();
        static std::array<double, 2> autoTwoBodyNumMethodGenerator(Body body1, Body body2);
        static std::array<double, 2> autoThreeBodyNumMethodGenerator(Body body1, Body body2, Body body3);
        static std::array<double, 2> autoThreeBodyNumMethodGenerator();
        static std::array<double, 2> autoNBodyNumMethodGenerator(const std::vector<Body>& bodies);
        static std::array<double, 2> autoNBodyNumMethodGenerator();
        static Body manualBodyGenerator();
        static std::array<double, 2> manualSingleBodyNumMethodGenerator();
        static std::array<double, 2> manualSingleBodyProjectileICGenerator();
        static std::array<double, 2> manualTwoBodyNumMethodGenerator();
        static std::array<double, 2> manualThreeBodyNumMethodGenerator();
        
        // Automatic Simulation Methods
        static void autoSingleBodySimulation();
        static void autoTwoBodySimulation();
        static void autoThreeBodySimulation();
        static void autoNBodySimulation();

        // Manual Simulation Methods
        static void manualSingleBodySimulation();
        static void manualTwoBodySimulation();
        static void manualThreeBodySimulation();
        static void manualNBodySimulation();
        static std::vector<Body> manualNBodiesGenerator();
        static std::array<double, 2> manualNBodyNumMethodGenerator();

        // Model Methods
        static void modelSingleBodyEvaluate();
        static void modelSingleBodyPredict();
        static void modelSingleBodyTrain();

        // Plotting Methods
        static void plotSingleBodyResult(std::string directory, bool isEvaluation = false);
        static void plotTwoBodyResult(std::string directory, bool isEvaluation = false);
        static void plotThreeBodyResult(std::string directory, bool isEvaluation = false);
        static void plotNBodyResult(std::string directory, bool isEvaluation = false);
        
        // Selection Methods
        static void automaticSimulationSelection();
        static void manualSimulationSelection();
        static void modelEvaluationSelection();
        static void modelPredictionSelection();
        static std::string modelSingleBodyEvaluateSelection();
        static std::string modelSingleBodyPredictSelection();
        static std::string modelSingleBodyTrainSelection();
        static void modelTrainSelection();
        static void plotSelection();
        static void modeSelection();
        static void utilitiesMenuSelection();
        static void returnToModeSelection();

        // Utility Methods
        static void eraseSingleBodyRK4Data();
        static void eraseSingleBodyEvalData();
        static void eraseSingleBodyPredictData();
        static void eraseSingleBodyTestData();
        static void eraseSingleBodyTrainingData();
        static void eraseSingleBodyValidationData();
        static void eraseSingleBodyModel();
        static void eraseTwoBodyRK4Data();
        static void eraseThreeBodyRK4Data();
        static void eraseNBodyRK4Data();

        // Main Run Method
        static void run();

    private:
        // Helper Methods
        static std::vector<std::pair<std::string, std::string>> getAvailableSingleBodyModels();
        static Body getBodyFromName(const std::string& bodyName);
        static std::vector<std::pair<std::string, std::string>> getAvailableDataDirectories(const std::string& dataType);
        static std::pair<std::string, std::string> plotBodyWithDataSelection(const std::string& dataType, const std::string& prompt);
        static std::string utilityBodySelection(const std::string& prompt);
};
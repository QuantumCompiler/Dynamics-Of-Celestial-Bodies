#pragma once
#include <string>

class UniversalConstants {
    public:
        // Single body parameter constraints
        inline static const double maxSingleBodyPosition = 1e4;
        inline static const double maxSingleBodyTimeSpan = 60;
        inline static const double maxSingleBodyTimeStep = 0.01;
        inline static const double maxSingleBodyVelocity = 1e3;
        inline static const double minSingleBodyPosition = 0;
        inline static const double minSingleBodyTimeSpan = 5;
        inline static const double minSingleBodyTimeStep = 0.001;
        inline static const double minSingleBodyVelocity = 0;

        // Master Directories
        inline static const std::string resultsDir = "Results";
        inline static const std::string modelsDir = "Models";
        inline static const std::string singleBodySubDir = "Single Body";
        inline static const std::string twoBodySubDir = "Two Body";
        inline static const std::string threeBodySubDir = "Three Body";
        inline static const std::string nBodySubDir = "N Body";
        inline static const std::string numericalMethodsDir = resultsDir + "/" + "Numerical Methods";
        inline static const std::string machineLearningDir = resultsDir + "/" + "Machine Learning";
        inline static const std::string rk4Dir = numericalMethodsDir + "/" + "RK4";

        // File Names
        inline static const std::string singleBodyFile = "Single-Body";
        inline static const std::string twoBodyFile = "Two-Body";
        inline static const std::string threeBodyFile = "Three-Body";
        inline static const std::string nBodyFile = "N-Body";

        // Model Names
        inline static const std::string singleBodyModelName = "SingleBodyMLP.pt";
        inline static const std::string singleBodySunModelName = "SingleBodyMLP_Sun.pt";
        inline static const std::string singleBodyMercuryModelName = "SingleBodyMLP_Mercury.pt";
        inline static const std::string singleBodyVenusModelName = "SingleBodyMLP_Venus.pt";
        inline static const std::string singleBodyEarthModelName = "SingleBodyMLP_Earth.pt";
        inline static const std::string singleBodyMarsModelName = "SingleBodyMLP_Mars.pt";
        inline static const std::string singleBodyJupiterModelName = "SingleBodyMLP_Jupiter.pt";
        inline static const std::string singleBodySaturnModelName = "SingleBodyMLP_Saturn.pt";
        inline static const std::string singleBodyUranusModelName = "SingleBodyMLP_Uranus.pt";
        inline static const std::string singleBodyNeptuneModelName = "SingleBodyMLP_Neptune.pt";
        inline static const std::string singleBodyPlutoModelName = "SingleBodyMLP_Pluto.pt";
        // Model Directories And Paths
        inline static const std::string singleBodyModelsPath = modelsDir + "/" + singleBodySubDir;
        inline static const std::string twoBodyModelsPath = modelsDir + "/" + twoBodySubDir;
        inline static const std::string threeBodyModelsPath = modelsDir + "/" + threeBodySubDir;
        // Single Body paths
        inline static const std::string singleBodyModelsSunPath = singleBodyModelsPath + "/" + "Sun";
        inline static const std::string singleBodyModelsMercuryPath = singleBodyModelsPath + "/" + "Mercury";
        inline static const std::string singleBodyModelsVenusPath = singleBodyModelsPath + "/" + "Venus";
        inline static const std::string singleBodyModelsEarthPath = singleBodyModelsPath + "/" + "Earth";
        inline static const std::string singleBodyModelsMarsPath = singleBodyModelsPath + "/" + "Mars";
        inline static const std::string singleBodyModelsJupiterPath = singleBodyModelsPath + "/" + "Jupiter";
        inline static const std::string singleBodyModelsSaturnPath = singleBodyModelsPath + "/" + "Saturn";
        inline static const std::string singleBodyModelsUranusPath = singleBodyModelsPath + "/" + "Uranus";
        inline static const std::string singleBodyModelsNeptunePath = singleBodyModelsPath + "/" + "Neptune";
        inline static const std::string singleBodyModelsPlutoPath = singleBodyModelsPath + "/" + "Pluto";
        // Scaler Files
        inline static const std::string singleBodyModelScalers = "SingleBodyScalers.json";
        inline static const std::string singleBodySunModelScalers = "SingleBodyScalers_Sun.json";
        inline static const std::string singleBodyMercuryModelScalers = "SingleBodyScalers_Mercury.json";
        inline static const std::string singleBodyVenusModelScalers = "SingleBodyScalers_Venus.json";
        inline static const std::string singleBodyEarthModelScalers = "SingleBodyScalers_Earth.json";
        inline static const std::string singleBodyMarsModelScalers = "SingleBodyScalers_Mars.json";
        inline static const std::string singleBodyJupiterModelScalers = "SingleBodyScalers_Jupiter.json";
        inline static const std::string singleBodySaturnModelScalers = "SingleBodyScalers_Saturn.json";
        inline static const std::string singleBodyUranusModelScalers = "SingleBodyScalers_Uranus.json";
        inline static const std::string singleBodyNeptuneModelScalers = "SingleBodyScalers_Neptune.json";
        inline static const std::string singleBodyPlutoModelScalers = "SingleBodyScalers_Pluto.json";
        // Scaler Paths
        inline static const std::string singleBodyModelScalersPath = singleBodyModelsPath + "/" + singleBodyModelScalers;
        inline static const std::string singleBodyModelSunScalersPath = singleBodyModelsSunPath + "/" + singleBodySunModelScalers;
        inline static const std::string singleBodyModelMercuryScalersPath = singleBodyModelsMercuryPath + "/" + singleBodyMercuryModelScalers;
        inline static const std::string singleBodyModelVenusScalersPath = singleBodyModelsVenusPath + "/" + singleBodyVenusModelScalers;
        inline static const std::string singleBodyModelEarthScalersPath = singleBodyModelsEarthPath + "/" + singleBodyEarthModelScalers;
        inline static const std::string singleBodyModelMarsScalersPath = singleBodyModelsMarsPath + "/" + singleBodyMarsModelScalers;
        inline static const std::string singleBodyModelJupiterScalersPath = singleBodyModelsJupiterPath + "/" + singleBodyJupiterModelScalers;
        inline static const std::string singleBodyModelSaturnScalersPath = singleBodyModelsSaturnPath + "/" + singleBodySaturnModelScalers;
        inline static const std::string singleBodyModelUranusScalersPath = singleBodyModelsUranusPath + "/" + singleBodyUranusModelScalers;
        inline static const std::string singleBodyModelNeptuneScalersPath = singleBodyModelsNeptunePath + "/" + singleBodyNeptuneModelScalers;
        inline static const std::string singleBodyModelPlutoScalersPath = singleBodyModelsPlutoPath + "/" + singleBodyPlutoModelScalers;
        // Model Summary Files
        inline static const std::string singleBodyModelSummary = "SingleBodyMLP_RunSummary.json";
        inline static const std::string singleBodySunModelSummary = "SingleBodyMLP_Sun_RunSummary.json";
        inline static const std::string singleBodyMercuryModelSummary = "SingleBodyMLP_Mercury_RunSummary.json";
        inline static const std::string singleBodyVenusModelSummary = "SingleBodyMLP_Venus_RunSummary.json";
        inline static const std::string singleBodyEarthModelSummary = "SingleBodyMLP_Earth_RunSummary.json";
        inline static const std::string singleBodyMarsModelSummary = "SingleBodyMLP_Mars_RunSummary.json";
        inline static const std::string singleBodyJupiterModelSummary = "SingleBodyMLP_Jupiter_RunSummary.json";
        inline static const std::string singleBodySaturnModelSummary = "SingleBodyMLP_Saturn_RunSummary.json";
        inline static const std::string singleBodyUranusModelSummary = "SingleBodyMLP_Uranus_RunSummary.json";
        inline static const std::string singleBodyNeptuneModelSummary = "SingleBodyMLP_Neptune_RunSummary.json";
        inline static const std::string singleBodyPlutoModelSummary = "SingleBodyMLP_Pluto_RunSummary.json";
        // Model Summary Paths
        inline static const std::string singleBodyModelSummaryPath = singleBodyModelsPath + "/" + singleBodyModelSummary;
        inline static const std::string singleBodySunModelSummaryPath = singleBodyModelsSunPath + "/" + singleBodySunModelSummary;
        inline static const std::string singleBodyMercuryModelSummaryPath = singleBodyModelsMercuryPath + "/" + singleBodyMercuryModelSummary;
        inline static const std::string singleBodyVenusModelSummaryPath = singleBodyModelsVenusPath + "/" + singleBodyVenusModelSummary;
        inline static const std::string singleBodyEarthModelSummaryPath = singleBodyModelsEarthPath + "/" + singleBodyEarthModelSummary;
        inline static const std::string singleBodyMarsModelSummaryPath = singleBodyModelsMarsPath + "/" + singleBodyMarsModelSummary;
        inline static const std::string singleBodyJupiterModelSummaryPath = singleBodyModelsJupiterPath + "/" + singleBodyJupiterModelSummary;
        inline static const std::string singleBodySaturnModelSummaryPath = singleBodyModelsSaturnPath + "/" + singleBodySaturnModelSummary;
        inline static const std::string singleBodyUranusModelSummaryPath = singleBodyModelsUranusPath + "/" + singleBodyUranusModelSummary;
        inline static const std::string singleBodyNeptuneModelSummaryPath = singleBodyModelsNeptunePath + "/" + singleBodyNeptuneModelSummary;
        inline static const std::string singleBodyPlutoModelSummaryPath = singleBodyModelsPlutoPath + "/" + singleBodyPlutoModelSummary;
        // RK4 Results Directories
        inline static const std::string singleBodyRK4Dir = rk4Dir + "/" + singleBodySubDir;
        inline static const std::string twoBodyRK4Dir = rk4Dir + "/" + twoBodySubDir;
        inline static const std::string threeBodyRK4Dir = rk4Dir + "/" + threeBodySubDir;
        inline static const std::string nBodyRK4Dir = rk4Dir + "/" + nBodySubDir;
        // ML Predictions Directories
        inline static const std::string singleBodyModelPredictionsDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Prediction Data";
        inline static const std::string singleBodyModelSunPredictionsDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Sun" + "/" + "Prediction Data";
        inline static const std::string singleBodyModelMercuryPredictionsDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Mercury" + "/" + "Prediction Data";
        inline static const std::string singleBodyModelVenusPredictionsDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Venus" + "/" + "Prediction Data";
        inline static const std::string singleBodyModelEarthPredictionsDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Earth" + "/" + "Prediction Data";
        inline static const std::string singleBodyModelMarsPredictionsDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Mars" + "/" + "Prediction Data";
        inline static const std::string singleBodyModelJupiterPredictionsDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Jupiter" + "/" + "Prediction Data";
        inline static const std::string singleBodyModelSaturnPredictionsDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Saturn" + "/" + "Prediction Data";
        inline static const std::string singleBodyModelUranusPredictionsDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Uranus" + "/" + "Prediction Data";
        inline static const std::string singleBodyModelNeptunePredictionsDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Neptune" + "/" + "Prediction Data";
        inline static const std::string singleBodyModelPlutoPredictionsDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Pluto" + "/" + "Prediction Data";
        // ML Evaluation Directories
        inline static const std::string singleBodyEvalDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Evaluation Data";
        inline static const std::string singleBodyEvalSunDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Sun" + "/" + "Evaluation Data";
        inline static const std::string singleBodyEvalMercuryDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Mercury" + "/" + "Evaluation Data";
        inline static const std::string singleBodyEvalVenusDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Venus" + "/" + "Evaluation Data";
        inline static const std::string singleBodyEvalEarthDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Earth" + "/" + "Evaluation Data";
        inline static const std::string singleBodyEvalMarsDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Mars" + "/" + "Evaluation Data";
        inline static const std::string singleBodyEvalJupiterDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Jupiter" + "/" + "Evaluation Data";
        inline static const std::string singleBodyEvalSaturnDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Saturn" + "/" + "Evaluation Data";
        inline static const std::string singleBodyEvalUranusDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Uranus" + "/" + "Evaluation Data";
        inline static const std::string singleBodyEvalNeptuneDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Neptune" + "/" + "Evaluation Data";
        inline static const std::string singleBodyEvalPlutoDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Pluto" + "/" + "Evaluation Data";
        // ML Training Directories
        inline static const std::string singleBodyTrainDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Training Data";
        inline static const std::string singleBodyTrainSunDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Sun" + "/" + "Training Data";
        inline static const std::string singleBodyTrainMercuryDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Mercury" + "/" + "Training Data";
        inline static const std::string singleBodyTrainVenusDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Venus" + "/" + "Training Data";
        inline static const std::string singleBodyTrainEarthDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Earth" + "/" + "Training Data";
        inline static const std::string singleBodyTrainMarsDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Mars" + "/" + "Training Data";
        inline static const std::string singleBodyTrainJupiterDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Jupiter" + "/" + "Training Data";
        inline static const std::string singleBodyTrainSaturnDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Saturn" + "/" + "Training Data";
        inline static const std::string singleBodyTrainUranusDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Uranus" + "/" + "Training Data";
        inline static const std::string singleBodyTrainNeptuneDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Neptune" + "/" + "Training Data";
        inline static const std::string singleBodyTrainPlutoDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Pluto" + "/" + "Training Data";
        // ML Validation Directories
        inline static const std::string singleBodyValDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Validation Data";
        inline static const std::string singleBodyValSunDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Sun" + "/" + "Validation Data";
        inline static const std::string singleBodyValMercuryDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Mercury" + "/" + "Validation Data";
        inline static const std::string singleBodyValVenusDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Venus" + "/" + "Validation Data";
        inline static const std::string singleBodyValEarthDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Earth" + "/" + "Validation Data";
        inline static const std::string singleBodyValMarsDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Mars" + "/" + "Validation Data";
        inline static const std::string singleBodyValJupiterDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Jupiter" + "/" + "Validation Data";
        inline static const std::string singleBodyValSaturnDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Saturn" + "/" + "Validation Data";
        inline static const std::string singleBodyValUranusDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Uranus" + "/" + "Validation Data";
        inline static const std::string singleBodyValNeptuneDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Neptune" + "/" + "Validation Data";
        inline static const std::string singleBodyValPlutoDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Pluto" + "/" + "Validation Data";
        // ML Test Directories
        inline static const std::string singleBodyTestDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Test Data";
        inline static const std::string singleBodyTestSunDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Sun" + "/" + "Test Data";
        inline static const std::string singleBodyTestMercuryDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Mercury" + "/" + "Test Data";
        inline static const std::string singleBodyTestVenusDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Venus" + "/" + "Test Data";
        inline static const std::string singleBodyTestEarthDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Earth" + "/" + "Test Data";
        inline static const std::string singleBodyTestMarsDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Mars" + "/" + "Test Data";
        inline static const std::string singleBodyTestJupiterDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Jupiter" + "/" + "Test Data";
        inline static const std::string singleBodyTestSaturnDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Saturn" + "/" + "Test Data";
        inline static const std::string singleBodyTestUranusDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Uranus" + "/" + "Test Data";
        inline static const std::string singleBodyTestNeptuneDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Neptune" + "/" + "Test Data";
        inline static const std::string singleBodyTestPlutoDir = machineLearningDir + "/" + singleBodySubDir + "/" + "Pluto" + "/" + "Test Data";

        // CSV Columns
        // Single Body Simulation
        inline static const std::string singleBodyMass = "Body Mass (Kg)";
        inline static const std::string singleBodyName = "Body Name";
        inline static const std::string singleBodyBodyRad = "Body Radius (m)";
        inline static const std::string singleBodyInitProjP = "Initial Projectile Position (m)";
        inline static const std::string singleBodyInitProjV = "Initial Projectile Velocity (m/s)";
        inline static const std::string singleBodyInitTime = "Initial Simulation Time (s)";
        inline static const std::string singleBodyRKRProjP = "RK4 Projectile Position (m)";
        inline static const std::string singleBodyModelProjP = "ML Model Projectile Position (m)";
        inline static const std::string singleBodyRK4ProjV = "RK4 Projectile Velocity (m/s)";
        inline static const std::string singleBodyModelProjV = "ML Model Projectile Velocity (m/s)";
        inline static const std::string singleBodyRK4Times = "RK4 Simulation Time (s)";
        inline static const std::string singleBodyModelTimes = "Model Simulation Time (s)";
        inline static const std::string singleBodySimTimeSpan = "Simulation Time Span (s)";
        inline static const std::string singleBodySimTimeStep = "Simulation Time Step (s)";

        // Two Body Simulation
        inline static const std::string twoBodyBody1Mass = "Body 1 Mass (Kg)";
        inline static const std::string twoBodyBody2Mass = "Body 2 Mass (Kg)";
        inline static const std::string twoBodyBody1Name = "Body 1 Name";
        inline static const std::string twoBodyBody2Name = "Body 2 Name";
        inline static const std::string twoBodyBody1Rad = "Body 1 Radius (m)";
        inline static const std::string twoBodyBody2Rad = "Body 2 Radius (m)";
        inline static const std::string twoBodyBody1InitPosX = "Body 1 Initial Position X (m)";
        inline static const std::string twoBodyBody1InitPosY = "Body 1 Initial Position Y (m)";
        inline static const std::string twoBodyBody1InitPosZ = "Body 1 Initial Position Z (m)";
        inline static const std::string twoBodyBody2InitPosX = "Body 2 Initial Position X (m)";
        inline static const std::string twoBodyBody2InitPosY = "Body 2 Initial Position Y (m)";
        inline static const std::string twoBodyBody2InitPosZ = "Body 2 Initial Position Z (m)";
        inline static const std::string twoBodyBody1InitVelX = "Body 1 Initial Velocity X (m/s)";
        inline static const std::string twoBodyBody1InitVelY = "Body 1 Initial Velocity Y (m/s)";
        inline static const std::string twoBodyBody1InitVelZ = "Body 1 Initial Velocity Z (m/s)";
        inline static const std::string twoBodyBody2InitVelX = "Body 2 Initial Velocity X (m/s)";
        inline static const std::string twoBodyBody2InitVelY = "Body 2 Initial Velocity Y (m/s)";
        inline static const std::string twoBodyBody2InitVelZ = "Body 2 Initial Velocity Z (m/s)";
        inline static const std::string twoBodyRK4Body1PosX = "RK4 Body 1 Position X (m)";
        inline static const std::string twoBodyRK4Body1PosY = "RK4 Body 1 Position Y (m)";
        inline static const std::string twoBodyRK4Body1PosZ = "RK4 Body 1 Position Z (m)";
        inline static const std::string twoBodyRK4Body2PosX = "RK4 Body 2 Position X (m)";
        inline static const std::string twoBodyRK4Body2PosY = "RK4 Body 2 Position Y (m)";
        inline static const std::string twoBodyRK4Body2PosZ = "RK4 Body 2 Position Z (m)";
        inline static const std::string twoBodyRK4Body1VelX = "RK4 Body 1 Velocity X (m/s)";
        inline static const std::string twoBodyRK4Body1VelY = "RK4 Body 1 Velocity Y (m/s)";
        inline static const std::string twoBodyRK4Body1VelZ = "RK4 Body 1 Velocity Z (m/s)";
        inline static const std::string twoBodyRK4Body2VelX = "RK4 Body 2 Velocity X (m/s)";
        inline static const std::string twoBodyRK4Body2VelY = "RK4 Body 2 Velocity Y (m/s)";
        inline static const std::string twoBodyRK4Body2VelZ = "RK4 Body 2 Velocity Z (m/s)";
        inline static const std::string twoBodyRK4Times = "RK4 Simulation Time (s)";
        inline static const std::string twoBodySimTimeSpan = "Simulation Time Span (s)";
        inline static const std::string twoBodySimTimeStep = "Simulation Time Step (s)";

        // Three Body Simulation
        inline static const std::string threeBodyBody1Mass = "Body 1 Mass (Kg)";
        inline static const std::string threeBodyBody2Mass = "Body 2 Mass (Kg)";
        inline static const std::string threeBodyBody3Mass = "Body 3 Mass (Kg)";
        inline static const std::string threeBodyBody1Name = "Body 1 Name";
        inline static const std::string threeBodyBody2Name = "Body 2 Name";
        inline static const std::string threeBodyBody3Name = "Body 3 Name";
        inline static const std::string threeBodyBody1Rad = "Body 1 Radius (m)";
        inline static const std::string threeBodyBody2Rad = "Body 2 Radius (m)";
        inline static const std::string threeBodyBody3Rad = "Body 3 Radius (m)";
        inline static const std::string threeBodyBody1InitPosX = "Body 1 Initial Position X (m)";
        inline static const std::string threeBodyBody1InitPosY = "Body 1 Initial Position Y (m)";
        inline static const std::string threeBodyBody1InitPosZ = "Body 1 Initial Position Z (m)";
        inline static const std::string threeBodyBody2InitPosX = "Body 2 Initial Position X (m)";
        inline static const std::string threeBodyBody2InitPosY = "Body 2 Initial Position Y (m)";
        inline static const std::string threeBodyBody2InitPosZ = "Body 2 Initial Position Z (m)";
        inline static const std::string threeBodyBody3InitPosX = "Body 3 Initial Position X (m)";
        inline static const std::string threeBodyBody3InitPosY = "Body 3 Initial Position Y (m)";
        inline static const std::string threeBodyBody3InitPosZ = "Body 3 Initial Position Z (m)";
        inline static const std::string threeBodyBody1InitVelX = "Body 1 Initial Velocity X (m/s)";
        inline static const std::string threeBodyBody1InitVelY = "Body 1 Initial Velocity Y (m/s)";
        inline static const std::string threeBodyBody1InitVelZ = "Body 1 Initial Velocity Z (m/s)";
        inline static const std::string threeBodyBody2InitVelX = "Body 2 Initial Velocity X (m/s)";
        inline static const std::string threeBodyBody2InitVelY = "Body 2 Initial Velocity Y (m/s)";
        inline static const std::string threeBodyBody2InitVelZ = "Body 2 Initial Velocity Z (m/s)";
        inline static const std::string threeBodyBody3InitVelX = "Body 3 Initial Velocity X (m/s)";
        inline static const std::string threeBodyBody3InitVelY = "Body 3 Initial Velocity Y (m/s)";
        inline static const std::string threeBodyBody3InitVelZ = "Body 3 Initial Velocity Z (m/s)";
        inline static const std::string threeBodyRK4Body1PosX = "RK4 Body 1 Position X (m)";
        inline static const std::string threeBodyRK4Body1PosY = "RK4 Body 1 Position Y (m)";
        inline static const std::string threeBodyRK4Body1PosZ = "RK4 Body 1 Position Z (m)";
        inline static const std::string threeBodyRK4Body2PosX = "RK4 Body 2 Position X (m)";
        inline static const std::string threeBodyRK4Body2PosY = "RK4 Body 2 Position Y (m)";
        inline static const std::string threeBodyRK4Body2PosZ = "RK4 Body 2 Position Z (m)";
        inline static const std::string threeBodyRK4Body3PosX = "RK4 Body 3 Position X (m)";
        inline static const std::string threeBodyRK4Body3PosY = "RK4 Body 3 Position Y (m)";
        inline static const std::string threeBodyRK4Body3PosZ = "RK4 Body 3 Position Z (m)";
        inline static const std::string threeBodyRK4Body1VelX = "RK4 Body 1 Velocity X (m/s)";
        inline static const std::string threeBodyRK4Body1VelY = "RK4 Body 1 Velocity Y (m/s)";
        inline static const std::string threeBodyRK4Body1VelZ = "RK4 Body 1 Velocity Z (m/s)";
        inline static const std::string threeBodyRK4Body2VelX = "RK4 Body 2 Velocity X (m/s)";
        inline static const std::string threeBodyRK4Body2VelY = "RK4 Body 2 Velocity Y (m/s)";
        inline static const std::string threeBodyRK4Body2VelZ = "RK4 Body 2 Velocity Z (m/s)";
        inline static const std::string threeBodyRK4Body3VelX = "RK4 Body 3 Velocity X (m/s)";
        inline static const std::string threeBodyRK4Body3VelY = "RK4 Body 3 Velocity Y (m/s)";
        inline static const std::string threeBodyRK4Body3VelZ = "RK4 Body 3 Velocity Z (m/s)";
        inline static const std::string threeBodyRK4Times = "RK4 Simulation Time (s)";
        inline static const std::string threeBodySimTimeSpan = "Simulation Time Span (s)";
        inline static const std::string threeBodySimTimeStep = "Simulation Time Step (s)";

        // N-Body Simulation
        inline static const std::string nBodyRK4Times = "RK4 Simulation Time (s)";
        inline static const std::string nBodySimTimeSpan = "Simulation Time Span (s)";
        inline static const std::string nBodySimTimeStep = "Simulation Time Step (s)";

        // Body-specific path helpers
        static std::string getSingleBodyModelPath(const std::string& bodyName) {
            if (bodyName == "Sun") return singleBodyModelsSunPath;
            if (bodyName == "Mercury") return singleBodyModelsMercuryPath;
            if (bodyName == "Venus") return singleBodyModelsVenusPath;
            if (bodyName == "Earth") return singleBodyModelsEarthPath;
            if (bodyName == "Mars") return singleBodyModelsMarsPath;
            if (bodyName == "Jupiter") return singleBodyModelsJupiterPath;
            if (bodyName == "Saturn") return singleBodyModelsSaturnPath;
            if (bodyName == "Uranus") return singleBodyModelsUranusPath;
            if (bodyName == "Neptune") return singleBodyModelsNeptunePath;
            if (bodyName == "Pluto") return singleBodyModelsPlutoPath;
            return singleBodyModelScalersPath;  // Default/generic
        }

        static std::string getSingleBodyScalersPath(const std::string& bodyName) {
            if (bodyName == "Sun") return singleBodyModelSunScalersPath;
            if (bodyName == "Mercury") return singleBodyModelMercuryScalersPath;
            if (bodyName == "Venus") return singleBodyModelVenusScalersPath;
            if (bodyName == "Earth") return singleBodyModelEarthScalersPath;
            if (bodyName == "Mars") return singleBodyModelMarsScalersPath;
            if (bodyName == "Jupiter") return singleBodyModelJupiterScalersPath;
            if (bodyName == "Saturn") return singleBodyModelSaturnScalersPath;
            if (bodyName == "Uranus") return singleBodyModelUranusScalersPath;
            if (bodyName == "Neptune") return singleBodyModelNeptuneScalersPath;
            if (bodyName == "Pluto") return singleBodyModelPlutoScalersPath;
            return singleBodyModelScalers;  // Default/generic
        }

        static std::string getSingleBodySummaryPath(const std::string& bodyName) {
            if (bodyName == "Sun") return singleBodySunModelSummaryPath;
            if (bodyName == "Mercury") return singleBodyMercuryModelSummaryPath;
            if (bodyName == "Venus") return singleBodyVenusModelSummaryPath;
            if (bodyName == "Earth") return singleBodyEarthModelSummaryPath;
            if (bodyName == "Mars") return singleBodyMarsModelSummaryPath;
            if (bodyName == "Jupiter") return singleBodyJupiterModelSummaryPath;
            if (bodyName == "Saturn") return singleBodySaturnModelSummaryPath;
            if (bodyName == "Uranus") return singleBodyUranusModelSummaryPath;
            if (bodyName == "Neptune") return singleBodyNeptuneModelSummaryPath;
            if (bodyName == "Pluto") return singleBodyPlutoModelSummaryPath;
            return singleBodyModelSummaryPath;  // Default/generic
        }

        static std::string getSingleBodyPredictionsDir(const std::string& bodyName) {
            if (bodyName == "Sun") return singleBodyModelSunPredictionsDir;
            if (bodyName == "Mercury") return singleBodyModelMercuryPredictionsDir;
            if (bodyName == "Venus") return singleBodyModelVenusPredictionsDir;
            if (bodyName == "Earth") return singleBodyModelEarthPredictionsDir;
            if (bodyName == "Mars") return singleBodyModelMarsPredictionsDir;
            if (bodyName == "Jupiter") return singleBodyModelJupiterPredictionsDir;
            if (bodyName == "Saturn") return singleBodyModelSaturnPredictionsDir;
            if (bodyName == "Uranus") return singleBodyModelUranusPredictionsDir;
            if (bodyName == "Neptune") return singleBodyModelNeptunePredictionsDir;
            if (bodyName == "Pluto") return singleBodyModelPlutoPredictionsDir;
            return singleBodyModelPredictionsDir;  // Default/generic
        }

        static std::string getSingleBodyEvalDir(const std::string& bodyName) {
            if (bodyName == "Sun") return singleBodyEvalSunDir;
            if (bodyName == "Mercury") return singleBodyEvalMercuryDir;
            if (bodyName == "Venus") return singleBodyEvalVenusDir;
            if (bodyName == "Earth") return singleBodyEvalEarthDir;
            if (bodyName == "Mars") return singleBodyEvalMarsDir;
            if (bodyName == "Jupiter") return singleBodyEvalJupiterDir;
            if (bodyName == "Saturn") return singleBodyEvalSaturnDir;
            if (bodyName == "Uranus") return singleBodyEvalUranusDir;
            if (bodyName == "Neptune") return singleBodyEvalNeptuneDir;
            if (bodyName == "Pluto") return singleBodyEvalPlutoDir;
            return singleBodyEvalDir;  // Default/generic
        }

        static std::string getSingleBodyTrainDir(const std::string& bodyName) {
            if (bodyName == "Sun") return singleBodyTrainSunDir;
            if (bodyName == "Mercury") return singleBodyTrainMercuryDir;
            if (bodyName == "Venus") return singleBodyTrainVenusDir;
            if (bodyName == "Earth") return singleBodyTrainEarthDir;
            if (bodyName == "Mars") return singleBodyTrainMarsDir;
            if (bodyName == "Jupiter") return singleBodyTrainJupiterDir;
            if (bodyName == "Saturn") return singleBodyTrainSaturnDir;
            if (bodyName == "Uranus") return singleBodyTrainUranusDir;
            if (bodyName == "Neptune") return singleBodyTrainNeptuneDir;
            if (bodyName == "Pluto") return singleBodyTrainPlutoDir;
            return singleBodyTrainDir;  // Default/generic
        }

        static std::string getSingleBodyValDir(const std::string& bodyName) {
            if (bodyName == "Sun") return singleBodyValSunDir;
            if (bodyName == "Mercury") return singleBodyValMercuryDir;
            if (bodyName == "Venus") return singleBodyValVenusDir;
            if (bodyName == "Earth") return singleBodyValEarthDir;
            if (bodyName == "Mars") return singleBodyValMarsDir;
            if (bodyName == "Jupiter") return singleBodyValJupiterDir;
            if (bodyName == "Saturn") return singleBodyValSaturnDir;
            if (bodyName == "Uranus") return singleBodyValUranusDir;
            if (bodyName == "Neptune") return singleBodyValNeptuneDir;
            if (bodyName == "Pluto") return singleBodyValPlutoDir;
            return singleBodyValDir;  // Default/generic
        }

        static std::string getSingleBodyTestDir(const std::string& bodyName) {
            if (bodyName == "Sun") return singleBodyTestSunDir;
            if (bodyName == "Mercury") return singleBodyTestMercuryDir;
            if (bodyName == "Venus") return singleBodyTestVenusDir;
            if (bodyName == "Earth") return singleBodyTestEarthDir;
            if (bodyName == "Mars") return singleBodyTestMarsDir;
            if (bodyName == "Jupiter") return singleBodyTestJupiterDir;
            if (bodyName == "Saturn") return singleBodyTestSaturnDir;
            if (bodyName == "Uranus") return singleBodyTestUranusDir;
            if (bodyName == "Neptune") return singleBodyTestNeptuneDir;
            if (bodyName == "Pluto") return singleBodyTestPlutoDir;
            return singleBodyTestDir;  // Default/generic
        }

        // Get body-specific model file path (full path to .pt file)
        static std::string getSingleBodyModelFilePath(const std::string& bodyName) {
            return getSingleBodyModelPath(bodyName) + "/SingleBodyMLP.pt";
        }

        // Get body-specific scalers file path (full path to .json file)
        static std::string getSingleBodyScalersFilePath(const std::string& bodyName) {
            return getSingleBodyModelPath(bodyName) + "/SingleBodyScalers.json";
        }

        // Get body-specific summary file path (full path to .json file)
        static std::string getSingleBodySummaryFilePath(const std::string& bodyName) {
            return getSingleBodyModelPath(bodyName) + "/SingleBodyMLP_RunSummary.json";
        }
};
#include "machine_learning.h"

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PUBLIC METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// Single Body Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Trains a single body machine learning model
void MachineLearning::trainSingleBodyModel(bool resumeTraining, const std::string& bodyName) 
{ 
    if (!bodyName.empty()) {
        std::cout << "Training Single Body ML Model with LibTorch for body: " << bodyName << std::endl;
    } else {
        std::cout << "Training Single Body ML Model with LibTorch (generic)..." << std::endl;
    }
    
    SingleBodyTorchModel torchModel(bodyName);
    torchModel.train(resumeTraining);
}

// Predicts single body motion using trained machine learning model
SingleBodySolution MachineLearning::predictSingleBodyModel(SingleBodyIC initialConditions) 
{
    std::cout << "Predicting Single body trajectory with LibTorch ML Model for body: " 
            << initialConditions.bodyName << std::endl;

    // Use the body name from initial conditions to load the correct model
    SingleBodyTorchModel torchModel(initialConditions.bodyName);
    SingleBodySolution solution = torchModel.predict(initialConditions);

    std::cout << "Prediction completed successfully!" << std::endl;

    return solution;
}
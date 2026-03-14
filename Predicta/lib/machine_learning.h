#pragma once
#include <iostream>
#include <string>
#include <vector>
#include "constants.h"
#include "rk4.h"
#include "single_body_torch.h"
#include "utilities.h"

class MachineLearning {
    public:
        // Single Body Methods
        static void trainSingleBodyModel(bool resumeTraining, const std::string& bodyName = "");
        static SingleBodySolution predictSingleBodyModel(SingleBodyIC initialConditions);
};
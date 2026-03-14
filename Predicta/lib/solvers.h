#pragma once
#include "models.h"
#include "rk4.h"
#include <array>
#include <vector>

class Solvers {
    public:
        // Solver Methods
        SingleBodySolution RK4SingleBody(SingleBodyIC initialConditions);
        TwoBodySolution RK4TwoBody(TwoBodyIC initialConditions);
        ThreeBodySolution RK4ThreeBody(ThreeBodyIC initialConditions);
        NBodySolution RK4NBody(const NBodyIC& initialConditions);
};
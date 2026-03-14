#pragma once
#include <vector>
#include <functional>
#include <utility>
#include <cmath>
#include <cstddef>
#include <stdexcept>
#include <array>
#include <tuple>
#include "models.h"

// RK4 slopes struct for single body
struct SingleBodyRK4Slopes {
    double k_a;
    double k_b;

    SingleBodyRK4Slopes(const SingleBodyEOM& ode_result) : k_a(ode_result.equations[0]), k_b(ode_result.equations[1]) {}
};

// RK4 slopes struct for two body
struct TwoBodyRK4Slopes {
std::array<double, 3> k_body1Position;
    std::array<double, 3> k_body2Position;
    std::array<double, 3> k_body1Velocity;
    std::array<double, 3> k_body2Velocity;

    TwoBodyRK4Slopes(const TwoBodyEOM& ode_result) :
        k_body1Position({ode_result.equations[0], ode_result.equations[1], ode_result.equations[2]}),
        k_body2Position({ode_result.equations[3], ode_result.equations[4], ode_result.equations[5]}),
        k_body1Velocity({ode_result.equations[6], ode_result.equations[7], ode_result.equations[8]}),
        k_body2Velocity({ode_result.equations[9], ode_result.equations[10], ode_result.equations[11]}) {}
};

// RK4 k-variable struct for two body
struct TwoBodyRK4State {
    double time;
    std::array<double, 2> bodyMasses;
    std::array<double, 3> body1Position;
    std::array<double, 3> body2Position;
    std::array<double, 3> body1Velocity;
    std::array<double, 3> body2Velocity;
    std::function<TwoBodyEOM(TwoBodyDiffyEqs)> ODE;

    TwoBodyRK4Slopes computeSlopes() const {
        TwoBodyDiffyEqs state = {time, bodyMasses, body1Position, body2Position, body1Velocity, body2Velocity};
        return TwoBodyRK4Slopes(ODE(state));
    }
};

// RK4 slopes struct for three body
struct ThreeBodyRK4Slopes {
    std::array<double, 3> k_body1Position;
    std::array<double, 3> k_body2Position;
    std::array<double, 3> k_body3Position;
    std::array<double, 3> k_body1Velocity;
    std::array<double, 3> k_body2Velocity;
    std::array<double, 3> k_body3Velocity;

    ThreeBodyRK4Slopes(const ThreeBodyEOM& ode_result) :
        k_body1Position({ode_result.equations[0], ode_result.equations[1], ode_result.equations[2]}),
        k_body2Position({ode_result.equations[3], ode_result.equations[4], ode_result.equations[5]}),
        k_body3Position({ode_result.equations[6], ode_result.equations[7], ode_result.equations[8]}),
        k_body1Velocity({ode_result.equations[9], ode_result.equations[10], ode_result.equations[11]}),
        k_body2Velocity({ode_result.equations[12], ode_result.equations[13], ode_result.equations[14]}),
        k_body3Velocity({ode_result.equations[15], ode_result.equations[16], ode_result.equations[17]}) {}
};

// RK4 k-variable struct for three body
struct ThreeBodyRK4State {
    double time;
    std::array<double, 3> bodyMasses;
    std::array<double, 3> body1Position;
    std::array<double, 3> body2Position;
    std::array<double, 3> body3Position;
    std::array<double, 3> body1Velocity;
    std::array<double, 3> body2Velocity;
    std::array<double, 3> body3Velocity;
    std::function<ThreeBodyEOM(ThreeBodyDiffyEqs)> ODE;

    ThreeBodyRK4Slopes computeSlopes() const {
        ThreeBodyDiffyEqs state = {time, bodyMasses, body1Position, body2Position, body3Position, body1Velocity, body2Velocity, body3Velocity};
        return ThreeBodyRK4Slopes(ODE(state));
    }
};

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// N-Body RK4 Structures (Generic for N >= 2 bodies)
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// N-Body Initial Conditions for RK4 Solver
struct NBodyRK4IC {
    std::vector<double> masses;        
    std::vector<double> initialState;  
    double initTime = 0.0;
    double timeSpan = 0.0;
    double timeStep = 0.0;
};

// N-Body Solution for RK4 Solver
struct NBodyRK4Solution {
    std::vector<double> times;                
    std::vector<std::vector<double>> states;
    
    // Returns the number of bodies N (derived from state size)
    size_t numBodies() const {
        if (states.empty()) return 0;
        return states[0].size() / 6;
    }
};

// N-Body RK4 Slopes (dydt at an evaluation point)
struct NBodyRK4Slopes {
    std::vector<double> k;
    
    // Default constructor
    NBodyRK4Slopes() = default;
    
    // Constructor from dydt vector
    explicit NBodyRK4Slopes(std::vector<double> dydt) : k(std::move(dydt)) {}
};

// N-Body RK4 State (holds references to avoid copies)
struct NBodyRK4State {
    double time;
    const std::vector<double>* masses;
    const std::vector<double>* state;
    std::function<std::vector<double>(double, const std::vector<double>&, const std::vector<double>&)> ODE;
    
    // Compute slopes (dydt) at the current state
    NBodyRK4Slopes computeSlopes() const {
        return NBodyRK4Slopes(ODE(time, *state, *masses));
    }
};

// RK4 k-variable struct for single body
struct SingleBodyRK4State {
    double time;
    double position;
    double velocity; 
    double bodyMass;
    double bodyRadius;
    std::function<SingleBodyEOM(SingleBodyDiffyEqs)> ODE;

    SingleBodyRK4Slopes computeSlopes() const {
        SingleBodyDiffyEqs state = {time, position, velocity, bodyMass, bodyRadius};
        return SingleBodyRK4Slopes(ODE(state));
    }
};

class RK4 {
    public:
        // RK4 Methods
        static SingleBodySolution singleBody(const std::function<SingleBodyEOM(SingleBodyDiffyEqs)>& ODE, SingleBodyIC initialConditions);
        static TwoBodySolution twoBody(const std::function<TwoBodyEOM(TwoBodyDiffyEqs)>& ODE, TwoBodyIC initialConditions);
        static ThreeBodySolution threeBody(const std::function<ThreeBodyEOM(ThreeBodyDiffyEqs)>& ODE, ThreeBodyIC initialConditions);
        
        // N-Body RK4 Solver
        static NBodyRK4Solution nBody(
            const std::function<std::vector<double>(double, const std::vector<double>&, const std::vector<double>&)>& ODE,
            const NBodyRK4IC& initialConditions
        );

    private:
        // RK4 Helper Methods
        static SingleBodyRK4Slopes computeSingleBodySlopes(const SingleBodyRK4State& var) {
            return var.computeSlopes();
        }
        static TwoBodyRK4Slopes computeTwoBodySlopes(const TwoBodyRK4State& var) {
            return var.computeSlopes();
        }
        static ThreeBodyRK4Slopes computeThreeBodySlopes(const ThreeBodyRK4State& var) {
            return var.computeSlopes();
        }
        static NBodyRK4Slopes computeNBodySlopes(const NBodyRK4State& state) {
            return state.computeSlopes();
        }
        
        // N-Body Vector Arithmetic Helpers
        static std::vector<double> addScaled(const std::vector<double>& a, const std::vector<double>& b, double s);
        static void axpyInPlace(std::vector<double>& y, const std::vector<double>& x, double a);
};
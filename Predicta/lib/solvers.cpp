#include "solvers.h"

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PUBLIC METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// Solver Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Single Body RK4 Solver
SingleBodySolution Solvers::RK4SingleBody(SingleBodyIC initialConditions) {
    Models models_instance;
    auto projectile_motion_ode = [&models_instance](SingleBodyDiffyEqs modelData) {
        return models_instance.singleBodySystem(modelData);
    };
    SingleBodySolution result = RK4::singleBody(projectile_motion_ode, initialConditions);
    return result;
}

// Two Body RK4 Solver
TwoBodySolution Solvers::RK4TwoBody(TwoBodyIC initialConditions) {
    Models models_instance;
    auto two_body_ode = [&models_instance](TwoBodyDiffyEqs modelData) {
        return models_instance.twoBodySystem(modelData);
    };
    TwoBodySolution result = RK4::twoBody(two_body_ode, initialConditions);
    return result;
}

// Three Body RK4 Solver
ThreeBodySolution Solvers::RK4ThreeBody(ThreeBodyIC initialConditions) {
    Models models_instance;
    auto three_body_ode = [&models_instance](ThreeBodyDiffyEqs modelData) {
        return models_instance.threeBodySystem(modelData);
    };
    ThreeBodySolution result = RK4::threeBody(three_body_ode, initialConditions);
    return result;
}

// N-Body RK4 Solver
NBodySolution Solvers::RK4NBody(const NBodyIC& initialConditions) {
    Models models_instance;
    const size_t N = initialConditions.bodyMasses.size();
    
    // Create ODE lambda that adapts between RK4's vector-based interface and Models::nBodySystem
    // RK4 state layout: y = [x0,y0,z0,...,x(N-1),y(N-1),z(N-1), vx0,vy0,vz0,...,vx(N-1),vy(N-1),vz(N-1)]
    // Models expects: NBodyDiffyEqs with separate positions (3N) and velocities (3N) vectors
    auto n_body_ode = [&models_instance, N](double t, const std::vector<double>& y, const std::vector<double>& masses) -> std::vector<double> {
        // Extract positions (first 3N elements) and velocities (next 3N elements) from state y
        std::vector<double> positions(y.begin(), y.begin() + 3 * N);
        std::vector<double> velocities(y.begin() + 3 * N, y.end());
        
        // Build NBodyDiffyEqs for Models::nBodySystem
        NBodyDiffyEqs modelData;
        modelData.masses = masses;
        modelData.positions = positions;
        modelData.velocities = velocities;
        
        // Call the model and return the equations vector
        NBodyEOM eom = models_instance.nBodySystem(modelData);
        return eom.equations;
    };
    
    // Convert NBodyIC to NBodyRK4IC
    // NBodyIC has separate initialPositions (3N) and initialVelocities (3N)
    // NBodyRK4IC needs combined initialState (6N)
    NBodyRK4IC rk4_ic;
    rk4_ic.masses = initialConditions.bodyMasses;
    rk4_ic.initTime = initialConditions.initTime;
    rk4_ic.timeSpan = initialConditions.timeSpan;
    rk4_ic.timeStep = initialConditions.timeStep;
    
    // Build combined state vector: [positions (3N), velocities (3N)]
    rk4_ic.initialState.reserve(6 * N);
    rk4_ic.initialState.insert(rk4_ic.initialState.end(), 
        initialConditions.initialPositions.begin(), initialConditions.initialPositions.end());
    rk4_ic.initialState.insert(rk4_ic.initialState.end(), 
        initialConditions.initialVelocities.begin(), initialConditions.initialVelocities.end());
    
    // Run RK4 integration
    NBodyRK4Solution rk4_result = RK4::nBody(n_body_ode, rk4_ic);
    
    // Convert NBodyRK4Solution to NBodySolution
    // NBodyRK4Solution has combined states (6N each)
    // NBodySolution needs separate positions and velocities vectors
    NBodySolution result;
    result.numBodies = N;
    result.times = rk4_result.times;
    result.positions.resize(rk4_result.states.size());
    result.velocities.resize(rk4_result.states.size());
    
    for (size_t i = 0; i < rk4_result.states.size(); ++i) {
        const std::vector<double>& state = rk4_result.states[i];
        // Extract positions (first 3N) and velocities (next 3N)
        result.positions[i] = std::vector<double>(state.begin(), state.begin() + 3 * N);
        result.velocities[i] = std::vector<double>(state.begin() + 3 * N, state.end());
    }
    
    return result;
}
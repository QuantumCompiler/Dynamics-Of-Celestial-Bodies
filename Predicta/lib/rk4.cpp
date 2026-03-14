#include "rk4.h"

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PUBLIC METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// RK4 Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Single Body RK4 Solver
SingleBodySolution RK4::singleBody(const std::function<SingleBodyEOM(SingleBodyDiffyEqs)>& ODE, SingleBodyIC initialConditions) {
    // Unpack initial conditions
    const std::array<double, 2> projectileInitialConditions = {initialConditions.initialPosition, initialConditions.initialVelocity};
    double initialTime = initialConditions.initTime;
    double totalTime = initialConditions.initTime + initialConditions.timeSpan;
    double h = initialConditions.timeStep;
    double bodyMass = initialConditions.bodyMass;
    double bodyRadius = initialConditions.bodyRadius;

    // Initialize solution struct and check step size
    SingleBodySolution solution;

    if (h <= 0.0) h = 0.001;  // Default small step size

    // Calculate number of steps
    int n = static_cast<int>(std::floor((totalTime - initialTime) / h));
    if (n < 0) n = 0;

    // Resize solution vectors
    solution.positions.resize(n + 1);
    solution.velocities.resize(n + 1);
    solution.times.resize(n + 1);
    solution.positions[0] = projectileInitialConditions[0];
    solution.velocities[0] = projectileInitialConditions[1];

    // Initialize time vector
    for (int i = 0; i <= n; ++i) solution.times[i] = initialTime + i * h;

    // RK4 integration
    for (int i = 0; i < n; ++i) {
        // Current state
        double a = solution.positions[i];
        double b = solution.velocities[i];
        double t = solution.times[i];

        // State 1 iteration
        SingleBodyRK4State state1 = {t, a, b, bodyMass, bodyRadius, ODE};
        SingleBodyRK4Slopes slopes1 = computeSingleBodySlopes(state1);

        // State 2 iteration
        SingleBodyRK4State state2 = {t + 0.5 * h,
                                    a + 0.5 * h * slopes1.k_a,
                                    b + 0.5 * h * slopes1.k_b,
                                    bodyMass, bodyRadius, ODE};
        SingleBodyRK4Slopes slopes2 = computeSingleBodySlopes(state2);

        // State 3 iteration
        SingleBodyRK4State state3 = {t + 0.5 * h,
                                    a + 0.5 * h * slopes2.k_a,
                                    b + 0.5 * h * slopes2.k_b,
                                    bodyMass, bodyRadius, ODE};
        SingleBodyRK4Slopes slopes3 = computeSingleBodySlopes(state3);

        // State 4 iteration
        SingleBodyRK4State state4 = {t + h,
                                    a + h * slopes3.k_a,
                                    b + h * slopes3.k_b,
                                    bodyMass, bodyRadius, ODE};
        SingleBodyRK4Slopes slopes4 = computeSingleBodySlopes(state4);

        // Update state using RK4 formula
        solution.positions[i + 1] = a + (h / 6.0) * (slopes1.k_a + 2.0 * slopes2.k_a + 2.0 * slopes3.k_a + slopes4.k_a);
        solution.velocities[i + 1] = b + (h / 6.0) * (slopes1.k_b + 2.0 * slopes2.k_b + 2.0 * slopes3.k_b + slopes4.k_b);
    }

    return solution;
}

// Two Body RK4 Solver
TwoBodySolution RK4::twoBody(const std::function<TwoBodyEOM(TwoBodyDiffyEqs)>& ODE, TwoBodyIC initialConditions) {
    // Unpack initial conditions
    double t0 = initialConditions.initTime;
    double tn = initialConditions.initTime + initialConditions.timeSpan;
    double h = initialConditions.timeStep;

    // Initialize solution struct and check step size
    TwoBodySolution solution;

    if (h <= 0.0) h = 0.001;  // Default small step size

    // Calculate number of steps
    int n = static_cast<int>(std::floor((tn - t0) / h));
    if (n < 0) n = 0;

    // Resize solution vectors
    solution.body1Positions.resize(n + 1);
    solution.body2Positions.resize(n + 1);
    solution.body1Velocities.resize(n + 1);
    solution.body2Velocities.resize(n + 1);
    solution.times.resize(n + 1);

    // Initialize from initial conditions
    solution.body1Positions[0] = initialConditions.body1InitialPosition;
    solution.body2Positions[0] = initialConditions.body2InitialPosition;
    solution.body1Velocities[0] = initialConditions.body1InitialVelocity;
    solution.body2Velocities[0] = initialConditions.body2InitialVelocity;

    for (int i = 0; i <= n; ++i) solution.times[i] = t0 + i * h;

    // RK4 integration
    for (int i = 0; i < n; ++i) {
        double t = solution.times[i];
        std::array<double, 3> b1p = solution.body1Positions[i];
        std::array<double, 3> b2p = solution.body2Positions[i];
        std::array<double, 3> b1v = solution.body1Velocities[i];
        std::array<double, 3> b2v = solution.body2Velocities[i];

        // State 1 iteration
        TwoBodyRK4State state1 = {t, initialConditions.bodyMasses, b1p, b2p, b1v, b2v, ODE};
        TwoBodyRK4Slopes slopes1 = computeTwoBodySlopes(state1);

        // State 2 iteration
        TwoBodyRK4State state2 = {t + 0.5 * h, initialConditions.bodyMasses,
            {b1p[0] + 0.5 * h * slopes1.k_body1Position[0], b1p[1] + 0.5 * h * slopes1.k_body1Position[1], b1p[2] + 0.5 * h * slopes1.k_body1Position[2]},
            {b2p[0] + 0.5 * h * slopes1.k_body2Position[0], b2p[1] + 0.5 * h * slopes1.k_body2Position[1], b2p[2] + 0.5 * h * slopes1.k_body2Position[2]},
            {b1v[0] + 0.5 * h * slopes1.k_body1Velocity[0], b1v[1] + 0.5 * h * slopes1.k_body1Velocity[1], b1v[2] + 0.5 * h * slopes1.k_body1Velocity[2]},
            {b2v[0] + 0.5 * h * slopes1.k_body2Velocity[0], b2v[1] + 0.5 * h * slopes1.k_body2Velocity[1], b2v[2] + 0.5 * h * slopes1.k_body2Velocity[2]},
            ODE};
        TwoBodyRK4Slopes slopes2 = computeTwoBodySlopes(state2);

        // State 3 iteration
        TwoBodyRK4State state3 = {t + 0.5 * h, initialConditions.bodyMasses,
            {b1p[0] + 0.5 * h * slopes2.k_body1Position[0], b1p[1] + 0.5 * h * slopes2.k_body1Position[1], b1p[2] + 0.5 * h * slopes2.k_body1Position[2]},
            {b2p[0] + 0.5 * h * slopes2.k_body2Position[0], b2p[1] + 0.5 * h * slopes2.k_body2Position[1], b2p[2] + 0.5 * h * slopes2.k_body2Position[2]},
            {b1v[0] + 0.5 * h * slopes2.k_body1Velocity[0], b1v[1] + 0.5 * h * slopes2.k_body1Velocity[1], b1v[2] + 0.5 * h * slopes2.k_body1Velocity[2]},
            {b2v[0] + 0.5 * h * slopes2.k_body2Velocity[0], b2v[1] + 0.5 * h * slopes2.k_body2Velocity[1], b2v[2] + 0.5 * h * slopes2.k_body2Velocity[2]},
            ODE};
        TwoBodyRK4Slopes slopes3 = computeTwoBodySlopes(state3);

        // State 4 iteration
        TwoBodyRK4State state4 = {t + h, initialConditions.bodyMasses,
            {b1p[0] + h * slopes3.k_body1Position[0], b1p[1] + h * slopes3.k_body1Position[1], b1p[2] + h * slopes3.k_body1Position[2]},
            {b2p[0] + h * slopes3.k_body2Position[0], b2p[1] + h * slopes3.k_body2Position[1], b2p[2] + h * slopes3.k_body2Position[2]},
            {b1v[0] + h * slopes3.k_body1Velocity[0], b1v[1] + h * slopes3.k_body1Velocity[1], b1v[2] + h * slopes3.k_body1Velocity[2]},
            {b2v[0] + h * slopes3.k_body2Velocity[0], b2v[1] + h * slopes3.k_body2Velocity[1], b2v[2] + h * slopes3.k_body2Velocity[2]},
            ODE};
        TwoBodyRK4Slopes slopes4 = computeTwoBodySlopes(state4);

        // Update state using RK4 formula
        const double h_sixth = h / 6.0;
        for (int j = 0; j < 3; ++j) {
            solution.body1Positions[i + 1][j] = b1p[j] + h_sixth * (slopes1.k_body1Position[j] + 2.0 * slopes2.k_body1Position[j] + 2.0 * slopes3.k_body1Position[j] + slopes4.k_body1Position[j]);
            solution.body2Positions[i + 1][j] = b2p[j] + h_sixth * (slopes1.k_body2Position[j] + 2.0 * slopes2.k_body2Position[j] + 2.0 * slopes3.k_body2Position[j] + slopes4.k_body2Position[j]);
            solution.body1Velocities[i + 1][j] = b1v[j] + h_sixth * (slopes1.k_body1Velocity[j] + 2.0 * slopes2.k_body1Velocity[j] + 2.0 * slopes3.k_body1Velocity[j] + slopes4.k_body1Velocity[j]);
            solution.body2Velocities[i + 1][j] = b2v[j] + h_sixth * (slopes1.k_body2Velocity[j] + 2.0 * slopes2.k_body2Velocity[j] + 2.0 * slopes3.k_body2Velocity[j] + slopes4.k_body2Velocity[j]);
        }
    }

    return solution;
}

// Three Body RK4 Solver
ThreeBodySolution RK4::threeBody(const std::function<ThreeBodyEOM(ThreeBodyDiffyEqs)>& ODE, ThreeBodyIC initialConditions) {
    double t0 = initialConditions.initTime;
    double tn = initialConditions.initTime + initialConditions.timeSpan;
    double h = initialConditions.timeStep;

    ThreeBodySolution solution;

    if (h <= 0.0) h = 0.001;  // Default small step size

    int n = static_cast<int>(std::floor((tn - t0) / h));
    if (n < 0) n = 0;

    solution.body1Positions.resize(n + 1);
    solution.body2Positions.resize(n + 1);
    solution.body3Positions.resize(n + 1);
    solution.body1Velocities.resize(n + 1);
    solution.body2Velocities.resize(n + 1);
    solution.body3Velocities.resize(n + 1);
    solution.times.resize(n + 1);

    // Initialize from initial conditions
    solution.body1Positions[0] = initialConditions.body1InitialPosition;
    solution.body2Positions[0] = initialConditions.body2InitialPosition;
    solution.body3Positions[0] = initialConditions.body3InitialPosition;
    solution.body1Velocities[0] = initialConditions.body1InitialVelocity;
    solution.body2Velocities[0] = initialConditions.body2InitialVelocity;
    solution.body3Velocities[0] = initialConditions.body3InitialVelocity;

    for (int i = 0; i <= n; ++i) solution.times[i] = t0 + i * h;

    // RK4 integration
    for (int i = 0; i < n; ++i) {
        double t = solution.times[i];
        std::array<double, 3> b1p = solution.body1Positions[i];
        std::array<double, 3> b2p = solution.body2Positions[i];
        std::array<double, 3> b3p = solution.body3Positions[i];
        std::array<double, 3> b1v = solution.body1Velocities[i];
        std::array<double, 3> b2v = solution.body2Velocities[i];
        std::array<double, 3> b3v = solution.body3Velocities[i];

        // State 1 iteration
        ThreeBodyRK4State state1 = {t, initialConditions.bodyMasses, b1p, b2p, b3p, b1v, b2v, b3v, ODE};
        ThreeBodyRK4Slopes slopes1 = computeThreeBodySlopes(state1);

        // State 2 iteration
        ThreeBodyRK4State state2 = {t + 0.5 * h, initialConditions.bodyMasses,
            {b1p[0] + 0.5 * h * slopes1.k_body1Position[0], b1p[1] + 0.5 * h * slopes1.k_body1Position[1], b1p[2] + 0.5 * h * slopes1.k_body1Position[2]},
            {b2p[0] + 0.5 * h * slopes1.k_body2Position[0], b2p[1] + 0.5 * h * slopes1.k_body2Position[1], b2p[2] + 0.5 * h * slopes1.k_body2Position[2]},
            {b3p[0] + 0.5 * h * slopes1.k_body3Position[0], b3p[1] + 0.5 * h * slopes1.k_body3Position[1], b3p[2] + 0.5 * h * slopes1.k_body3Position[2]},
            {b1v[0] + 0.5 * h * slopes1.k_body1Velocity[0], b1v[1] + 0.5 * h * slopes1.k_body1Velocity[1], b1v[2] + 0.5 * h * slopes1.k_body1Velocity[2]},
            {b2v[0] + 0.5 * h * slopes1.k_body2Velocity[0], b2v[1] + 0.5 * h * slopes1.k_body2Velocity[1], b2v[2] + 0.5 * h * slopes1.k_body2Velocity[2]},
            {b3v[0] + 0.5 * h * slopes1.k_body3Velocity[0], b3v[1] + 0.5 * h * slopes1.k_body3Velocity[1], b3v[2] + 0.5 * h * slopes1.k_body3Velocity[2]},
            ODE};
        ThreeBodyRK4Slopes slopes2 = computeThreeBodySlopes(state2);

        // State 3 iteration
        ThreeBodyRK4State state3 = {t + 0.5 * h, initialConditions.bodyMasses,
            {b1p[0] + 0.5 * h * slopes2.k_body1Position[0], b1p[1] + 0.5 * h * slopes2.k_body1Position[1], b1p[2] + 0.5 * h * slopes2.k_body1Position[2]},
            {b2p[0] + 0.5 * h * slopes2.k_body2Position[0], b2p[1] + 0.5 * h * slopes2.k_body2Position[1], b2p[2] + 0.5 * h * slopes2.k_body2Position[2]},
            {b3p[0] + 0.5 * h * slopes2.k_body3Position[0], b3p[1] + 0.5 * h * slopes2.k_body3Position[1], b3p[2] + 0.5 * h * slopes2.k_body3Position[2]},
            {b1v[0] + 0.5 * h * slopes2.k_body1Velocity[0], b1v[1] + 0.5 * h * slopes2.k_body1Velocity[1], b1v[2] + 0.5 * h * slopes2.k_body1Velocity[2]},
            {b2v[0] + 0.5 * h * slopes2.k_body2Velocity[0], b2v[1] + 0.5 * h * slopes2.k_body2Velocity[1], b2v[2] + 0.5 * h * slopes2.k_body2Velocity[2]},
            {b3v[0] + 0.5 * h * slopes2.k_body3Velocity[0], b3v[1] + 0.5 * h * slopes2.k_body3Velocity[1], b3v[2] + 0.5 * h * slopes2.k_body3Velocity[2]},
            ODE};
        ThreeBodyRK4Slopes slopes3 = computeThreeBodySlopes(state3);

        // State 4 iteration
        ThreeBodyRK4State state4 = {t + h, initialConditions.bodyMasses,
            {b1p[0] + h * slopes3.k_body1Position[0], b1p[1] + h * slopes3.k_body1Position[1], b1p[2] + h * slopes3.k_body1Position[2]},
            {b2p[0] + h * slopes3.k_body2Position[0], b2p[1] + h * slopes3.k_body2Position[1], b2p[2] + h * slopes3.k_body2Position[2]},
            {b3p[0] + h * slopes3.k_body3Position[0], b3p[1] + h * slopes3.k_body3Position[1], b3p[2] + h * slopes3.k_body3Position[2]},
            {b1v[0] + h * slopes3.k_body1Velocity[0], b1v[1] + h * slopes3.k_body1Velocity[1], b1v[2] + h * slopes3.k_body1Velocity[2]},
            {b2v[0] + h * slopes3.k_body2Velocity[0], b2v[1] + h * slopes3.k_body2Velocity[1], b2v[2] + h * slopes3.k_body2Velocity[2]},
            {b3v[0] + h * slopes3.k_body3Velocity[0], b3v[1] + h * slopes3.k_body3Velocity[1], b3v[2] + h * slopes3.k_body3Velocity[2]},
            ODE};
        ThreeBodyRK4Slopes slopes4 = computeThreeBodySlopes(state4);

        // Update state using RK4 formula
        const double h_sixth = h / 6.0;
        for (int j = 0; j < 3; ++j) {
            solution.body1Positions[i + 1][j] = b1p[j] + h_sixth * (slopes1.k_body1Position[j] + 2.0 * slopes2.k_body1Position[j] + 2.0 * slopes3.k_body1Position[j] + slopes4.k_body1Position[j]);
            solution.body2Positions[i + 1][j] = b2p[j] + h_sixth * (slopes1.k_body2Position[j] + 2.0 * slopes2.k_body2Position[j] + 2.0 * slopes3.k_body2Position[j] + slopes4.k_body2Position[j]);
            solution.body3Positions[i + 1][j] = b3p[j] + h_sixth * (slopes1.k_body3Position[j] + 2.0 * slopes2.k_body3Position[j] + 2.0 * slopes3.k_body3Position[j] + slopes4.k_body3Position[j]);
            solution.body1Velocities[i + 1][j] = b1v[j] + h_sixth * (slopes1.k_body1Velocity[j] + 2.0 * slopes2.k_body1Velocity[j] + 2.0 * slopes3.k_body1Velocity[j] + slopes4.k_body1Velocity[j]);
            solution.body2Velocities[i + 1][j] = b2v[j] + h_sixth * (slopes1.k_body2Velocity[j] + 2.0 * slopes2.k_body2Velocity[j] + 2.0 * slopes3.k_body2Velocity[j] + slopes4.k_body2Velocity[j]);
            solution.body3Velocities[i + 1][j] = b3v[j] + h_sixth * (slopes1.k_body3Velocity[j] + 2.0 * slopes2.k_body3Velocity[j] + 2.0 * slopes3.k_body3Velocity[j] + slopes4.k_body3Velocity[j]);
        }
    }

    return solution;
}

// N-Body RK4 Solver
NBodyRK4Solution RK4::nBody(
    const std::function<std::vector<double>(double, const std::vector<double>&, const std::vector<double>&)>& ODE,
    const NBodyRK4IC& initialConditions
) {
    // ----- Input Validation -----
    
    // Check masses vector
    if (initialConditions.masses.empty()) {
        throw std::invalid_argument("N-body RK4: masses vector cannot be empty");
    }
    
    const size_t N = initialConditions.masses.size();
    
    // Check for minimum number of bodies
    if (N < 2) {
        throw std::invalid_argument("N-body RK4: requires at least 2 bodies");
    }
    
    // Check state vector size matches 6N
    if (initialConditions.initialState.size() != 6 * N) {
        throw std::invalid_argument("N-body RK4: initialState size must be 6N (got " + 
            std::to_string(initialConditions.initialState.size()) + 
            ", expected " + std::to_string(6 * N) + ")");
    }
    
    // Check time step
    if (initialConditions.timeStep <= 0.0) {
        throw std::invalid_argument("N-body RK4: timeStep must be > 0");
    }
    
    // Check time span
    if (initialConditions.timeSpan < 0.0) {
        throw std::invalid_argument("N-body RK4: timeSpan must be >= 0");
    }
    
    // ----- Unpack initial conditions -----
    double t0 = initialConditions.initTime;
    double tn = initialConditions.initTime + initialConditions.timeSpan;
    double h = initialConditions.timeStep;
    const std::vector<double>& masses = initialConditions.masses;
    
    // ----- Initialize solution -----
    NBodyRK4Solution solution;
    
    // Calculate number of steps (consistent with existing solvers)
    int numSteps = static_cast<int>(std::floor((tn - t0) / h));
    if (numSteps < 0) numSteps = 0;
    
    // Resize solution vectors
    solution.times.resize(numSteps + 1);
    solution.states.resize(numSteps + 1);
    
    // Initialize time vector
    for (int i = 0; i <= numSteps; ++i) {
        solution.times[i] = t0 + i * h;
    }
    
    // Set initial state
    solution.states[0] = initialConditions.initialState;
    
    // ----- RK4 Integration Loop -----
    for (int i = 0; i < numSteps; ++i) {
        double t = solution.times[i];
        const std::vector<double>& y = solution.states[i];
        
        // k1 = ODE(t, y)
        NBodyRK4State state1;
        state1.time = t;
        state1.masses = &masses;
        state1.state = &y;
        state1.ODE = ODE;
        NBodyRK4Slopes slopes1 = computeNBodySlopes(state1);
        
        // k2 = ODE(t + h/2, y + h/2 * k1)
        std::vector<double> y2 = addScaled(y, slopes1.k, 0.5 * h);
        NBodyRK4State state2;
        state2.time = t + 0.5 * h;
        state2.masses = &masses;
        state2.state = &y2;
        state2.ODE = ODE;
        NBodyRK4Slopes slopes2 = computeNBodySlopes(state2);
        
        // k3 = ODE(t + h/2, y + h/2 * k2)
        std::vector<double> y3 = addScaled(y, slopes2.k, 0.5 * h);
        NBodyRK4State state3;
        state3.time = t + 0.5 * h;
        state3.masses = &masses;
        state3.state = &y3;
        state3.ODE = ODE;
        NBodyRK4Slopes slopes3 = computeNBodySlopes(state3);
        
        // k4 = ODE(t + h, y + h * k3)
        std::vector<double> y4 = addScaled(y, slopes3.k, h);
        NBodyRK4State state4;
        state4.time = t + h;
        state4.masses = &masses;
        state4.state = &y4;
        state4.ODE = ODE;
        NBodyRK4Slopes slopes4 = computeNBodySlopes(state4);
        
        // Update state: y_new = y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
        std::vector<double> y_new = y;  // Copy current state
        const double h_sixth = h / 6.0;
        
        // y_new += (h/6) * k1
        axpyInPlace(y_new, slopes1.k, h_sixth);
        // y_new += (h/6) * 2 * k2
        axpyInPlace(y_new, slopes2.k, 2.0 * h_sixth);
        // y_new += (h/6) * 2 * k3
        axpyInPlace(y_new, slopes3.k, 2.0 * h_sixth);
        // y_new += (h/6) * k4
        axpyInPlace(y_new, slopes4.k, h_sixth);
        
        solution.states[i + 1] = std::move(y_new);
    }
    
    return solution;
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PRIVATE METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// RK4 Helper Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// N-Body Vector Arithmetic: Returns a + s * b (element-wise)
std::vector<double> RK4::addScaled(const std::vector<double>& a, const std::vector<double>& b, double s) {
    std::vector<double> result(a.size());
    for (size_t i = 0; i < a.size(); ++i) {
        result[i] = a[i] + s * b[i];
    }
    return result;
}

// N-Body Vector Arithmetic: In-place y += a * x (element-wise)
void RK4::axpyInPlace(std::vector<double>& y, const std::vector<double>& x, double a) {
    for (size_t i = 0; i < y.size(); ++i) {
        y[i] += a * x[i];
    }
}
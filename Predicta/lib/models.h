#pragma once
#include <array>
#include <cmath>
#include <cstddef>
#include <stdexcept>
#include <string>
#include <vector>

// Differential Equations Structures For Single Body
struct SingleBodyDiffyEqs {
    double time;
    double position;
    double velocity;
    double bodyMass;
    double bodyRadius;
};

// Differential Equations Structures For Two Body
struct TwoBodyDiffyEqs {
    double time;
    std::array<double, 2> bodyMasses;
    std::array<double, 3> body1Position;
    std::array<double, 3> body2Position;
    std::array<double, 3> body1Velocity;
    std::array<double, 3> body2Velocity;
};

// Differential Equations Structures For Three Body
struct ThreeBodyDiffyEqs {
    double time;
    std::array<double, 3> bodyMasses;
    std::array<double, 3> body1Position;
    std::array<double, 3> body2Position;
    std::array<double, 3> body3Position;
    std::array<double, 3> body1Velocity;
    std::array<double, 3> body2Velocity;
    std::array<double, 3> body3Velocity;
};

// Equations of Motion Structures For Single Body
struct SingleBodyEOM {
    std::array<double, 2> equations;
};

// Equations of Motion Structures For Two Body
struct TwoBodyEOM {
    std::array<double, 12> equations;
};

// Equations of Motion Structures For Three Body
struct ThreeBodyEOM {
    std::array<double, 18> equations;
};

// Initial Conditions Structures For Single Body
struct SingleBodyIC {
    double initialPosition;
    double initialVelocity;
    std::string bodyName;
    double bodyMass;
    double bodyRadius;
    double initTime;
    double timeSpan;
    double timeStep;
};

// Initial Conditions Structures For Two Body
struct TwoBodyIC {
    std::array<double, 3> body1InitialPosition;
    std::array<double, 3> body2InitialPosition;
    std::array<double, 3> body1InitialVelocity;
    std::array<double, 3> body2InitialVelocity;
    std::array<double, 2> bodyMasses;
    std::array<double, 2> bodyRadii;
    std::string body1Name;
    std::string body2Name;
    double initTime;
    double timeSpan;
    double timeStep;
};

// Initial Conditions Structures For Three Body
struct ThreeBodyIC {
    std::array<double, 3> body1InitialPosition;
    std::array<double, 3> body2InitialPosition;
    std::array<double, 3> body3InitialPosition;
    std::array<double, 3> body1InitialVelocity;
    std::array<double, 3> body2InitialVelocity;
    std::array<double, 3> body3InitialVelocity;
    std::array<double, 3> bodyMasses;
    std::array<double, 3> bodyRadii;
    std::string body1Name;
    std::string body2Name;
    std::string body3Name;
    double initTime;
    double timeSpan;
    double timeStep;
};

// Solution Structures For Single Body
struct SingleBodySolution {
    std::vector<double> positions;
    std::vector<double> velocities;
    std::vector<double> times;
};

// Solution Structures For Two Body
struct TwoBodySolution {
    std::vector<std::array<double, 3>> body1Positions;
    std::vector<std::array<double, 3>> body2Positions;
    std::vector<std::array<double, 3>> body1Velocities;
    std::vector<std::array<double, 3>> body2Velocities;
    std::vector<double> times;
};

// Solution Structures For Three Body
struct ThreeBodySolution {
    std::vector<std::array<double, 3>> body1Positions;
    std::vector<std::array<double, 3>> body2Positions;
    std::vector<std::array<double, 3>> body3Positions;
    std::vector<std::array<double, 3>> body1Velocities;
    std::vector<std::array<double, 3>> body2Velocities;
    std::vector<std::array<double, 3>> body3Velocities;
    std::vector<double> times;
};

// Single Body Model Parameters Structure
struct SingleBodyModelParameters {
    double bodyMass;
    double bodyRadius;
    double projectilePosition;
    double projectileVelocity;
};

// Two Body Model Parameters Structure
struct TwoBodyModelParameters {
    double opposingBodyMass;
    double positionComponent;
    double distanceVectorComponent;
};

// Three Body Model Parameters Structure
struct ThreeBodyModelParameters {
    double bodyMass1;
    double bodyMass2;
    double body1PositionComponent;
    double body2PositionComponent;
    double distanceVectorCentralBodyToBody1Component;
    double distanceVectorCentralBodyToBody2Component;
};

// Differential Equations Structure For N-Body
struct NBodyDiffyEqs {
    std::vector<double> masses;      // size N
    std::vector<double> positions;   // size 3N: [x0,y0,z0, x1,y1,z1, ...]
    std::vector<double> velocities;  // size 3N: [vx0,vy0,vz0, vx1,vy1,vz1, ...]
};

// Equations of Motion Structure For N-Body
struct NBodyEOM {
    std::vector<double> equations;   // size 6N
};

// N-Body Model Parameters Structure (helper for acceleration calculation)
struct NBodyModelParameters {
    double mass_j;       // mass of body j
    double dx, dy, dz;   // rij = rj - ri components (vector from i to j)
    double invR3;        // softened 1/r^3
};

// Initial Conditions Structure For N-Body
struct NBodyIC {
    std::vector<std::string> bodyNames;    // size N
    std::vector<double> bodyMasses;        // size N
    std::vector<double> bodyRadii;         // size N
    std::vector<double> initialPositions;  // size 3N: [x0,y0,z0, x1,y1,z1, ...]
    std::vector<double> initialVelocities; // size 3N: [vx0,vy0,vz0, vx1,vy1,vz1, ...]
    double initTime;
    double timeSpan;
    double timeStep;
};

// Solution Structure For N-Body
struct NBodySolution {
    std::vector<std::vector<double>> positions;   // size (steps+1) x 3N
    std::vector<std::vector<double>> velocities;  // size (steps+1) x 3N
    std::vector<double> times;                    // size (steps+1)
    size_t numBodies;                             // N
};

class Models {
    protected:
        double G = 6.67430e-11;
        const double epsilon = 1e-10;

    public:
        // Equations of Motion Methods
        SingleBodyEOM singleBodySystem(SingleBodyDiffyEqs modelData) const;
        TwoBodyEOM twoBodySystem(TwoBodyDiffyEqs modelData) const;
        ThreeBodyEOM threeBodySystem(ThreeBodyDiffyEqs modelData) const;
        NBodyEOM nBodySystem(const NBodyDiffyEqs& model) const;
        
        // Convert TwoBodyDiffyEqs to NBodyDiffyEqs
        static NBodyDiffyEqs toNBody(const TwoBodyDiffyEqs& twoBody);
        
        // Convert ThreeBodyDiffyEqs to NBodyDiffyEqs
        static NBodyDiffyEqs toNBody(const ThreeBodyDiffyEqs& threeBody);

    private:
        // Distance Vector Helper Method
        double distanceVectorComponent(double xPositionVector, double yPositionVector, double zPositionVector) const;

        // Acceleration Helper Methods
        double singleBodyNewtonianAcceleration(SingleBodyModelParameters model) const;
        double twoBodyNewtonianAcceleration(TwoBodyModelParameters model) const;
        double threeBodyNewtonianAcceleration(ThreeBodyModelParameters model) const;
        
        // Index helper: returns index into flattened 3N array for body i, component c (0=x, 1=y, 2=z)
        static inline size_t idx3(size_t bodyIndex, size_t component) {
            return 3 * bodyIndex + component;
        }
        
        // Compute softened inverse distance cubed: 1 / (sqrt(dx^2 + dy^2 + dz^2 + eps^2))^3
        double invDistanceCubedSoftened(double dx, double dy, double dz) const;
        
        // Add pairwise gravitational acceleration between bodies i and j
        void addPairwiseGravity(size_t i, size_t j,
                                const std::vector<double>& masses,
                                const std::vector<double>& positions,
                                std::vector<double>& accel) const;
};
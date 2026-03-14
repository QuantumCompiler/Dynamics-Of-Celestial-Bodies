#include "models.h"

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PUBLIC METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// Equations of Motion Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Single Body Equations of Motion
SingleBodyEOM Models::singleBodySystem(SingleBodyDiffyEqs model) const {
    SingleBodyModelParameters modelParams = {
        model.bodyMass,
        model.bodyRadius,
        model.position,
        model.velocity
    };
    double acceleration = singleBodyNewtonianAcceleration(modelParams);
    return {model.velocity, acceleration};
}

// Two Body Equations of Motion
TwoBodyEOM Models::twoBodySystem(TwoBodyDiffyEqs model) const {
    // Direction components from body 1 to body 2
    double r12_xComponent = model.body1Position[0] - model.body2Position[0];
    double r12_yComponent = model.body1Position[1] - model.body2Position[1];
    double r12_zComponent = model.body1Position[2] - model.body2Position[2];
    double r12 = distanceVectorComponent(r12_xComponent, r12_yComponent, r12_zComponent);

    // Direction components from body 2 to body 1
    double r21_xComponent = model.body2Position[0] - model.body1Position[0];
    double r21_yComponent = model.body2Position[1] - model.body1Position[1];
    double r21_zComponent = model.body2Position[2] - model.body1Position[2];
    double r21 = distanceVectorComponent(r21_xComponent, r21_yComponent, r21_zComponent);

    // Acceleration components from body 1 due to body 2
    double m1a_xComponent = twoBodyNewtonianAcceleration({model.bodyMasses[1], r21_xComponent, r21});
    double m1a_yComponent = twoBodyNewtonianAcceleration({model.bodyMasses[1], r21_yComponent, r21});
    double m1a_zComponent = twoBodyNewtonianAcceleration({model.bodyMasses[1], r21_zComponent, r21});

    // Acceleration components from body 2 due to body 1
    double m2a_xComponent = twoBodyNewtonianAcceleration({model.bodyMasses[0], r12_xComponent, r12});
    double m2a_yComponent = twoBodyNewtonianAcceleration({model.bodyMasses[0], r12_yComponent, r12});
    double m2a_zComponent = twoBodyNewtonianAcceleration({model.bodyMasses[0], r12_zComponent, r12});

    return {
        model.body1Velocity[0], model.body1Velocity[1], model.body1Velocity[2],
        model.body2Velocity[0], model.body2Velocity[1], model.body2Velocity[2],
        m1a_xComponent, m1a_yComponent, m1a_zComponent,
        m2a_xComponent, m2a_yComponent, m2a_zComponent
    };
}

// Three Body Equations of Motion
ThreeBodyEOM Models::threeBodySystem(ThreeBodyDiffyEqs model) const {
    // Direction components from body 1 to body 2
    double r12_xComponent = model.body1Position[0] - model.body2Position[0];
    double r12_yComponent = model.body1Position[1] - model.body2Position[1];
    double r12_zComponent = model.body1Position[2] - model.body2Position[2];
    double r12 = distanceVectorComponent(r12_xComponent, r12_yComponent, r12_zComponent);

    // Direction components from body 2 to body 1
    double r21_xComponent = model.body2Position[0] - model.body1Position[0];
    double r21_yComponent = model.body2Position[1] - model.body1Position[1];
    double r21_zComponent = model.body2Position[2] - model.body1Position[2];
    double r21 = distanceVectorComponent(r21_xComponent, r21_yComponent, r21_zComponent);

    // Direction components from body 2 to body 3
    double r23_xComponent = model.body2Position[0] - model.body3Position[0];
    double r23_yComponent = model.body2Position[1] - model.body3Position[1];
    double r23_zComponent = model.body2Position[2] - model.body3Position[2];
    double r23 = distanceVectorComponent(r23_xComponent, r23_yComponent, r23_zComponent);

    // Direction components from body 3 to body 2
    double r32_xComponent = model.body3Position[0] - model.body2Position[0];
    double r32_yComponent = model.body3Position[1] - model.body2Position[1];
    double r32_zComponent = model.body3Position[2] - model.body2Position[2];
    double r32 = distanceVectorComponent(r32_xComponent, r32_yComponent, r32_zComponent);

    // Direction components from body 1 to body 3
    double r13_xComponent = model.body1Position[0] - model.body3Position[0];
    double r13_yComponent = model.body1Position[1] - model.body3Position[1];
    double r13_zComponent = model.body1Position[2] - model.body3Position[2];
    double r13 = distanceVectorComponent(r13_xComponent, r13_yComponent, r13_zComponent);

    // Direction components from body 3 to body 1
    double r31_xComponent = model.body3Position[0] - model.body1Position[0];
    double r31_yComponent = model.body3Position[1] - model.body1Position[1];
    double r31_zComponent = model.body3Position[2] - model.body1Position[2];
    double r31 = distanceVectorComponent(r31_xComponent, r31_yComponent, r31_zComponent);

    // Acceleration components from body 1 due to body 2 and body 3
    double m1a_xComponent = threeBodyNewtonianAcceleration({model.bodyMasses[1], model.bodyMasses[2], r21_xComponent, r31_xComponent, r21, r31});
    double m1a_yComponent = threeBodyNewtonianAcceleration({model.bodyMasses[1], model.bodyMasses[2], r21_yComponent, r31_yComponent, r21, r31});
    double m1a_zComponent = threeBodyNewtonianAcceleration({model.bodyMasses[1], model.bodyMasses[2], r21_zComponent, r31_zComponent, r21, r31});

    // Acceleration components from body 2 due to body 1 and body 3
    double m2a_xComponent = threeBodyNewtonianAcceleration({model.bodyMasses[0], model.bodyMasses[2], r12_xComponent, r32_xComponent, r12, r32});
    double m2a_yComponent = threeBodyNewtonianAcceleration({model.bodyMasses[0], model.bodyMasses[2], r12_yComponent, r32_yComponent, r12, r32});
    double m2a_zComponent = threeBodyNewtonianAcceleration({model.bodyMasses[0], model.bodyMasses[2], r12_zComponent, r32_zComponent, r12, r32});

    // Acceleration components from body 3 due to body 1 and body 2
    double m3a_xComponent = threeBodyNewtonianAcceleration({model.bodyMasses[0], model.bodyMasses[1], r13_xComponent, r23_xComponent, r13, r23});
    double m3a_yComponent = threeBodyNewtonianAcceleration({model.bodyMasses[0], model.bodyMasses[1], r13_yComponent, r23_yComponent, r13, r23});
    double m3a_zComponent = threeBodyNewtonianAcceleration({model.bodyMasses[0], model.bodyMasses[1], r13_zComponent, r23_zComponent, r13, r23});

    return {
        model.body1Velocity[0], model.body1Velocity[1], model.body1Velocity[2],
        model.body2Velocity[0], model.body2Velocity[1], model.body2Velocity[2],
        model.body3Velocity[0], model.body3Velocity[1], model.body3Velocity[2],
        m1a_xComponent, m1a_yComponent, m1a_zComponent,
        m2a_xComponent, m2a_yComponent, m2a_zComponent,
        m3a_xComponent, m3a_yComponent, m3a_zComponent
    };
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PRIVATE METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// Generic Helper Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Distance Vector Component Helper
double Models::distanceVectorComponent(double xPositionVector, double yPositionVector, double zPositionVector) const {
    return std::pow(std::pow(xPositionVector, 2) + std::pow(yPositionVector, 2) + std::pow(zPositionVector, 2), 1.5);
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// Acceleration Helper Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Single Body Newtonian Acceleration Helper
double Models::singleBodyNewtonianAcceleration(SingleBodyModelParameters model) const {
    double r = model.bodyRadius + model.projectilePosition;
    return - (G * model.bodyMass) / (r * r);
}

// Two Body Newtonian Acceleration Helper
double Models::twoBodyNewtonianAcceleration(TwoBodyModelParameters model) const {
    return (G * model.opposingBodyMass * model.positionComponent) / model.distanceVectorComponent;
}

// Three Body Newtonian Acceleration Helper
double Models::threeBodyNewtonianAcceleration(ThreeBodyModelParameters model) const {
    return (G * model.bodyMass1 * model.body1PositionComponent) / model.distanceVectorCentralBodyToBody1Component +
        (G * model.bodyMass2 * model.body2PositionComponent) / model.distanceVectorCentralBodyToBody2Component;
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// N-Body Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Compute softened inverse distance cubed: 1 / (sqrt(dx^2 + dy^2 + dz^2 + eps^2))^3
double Models::invDistanceCubedSoftened(double dx, double dy, double dz) const {
    double r2 = dx * dx + dy * dy + dz * dz + epsilon * epsilon;
    double r = std::sqrt(r2);
    return 1.0 / (r * r * r);
}

// Add pairwise gravitational acceleration between bodies i and j
void Models::addPairwiseGravity(size_t i, size_t j,
                                const std::vector<double>& masses,
                                const std::vector<double>& positions,
                                std::vector<double>& accel) const {
    // Compute rij = rj - ri (vector from body i to body j)
    double dx = positions[idx3(j, 0)] - positions[idx3(i, 0)];
    double dy = positions[idx3(j, 1)] - positions[idx3(i, 1)];
    double dz = positions[idx3(j, 2)] - positions[idx3(i, 2)];
    
    // Compute softened 1/r^3
    double invR3 = invDistanceCubedSoftened(dx, dy, dz);
    
    // Gravitational acceleration magnitude factors
    double Gmj_invR3 = G * masses[j] * invR3;
    double Gmi_invR3 = G * masses[i] * invR3;
    
    // Apply Newton's third law:
    // Body i accelerates toward j: ai += G * mj * rij / |rij|^3
    accel[idx3(i, 0)] += Gmj_invR3 * dx;
    accel[idx3(i, 1)] += Gmj_invR3 * dy;
    accel[idx3(i, 2)] += Gmj_invR3 * dz;
    
    // Body j accelerates toward i: aj -= G * mi * rij / |rij|^3 (opposite direction)
    accel[idx3(j, 0)] -= Gmi_invR3 * dx;
    accel[idx3(j, 1)] -= Gmi_invR3 * dy;
    accel[idx3(j, 2)] -= Gmi_invR3 * dz;
}

// N-Body Equations of Motion
NBodyEOM Models::nBodySystem(const NBodyDiffyEqs& model) const {
    size_t N = model.masses.size();
    
    // Validate input sizes
    if (N < 2) {
        throw std::invalid_argument("N-body system requires at least 2 bodies");
    }
    if (model.positions.size() != 3 * N) {
        throw std::invalid_argument("positions vector must have size 3N");
    }
    if (model.velocities.size() != 3 * N) {
        throw std::invalid_argument("velocities vector must have size 3N");
    }
    
    // Initialize acceleration vector (size 3N, all zeros)
    std::vector<double> accel(3 * N, 0.0);
    
    // Compute pairwise gravitational accelerations
    // Loop over all unique pairs (i, j) where i < j
    for (size_t i = 0; i < N; ++i) {
        for (size_t j = i + 1; j < N; ++j) {
            addPairwiseGravity(i, j, model.masses, model.positions, accel);
        }
    }
    
    // Build equations vector (size 6N)
    // First 3N entries: velocities
    // Next 3N entries: accelerations
    std::vector<double> equations(6 * N);
    
    // Copy velocities to first 3N entries
    for (size_t k = 0; k < 3 * N; ++k) {
        equations[k] = model.velocities[k];
    }
    
    // Copy accelerations to next 3N entries
    for (size_t k = 0; k < 3 * N; ++k) {
        equations[3 * N + k] = accel[k];
    }
    
    return NBodyEOM{equations};
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// N-Body Adapter Functions (for backward compatibility)
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Convert TwoBodyDiffyEqs to NBodyDiffyEqs
NBodyDiffyEqs Models::toNBody(const TwoBodyDiffyEqs& twoBody) {
    NBodyDiffyEqs nBody;
    
    // Masses: [m0, m1]
    nBody.masses = {twoBody.bodyMasses[0], twoBody.bodyMasses[1]};
    
    // Positions: [x0,y0,z0, x1,y1,z1]
    nBody.positions = {
        twoBody.body1Position[0], twoBody.body1Position[1], twoBody.body1Position[2],
        twoBody.body2Position[0], twoBody.body2Position[1], twoBody.body2Position[2]
    };
    
    // Velocities: [vx0,vy0,vz0, vx1,vy1,vz1]
    nBody.velocities = {
        twoBody.body1Velocity[0], twoBody.body1Velocity[1], twoBody.body1Velocity[2],
        twoBody.body2Velocity[0], twoBody.body2Velocity[1], twoBody.body2Velocity[2]
    };
    
    return nBody;
}

// Convert ThreeBodyDiffyEqs to NBodyDiffyEqs
NBodyDiffyEqs Models::toNBody(const ThreeBodyDiffyEqs& threeBody) {
    NBodyDiffyEqs nBody;
    
    // Masses: [m0, m1, m2]
    nBody.masses = {threeBody.bodyMasses[0], threeBody.bodyMasses[1], threeBody.bodyMasses[2]};
    
    // Positions: [x0,y0,z0, x1,y1,z1, x2,y2,z2]
    nBody.positions = {
        threeBody.body1Position[0], threeBody.body1Position[1], threeBody.body1Position[2],
        threeBody.body2Position[0], threeBody.body2Position[1], threeBody.body2Position[2],
        threeBody.body3Position[0], threeBody.body3Position[1], threeBody.body3Position[2]
    };
    
    // Velocities: [vx0,vy0,vz0, vx1,vy1,vz1, vx2,vy2,vz2]
    nBody.velocities = {
        threeBody.body1Velocity[0], threeBody.body1Velocity[1], threeBody.body1Velocity[2],
        threeBody.body2Velocity[0], threeBody.body2Velocity[1], threeBody.body2Velocity[2],
        threeBody.body3Velocity[0], threeBody.body3Velocity[1], threeBody.body3Velocity[2]
    };
    
    return nBody;
}
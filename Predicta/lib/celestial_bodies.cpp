#include "celestial_bodies.h"

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PUBLIC METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// Common Celestial Bodies Initialization
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Sun
const Body CelestialBody::sun = {
    "Sun",
    2e30,
    6.96265e8,
    0,
    {0, 0, 0},
    {0, 0, 0}
};

// Mercury
const Body CelestialBody::mercury = {
    "Mercury",
    3.30104e23,
    2.439700e6,
    88 * CelestialBody::DS,
    {0.4 * CelestialBody::AU, 0, 0},
    {0, 4.7800e4, 0}
};

// Venus
const Body CelestialBody::venus = {
    "Venus",
    4.86732e24,
    6.05e6,
    225 * CelestialBody::DS,
    {0.72 * CelestialBody::AU, 0, 0},
    {0, 3.5021e4, 0}
};

// Earth
const Body CelestialBody::earth = {
    "Earth",
    5.972e24,
    6.3781e6,
    365.25 * CelestialBody::DS,
    {CelestialBody::AU, 0, 0},
    {0, 2.97848e4, 0}
};

// Mars
const Body CelestialBody::mars = {
    "Mars",
    6.41693e23,
    3.3895e6,
    647 * CelestialBody::DS,
    {1.52 * CelestialBody::AU, 0, 0},
    {0, 2.4077e4, 0}
};

// Jupiter
const Body CelestialBody::jupiter = {
    "Jupiter",
    1.9e27,
    6.9911e7,
    4.333e3 * CelestialBody::DS,
    {5.2 * CelestialBody::AU, 0, 0},
    {0, 1.3070e4, 0}
};

// Saturn
const Body CelestialBody::saturn = {
    "Saturn",
    5.68319e26,
    5.8232e7,
    1.0756e4 * CelestialBody::DS,
    {9.5 * CelestialBody::AU, 0, 0},
    {0, 9.680e3, 0}
};

// Uranus
const Body CelestialBody::uranus = {
    "Uranus",
    8.68103e25,
    2.5362000e7,
    3.0687e4 * CelestialBody::DS,
    {19.2 * CelestialBody::AU, 0, 0},
    {0, 6.810e3, 0}
};

// Neptune
const Body CelestialBody::neptune = {
    "Neptune",
    1.0241e26,
    2.4622e7,
    6.0190e4 * CelestialBody::DS,
    {30 * CelestialBody::AU, 0, 0},
    {0, 5.430e3, 0}
};

// Pluto
const Body CelestialBody::pluto = {
    "Pluto",
    1.30900e22,
    1.188000e6,
    9.0582e4 * CelestialBody::DS,
    {39 * CelestialBody::AU, 0, 0},
    {0, 4.666e3, 0}
};

// Common Bodies Array
const std::array<Body, 10> CelestialBody::commonBodies = {
    CelestialBody::sun,
    CelestialBody::mercury,
    CelestialBody::venus,
    CelestialBody::earth,
    CelestialBody::mars,
    CelestialBody::jupiter,
    CelestialBody::saturn,
    CelestialBody::uranus,
    CelestialBody::neptune,
    CelestialBody::pluto
};

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// Display Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Displays all common celestial bodies
void CelestialBody::displayCommonBodies() {
    const std::array<Body, 10> &commonBodies = CelestialBody::commonBodies;
    for (int i = 0; i < commonBodies.size(); ++i) {
        std::cout << "Name: " << commonBodies[i].name << std::endl;
        std::cout << "Mass: " << commonBodies[i].mass << std::endl;
        std::cout << "Radius: " << commonBodies[i].radius << std::endl;
        std::cout << "Period: " << commonBodies[i].period << std::endl;
        std::cout << "Initial Positions: " << commonBodies[i].position[0] << ", " << commonBodies[i].position[1] << ", " << commonBodies[i].position[2] << std::endl;
        std::cout << "Initial Velocities: " << commonBodies[i].velocity[0] << ", " << commonBodies[i].velocity[1] << ", " << commonBodies[i].velocity[2] << std::endl;
        std::cout << "------------------------" << std::endl;
    }
}

// Displays information for a specific common celestial body
void CelestialBody::displayBodyInfo(Body body) {
    std::cout << "Name: " << body.name << std::endl;
    std::cout << "Mass: " << body.mass << std::endl;
    std::cout << "Radius: " << body.radius << std::endl;
    std::cout << "Period: " << body.period << std::endl;
    std::cout << "Initial Positions: " << body.position[0] << ", " << body.position[1] << ", " << body.position[2] << std::endl;
    std::cout << "Initial Velocities: " << body.velocity[0] << ", " << body.velocity[1] << ", " << body.velocity[2] << std::endl;
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// Body Generation Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Generates a random common celestial body
Body CelestialBody::chooseRandomCommonBody() {
    int index = SystemUtilities::getRandomInt(0, CelestialBody::commonBodies.size() - 1);
    return CelestialBody::commonBodies[index];
}

// Generates a custom celestial body based on user input
Body CelestialBody::generateCustomBody() {
    std::string bodyName;
    double bodyMass;
    double bodyRadius;
    double bodyPeriod;
    std::array<double, 3> bodyPosition;;
    std::array<double, 3> bodyVelocity;

    std::cout << "Common Celestial Bodies For Reference:" << std::endl << std::endl;
    CelestialBody::displayCommonBodies();
    std::cout << std::endl;

    std::cout << "Enter the name of the celestial body: ";
    std::getline(std::cin, bodyName);
    std::cout << std::endl;
    std::cout << "Enter the mass of the celestial body (Kg): ";
    std::cin >> bodyMass;
    std::cout << std::endl;
    std::cout << "Enter the radius of the celestial body (m): ";
    std::cin >> bodyRadius;
    std::cout << std::endl;
    std::cout << "Enter the orbital period of the celestial body in earth years (yrs): ";
    double periodYears;
    std::cin >> periodYears;
    bodyPeriod = CelestialBody::earthYearsToSeconds(periodYears);
    std::cout << std::endl;
    std::cout << "Enter the initial x, y, z position of the celestial body in meters (m) separated by spaces: ";
    std::cin >> bodyPosition[0] >> bodyPosition[1] >> bodyPosition[2];
    std::cout << std::endl;
    std::cout << "Enter the initial x, y, z velocity of the celestial body in meters per second (m/s) separated by spaces: ";
    std::cin >> bodyVelocity[0] >> bodyVelocity[1] >> bodyVelocity[2];
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::cout << std::endl;
    return {
        bodyName,
        bodyMass,
        bodyRadius,
        bodyPeriod,
        bodyPosition,
        bodyVelocity
    };
}

// Generates a random celestial body
Body CelestialBody::generateRandomSingleBody() {
    std::string bodyName = "Random Body";
    double randomMass = SystemUtilities::getRandomDouble(CelestialBody::pluto.mass, CelestialBody::sun.mass);
    double randomRadius = SystemUtilities::getRandomDouble(CelestialBody::pluto.radius, CelestialBody::sun.radius);
    double randomPeriod = SystemUtilities::getRandomDouble(CelestialBody::mercury.period, CelestialBody::pluto.period);
    std::array<double, 3> randomPositions = {
        SystemUtilities::getRandomDouble(0, CelestialBody::AU * 10),
        SystemUtilities::getRandomDouble(0, CelestialBody::AU * 10),
        SystemUtilities::getRandomDouble(0, CelestialBody::AU * 10)
    };
    std::array<double, 3> randomVelocities = {
        SystemUtilities::getRandomDouble(0, 6e4),
        SystemUtilities::getRandomDouble(0, 6e4),
        SystemUtilities::getRandomDouble(0, 6e4)
    };
    return {
        bodyName,
        randomMass,
        randomRadius,
        randomPeriod,
        randomPositions,
        randomVelocities
    };
}

// Generates two random bodies with interesting orbital configurations
std::array<Body, 2> CelestialBody::generateRandomTwoBody() {
    // Generate a central massive body (like a star)
    double centralMass = SystemUtilities::getRandomDouble(1e28, 2e31);  // Star-like mass
    double centralRadius = SystemUtilities::getRandomDouble(1e8, 1e10);
    
    // Generate an orbiting body (like a planet)
    double orbitingMass = SystemUtilities::getRandomDouble(1e22, 1e27);  // Planet-like mass
    double orbitingRadius = SystemUtilities::getRandomDouble(1e6, 1e8);
    
    // Place central body at origin (or slight offset)
    std::array<double, 3> centralPos = {0.0, 0.0, 0.0};
    std::array<double, 3> centralVel = {0.0, 0.0, 0.0};
    
    // Generate orbital distance (semi-major axis) - use AU scale
    double orbitalDistance = SystemUtilities::getRandomDouble(0.3 * AU, 5.0 * AU);
    
    // Generate random orbital phase angle (0 to 2*PI)
    double theta = SystemUtilities::getRandomDouble(0.0, 2.0 * M_PI);
    
    // Place orbiting body at random position on orbit
    std::array<double, 3> orbitingPos = {
        orbitalDistance * std::cos(theta),
        orbitalDistance * std::sin(theta),
        0.0  // Keep in orbital plane for simplicity
    };
    
    // Calculate circular orbital velocity: v = sqrt(G * M / r)
    double orbitalSpeed = std::sqrt(G * centralMass / orbitalDistance);
    
    // Add some eccentricity variation (0.8 to 1.2 of circular velocity)
    double eccentricityFactor = SystemUtilities::getRandomDouble(0.8, 1.2);
    orbitalSpeed *= eccentricityFactor;
    
    // Velocity is perpendicular to position vector (for circular/elliptical orbit)
    std::array<double, 3> orbitingVel = {
        -orbitalSpeed * std::sin(theta),
        orbitalSpeed * std::cos(theta),
        0.0
    };
    
    // Adjust central body velocity for conservation of momentum (optional, for realism)
    double massRatio = orbitingMass / centralMass;
    centralVel = {
        -orbitingVel[0] * massRatio,
        -orbitingVel[1] * massRatio,
        -orbitingVel[2] * massRatio
    };
    
    // Estimate orbital period using Kepler's third law: T = 2*PI*sqrt(a^3/(G*M))
    double period = 2.0 * M_PI * std::sqrt(std::pow(orbitalDistance, 3) / (G * centralMass));
    
    Body body1 = {
        "Star_" + std::to_string(static_cast<int>(centralMass / 1e28)),
        centralMass,
        centralRadius,
        0.0,  // Central body doesn't have a meaningful period
        centralPos,
        centralVel
    };
    
    Body body2 = {
        "Planet_" + std::to_string(static_cast<int>(orbitalDistance / AU * 100)),
        orbitingMass,
        orbitingRadius,
        period,
        orbitingPos,
        orbitingVel
    };
    
    return {body1, body2};
}

// Generates three random bodies with interesting orbital configurations
std::array<Body, 3> CelestialBody::generateRandomThreeBody() {
    // Generate a central massive body (like a star)
    double centralMass = SystemUtilities::getRandomDouble(1e29, 2e31);  // Star-like mass
    double centralRadius = SystemUtilities::getRandomDouble(1e8, 1e10);
    
    // Generate two orbiting bodies (like planets)
    double orbitingMass1 = SystemUtilities::getRandomDouble(1e23, 1e27);  // Planet-like mass
    double orbitingRadius1 = SystemUtilities::getRandomDouble(1e6, 1e8);
    
    double orbitingMass2 = SystemUtilities::getRandomDouble(1e22, 1e26);  // Smaller planet
    double orbitingRadius2 = SystemUtilities::getRandomDouble(1e6, 1e7);
    
    // Place central body at origin
    std::array<double, 3> centralPos = {0.0, 0.0, 0.0};
    std::array<double, 3> centralVel = {0.0, 0.0, 0.0};
    
    // Generate orbital distances - ensure they're well separated to avoid collisions
    double orbitalDistance1 = SystemUtilities::getRandomDouble(0.3 * AU, 1.5 * AU);
    double orbitalDistance2 = SystemUtilities::getRandomDouble(2.0 * AU, 6.0 * AU);
    
    // Ensure body2 is always further out
    if (orbitalDistance2 < orbitalDistance1 * 1.5) {
        orbitalDistance2 = orbitalDistance1 * SystemUtilities::getRandomDouble(1.8, 3.0);
    }
    
    // Generate random orbital phase angles (0 to 2*PI) - different for each body
    double theta1 = SystemUtilities::getRandomDouble(0.0, 2.0 * M_PI);
    double theta2 = SystemUtilities::getRandomDouble(0.0, 2.0 * M_PI);
    
    // Ensure planets start at different orbital phases (at least 30 degrees apart)
    while (std::abs(theta2 - theta1) < M_PI / 6.0) {
        theta2 = SystemUtilities::getRandomDouble(0.0, 2.0 * M_PI);
    }
    
    // Place orbiting bodies at random positions on their orbits
    std::array<double, 3> orbitingPos1 = {
        orbitalDistance1 * std::cos(theta1),
        orbitalDistance1 * std::sin(theta1),
        0.0
    };
    
    std::array<double, 3> orbitingPos2 = {
        orbitalDistance2 * std::cos(theta2),
        orbitalDistance2 * std::sin(theta2),
        0.0
    };
    
    // Calculate circular orbital velocities: v = sqrt(G * M / r)
    double orbitalSpeed1 = std::sqrt(G * centralMass / orbitalDistance1);
    double orbitalSpeed2 = std::sqrt(G * centralMass / orbitalDistance2);
    
    // Add some eccentricity variation (0.85 to 1.15 of circular velocity)
    double eccentricityFactor1 = SystemUtilities::getRandomDouble(0.85, 1.15);
    double eccentricityFactor2 = SystemUtilities::getRandomDouble(0.85, 1.15);
    orbitalSpeed1 *= eccentricityFactor1;
    orbitalSpeed2 *= eccentricityFactor2;
    
    // Velocity is perpendicular to position vector (for circular/elliptical orbit)
    std::array<double, 3> orbitingVel1 = {
        -orbitalSpeed1 * std::sin(theta1),
        orbitalSpeed1 * std::cos(theta1),
        0.0
    };
    
    std::array<double, 3> orbitingVel2 = {
        -orbitalSpeed2 * std::sin(theta2),
        orbitalSpeed2 * std::cos(theta2),
        0.0
    };
    
    // Adjust central body velocity for conservation of momentum
    double massRatio1 = orbitingMass1 / centralMass;
    double massRatio2 = orbitingMass2 / centralMass;
    centralVel = {
        -(orbitingVel1[0] * massRatio1 + orbitingVel2[0] * massRatio2),
        -(orbitingVel1[1] * massRatio1 + orbitingVel2[1] * massRatio2),
        -(orbitingVel1[2] * massRatio1 + orbitingVel2[2] * massRatio2)
    };
    
    // Estimate orbital periods using Kepler's third law
    double period1 = 2.0 * M_PI * std::sqrt(std::pow(orbitalDistance1, 3) / (G * centralMass));
    double period2 = 2.0 * M_PI * std::sqrt(std::pow(orbitalDistance2, 3) / (G * centralMass));
    
    Body body1 = {
        "Star_" + std::to_string(static_cast<int>(centralMass / 1e28)),
        centralMass,
        centralRadius,
        0.0,
        centralPos,
        centralVel
    };
    
    Body body2 = {
        "Planet_Inner_" + std::to_string(static_cast<int>(orbitalDistance1 / AU * 100)),
        orbitingMass1,
        orbitingRadius1,
        period1,
        orbitingPos1,
        orbitingVel1
    };
    
    Body body3 = {
        "Planet_Outer_" + std::to_string(static_cast<int>(orbitalDistance2 / AU * 100)),
        orbitingMass2,
        orbitingRadius2,
        period2,
        orbitingPos2,
        orbitingVel2
    };
    
    return {body1, body2, body3};
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// Random Single Body Parameter Generation Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Generates random numerical method parameters for single body simulations
std::array<double, 2> CelestialBody::generateRandomSingleBodyNumMethodParams() {
    double randomTimeSpan = SystemUtilities::getRandomDouble(UniversalConstants::minSingleBodyTimeSpan, UniversalConstants::maxSingleBodyTimeSpan);
    double randomTimeStep = SystemUtilities::getRandomDouble(UniversalConstants::minSingleBodyTimeStep, UniversalConstants::maxSingleBodyTimeStep);
    return {randomTimeSpan, randomTimeStep};
}

// Generates random projectile initial conditions for single body simulations
std::array<double, 2> CelestialBody::generateRandomSingleBodyProjectileIC() {
    double randomPosition = SystemUtilities::getRandomDouble(UniversalConstants::minSingleBodyPosition, UniversalConstants::maxSingleBodyPosition);
    double randomVelocity = SystemUtilities::getRandomDouble(UniversalConstants::minSingleBodyVelocity, UniversalConstants::maxSingleBodyVelocity);
    return {randomPosition, randomVelocity};
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// Random Two Body Parameter Generation Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Generates random numerical method parameters for two body simulations
std::array<double, 2> CelestialBody::generateRandomTwoBodyNumMethodParams(Body body1, Body body2) {
    double maxPeriodBetweenBodies = std::max(body1.period, body2.period);
    double uniformTimeStep = maxPeriodBetweenBodies / 249999;
    return {maxPeriodBetweenBodies, uniformTimeStep};
}

// Generates random numerical method parameters for three body simulations
std::array<double, 2> CelestialBody::generateRandomThreeBodyNumMethodParams(Body body1, Body body2, Body body3) {
    double maxPeriodBetweenBodies = std::max({body1.period, body2.period, body3.period});
    double uniformTimeStep = maxPeriodBetweenBodies / 499999;
    return {maxPeriodBetweenBodies, uniformTimeStep};
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// Random N Body Parameter Generation Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Generates N random bodies (4-10) with interesting orbital configurations
std::vector<Body> CelestialBody::generateRandomNBody() {
    // Generate random number of bodies between 4 and 10
    int numBodies = SystemUtilities::getRandomInt(4, 10);
    std::vector<Body> bodies;
    bodies.reserve(numBodies);
    
    // Generate a central massive body (like a star)
    double centralMass = SystemUtilities::getRandomDouble(5e29, 3e31);  // Large star mass
    double centralRadius = SystemUtilities::getRandomDouble(1e8, 2e10);
    
    // Place central body at origin
    std::array<double, 3> centralPos = {0.0, 0.0, 0.0};
    std::array<double, 3> centralVel = {0.0, 0.0, 0.0};
    
    Body centralBody = {
        "Star_Central",
        centralMass,
        centralRadius,
        0.0,
        centralPos,
        centralVel
    };
    
    bodies.push_back(centralBody);
    
    // Generate orbital distances - spread them out to avoid collisions
    std::vector<double> orbitalDistances;
    orbitalDistances.reserve(numBodies - 1);
    
    // Create well-spaced orbital distances from 0.3 AU to 8 AU
    double minDistance = 0.3 * AU;
    double maxDistance = 8.0 * AU;
    double distanceStep = (maxDistance - minDistance) / (numBodies - 2);
    
    for (int i = 0; i < numBodies - 1; ++i) {
        double baseDistance = minDistance + i * distanceStep;
        // Add some randomness while maintaining order
        double randomOffset = SystemUtilities::getRandomDouble(-distanceStep * 0.15, distanceStep * 0.15);
        double distance = baseDistance + randomOffset;
        
        // Ensure minimum separation
        if (i > 0 && distance < orbitalDistances.back() * 1.2) {
            distance = orbitalDistances.back() * SystemUtilities::getRandomDouble(1.3, 1.6);
        }
        
        orbitalDistances.push_back(distance);
    }
    
    // Track total momentum for conservation
    std::array<double, 3> totalMomentum = {0.0, 0.0, 0.0};
    
    // Generate orbiting bodies
    for (int i = 0; i < numBodies - 1; ++i) {
        double orbitingMass = SystemUtilities::getRandomDouble(1e21, 1e27);  // Planet-like mass range
        double orbitingRadius = SystemUtilities::getRandomDouble(1e6, 1e8);
        double orbitalDistance = orbitalDistances[i];
        
        // Generate random orbital phase angle
        double theta = SystemUtilities::getRandomDouble(0.0, 2.0 * M_PI);
        
        // Add slight inclination variation (up to 10 degrees from orbital plane)
        double inclination = SystemUtilities::getRandomDouble(-M_PI / 18.0, M_PI / 18.0);
        double z_offset = orbitalDistance * std::sin(inclination);
        double xy_distance = orbitalDistance * std::cos(inclination);
        
        // Position in orbit with slight 3D variation
        std::array<double, 3> orbitingPos = {
            xy_distance * std::cos(theta),
            xy_distance * std::sin(theta),
            z_offset
        };
        
        // Calculate circular orbital velocity
        double orbitalSpeed = std::sqrt(G * centralMass / orbitalDistance);
        
        // Add eccentricity variation
        double eccentricityFactor = SystemUtilities::getRandomDouble(0.8, 1.25);
        orbitalSpeed *= eccentricityFactor;
        
        // Velocity perpendicular to position vector (with inclination consideration)
        std::array<double, 3> orbitingVel = {
            -orbitalSpeed * std::sin(theta) * std::cos(inclination),
            orbitalSpeed * std::cos(theta) * std::cos(inclination),
            orbitalSpeed * std::sin(inclination) * SystemUtilities::getRandomDouble(-0.1, 0.1)
        };
        
        // Calculate orbital period
        double period = 2.0 * M_PI * std::sqrt(std::pow(orbitalDistance, 3) / (G * centralMass));
        
        Body orbitingBody = {
            "Planet_" + std::to_string(i + 1) + "_" + std::to_string(static_cast<int>(orbitalDistance / AU * 100)),
            orbitingMass,
            orbitingRadius,
            period,
            orbitingPos,
            orbitingVel
        };
        
        bodies.push_back(orbitingBody);
        
        // Add to total momentum for conservation
        totalMomentum[0] += orbitingMass * orbitingVel[0];
        totalMomentum[1] += orbitingMass * orbitingVel[1];
        totalMomentum[2] += orbitingMass * orbitingVel[2];
    }
    
    // Adjust central body velocity for momentum conservation
    bodies[0].velocity[0] = -totalMomentum[0] / centralMass;
    bodies[0].velocity[1] = -totalMomentum[1] / centralMass;
    bodies[0].velocity[2] = -totalMomentum[2] / centralMass;
    
    return bodies;
}

// Generates random numerical method parameters for N body simulations
std::array<double, 2> CelestialBody::generateRandomNBodyNumMethodParams(const std::vector<Body>& bodies) {
    // Find the maximum period among all bodies to ensure we capture full orbital dynamics
    double maxPeriod = 0.0;
    for (const Body& body : bodies) {
        if (body.period > maxPeriod) {
            maxPeriod = body.period;
        }
    }
    
    // For N-body systems, we need very small time steps due to complex multi-body interactions
    // Use even smaller time steps than three-body system for numerical stability
    double uniformTimeStep = maxPeriod / 999999;  // Very high resolution for N-body stability
    
    return {maxPeriod, uniformTimeStep};
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// Uniform Single Body Parameter Generation Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Generates uniformly distributed numerical method parameters for single body simulations
std::vector<std::pair<double, double>> CelestialBody::generateUniformSingleBodyNumMethodParams(int spanBins, int stepBins, bool shuffle) {
    std::vector<std::pair<double, double>> params;

    if (spanBins <= 0 || stepBins <= 0) {
        return params;
    }

    std::vector<double> spans = CelestialBody::generateUniformSingleBodyProjectileTimeSpan(spanBins);
    std::vector<double> steps = CelestialBody::generateUniformSingleBodyProjectileTimeStep(stepBins);

    params.reserve(static_cast<size_t>(spans.size()) * static_cast<size_t>(steps.size()));

    for (double p : spans) {
        for (double v : steps) {
            params.emplace_back(p, v);
        }
    }

    if (shuffle && params.size() > 1) {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::shuffle(params.begin(), params.end(), gen);
    }

    return params;
}

// Generates uniformly distributed projectile initial conditions for single body simulations
std::vector<std::pair<double, double>> CelestialBody::generateUniformSingleBodyProjectileIC(int posBins, int velBins, bool shuffle) {
    std::vector<std::pair<double, double>> ics;

    if (posBins <= 0 || velBins <= 0) {
        return ics;
    }

    std::vector<double> positions = CelestialBody::generateUniformSingleBodyProjectilePositions(posBins);
    std::vector<double> velocities = CelestialBody::generateUniformSingleBodyProjectileVelocities(velBins);

    ics.reserve(static_cast<size_t>(positions.size()) * static_cast<size_t>(velocities.size()));

    for (double p : positions) {
        for (double v : velocities) {
            ics.emplace_back(p, v);
        }
    }

    if (shuffle && ics.size() > 1) {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::shuffle(ics.begin(), ics.end(), gen);
    }

    return ics;
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PRIVATE METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Generates uniformly distributed projectile positions for single body simulations
std::vector<double> CelestialBody::generateUniformSingleBodyProjectilePositions(int bins) {
    std::vector<double> positions;

    if (bins <= 0) {
        return positions;
    }

    const double minPos = UniversalConstants::minSingleBodyPosition;
    const double maxPos = UniversalConstants::maxSingleBodyPosition;
    const double posStep = (maxPos - minPos) / static_cast<double>(bins);

    positions.reserve(bins);

    for (int i = 0; i < bins; ++i) {
        const double binLow = minPos + static_cast<double>(i) * posStep;
        const double binHigh = (i == bins - 1) ? maxPos : (binLow + posStep);
        const double pos = SystemUtilities::getRandomDouble(binLow, binHigh);
        positions.push_back(pos);
    }

    return positions;
}

// Generates uniformly distributed projectile time spans for single body simulations
std::vector<double> CelestialBody::generateUniformSingleBodyProjectileTimeSpan(int bins) {
    std::vector<double> times;

    if (bins <= 0) {
        return times;
    }

    const double minSpan = UniversalConstants::minSingleBodyTimeSpan;
    const double maxSpan = UniversalConstants::maxSingleBodyTimeSpan;
    const double spanStep = (maxSpan - minSpan) / static_cast<double>(bins);

    times.reserve(bins);

    for (int i = 0; i < bins; ++i) {
        const double binLow = minSpan + static_cast<double>(i) * spanStep;
        const double binHigh = (i == bins - 1) ? maxSpan : (binLow + spanStep);
        const double time = SystemUtilities::getRandomDouble(binLow, binHigh);
        times.push_back(time);
    }

    return times;
}

// Generates uniformly distributed projectile time steps for single body simulations
std::vector<double> CelestialBody::generateUniformSingleBodyProjectileTimeStep(int bins) {
    std::vector<double> steps;

    if (bins <= 0) {
        return steps;
    }

    const double minStep = UniversalConstants::minSingleBodyTimeStep;
    const double maxStep = UniversalConstants::maxSingleBodyTimeStep;
    const double stepInc = (maxStep - minStep) / static_cast<double>(bins);

    steps.reserve(bins);

    for (int i = 0; i < bins; ++i) {
        const double binLow = minStep + static_cast<double>(i) * stepInc;
        const double binHigh = (i == bins - 1) ? maxStep : (binLow + stepInc);
        const double step = SystemUtilities::getRandomDouble(binLow, binHigh);
        steps.push_back(step);
    }

    return steps;
}

// Generates uniformly distributed projectile velocities for single body simulations
std::vector<double> CelestialBody::generateUniformSingleBodyProjectileVelocities(int bins) {
    std::vector<double> velocities;

    if (bins <= 0) {
        return velocities;
    }

    const double minVel = UniversalConstants::minSingleBodyVelocity;
    const double maxVel = UniversalConstants::maxSingleBodyVelocity;
    const double velStep = (maxVel - minVel) / static_cast<double>(bins);

    velocities.reserve(bins);

    for (int i = 0; i < bins; ++i) {
        const double binLow = minVel + static_cast<double>(i) * velStep;
        const double binHigh = (i == bins - 1) ? maxVel : (binLow + velStep);
        const double vel = SystemUtilities::getRandomDouble(binLow, binHigh);
        velocities.push_back(vel);
    }

    return velocities;
}
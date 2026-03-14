#include "predicta.h"
#include <cctype>
#include <limits>

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// Generation Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Generates a random celestial body
Body Predicta::autoBodyGenerator()
{
    return CelestialBody::generateRandomSingleBody();
}

// Generates random numerical method parameters for single body simulation
std::array<double, 2> Predicta::autoSingleBodyNumMethodGenerator()
{
    return CelestialBody::generateRandomSingleBodyNumMethodParams();
}

// Generates random projectile initial conditions for single body simulation
std::array<double, 2> Predicta::autoSingleBodyProjectileICGenerator()
{
    return CelestialBody::generateRandomSingleBodyProjectileIC();
}

// Generates numerical method parameters for two body simulation
std::array<double, 2> Predicta::autoTwoBodyNumMethodGenerator(Body body1, Body body2)
{
    return CelestialBody::generateRandomTwoBodyNumMethodParams(body1, body2);
}

// Generates numerical method parameters for three body simulation
std::array<double, 2> Predicta::autoThreeBodyNumMethodGenerator(Body body1, Body body2, Body body3)
{
    return CelestialBody::generateRandomThreeBodyNumMethodParams(body1, body2, body3);
}

// Generates numerical method parameters for three body simulation
std::array<double, 2> Predicta::autoThreeBodyNumMethodGenerator()
{
    return std::array<double, 2>{0,0}; // Placeholder
}

// Generates numerical method parameters for N body simulation
std::array<double, 2> Predicta::autoNBodyNumMethodGenerator(const std::vector<Body>& bodies)
{
    return CelestialBody::generateRandomNBodyNumMethodParams(bodies);
}

// Generates numerical method parameters for N body simulation
std::array<double, 2> Predicta::autoNBodyNumMethodGenerator()
{
    return std::array<double, 2>{0,0}; // Placeholder
}

// Allows user to select a celestial body from common bodies
Body Predicta::manualBodyGenerator()
{
    SystemUtilities::clearTerminal();

    std::vector<std::string> bodyTypeOptions = {
        "   1 : Common Celestial Body",
        "   2 : Custom Celestial Body"};
    std::string bodyTypeSelection = PythonUtilities::pythonInquirer(
        bodyTypeOptions,
        "Choose between a common celestial body or custom body for your simulation:");

    if (bodyTypeSelection == bodyTypeOptions[0])
    {
        std::vector<std::string> bodyOptions = {
            "   1 : Sun",
            "   2 : Mercury",
            "   3 : Venus",
            "   4 : Earth",
            "   5 : Mars",
            "   6 : Jupiter",
            "   7 : Saturn",
            "   8 : Uranus",
            "   9 : Neptune",
            "  10 : Pluto"};
        std::string selectedOption = PythonUtilities::pythonInquirer(
            bodyOptions,
            "Please select your common body from the list below:");
        if (selectedOption == bodyOptions[0])
            return CelestialBody::sun;
        if (selectedOption == bodyOptions[1])
            return CelestialBody::mercury;
        if (selectedOption == bodyOptions[2])
            return CelestialBody::venus;
        if (selectedOption == bodyOptions[3])
            return CelestialBody::earth;
        if (selectedOption == bodyOptions[4])
            return CelestialBody::mars;
        if (selectedOption == bodyOptions[5])
            return CelestialBody::jupiter;
        if (selectedOption == bodyOptions[6])
            return CelestialBody::saturn;
        if (selectedOption == bodyOptions[7])
            return CelestialBody::uranus;
        if (selectedOption == bodyOptions[8])
            return CelestialBody::neptune;
        if (selectedOption == bodyOptions[9])
            return CelestialBody::pluto;
    } else {
        return CelestialBody::generateCustomBody();
    }
}

// Prompts user for numerical method parameters for single body simulation
std::array<double, 2> Predicta::manualSingleBodyNumMethodGenerator()
{
    SystemUtilities::clearTerminal();
    double timeSpan;
    double timeStep;
    std::cout << "Enter the total time span of your simulation in seconds (s): ";
    std::cin >> timeSpan;
    std::cout << "Enter the time step for you simulation in seconds (s): ";
    std::cin >> timeStep;
    return std::array<double, 2>{timeSpan, timeStep};
}

// Prompts user for projectile initial conditions for single body simulation
std::array<double, 2> Predicta::manualSingleBodyProjectileICGenerator()
{
    SystemUtilities::clearTerminal();
    double pos;
    double vel;
    std::cout << "Enter the initial vertical position of your projectile in meters (m): ";
    std::cin >> pos;
    std::cout << "Enter the initial vertical velocity of your projectile in meters per second (m/s): ";
    std::cin >> vel;
    return std::array<double, 2>{pos, vel};
}

// Prompts user for projectile initial conditions for single body simulation
std::array<double, 2> Predicta::manualTwoBodyNumMethodGenerator()
{
    SystemUtilities::clearTerminal();
    double timeSpan;
    double timeStep;
    std::cout << "Enter the total time span of your simulation in earth years (yrs): ";
    std::cin >> timeSpan;
    timeSpan = CelestialBody::earthYearsToSeconds(timeSpan);
    std::cout << "Enter the time step for you simulation in seconds (s): ";
    std::cin >> timeStep;
    return std::array<double, 2>{timeSpan, timeStep};
}

// Prompts user for numerical method parameters for three body simulation
std::array<double, 2> Predicta::manualThreeBodyNumMethodGenerator()
{
    SystemUtilities::clearTerminal();
    double timeSpan;
    double timeStep;
    std::cout << "Enter the total time span of your simulation in earth years (yrs): ";
    std::cin >> timeSpan;
    timeSpan = CelestialBody::earthYearsToSeconds(timeSpan);
    std::cout << "Enter the time step for you simulation in seconds (s): ";
    std::cin >> timeStep;
    return std::array<double, 2>{timeSpan, timeStep};
}

// Prompts user for N bodies for N-body simulation
std::vector<Body> Predicta::manualNBodiesGenerator()
{
    SystemUtilities::clearTerminal();
    int N;
    std::cout << "Enter the number of bodies (N >= 2): ";
    std::cin >> N;
    while (N < 2) {
        std::cout << "Error: N must be at least 2. Please enter again: ";
        std::cin >> N;
    }
    std::vector<Body> bodies;
    for (int i = 0; i < N; ++i) {
        std::cout << "\n--- Entering data for Body " << i << " ---\n";
        Body body = Predicta::manualBodyGenerator();
        bodies.push_back(body);
    }
    return bodies;
}

// Prompts user for numerical method parameters for N-body simulation
std::array<double, 2> Predicta::manualNBodyNumMethodGenerator()
{
    SystemUtilities::clearTerminal();
    double timeSpan;
    double timeStep;
    std::cout << "Enter the total time span of your simulation in earth years (yrs): ";
    std::cin >> timeSpan;
    timeSpan = CelestialBody::earthYearsToSeconds(timeSpan);
    std::cout << "Enter the time step for you simulation in seconds (s): ";
    std::cin >> timeStep;
    return std::array<double, 2>{timeSpan, timeStep};
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// Automatic Simulation Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Runs automatic single body simulations
void Predicta::autoSingleBodySimulation()
{
    SystemUtilities::clearTerminal();
    std::vector<std::string> choices = {
        "   1 : Use common celestial Bodies for automatic single body simulations",
        "   2 : Generate random celestial Bodies for automatic single body simulations"};
    std::string selectedOption = PythonUtilities::pythonInquirer(
        choices,
        "Please select your automatic single body simulation mode:");
    std::cout << "Please enter the number of automatic single body simulations to run: ";
    int numSims;
    std::cin >> numSims;
    for (int i = 0; i < numSims; ++i)
    {
        Body CelestialBody;
        if (selectedOption == choices[0])
        {
            CelestialBody = CelestialBody::chooseRandomCommonBody();
        }
        else
        {
            CelestialBody = Predicta::autoBodyGenerator();
        }
        std::array<double, 2> projIC = Predicta::autoSingleBodyProjectileICGenerator();
        std::array<double, 2> numMethod = Predicta::autoSingleBodyNumMethodGenerator();
        Solvers solver_instance;
        SingleBodyIC initialConditions = {
            projIC[0],
            projIC[1],
            CelestialBody.name,
            CelestialBody.mass,
            CelestialBody.radius,
            0.0,
            numMethod[0],
            numMethod[1],
        };
        SingleBodySolution solution = solver_instance.RK4SingleBody(initialConditions);
        CSVUtilities::writeSingleBodySimDataCSV(initialConditions, solution, UniversalConstants::singleBodyRK4Dir);
        std::cout << "Simulation " << (i + 1) << " complete!" << std::endl;
    }
}

// Runs automatic two body simulations
void Predicta::autoTwoBodySimulation()
{
    SystemUtilities::clearTerminal();
    std::vector<std::string> choices = {
        "   1 : Use common celestial Bodies for automatic two body simulations",
        "   2 : Generate random celestial Bodies for automatic two body simulations"};
    std::string selectedOption = PythonUtilities::pythonInquirer(
        choices,
        "Please select your automatic two body simulation mode:");
    std::cout << "Please enter the number of automatic two body simulations to run: ";
    int numSims;
    std::cin >> numSims;
    for (int i = 0; i < numSims; ++i)
    {
        Body body1;
        Body body2;
        if (selectedOption == choices[0])
        {
            body1 = CelestialBody::chooseRandomCommonBody();
            body2 = CelestialBody::chooseRandomCommonBody();
        }
        else
        {
            std::array<Body, 2> bodies = CelestialBody::generateRandomTwoBody();
            body1 = bodies[0];
            body2 = bodies[1];
        }
        std::array<double, 2> numMethod = Predicta::autoTwoBodyNumMethodGenerator(body1, body2);
        Solvers solver_instance;
        TwoBodyIC initialConditions = {
            body1.position,
            body2.position,
            body1.velocity,
            body2.velocity,
            {body1.mass, body2.mass},
            {body1.radius, body2.radius},
            body1.name,
            body2.name,
            0.0,
            numMethod[0],
            numMethod[1],
        };
        TwoBodySolution solution = solver_instance.RK4TwoBody(initialConditions);
        CSVUtilities::writeTwoBodySimDataCSV(initialConditions, solution, UniversalConstants::twoBodyRK4Dir);
        std::cout << "Simulation " << (i + 1) << " complete!" << std::endl;
    }
}

// Runs automatic three body simulations
void Predicta::autoThreeBodySimulation()
{
    SystemUtilities::clearTerminal();
    std::vector<std::string> choices = {
        "   1 : Use common celestial Bodies for automatic three body simulations",
        "   2 : Generate random celestial Bodies for automatic three body simulations"};
    std::string selectedOption = PythonUtilities::pythonInquirer(
        choices,
        "Please select your automatic three body simulation mode:");
    std::cout << "Please enter the number of automatic three body simulations to run: ";
    int numSims;
    std::cin >> numSims;
    for (int i = 0; i < numSims; ++i)
    {
        Body body1;
        Body body2;
        Body body3;
        if (selectedOption == choices[0])
        {
            body1 = CelestialBody::chooseRandomCommonBody();
            body2 = CelestialBody::chooseRandomCommonBody();
            body3 = CelestialBody::chooseRandomCommonBody();
        }
        else
        {
            std::array<Body, 3> bodies = CelestialBody::generateRandomThreeBody();
            body1 = bodies[0];
            body2 = bodies[1];
            body3 = bodies[2];
        }
        std::array<double, 2> numMethod = Predicta::autoThreeBodyNumMethodGenerator(body1, body2, body3);
        Solvers solver_instance;
        ThreeBodyIC initialConditions = {
            body1.position,
            body2.position,
            body3.position,
            body1.velocity,
            body2.velocity,
            body3.velocity,
            {body1.mass, body2.mass, body3.mass},
            {body1.radius, body2.radius, body3.radius},
            body1.name,
            body2.name,
            body3.name,
            0.0,
            numMethod[0],
            numMethod[1],
        };
        ThreeBodySolution solution = solver_instance.RK4ThreeBody(initialConditions);
        CSVUtilities::writeThreeBodySimDataCSV(initialConditions, solution, UniversalConstants::threeBodyRK4Dir);
        std::cout << "Simulation " << (i + 1) << " complete!" << std::endl;
    }
}

// Runs automatic N body simulations
void Predicta::autoNBodySimulation()
{
    SystemUtilities::clearTerminal();
    std::vector<std::string> choices = {
        "   1 : Generate random celestial Bodies for automatic N body simulations"};
    std::string selectedOption = PythonUtilities::pythonInquirer(
        choices,
        "Please select your automatic N body simulation mode:");
    std::cout << "Please enter the number of automatic N body simulations to run: ";
    int numSims;
    std::cin >> numSims;
    for (int i = 0; i < numSims; ++i)
    {
        std::vector<Body> bodies = CelestialBody::generateRandomNBody();
        std::array<double, 2> numMethod = Predicta::autoNBodyNumMethodGenerator(bodies);
        size_t N = bodies.size();
        
        SystemUtilities::clearTerminal();
        std::cout << "Running automatic N body simulation " << (i + 1) << " of " << numSims << std::endl;
        std::cout << "Solving the " << N << "-body problem with the following initial conditions:" << std::endl;
        std::cout << std::endl;
        
        for (size_t j = 0; j < N; ++j) {
            std::cout << "Body " << (j + 1) << ":" << std::endl;
            CelestialBody::displayBodyInfo(bodies[j]);
        }
        
        std::cout << "Simulation time span (s): " << numMethod[0] << std::endl;
        std::cout << "Simulation time step (s): " << numMethod[1] << std::endl << std::endl;
        
        // Build NBodyIC
        NBodyIC initialConditions;
        initialConditions.initTime = 0.0;
        initialConditions.timeSpan = numMethod[0];
        initialConditions.timeStep = numMethod[1];
        
        for (size_t j = 0; j < N; ++j) {
            initialConditions.bodyNames.push_back(bodies[j].name);
            initialConditions.bodyMasses.push_back(bodies[j].mass);
            initialConditions.bodyRadii.push_back(bodies[j].radius);
            
            // Add position components
            initialConditions.initialPositions.push_back(bodies[j].position[0]);
            initialConditions.initialPositions.push_back(bodies[j].position[1]);
            initialConditions.initialPositions.push_back(bodies[j].position[2]);
            
            // Add velocity components
            initialConditions.initialVelocities.push_back(bodies[j].velocity[0]);
            initialConditions.initialVelocities.push_back(bodies[j].velocity[1]);
            initialConditions.initialVelocities.push_back(bodies[j].velocity[2]);
        }
        
        Solvers solver_instance;
        NBodySolution solution = solver_instance.RK4NBody(initialConditions);
        std::cout << "Simulation complete!" << std::endl;
        CSVUtilities::writeNBodySimDataCSV(initialConditions, solution, UniversalConstants::nBodyRK4Dir);
    }
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// Manual Simulation Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Runs manual single body simulation
void Predicta::manualSingleBodySimulation()
{
    Body commonBody = Predicta::manualBodyGenerator();
    std::array<double, 2> projIC = Predicta::manualSingleBodyProjectileICGenerator();
    std::array<double, 2> numMethod = Predicta::manualSingleBodyNumMethodGenerator();
    SystemUtilities::clearTerminal();
    std::cout << "Solving the single body problem with the following initial conditions:" << std::endl;
    std::cout << std::endl;
    CelestialBody::displayBodyInfo(commonBody);
    std::cout << "Projectile inital vertical position (m): " << projIC[0] << std::endl;
    std::cout << "Projectile initial vertical velocity (m/s): " << projIC[1] << std::endl;
    std::cout << "Simulation time span (s): " << numMethod[0] << std::endl;
    std::cout << "Simulation time step (s): " << numMethod[1] << std::endl << std::endl;
    Solvers solver_instance;
    SingleBodyIC initialConditions = {
        projIC[0],
        projIC[1],
        commonBody.name,
        commonBody.mass,
        commonBody.radius,
        0.0,
        numMethod[0],
        numMethod[1],
    };
    SingleBodySolution solution = solver_instance.RK4SingleBody(initialConditions);
    std::cout << "Simulation complete!" << std::endl;
    CSVUtilities::writeSingleBodySimDataCSV(initialConditions, solution, UniversalConstants::singleBodyRK4Dir);
}

// Runs manual two body simulation
void Predicta::manualTwoBodySimulation()
{
    Body body1 = Predicta::manualBodyGenerator();
    Body body2 = Predicta::manualBodyGenerator();
    std::array<double, 2> numMethod = Predicta::manualTwoBodyNumMethodGenerator();
    SystemUtilities::clearTerminal();
    std::cout << "Solving the two body problem with the following initial conditions:" << std::endl;
    std::cout << std::endl;
    std::cout << "Body 1:" << std::endl << std::endl;
    CelestialBody::displayBodyInfo(body1);
    std::cout << "Body 2:" << std::endl << std::endl;
    CelestialBody::displayBodyInfo(body2);
    std::cout << "Simulation time span (s): " << numMethod[0] << std::endl;
    std::cout << "Simulation time step (s): " << numMethod[1] << std::endl << std::endl;
    Solvers solver_instance;
    TwoBodyIC initialConditions = {
        body1.position,
        body2.position,
        body1.velocity,
        body2.velocity,
        {body1.mass, body2.mass},
        {body1.radius, body2.radius},
        body1.name,
        body2.name,
        0.0,
        numMethod[0],
        numMethod[1],
    };
    TwoBodySolution solution = solver_instance.RK4TwoBody(initialConditions);
    std::cout << "Simulation complete!" << std::endl;
    CSVUtilities::writeTwoBodySimDataCSV(initialConditions, solution, UniversalConstants::twoBodyRK4Dir);
}

// Runs the manual three body simulation
void Predicta::manualThreeBodySimulation()
{
    Body body1 = Predicta::manualBodyGenerator();
    Body body2 = Predicta::manualBodyGenerator();
    Body body3 = Predicta::manualBodyGenerator();
    std::array<double, 2> numMethod = Predicta::manualThreeBodyNumMethodGenerator();
    SystemUtilities::clearTerminal();
    std::cout << "Solving the three body problem with the following initial conditions:" << std::endl;
    std::cout << std::endl;
    std::cout << "Body 1:" << std::endl << std::endl;
    CelestialBody::displayBodyInfo(body1);
    std::cout << "Body 2:" << std::endl << std::endl;
    CelestialBody::displayBodyInfo(body2);
    std::cout << "Body 3:" << std::endl << std::endl;
    CelestialBody::displayBodyInfo(body3);
    std::cout << "Simulation time span (s): " << numMethod[0] << std::endl;
    std::cout << "Simulation time step (s): " << numMethod[1] << std::endl << std::endl;
    Solvers solver_instance;
    ThreeBodyIC initialConditions = {
        body1.position,
        body2.position,
        body3.position,
        body1.velocity,
        body2.velocity,
        body3.velocity,
        {body1.mass, body2.mass, body3.mass},
        {body1.radius, body2.radius, body3.radius},
        body1.name,
        body2.name,
        body3.name,
        0.0,
        numMethod[0],
        numMethod[1],
    };
    ThreeBodySolution solution = solver_instance.RK4ThreeBody(initialConditions);
    std::cout << "Simulation complete!" << std::endl;
    CSVUtilities::writeThreeBodySimDataCSV(initialConditions, solution, UniversalConstants::threeBodyRK4Dir);
}

// Runs manual N-body simulation
void Predicta::manualNBodySimulation()
{
    std::vector<Body> bodies = Predicta::manualNBodiesGenerator();
    std::array<double, 2> numMethod = Predicta::manualNBodyNumMethodGenerator();
    size_t N = bodies.size();

    SystemUtilities::clearTerminal();
    std::cout << "Solving the " << N << "-body problem with the following initial conditions:" << std::endl;
    std::cout << std::endl;

    for (size_t i = 0; i < N; ++i) {
        std::cout << "Body " << i << ":" << std::endl << std::endl;
        CelestialBody::displayBodyInfo(bodies[i]);
    }

    std::cout << "Simulation time span (s): " << numMethod[0] << std::endl;
    std::cout << "Simulation time step (s): " << numMethod[1] << std::endl << std::endl;

    // Build NBodyIC
    // N-body state uses 3D positions and velocities:
    //   initialPositions: size 3N with layout [x0,y0,z0, x1,y1,z1, ...]
    //   initialVelocities: size 3N with layout [vx0,vy0,vz0, vx1,vy1,vz1, ...]
    NBodyIC initialConditions;
    initialConditions.initTime = 0.0;
    initialConditions.timeSpan = numMethod[0];
    initialConditions.timeStep = numMethod[1];

    for (size_t i = 0; i < N; ++i) {
        initialConditions.bodyNames.push_back(bodies[i].name);
        initialConditions.bodyMasses.push_back(bodies[i].mass);
        initialConditions.bodyRadii.push_back(bodies[i].radius);

        // Add 3D position components
        initialConditions.initialPositions.push_back(bodies[i].position[0]);
        initialConditions.initialPositions.push_back(bodies[i].position[1]);
        initialConditions.initialPositions.push_back(bodies[i].position[2]);

        // Add 3D velocity components
        initialConditions.initialVelocities.push_back(bodies[i].velocity[0]);
        initialConditions.initialVelocities.push_back(bodies[i].velocity[1]);
        initialConditions.initialVelocities.push_back(bodies[i].velocity[2]);
    }

    Solvers solver_instance;
    NBodySolution solution = solver_instance.RK4NBody(initialConditions);
    std::cout << "Simulation complete!" << std::endl;
    CSVUtilities::writeNBodySimDataCSV(initialConditions, solution, UniversalConstants::nBodyRK4Dir);
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// Model Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Runs manual single body model evaluation
void Predicta::modelSingleBodyEvaluate()
{
    std::string body = Predicta::modelSingleBodyEvaluateSelection();
    if (body.empty()) {
        std::cout << "No model selected. Returning to menu." << std::endl;
        return;
    }
    
    SystemUtilities::clearTerminal();
    std::cout << "Evaluating model for " << body << std::endl;
    std::cout << std::endl;
    
    // Get the body struct
    Body commonBody = getBodyFromName(body);
    
    // Prompt for simulation parameters
    std::cout << "Enter simulation parameters:" << std::endl;
    std::array<double, 2> projIC = Predicta::manualSingleBodyProjectileICGenerator();
    std::array<double, 2> numMethod = Predicta::manualSingleBodyNumMethodGenerator();
    
    SingleBodyIC initialConditions = {
        projIC[0],       // initialPosition
        projIC[1],       // initialVelocity
        commonBody.name,
        commonBody.mass,
        commonBody.radius,
        0.0,             // initialTime
        numMethod[0],    // timeSpan
        numMethod[1],    // timeStep
    };
    
    // Run prediction and RK4 for comparison
    MachineLearning ml_instance;
    Solvers solver_instance;
    
    SingleBodySolution mlSolution = ml_instance.predictSingleBodyModel(initialConditions);
    SingleBodySolution rk4Solution = solver_instance.RK4SingleBody(initialConditions);
    
    // Use body-specific evaluation directory
    std::string evalDir = UniversalConstants::getSingleBodyEvalDir(body);
    CSVUtilities::writeSingleBodyEvaluationDataCSV(initialConditions, rk4Solution, mlSolution, evalDir);
    
    std::cout << "\nEvaluation complete! Results saved to: " << evalDir << std::endl;
}

// Runs manual single body model prediction
void Predicta::modelSingleBodyPredict()
{
    std::string body = Predicta::modelSingleBodyPredictSelection();
    if (body.empty()) {
        std::cout << "No model selected. Returning to menu." << std::endl;
        return;
    }
    
    SystemUtilities::clearTerminal();
    std::cout << "Predicting with model for " << body << std::endl;
    std::cout << std::endl;
    
    // Get the body struct
    Body commonBody = getBodyFromName(body);
    
    // Prompt for simulation parameters
    std::cout << "Enter simulation parameters:" << std::endl;
    std::array<double, 2> projIC = Predicta::manualSingleBodyProjectileICGenerator();
    std::array<double, 2> numMethod = Predicta::manualSingleBodyNumMethodGenerator();
    
    SingleBodyIC initialConditions = {
        projIC[0],       // initialPosition
        projIC[1],       // initialVelocity
        commonBody.name,
        commonBody.mass,
        commonBody.radius,
        0.0,             // initialTime
        numMethod[0],    // timeSpan
        numMethod[1],    // timeStep
    };
    
    // Run prediction
    MachineLearning ml_instance;
    SingleBodySolution solution = ml_instance.predictSingleBodyModel(initialConditions);
    
    // Use body-specific predictions directory
    std::string predictDir = UniversalConstants::getSingleBodyPredictionsDir(body);
    CSVUtilities::writeSingleBodyModelDataCSV(initialConditions, solution, predictDir);
    
    std::cout << "\nPrediction complete! Results saved to: " << predictDir << std::endl;
}

// Runs manual single body model training
void Predicta::modelSingleBodyTrain()
{
    std::string body = Predicta::modelSingleBodyTrainSelection();
    if (body.empty()) {
        std::cout << "No body selected. Aborting training." << std::endl;
        return;
    }
    
    SystemUtilities::clearTerminal();
    std::cout << "\nStarting model training for " << body << "...\n"
            << std::endl;
    MachineLearning ml_instance;
    ml_instance.trainSingleBodyModel(true, body);
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// Plotting Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Plots results from previous single body simulations
void Predicta::plotSingleBodyResult(std::string directory, bool isEvaluation)
{
    SystemUtilities::clearTerminal();

    // List available CSV files
    std::vector<std::string> csvFiles = CSVUtilities::listCSVFiles(directory);

    if (csvFiles.empty())
    {
        std::cout << "No simulation results found in: " << directory << std::endl;
        return;
    }

    std::string selectedFile = PythonUtilities::pythonInquirer(
        csvFiles,
        "Select a file to plot:");

    // Build full filepath
    std::string filepath = selectedFile;

    // Read the CSV
    SingleBodyIC initialConditions;
    SingleBodySolution rk4Solution;
    SingleBodySolution modelSolution;

    if (isEvaluation)
    {
        if (!CSVUtilities::readSingleBodyEvaluationDataCSV(filepath, initialConditions, rk4Solution, modelSolution))
        {
            std::cout << "Failed to read CSV file." << std::endl;
            return;
        }

        // Prepare position plot parameters for RK4 solution
        SingleBodyPlotParameters rk4ParamsPosition;
        rk4ParamsPosition.xlabel = "Time (s)";
        rk4ParamsPosition.ylabel = "Projectile Position (m)";
        rk4ParamsPosition.title = "Single Body Projectile Motion - RK4 vs ML Model";
        rk4ParamsPosition.method = "RK4";
        rk4ParamsPosition.xData = rk4Solution.times;
        rk4ParamsPosition.yData = rk4Solution.positions;

        // Prepare position plot parameters for Model solution
        SingleBodyPlotParameters modelParamsPosition;
        modelParamsPosition.xlabel = "Time (s)";
        modelParamsPosition.ylabel = "Projectile Position (m)";
        modelParamsPosition.title = "Single Body Projectile Motion - RK4 vs ML Model";
        modelParamsPosition.method = "ML Model";
        modelParamsPosition.xData = modelSolution.times;
        modelParamsPosition.yData = modelSolution.positions;

        // Prepare velocity plot parameters for RK4 solution
        SingleBodyPlotParameters rk4ParamsVelocity;
        rk4ParamsVelocity.xlabel = "Time (s)";
        rk4ParamsVelocity.ylabel = "Projectile Velocity (m/s)";
        rk4ParamsVelocity.title = "Single Body Projectile Velocity - RK4 vs ML Model";
        rk4ParamsVelocity.method = "RK4";
        rk4ParamsVelocity.xData = rk4Solution.times;
        rk4ParamsVelocity.yData = rk4Solution.velocities;

        // Prepare velocity plot parameters for Model solution
        SingleBodyPlotParameters modelParamsVelocity;
        modelParamsVelocity.xlabel = "Time (s)";
        modelParamsVelocity.ylabel = "Projectile Velocity (m/s)";
        modelParamsVelocity.title = "Single Body Projectile Velocity - RK4 vs ML Model";
        modelParamsVelocity.method = "ML Model";
        modelParamsVelocity.xData = modelSolution.times;
        modelParamsVelocity.yData = modelSolution.velocities;

        // Position plots - both on same graph
        Plotters::singleBodyEvaluationPlot(initialConditions, rk4ParamsPosition, modelParamsPosition);

        // Velocity plots - both on same graph
        Plotters::singleBodyEvaluationPlot(initialConditions, rk4ParamsVelocity, modelParamsVelocity);
    }
    else
    {
        // Determine if it's RK4 or Model data from directory
        bool isModelData = (directory.find("Model") != std::string::npos);
        std::string method = isModelData ? "ML Model" : "RK4";

        // Select solution based on data type
        SingleBodySolution solution;

        // Position plot parameters
        SingleBodyPlotParameters posParams;
        posParams.xlabel = "Time (s)";
        posParams.ylabel = "Projectile Position (m)";
        posParams.title = "Single Body Projectile Motion";

        // Velocity plot parameters
        SingleBodyPlotParameters velParams;
        velParams.xlabel = "Time (s)";
        velParams.ylabel = "Projectile Velocity (m/s)";
        velParams.title = "Single Body Projectile Velocity";

        if (isModelData)
        {
            if (!CSVUtilities::readSingleBodySimDataCSV(filepath, initialConditions, modelSolution))
            {
                std::cout << "Failed to read CSV file." << std::endl;
                return;
            }
            solution = modelSolution;
            posParams.method = "ML Model";
            posParams.xData = solution.times;
            posParams.yData = solution.positions;
            velParams.method = "ML Model";
            velParams.xData = solution.times;
            velParams.yData = solution.velocities;
        }
        else
        {
            if (!CSVUtilities::readSingleBodySimDataCSV(filepath, initialConditions, rk4Solution))
            {
                std::cout << "Failed to read CSV file." << std::endl;
                return;
            }
            solution = rk4Solution;
            posParams.method = "RK4";
            posParams.xData = solution.times;
            posParams.yData = solution.positions;
            velParams.method = "RK4";
            velParams.xData = solution.times;
            velParams.yData = solution.velocities;
        }

        // Position plot
        Plotters::singleBodyPlot(initialConditions, posParams);

        // Velocity plot
        Plotters::singleBodyPlot(initialConditions, velParams);
    }
}

// Plots results from previous two body simulations
void Predicta::plotTwoBodyResult(std::string directory, bool isEvaluation)
{
    SystemUtilities::clearTerminal();

    // List available CSV files
    std::vector<std::string> csvFiles = CSVUtilities::listCSVFiles(directory);

    if (csvFiles.empty())
    {
        std::cout << "No simulation results found in: " << directory << std::endl;
        return;
    }

    std::string selectedFile = PythonUtilities::pythonInquirer(
        csvFiles,
        "Select a file to plot:");

    // Build full filepath
    std::string filepath = selectedFile;

    // Read the CSV
    TwoBodyIC initialConditions;
    TwoBodySolution rk4Solution;

    if (isEvaluation)
    {
        // TODO: Implement two body evaluation plotting when evaluation CSV reader is available
        std::cout << "Two body evaluation plotting not yet implemented." << std::endl;
        return;
    }
    else
    {
        // Determine if it's RK4 or Model data from directory
        bool isModelData = (directory.find("Model") != std::string::npos);
        std::string method = isModelData ? "ML Model" : "RK4";

        if (!CSVUtilities::readTwoBodySimDataCSV(filepath, initialConditions, rk4Solution))
        {
            std::cout << "Failed to read CSV file." << std::endl;
            return;
        }

        // Prepare position parameters for plotting
        TwoBodyPlotParameters posPlotParams;
        posPlotParams.xlabel = "X Position (m)";
        posPlotParams.ylabel = "Y Position (m)";
        posPlotParams.title = "Two Body Position";
        posPlotParams.method = "RK4";
        posPlotParams.xData = rk4Solution.times;
        posPlotParams.body1Data = rk4Solution.body1Positions;
        posPlotParams.body2Data = rk4Solution.body2Positions;
        posPlotParams.isPos = true;

        // Prepare velocity parameters for plotting
        TwoBodyPlotParameters velPlotParams;
        velPlotParams.xlabel = "Time (s)";
        velPlotParams.ylabel = "Velocity (m/s)";
        velPlotParams.title = "Two Body Velocity";
        velPlotParams.method = "RK4";
        velPlotParams.xData = rk4Solution.times;
        velPlotParams.body1Data = rk4Solution.body1Velocities;
        velPlotParams.body2Data = rk4Solution.body2Velocities;
        velPlotParams.isPos = false;

        // Position plot
        Plotters::twoBodyPlot(initialConditions, posPlotParams);

        // Velocity plot
        Plotters::twoBodyPlot(initialConditions, velPlotParams);
    }
}

// Plots results from previous three body simulations
void Predicta::plotThreeBodyResult(std::string directory, bool isEvaluation)
{
    SystemUtilities::clearTerminal();

    // List available CSV files
    std::vector<std::string> csvFiles = CSVUtilities::listCSVFiles(directory);

    if (csvFiles.empty())
    {
        std::cout << "No simulation results found in: " << directory << std::endl;
        return;
    }

    std::string selectedFile = PythonUtilities::pythonInquirer(
        csvFiles,
        "Select a file to plot:");

    // Build full filepath
    std::string filepath = selectedFile;

    // Read the CSV
    ThreeBodyIC initialConditions;
    ThreeBodySolution rk4Solution;

    if (isEvaluation)
    {
        // TODO: Implement three body evaluation plotting when evaluation CSV reader is available
        std::cout << "Three body evaluation plotting not yet implemented." << std::endl;
    }
    else
    {
        // Determine if it's RK4 or Model data from directory
        bool isModelData = (directory.find("Model") != std::string::npos);
        std::string method = isModelData ? "ML Model" : "RK4";

        if (!CSVUtilities::readThreeBodySimDataCSV(filepath, initialConditions, rk4Solution))
        {
            std::cout << "Failed to read CSV file." << std::endl;
            return;
        }

        // Prepare position plot parameters for plotting
        ThreeBodyPlotParameters posPlotParams;
        posPlotParams.xlabel = "X Position (m)";
        posPlotParams.ylabel = "Y Position (m)";
        posPlotParams.title = "Three Body Position";
        posPlotParams.method = "RK4";
        posPlotParams.xData = rk4Solution.times;
        posPlotParams.body1Data = rk4Solution.body1Positions;
        posPlotParams.body2Data = rk4Solution.body2Positions;
        posPlotParams.body3Data = rk4Solution.body3Positions;
        posPlotParams.isPos = true;

        // Prepare velocity plot parameters for plotting
        ThreeBodyPlotParameters velPlotParams;
        velPlotParams.xlabel = "Time (s)";
        velPlotParams.ylabel = "Velocity (m/s)";
        velPlotParams.title = "Three Body Velocity";
        velPlotParams.method = "RK4";
        velPlotParams.xData = rk4Solution.times;
        velPlotParams.body1Data = rk4Solution.body1Velocities;
        velPlotParams.body2Data = rk4Solution.body2Velocities;
        velPlotParams.body3Data = rk4Solution.body3Velocities;
        velPlotParams.isPos = false;

        // Position plot
        Plotters::threeBodyPlot(initialConditions, posPlotParams);

        // Velocity plot
        Plotters::threeBodyPlot(initialConditions, velPlotParams);
    }
}

// Plots results from previous N-body simulations
void Predicta::plotNBodyResult(std::string directory, bool isEvaluation)
{
    SystemUtilities::clearTerminal();

    // List available CSV files
    std::vector<std::string> csvFiles = CSVUtilities::listCSVFiles(directory);

    if (csvFiles.empty())
    {
        std::cout << "No simulation results found in: " << directory << std::endl;
        return;
    }

    std::string selectedFile = PythonUtilities::pythonInquirer(
        csvFiles,
        "Select a file to plot:");

    // Build full filepath
    std::string filepath = selectedFile;

    // Read the CSV
    NBodyIC initialConditions;
    NBodySolution rk4Solution;

    if (isEvaluation)
    {
        // TODO: Implement N-body evaluation plotting when evaluation CSV reader is available
        std::cout << "N-body evaluation plotting not yet implemented." << std::endl;
        return;
    }
    else
    {
        // Determine if it's RK4 or Model data from directory
        bool isModelData = (directory.find("Model") != std::string::npos);
        std::string method = isModelData ? "ML Model" : "RK4";

        if (!CSVUtilities::readNBodySimDataCSV(filepath, initialConditions, rk4Solution))
        {
            std::cout << "Failed to read CSV file." << std::endl;
            return;
        }

        size_t N = rk4Solution.numBodies;
        size_t numSteps = rk4Solution.times.size();

        // Convert flat position/velocity arrays to per-body array<double,3> format
        // rk4Solution.positions[t] is a 3N vector: [x0,y0,z0, x1,y1,z1, ...]
        std::vector<std::vector<std::array<double, 3>>> bodyPositions(N);
        std::vector<std::vector<std::array<double, 3>>> bodyVelocities(N);

        for (size_t i = 0; i < N; ++i) {
            bodyPositions[i].resize(numSteps);
            bodyVelocities[i].resize(numSteps);
        }

        for (size_t t = 0; t < numSteps; ++t) {
            for (size_t i = 0; i < N; ++i) {
                bodyPositions[i][t] = {
                    rk4Solution.positions[t][3 * i + 0],
                    rk4Solution.positions[t][3 * i + 1],
                    rk4Solution.positions[t][3 * i + 2]
                };
                bodyVelocities[i][t] = {
                    rk4Solution.velocities[t][3 * i + 0],
                    rk4Solution.velocities[t][3 * i + 1],
                    rk4Solution.velocities[t][3 * i + 2]
                };
            }
        }

        // Prepare position plot parameters
        NBodyPlotParameters posPlotParams;
        posPlotParams.xlabel = "X Position (m)";
        posPlotParams.ylabel = "Y Position (m)";
        posPlotParams.title = std::to_string(N) + "-Body Position";
        posPlotParams.method = method;
        posPlotParams.xData = rk4Solution.times;
        posPlotParams.bodyData = bodyPositions;
        posPlotParams.isPos = true;
        posPlotParams.bodyLabels = initialConditions.bodyNames;

        // Position plot
        Plotters::nBodyPlot(initialConditions, posPlotParams);
    }
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// Selection Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Lets user select automatic simulation type
void Predicta::automaticSimulationSelection()
{
    SystemUtilities::clearTerminal();
    std::vector<std::string> choices = {
        "   1 : Single Body Simulation",
        "   2 : Two Body Simulation",
        "   3 : Three Body Simulation",
        "   4 : N Body Simulation",
        "   5 : Return to Main Menu"
    };
    std::string selection = PythonUtilities::pythonInquirer(
        choices,
        "Please select the automatic simulation type (using arrow keys) to run:");
    switch (selection[3] - '0')
    {
        case 1:
            Predicta::autoSingleBodySimulation();
            break;
        case 2:
            Predicta::autoTwoBodySimulation();
            break;
        case 3:
            Predicta::autoThreeBodySimulation();
            break;
        case 4:
            Predicta::autoNBodySimulation();
            break;
        case 5:
            Predicta::returnToModeSelection();
            break;
        default:
            break;
    }
}

// Lets user select manual simulation type
void Predicta::manualSimulationSelection()
{
    SystemUtilities::clearTerminal();
    std::vector<std::string> choices = {
        "   1 : Single Body Simulation",
        "   2 : Two Body Simulation",
        "   3 : Three Body Simulation",
        "   4 : N Body Simulation",
        "   5 : Return to Main Menu"
    };
    std::string selection = PythonUtilities::pythonInquirer(
        choices,
        "Please select the manual simulation type (using arrow keys) to run:");
    switch (selection[3] - '0')
    {
        case 1:
            Predicta::manualSingleBodySimulation();
            break;
        case 2:
            Predicta::manualTwoBodySimulation();
            break;
        case 3:
            Predicta::manualThreeBodySimulation();
            break;
        case 4:
            Predicta::manualNBodySimulation();
            break;
        case 5:
            Predicta::returnToModeSelection();
            break;
        default:
            break;
    }
}

// Lets user select model evaluation type
void Predicta::modelEvaluationSelection()
{
    SystemUtilities::clearTerminal();
    std::vector<std::string> choices = {
        "   1 : Single Body Model Evaluation",
        "   2 : Two Body Model Evaluation",
        "   3 : Three Body Model Evaluation",
        "   4 : Return to Main Menu"
    };
    std::string selection = PythonUtilities::pythonInquirer(
        choices,
        "Please select the model evaluation type (using arrow keys) to run:");
    switch (selection[3] - '0')
    {
        case 1:
            Predicta::modelSingleBodyEvaluate();
            break;
        case 2:
            std::cout << "Two Body model evaluation not yet implemented." << std::endl;
            Predicta::returnToModeSelection();
            break;
        case 3:
            std::cout << "Three Body model evaluation not yet implemented." << std::endl;
            Predicta::returnToModeSelection();
            break;
        case 4:
            Predicta::returnToModeSelection();
            break;
        default:
            break;
    }
}

// Lets user select model prediction type
void Predicta::modelPredictionSelection()
{
    SystemUtilities::clearTerminal();
    std::vector<std::string> choices = {
        "   1 : Single Body Model Prediction",
        "   2 : Two Body Model Prediction",
        "   3 : Three Body Model Prediction",
        "   4 : Return to Main Menu"
    };
    std::string selection = PythonUtilities::pythonInquirer(
        choices,
        "Please select the model prediction type (using arrow keys) to run:");
    switch (selection[3] - '0')
    {
        case 1:
            Predicta::modelSingleBodyPredict();
            break;
        case 2:
            std::cout << "Two Body model prediction not yet implemented." << std::endl;
            Predicta::returnToModeSelection();
            break;
        case 3:
            std::cout << "Three Body model prediction not yet implemented." << std::endl;
            Predicta::returnToModeSelection();
            break;
        case 4:
            Predicta::returnToModeSelection();
            break;
        default:
            break;
    }
}

// Helper function to get available trained models for single body
std::vector<std::pair<std::string, std::string>> Predicta::getAvailableSingleBodyModels() {
    std::vector<std::pair<std::string, std::string>> availableModels; // {bodyName, displayName}
    
    // Check each common body for a trained model
    const std::vector<std::string> bodyNames = {
        "Sun", "Mercury", "Venus", "Earth", "Mars",
        "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"
    };
    
    std::filesystem::path execDir = SystemUtilities::getExecutableDir();
    
    for (const auto& bodyName : bodyNames) {
        // Check if model file exists
        std::string modelPath = UniversalConstants::getSingleBodyModelFilePath(bodyName);
        std::string scalerPath = UniversalConstants::getSingleBodyScalersFilePath(bodyName);
        
        std::filesystem::path fullModelPath = execDir / modelPath;
        std::filesystem::path fullScalerPath = execDir / scalerPath;
        
        if (std::filesystem::exists(fullModelPath) && std::filesystem::exists(fullScalerPath)) {
            availableModels.push_back({bodyName, bodyName + " (trained)"});
        }
    }
    
    return availableModels;
}

// Helper to get Body struct from name
Body Predicta::getBodyFromName(const std::string& bodyName) {
    if (bodyName == "Sun") return CelestialBody::sun;
    if (bodyName == "Mercury") return CelestialBody::mercury;
    if (bodyName == "Venus") return CelestialBody::venus;
    if (bodyName == "Earth") return CelestialBody::earth;
    if (bodyName == "Mars") return CelestialBody::mars;
    if (bodyName == "Jupiter") return CelestialBody::jupiter;
    if (bodyName == "Saturn") return CelestialBody::saturn;
    if (bodyName == "Uranus") return CelestialBody::uranus;
    if (bodyName == "Neptune") return CelestialBody::neptune;
    if (bodyName == "Pluto") return CelestialBody::pluto;
    return CelestialBody::earth; // Default fallback
}

std::string Predicta::modelSingleBodyEvaluateSelection() 
{
    SystemUtilities::clearTerminal();
    
    // Get available trained models
    auto availableModels = getAvailableSingleBodyModels();
    
    if (availableModels.empty()) {
        std::cout << "No trained models found. Please train a model first." << std::endl;
        std::cout << "\nPress Enter to continue..." << std::endl;
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cin.get();
        return "";
    }
    
    // Build choices list
    std::vector<std::string> choices;
    int idx = 1;
    for (const auto& [bodyName, displayName] : availableModels) {
        std::string prefix = (idx < 10) ? "   " : "  ";
        choices.push_back(prefix + std::to_string(idx) + " : " + displayName);
        ++idx;
    }
    choices.push_back("  " + std::to_string(idx) + " : Cancel");
    
    std::string selection = PythonUtilities::pythonInquirer(
        choices,
        "Select a trained model to evaluate (using arrow keys):");
    
    // Parse selection number
    int selectedIdx = 0;
    if (selection.length() >= 4) {
        // Handle both single and double digit numbers
        std::string numStr;
        for (size_t i = 0; i < selection.length(); ++i) {
            if (std::isdigit(selection[i])) {
                numStr += selection[i];
            } else if (!numStr.empty()) {
                break; // Stop after first number
            }
        }
        if (!numStr.empty()) {
            selectedIdx = std::stoi(numStr);
        }
    }
    
    // Check if cancel was selected
    if (selectedIdx == 0 || selectedIdx > static_cast<int>(availableModels.size())) {
        return "";
    }
    
    return availableModels[selectedIdx - 1].first;
}

// Lets user select single body model prediction option
std::string Predicta::modelSingleBodyPredictSelection() 
{
    SystemUtilities::clearTerminal();
    
    // Get available trained models
    auto availableModels = getAvailableSingleBodyModels();
    
    if (availableModels.empty()) {
        std::cout << "No trained models found. Please train a model first." << std::endl;
        std::cout << "\nPress Enter to continue..." << std::endl;
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cin.get();
        return "";
    }
    
    // Build choices list
    std::vector<std::string> choices;
    int idx = 1;
    for (const auto& [bodyName, displayName] : availableModels) {
        std::string prefix = (idx < 10) ? "   " : "  ";
        choices.push_back(prefix + std::to_string(idx) + " : " + displayName);
        ++idx;
    }
    choices.push_back("  " + std::to_string(idx) + " : Cancel");
    
    std::string selection = PythonUtilities::pythonInquirer(
        choices,
        "Select a trained model to predict with (using arrow keys):");
    
    // Parse selection number
    int selectedIdx = 0;
    if (selection.length() >= 4) {
        std::string numStr;
        for (size_t i = 0; i < selection.length(); ++i) {
            if (std::isdigit(selection[i])) {
                numStr += selection[i];
            } else if (!numStr.empty()) {
                break;
            }
        }
        if (!numStr.empty()) {
            selectedIdx = std::stoi(numStr);
        }
    }
    
    // Check if cancel was selected
    if (selectedIdx == 0 || selectedIdx > static_cast<int>(availableModels.size())) {
        return "";
    }
    
    return availableModels[selectedIdx - 1].first;
}

// Lets user select single body model prediction option
std::string Predicta::modelSingleBodyTrainSelection() 
{
    SystemUtilities::clearTerminal();
    std::vector<std::string> choices = {
        "   1 : Sun",
        "   2 : Mercury",
        "   3 : Venus",
        "   4 : Earth",
        "   5 : Mars",
        "   6 : Jupiter",
        "   7 : Saturn",
        "   8 : Uranus",
        "   9 : Neptune",
        "  10 : Pluto"
    };
    std::string selection = PythonUtilities::pythonInquirer(
        choices,
        "Please select from the following models to train with (using arrow keys):");
    switch (selection[3] - '0')
    {
        case 1:
            return CelestialBody::sun.name;
        case 2:
            return CelestialBody::mercury.name;
        case 3:
            return CelestialBody::venus.name;
        case 4:
            return CelestialBody::earth.name;
        case 5:
            return CelestialBody::mars.name;
        case 6:
            return CelestialBody::jupiter.name;
        case 7:
            return CelestialBody::saturn.name;
        case 8:
            return CelestialBody::uranus.name;
        case 9:
            return CelestialBody::neptune.name;
        case 10:
            return CelestialBody::pluto.name;
        default:
            break;
    }
    return "";
}

// Lets user select model training type
void Predicta::modelTrainSelection()
{
    SystemUtilities::clearTerminal();
    std::vector<std::string> choices = {
        "   1 : Single Body Model Training",
        "   2 : Two Body Model Training",
        "   3 : Three Body Model Training",
        "   4 : Return to Main Menu"
    };
    std::string selection = PythonUtilities::pythonInquirer(
        choices,
        "Please select the model training type (using arrow keys) to run:");
    switch (selection[3] - '0')
    {
        case 1:
            Predicta::modelSingleBodyTrain();
            break;
        case 2:
            std::cout << "Two Body model training not yet implemented." << std::endl;
            Predicta::returnToModeSelection();
            break;
        case 3:
            std::cout << "Three Body model training not yet implemented." << std::endl;
            Predicta::returnToModeSelection();
            break;
        case 4:
            Predicta::returnToModeSelection();
            break;
        default:
            break;
    }
}

// Helper function to get available directories with data for a given type
// Returns pairs of {bodyName, directory} for directories that contain CSV files
std::vector<std::pair<std::string, std::string>> Predicta::getAvailableDataDirectories(const std::string& dataType) {
    std::vector<std::pair<std::string, std::string>> availableDirs;
    
    const std::vector<std::string> bodyNames = {
        "Sun", "Mercury", "Venus", "Earth", "Mars",
        "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"
    };
    
    for (const auto& bodyName : bodyNames) {
        std::string dir;
        if (dataType == "predictions") {
            dir = UniversalConstants::getSingleBodyPredictionsDir(bodyName);
        } else if (dataType == "evaluations") {
            dir = UniversalConstants::getSingleBodyEvalDir(bodyName);
        } else {
            continue;
        }
        
        // Check if directory has CSV files
        std::vector<std::string> csvFiles = CSVUtilities::listCSVFiles(dir);
        if (!csvFiles.empty()) {
            availableDirs.push_back({bodyName, dir});
        }
    }
    
    return availableDirs;
}

// Helper function for selecting a body with available data for plotting
std::pair<std::string, std::string> Predicta::plotBodyWithDataSelection(const std::string& dataType, const std::string& prompt) {
    SystemUtilities::clearTerminal();
    
    auto availableDirs = getAvailableDataDirectories(dataType);
    
    if (availableDirs.empty()) {
        std::cout << "No " << dataType << " data found. Please generate some data first." << std::endl;
        std::cout << "\nPress Enter to continue..." << std::endl;
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cin.get();
        return {"", ""};
    }
    
    // Build choices list
    std::vector<std::string> choices;
    int idx = 1;
    for (const auto& [bodyName, dir] : availableDirs) {
        std::vector<std::string> csvFiles = CSVUtilities::listCSVFiles(dir);
        std::string prefix = (idx < 10) ? "   " : "  ";
        choices.push_back(prefix + std::to_string(idx) + " : " + bodyName + " (" + std::to_string(csvFiles.size()) + " files)");
        ++idx;
    }
    choices.push_back("  " + std::to_string(idx) + " : Return to Plot Menu");
    
    std::string selection = PythonUtilities::pythonInquirer(choices, prompt);
    
    // Parse selection number
    int selectedIdx = 0;
    if (selection.length() >= 4) {
        std::string numStr;
        for (size_t i = 0; i < selection.length(); ++i) {
            if (std::isdigit(selection[i])) {
                numStr += selection[i];
            } else if (!numStr.empty()) {
                break;
            }
        }
        if (!numStr.empty()) {
            selectedIdx = std::stoi(numStr);
        }
    }
    
    // Check if cancel was selected
    if (selectedIdx == 0 || selectedIdx > static_cast<int>(availableDirs.size())) {
        return {"", ""};
    }
    
    return availableDirs[selectedIdx - 1];
}

// Plots selection menu
void Predicta::plotSelection()
{
    SystemUtilities::clearTerminal();
    std::vector<std::string> choices = {
        "   1 : Single Body Simulation Results",
        "   2 : Single Body Model Results",
        "   3 : Single Body Evaluation Results",
        "   4 : Two Body Simulation Results",
        "   5 : Three Body Simulation Results",
        "   6 : N-Body Simulation Results",
        "   7 : Return to Main Menu"
    };
    std::string selection = PythonUtilities::pythonInquirer(
        choices,
        "Please select the plot type (using arrow keys) to generate:");
    switch (selection[3] - '0')
    {
        case 1:
            Predicta::plotSingleBodyResult(UniversalConstants::singleBodyRK4Dir, false);
            break;
        case 2:
        {
            // Select body with available prediction data
            auto [body, predictDir] = plotBodyWithDataSelection("predictions", "Select a body with prediction data to plot:");
            if (!body.empty()) {
                Predicta::plotSingleBodyResult(predictDir, false);
            } else {
                Predicta::plotSelection();
            }
            break;
        }
        case 3:
        {
            // Select body with available evaluation data
            auto [body, evalDir] = plotBodyWithDataSelection("evaluations", "Select a body with evaluation data to plot:");
            if (!body.empty()) {
                Predicta::plotSingleBodyResult(evalDir, true);
            } else {
                Predicta::plotSelection();
            }
            break;
        }
        case 4:
            Predicta::plotTwoBodyResult(UniversalConstants::twoBodyRK4Dir, false);
            break;
        case 5:
            Predicta::plotThreeBodyResult(UniversalConstants::threeBodyRK4Dir, false);
            break;
        case 6:
            Predicta::plotNBodyResult(UniversalConstants::nBodyRK4Dir, false);
            break;
        case 7:
            Predicta::returnToModeSelection();
            break;
        default:
            break;
    }
}

// Prompts user to select mode of operation
void Predicta::modeSelection()
{
    SystemUtilities::clearTerminal();
    std::vector<std::string> choices = {
        "   1 : Manual Data Production",
        "   2 : Automatic Data Production",
        "   3 : Plot Results",
        "   4 : Train ML Model",
        "   5 : Predict With ML Model",
        "   6 : Evaluate ML Model",
        "   7 : Utilities Menu"};
    std::string selection = PythonUtilities::pythonInquirer(
        choices,
        "Please select the mode (using arrow keys) to run:");
    switch (selection[3] - '0')
    {
        case 1:
            Predicta::manualSimulationSelection();
            break;
        case 2:
            Predicta::automaticSimulationSelection();
            break;
        case 3:
            Predicta::plotSelection();
            break;
        case 4:
            Predicta::modelTrainSelection();
            break;
        case 5:
            Predicta::modelPredictionSelection();
            break;
        case 6:
            Predicta::modelEvaluationSelection();
            break;
        case 7:
            Predicta::utilitiesMenuSelection();
            break;
        default:
            break;
    }

}

// Prompts user to select utilities option
void Predicta::utilitiesMenuSelection()
{
    SystemUtilities::clearTerminal();
    std::vector<std::string> choices = {
        "   1 : Erase Single Body RK4 Data",
        "   2 : Erase Single Body Eval Data",
        "   3 : Erase Single Body Prediction Data",
        "   4 : Erase Single Body Test Data",
        "   5 : Erase Single Body Training Data",
        "   6 : Erase Single Body Validation Data",
        "   7 : Erase Single Body ML Models",
        "   8 : Erase Two Body RK4 Data",
        "   9 : Erase Three Body RK4 Data",
        "  10 : Erase N Body RK4 Data",
        "  11 : Return to Main Menu"
    };
    std::string selection = PythonUtilities::pythonInquirer(
        choices,
        "Please select the utility (using arrow keys) to run:");
    switch (selection[3] - '0')
    {
        case 1:
            Predicta::eraseSingleBodyRK4Data();
            break;
        case 2:
            Predicta::eraseSingleBodyEvalData();
            break;
        case 3:
            Predicta::eraseSingleBodyPredictData();
            break;
        case 4:
            Predicta::eraseSingleBodyTestData();
            break;
        case 5:
            Predicta::eraseSingleBodyTrainingData();
            break;
        case 6:
            Predicta::eraseSingleBodyValidationData();
            break;
        case 7:
            Predicta::eraseSingleBodyModel();
            break;
        case 8:
            Predicta::eraseTwoBodyRK4Data();
            break;
        case 9:
            Predicta::eraseThreeBodyRK4Data();
            break;
        case 10:
            Predicta::eraseNBodyRK4Data();
            break;
        case 11:
            Predicta::returnToModeSelection();
            break;
        default:
            break;
    }
}

// Returns to mode selection menu
void Predicta::returnToModeSelection()
{
    Predicta::run();
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// Utilities Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Helper function for selecting a body for utilities
std::string Predicta::utilityBodySelection(const std::string& prompt)
{
    SystemUtilities::clearTerminal();
    std::vector<std::string> choices = {
        "   1 : Sun",
        "   2 : Mercury",
        "   3 : Venus",
        "   4 : Earth",
        "   5 : Mars",
        "   6 : Jupiter",
        "   7 : Saturn",
        "   8 : Uranus",
        "   9 : Neptune",
        "  10 : Pluto",
        "  11 : All Bodies",
        "  12 : Cancel"
    };
    std::string selection = PythonUtilities::pythonInquirer(choices, prompt);
    
    // Handle two-digit selections
    if (selection.length() >= 4 && selection[2] == '1') {
        if (selection[3] == '0') return CelestialBody::pluto.name;
        if (selection[3] == '1') return "ALL";
        if (selection[3] == '2') return "";
    }
    
    switch (selection[3] - '0')
    {
        case 1: return CelestialBody::sun.name;
        case 2: return CelestialBody::mercury.name;
        case 3: return CelestialBody::venus.name;
        case 4: return CelestialBody::earth.name;
        case 5: return CelestialBody::mars.name;
        case 6: return CelestialBody::jupiter.name;
        case 7: return CelestialBody::saturn.name;
        case 8: return CelestialBody::uranus.name;
        case 9: return CelestialBody::neptune.name;
        default: return "";
    }
}

// Clears single body RK4 data
void Predicta::eraseSingleBodyRK4Data()
{
    CSVUtilities::emptyDirectory(UniversalConstants::singleBodyRK4Dir);
}

// Clears single body model evaluation data
void Predicta::eraseSingleBodyEvalData()
{
    std::string body = utilityBodySelection("Select body to erase evaluation data for:");
    if (body.empty()) {
        std::cout << "Operation cancelled." << std::endl;
        return;
    }
    
    if (body == "ALL") {
        // Erase for all bodies
        for (const auto& b : CelestialBody::commonBodies) {
            std::string dir = UniversalConstants::getSingleBodyEvalDir(b.name);
            CSVUtilities::emptyDirectory(dir);
        }
        std::cout << "Erased evaluation data for all bodies." << std::endl;
    } else {
        std::string dir = UniversalConstants::getSingleBodyEvalDir(body);
        CSVUtilities::emptyDirectory(dir);
        std::cout << "Erased evaluation data for " << body << "." << std::endl;
    }
}

// Clears single body model prediction data
void Predicta::eraseSingleBodyPredictData()
{
    std::string body = utilityBodySelection("Select body to erase prediction data for:");
    if (body.empty()) {
        std::cout << "Operation cancelled." << std::endl;
        return;
    }
    
    if (body == "ALL") {
        // Erase for all bodies
        for (const auto& b : CelestialBody::commonBodies) {
            std::string dir = UniversalConstants::getSingleBodyPredictionsDir(b.name);
            CSVUtilities::emptyDirectory(dir);
        }
        std::cout << "Erased prediction data for all bodies." << std::endl;
    } else {
        std::string dir = UniversalConstants::getSingleBodyPredictionsDir(body);
        CSVUtilities::emptyDirectory(dir);
        std::cout << "Erased prediction data for " << body << "." << std::endl;
    }
}

// Clears single body model test data
void Predicta::eraseSingleBodyTestData()
{
    std::string body = utilityBodySelection("Select body to erase test data for:");
    if (body.empty()) {
        std::cout << "Operation cancelled." << std::endl;
        return;
    }
    
    if (body == "ALL") {
        // Erase for all bodies
        for (const auto& b : CelestialBody::commonBodies) {
            std::string dir = UniversalConstants::getSingleBodyTestDir(b.name);
            CSVUtilities::emptyDirectory(dir);
        }
        std::cout << "Erased test data for all bodies." << std::endl;
    } else {
        std::string dir = UniversalConstants::getSingleBodyTestDir(body);
        CSVUtilities::emptyDirectory(dir);
        std::cout << "Erased test data for " << body << "." << std::endl;
    }
}

// Clears single body model training data
void Predicta::eraseSingleBodyTrainingData()
{
    std::string body = utilityBodySelection("Select body to erase training data for:");
    if (body.empty()) {
        std::cout << "Operation cancelled." << std::endl;
        return;
    }
    
    if (body == "ALL") {
        // Erase for all bodies
        for (const auto& b : CelestialBody::commonBodies) {
            std::string dir = UniversalConstants::getSingleBodyTrainDir(b.name);
            CSVUtilities::emptyDirectory(dir);
        }
        std::cout << "Erased training data for all bodies." << std::endl;
    } else {
        std::string dir = UniversalConstants::getSingleBodyTrainDir(body);
        CSVUtilities::emptyDirectory(dir);
        std::cout << "Erased training data for " << body << "." << std::endl;
    }
}

// Clears single body model validation data
void Predicta::eraseSingleBodyValidationData()
{
    std::string body = utilityBodySelection("Select body to erase validation data for:");
    if (body.empty()) {
        std::cout << "Operation cancelled." << std::endl;
        return;
    }
    
    if (body == "ALL") {
        // Erase for all bodies
        for (const auto& b : CelestialBody::commonBodies) {
            std::string dir = UniversalConstants::getSingleBodyValDir(b.name);
            CSVUtilities::emptyDirectory(dir);
        }
        std::cout << "Erased validation data for all bodies." << std::endl;
    } else {
        std::string dir = UniversalConstants::getSingleBodyValDir(body);
        CSVUtilities::emptyDirectory(dir);
        std::cout << "Erased validation data for " << body << "." << std::endl;
    }
}

// Clears single body ML model
void Predicta::eraseSingleBodyModel()
{
    std::string body = utilityBodySelection("Select body to erase ML model for:");
    if (body.empty()) {
        std::cout << "Operation cancelled." << std::endl;
        return;
    }
    
    if (body == "ALL") {
        // Erase for all bodies
        for (const auto& b : CelestialBody::commonBodies) {
            std::string dir = UniversalConstants::getSingleBodyModelPath(b.name);
            CSVUtilities::emptyDirectory(dir);
        }
        std::cout << "Erased ML models for all bodies." << std::endl;
    } else {
        std::string dir = UniversalConstants::getSingleBodyModelPath(body);
        CSVUtilities::emptyDirectory(dir);
        std::cout << "Erased ML model for " << body << "." << std::endl;
    }
}

// Clears two body RK4 data
void Predicta::eraseTwoBodyRK4Data()
{
    CSVUtilities::emptyDirectory(UniversalConstants::twoBodyRK4Dir);
}

// Clears three body RK4 data
void Predicta::eraseThreeBodyRK4Data()
{
    CSVUtilities::emptyDirectory(UniversalConstants::threeBodyRK4Dir);
}

// Clears N body RK4 data
void Predicta::eraseNBodyRK4Data()
{
    CSVUtilities::emptyDirectory(UniversalConstants::nBodyRK4Dir);
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// Run Method
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Main run function for Predicta class
void Predicta::run()
{
    Py_Initialize();
    Predicta::modeSelection();
    Py_Finalize();
}
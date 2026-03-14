#include "utilities.h"

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
//                                                                               CSV UTILITIES
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PUBLIC METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 
// CSV File and Directory Utilities
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 

// Checks if the specified directory is empty
bool CSVUtilities::checkForEmptyDirectory(const std::string& directory) {
    auto csvFiles = listCSVFiles(directory);
    return csvFiles.empty();
}

// Copies a random selection of CSV files from sourceDir to destDir
void CSVUtilities::copyRandomCSVFiles(const std::string& sourceDir, const std::string& destDir, int numFiles) {
    auto csvFiles = listCSVFiles(sourceDir);
    if (csvFiles.empty()) {
        std::cerr << "Warning: No CSV files found in " << sourceDir << std::endl;
        return;
    }

    SystemUtilities::createDirectory(destDir);

    std::random_device rd;
    std::mt19937 gen(rd());
    std::shuffle(csvFiles.begin(), csvFiles.end(), gen);

    int filesToCopy = std::min(numFiles, static_cast<int>(csvFiles.size()));
    std::cout << "Copying " << filesToCopy << " random CSV files from " << sourceDir << " to " << destDir << "..." << std::endl;

    for (int i = 0; i < filesToCopy; ++i) {
        const std::string& srcFile = csvFiles[i];
        std::filesystem::path srcPath(srcFile);
        std::filesystem::path destPath = std::filesystem::path(destDir) / srcPath.filename();

        try {
            std::filesystem::copy_file(srcPath, destPath, std::filesystem::copy_options::overwrite_existing);
        } catch (const std::filesystem::filesystem_error& e) {
            std::cerr << "Error copying file " << srcFile << ": " << e.what() << std::endl;
        }
    }

    std::cout << "Successfully copied " << filesToCopy << " random CSV files from " << sourceDir << " to " << destDir << "!" << std::endl;
}

// Copies all CSV files from sourceDir to destDir
void CSVUtilities::copyCSVFiles(const std::string& sourceDir, const std::string& destDir) {
    // Check if source directory has any CSV files
    auto csvFiles = listCSVFiles(sourceDir);
    
    if (csvFiles.empty()) {
        std::cerr << "Warning: No CSV files found in " << sourceDir << std::endl;
        return;
    }
    
    SystemUtilities::createDirectory(destDir);
    
    std::cout << "Copying CSV files from " << sourceDir << " to " << destDir << "..." << std::endl;

    #ifdef _WIN32
        std::string cmd = "copy \"" + sourceDir + "\\*.csv\" \"" + destDir + "\\\" 2>nul";
    #else
        std::string cmd = "cp \"" + sourceDir + "\"/*.csv \"" + destDir + "/\" 2>/dev/null";
    #endif
    
    int result = system(cmd.c_str());
    if (result != 0) {
        std::cerr << "Error: Failed to copy CSV files from " << sourceDir << " to " << destDir << std::endl;
    }

    std::cout << "Successfully copied CSV files from " << sourceDir << " to " << destDir << "!" << std::endl;
}

// Empties all files in the specified directory
void CSVUtilities::emptyDirectory(const std::string& directory) {
    SystemUtilities::createDirectory(directory);
    
    #ifdef _WIN32
        std::string cmd = "del /Q \"" + directory + "\\*\" 2>nul";
    #else
        std::string cmd = "rm -f \"" + directory + "\"/* 2>/dev/null";
    #endif
    
    int result = system(cmd.c_str());
    if (result != 0) {
        std::cerr << "Error: Failed to empty directory " << directory << std::endl;
    } else {
        std::cout << "Emptied directory: " << directory << std::endl;
    }
}

// Lists all CSV files in the specified directory
std::vector<std::string> CSVUtilities::listCSVFiles(const std::string& directory) {
    std::vector<std::string> files;
    
    #ifdef _WIN32
        std::string cmd = "dir /b \"" + directory + "\\*.csv\" 2>nul";
    #else
        std::string cmd = "ls \"" + directory + "\"/*.csv 2>/dev/null";
    #endif
    
    FILE* pipe = popen(cmd.c_str(), "r");
    if (!pipe) return files;
    
    char buffer[256];
    while (fgets(buffer, sizeof(buffer), pipe) != nullptr) {
        std::string filename(buffer);
        // Remove trailing newline
        if (!filename.empty() && filename.back() == '\n') {
            filename.pop_back();
        }
        files.push_back(filename);
    }
    
    pclose(pipe);
    return files;
}

// Constructs a CSV file path with timestamp
std::string CSVUtilities::makeCSVPath(const std::string& directory, const std::string& fileNameBase) {
    std::string fname = fileNameBase + "-" + SystemUtilities::timeStamp() + ".csv";
    std::string fullpath = directory + "/" + fname;
    return fullpath;
}

// Moves all CSV files from sourceDir to destDir
void CSVUtilities::moveCSVFiles(const std::string& sourceDir, const std::string& destDir) {
    // Check if source directory has any CSV files
    auto csvFiles = listCSVFiles(sourceDir);

    if (csvFiles.empty()) {
        std::cerr << "Warning: No CSV files found in " << sourceDir << std::endl;
        return;
    }

    SystemUtilities::createDirectory(destDir);
    std::cout << "Moving CSV files from " << sourceDir << " to " << destDir << "..." << std::endl;

    #ifdef _WIN32
        std::string cmd = "move \"" + sourceDir + "\\*.csv\" \"" + destDir + "\\\" 2>nul";
    #else
        std::string cmd = "mv \"" + sourceDir + "\"/*.csv \"" + destDir + "/\" 2>/dev/null";
    #endif

    int result = system(cmd.c_str());
    if (result != 0) {
        std::cerr << "Error: Failed to move CSV files from " << sourceDir << " to " << destDir << std::endl;
    }

    std::cout << "Successfully moved CSV files from " << sourceDir << " to " << destDir << "!" << std::endl;
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 
// Single Body CSV Read Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 

// Reads single body simulation data from CSV file
bool CSVUtilities::readSingleBodySimDataCSV(const std::string& filepath,
        SingleBodyIC& initialConditions,
        SingleBodySolution& rk4Solution) {

    std::ifstream file(filepath);

    if (!file.is_open()) {
        std::cerr << "Error: Could not open file " << filepath << std::endl;
        return false;
    }

    std::string line;

    // Read and skip header line
    if (!std::getline(file, line)) {
        std::cerr << "Error: Empty file" << std::endl;
        return false; 
    }

    // Clear solution vectors
    rk4Solution.times.clear();
    rk4Solution.positions.clear();
    rk4Solution.velocities.clear();

    bool firstRow = true;

    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::string item;
        std::vector<std::string> tokens;

        // Split by comma
        while (std::getline(ss, item, ',')) {
            tokens.push_back(item);
        }

        // Standard format: time, pos, vel, ...
        if (tokens.size() < 3) continue; // Need at least time, pos, vel

        double time = std::stod(tokens[0]);
        double position = std::stod(tokens[1]);
        double velocity = std::stod(tokens[2]);

        rk4Solution.times.push_back(time);
        rk4Solution.positions.push_back(position);
        rk4Solution.velocities.push_back(velocity);

        // First row contains initial conditions
        if (firstRow && tokens.size() >= 11) {
            initialConditions.bodyName = tokens[3];
            initialConditions.bodyMass = std::stod(tokens[4]);
            initialConditions.bodyRadius = std::stod(tokens[5]);
            initialConditions.initialPosition = std::stod(tokens[6]);
            initialConditions.initialVelocity = std::stod(tokens[7]);
            initialConditions.initTime = std::stod(tokens[8]);
            initialConditions.timeSpan = std::stod(tokens[9]);
            initialConditions.timeStep = std::stod(tokens[10]);
            firstRow = false;
        }
    }

    file.close();

    // Check that solution has data
    if (rk4Solution.times.empty()) {
        std::cerr << "Error: No data rows found in file" << std::endl;
        return false;
    }

    return true;
}

// Reads single body model data from CSV file
bool CSVUtilities::readSingleBodyModelDataCSV(const std::string& filepath,
        SingleBodyIC& initialConditions,
        SingleBodySolution& modelSolution) {

    std::ifstream file(filepath);

    if (!file.is_open()) {
        std::cerr << "Error: Could not open file " << filepath << std::endl;
        return false;
    }

    std::string line;
    // Read and skip header line

    if (!std::getline(file, line)) {
        std::cerr << "Error: Empty file" << std::endl;
        return false; 
    }

    // Clear solution vectors
    modelSolution.times.clear();
    modelSolution.positions.clear();
    modelSolution.velocities.clear();

    bool firstRow = true;

    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::string item;
        std::vector<std::string> tokens;

        // Split by comma
        while (std::getline(ss, item, ',')) {
            tokens.push_back(item);
        }

        // Standard format: time, pos, vel, ...
        if (tokens.size() < 3) continue; // Need at least time, pos, vel

        double time = std::stod(tokens[0]);
        double position = std::stod(tokens[1]);
        double velocity = std::stod(tokens[2]);

        modelSolution.times.push_back(time);
        modelSolution.positions.push_back(position);
        modelSolution.velocities.push_back(velocity);

        // First row contains initial conditions
        if (firstRow && tokens.size() >= 11) {
            initialConditions.bodyName = tokens[3];
            initialConditions.bodyMass = std::stod(tokens[4]);
            initialConditions.bodyRadius = std::stod(tokens[5]);
            initialConditions.initialPosition = std::stod(tokens[6]);
            initialConditions.initialVelocity = std::stod(tokens[7]);
            initialConditions.initTime = std::stod(tokens[8]);
            initialConditions.timeSpan = std::stod(tokens[9]);
            initialConditions.timeStep = std::stod(tokens[10]);
            firstRow = false;
        }
    }

    file.close();

    // Check that solution has data
    if (modelSolution.times.empty()) {
        std::cerr << "Error: No data rows found in file" << std::endl;
        return false;
    } 

    return true;
}

// Reads single body evaluation data from CSV file
bool CSVUtilities::readSingleBodyEvaluationDataCSV(const std::string& filepath,
        SingleBodyIC& initialConditions,
        SingleBodySolution& rk4Solution,
        SingleBodySolution& modelSolution) {

    std::ifstream file(filepath);

    if (!file.is_open()) {
        std::cerr << "Error: Could not open file " << filepath << std::endl;
        return false;
    }

    std::string line;

    // Read and skip header line
    if (!std::getline(file, line)) {
        std::cerr << "Error: Empty file" << std::endl;
        return false; 
    }

    // Clear solution vectors
    rk4Solution.times.clear();
    rk4Solution.positions.clear();
    rk4Solution.velocities.clear();
    modelSolution.times.clear();
    modelSolution.positions.clear();
    modelSolution.velocities.clear();

    bool firstRow = true;

    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::string item;
        std::vector<std::string> tokens;

        // Split by comma
        while (std::getline(ss, item, ',')) {
            tokens.push_back(item);
        }

        // Evaluation data format: RK4_time, Model_time, RK4_pos, Model_pos, RK4_vel, Model_vel, ...
        if (tokens.size() < 6) continue; // Need at least both times, positions, and velocities

        // Read RK4 data
        if (!tokens[0].empty()) {
            rk4Solution.times.push_back(std::stod(tokens[0]));
        }
        if (!tokens[2].empty()) {
            rk4Solution.positions.push_back(std::stod(tokens[2]));
        }
        if (!tokens[4].empty()) {
            rk4Solution.velocities.push_back(std::stod(tokens[4]));
        }

        // Read Model data
        if (!tokens[1].empty()) {
            modelSolution.times.push_back(std::stod(tokens[1]));
        }
        if (!tokens[3].empty()) {
            modelSolution.positions.push_back(std::stod(tokens[3]));
        }
        if (!tokens[5].empty()) {
            modelSolution.velocities.push_back(std::stod(tokens[5]));
        }

        // First row contains initial conditions (starts at index 6 for evaluation data)
        if (firstRow && tokens.size() >= 14) {
            initialConditions.bodyName = tokens[6];
            initialConditions.bodyMass = std::stod(tokens[7]);
            initialConditions.bodyRadius = std::stod(tokens[8]);
            initialConditions.initialPosition = std::stod(tokens[9]);
            initialConditions.initialVelocity = std::stod(tokens[10]);
            initialConditions.initTime = std::stod(tokens[11]);
            initialConditions.timeSpan = std::stod(tokens[12]);
            initialConditions.timeStep = std::stod(tokens[13]);
            firstRow = false;
        }
    }

    file.close();

    // Check that both solutions have data
    if (rk4Solution.times.empty() || modelSolution.times.empty()) {
        std::cerr << "Error: No data rows found in file" << std::endl;
        return false;
    }

    return true;
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 
// Single Body CSV Write Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 

// Writes single body numerical method simulation data to CSV file
void CSVUtilities::writeSingleBodySimDataCSV(const SingleBodyIC& initialConditions, 
        const SingleBodySolution rk4Solution,
        const std::string& directory) {

    // Create directory if it doesn't exist
    SystemUtilities::createDirectory(directory);
    std::string filePath = makeCSVPath(directory, UniversalConstants::singleBodyFile);
    std::ofstream file(filePath);
    
    // Cannot open file
    if (!file.is_open()) {
        std::cerr << "Error: Could not open file " << filePath << std::endl;
        return;
    }

    // Write header
    file << UniversalConstants::singleBodyRK4Times +
        "," + UniversalConstants::singleBodyRKRProjP + 
        "," + UniversalConstants::singleBodyRK4ProjV +
        "," + UniversalConstants::singleBodyName +
        "," + UniversalConstants::singleBodyMass +
        "," + UniversalConstants::singleBodyBodyRad +
        "," + UniversalConstants::singleBodyInitProjP +
        "," + UniversalConstants::singleBodyInitProjV +
        "," + UniversalConstants::singleBodyInitTime +
        "," + UniversalConstants::singleBodySimTimeSpan +
        "," + UniversalConstants::singleBodySimTimeStep + "\n";

    // Write first row with initial conditions
    file << rk4Solution.times[0] << ","
        << rk4Solution.positions[0] << ","
        << rk4Solution.velocities[0] << ","
        << initialConditions.bodyName << ","
        << initialConditions.bodyMass << ","
        << initialConditions.bodyRadius << ","
        << initialConditions.initialPosition << ","
        << initialConditions.initialVelocity << ","
        << initialConditions.initTime << ","
        << initialConditions.timeSpan << ","
        << initialConditions.timeStep << "\n";

    // Write simulation data
    for (size_t i = 1; i < rk4Solution.times.size(); ++i) {
        file << rk4Solution.times[i] << ","
            << rk4Solution.positions[i] << ","
            << rk4Solution.velocities[i] << "\n";
    }

    file.close();
}

// Writes single body machine learning model data to CSV file
void CSVUtilities::writeSingleBodyModelDataCSV(const SingleBodyIC& initialConditions,
        const SingleBodySolution& mlSolution,
        const std::string& directory) {

    // Create directory if it doesn't exist
    SystemUtilities::createDirectory(directory);
    std::string filePath = makeCSVPath(directory, UniversalConstants::singleBodyFile);
    std::ofstream file(filePath);
    
    // Cannot open file
    if (!file.is_open()) {
        std::cerr << "Error: Could not open file " << filePath << std::endl;
        return;
    }

    // Write header
    file << UniversalConstants::singleBodyModelTimes +
        "," + UniversalConstants::singleBodyModelProjP + 
        "," + UniversalConstants::singleBodyModelProjV +
        "," + UniversalConstants::singleBodyName +
        "," + UniversalConstants::singleBodyMass +
        "," + UniversalConstants::singleBodyBodyRad +
        "," + UniversalConstants::singleBodyInitProjP +
        "," + UniversalConstants::singleBodyInitProjV +
        "," + UniversalConstants::singleBodyInitTime +
        "," + UniversalConstants::singleBodySimTimeSpan +
        "," + UniversalConstants::singleBodySimTimeStep + "\n";

    // Write first row with initial conditions
    file << mlSolution.times[0] << ","
        << mlSolution.positions[0] << ","
        << mlSolution.velocities[0] << ","
        << initialConditions.bodyName << ","
        << initialConditions.bodyMass << ","
        << initialConditions.bodyRadius << ","
        << initialConditions.initialPosition << ","
        << initialConditions.initialVelocity << ","
        << initialConditions.initTime << ","
        << initialConditions.timeSpan << ","
        << initialConditions.timeStep << "\n";

    // Write simulation data
    for (size_t i = 1; i < mlSolution.times.size(); ++i) {
        file << mlSolution.times[i] << ","
            << mlSolution.positions[i] << ","
            << mlSolution.velocities[i] << "\n";
    }

    file.close();
}

// Writes single body evaluation data to CSV file
void CSVUtilities::writeSingleBodyEvaluationDataCSV(const SingleBodyIC& initialConditions,
        const SingleBodySolution& rk4Solution,
        const SingleBodySolution& mlSolution,
        const std::string& directory) {

    // Create directory if it doesn't exist
    SystemUtilities::createDirectory(directory);
    std::string filePath = makeCSVPath(directory, UniversalConstants::singleBodyFile);
    std::ofstream file(filePath);

    // Cannot open file
    if (!file.is_open()) {
        std::cerr << "Error: Could not open file " << filePath << std::endl;
        return;
    }

    // Write header
    file << UniversalConstants::singleBodyRK4Times +
        "," + UniversalConstants::singleBodyModelTimes + 
        "," + UniversalConstants::singleBodyRKRProjP + 
        "," + UniversalConstants::singleBodyModelProjP + 
        "," + UniversalConstants::singleBodyRK4ProjV +
        "," + UniversalConstants::singleBodyModelProjV +
        "," + UniversalConstants::singleBodyName +
        "," + UniversalConstants::singleBodyMass +
        "," + UniversalConstants::singleBodyBodyRad +
        "," + UniversalConstants::singleBodyInitProjP +
        "," + UniversalConstants::singleBodyInitProjV +
        "," + UniversalConstants::singleBodyInitTime +
        "," + UniversalConstants::singleBodySimTimeSpan +
        "," + UniversalConstants::singleBodySimTimeStep + "\n";

    // Write first row with initial conditions
    file << rk4Solution.times[0] << ","
        << mlSolution.times[0] << ","
        << rk4Solution.positions[0] << ","
        << mlSolution.positions[0] << ","
        << rk4Solution.velocities[0] << ","
        << mlSolution.velocities[0] << ","
        << initialConditions.bodyName << ","
        << initialConditions.bodyMass << ","
        << initialConditions.bodyRadius << ","
        << initialConditions.initialPosition << ","
        << initialConditions.initialVelocity << ","
        << initialConditions.initTime << ","
        << initialConditions.timeSpan << ","
        << initialConditions.timeStep << "\n";

    // Write simulation data
    size_t dataSize = std::min(rk4Solution.times.size(), mlSolution.times.size());
    for (size_t i = 1; i < dataSize; ++i) {
        file << rk4Solution.times[i] << ","
            << mlSolution.times[i] << ","
            << rk4Solution.positions[i] << ","
            << mlSolution.positions[i] << ","
            << rk4Solution.velocities[i] << ","
            << mlSolution.velocities[i] << "\n";
    }

    file.close();

}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 
// Two Body CSV Read Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 

// Reads the two body simulation data from CSV file
bool CSVUtilities::readTwoBodySimDataCSV(const std::string& filepath,
        TwoBodyIC& initialConditions,
        TwoBodySolution& rk4Solution) {

    std::ifstream file(filepath);

    if (!file.is_open()) {
        std::cerr << "Error: Could not open file " << filepath << std::endl;
        return false;
    }

    std::string line;

    // Read and skip header line
    if (!std::getline(file, line)) {
        std::cerr << "Error: Empty file" << std::endl;
        return false;
    }

    // Clear solution vectors
    rk4Solution.times.clear();
    rk4Solution.body1Positions.clear();
    rk4Solution.body2Positions.clear();
    rk4Solution.body1Velocities.clear();
    rk4Solution.body2Velocities.clear();

    bool firstRow = true;

    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::string item;
        std::vector<std::string> tokens;

        // Split by comma
        while (std::getline(ss, item, ',')) {
            tokens.push_back(item);
        }

        // Need at least time + 12 position/velocity values (1 + 6 + 6 = 13)
        if (tokens.size() < 13) continue;

        // Parse time
        double time = std::stod(tokens[0]);
        rk4Solution.times.push_back(time);

        // Parse Body 1 Position (x, y, z)
        std::array<double, 3> b1Pos = {
            std::stod(tokens[1]),
            std::stod(tokens[2]),
            std::stod(tokens[3])
        };
        rk4Solution.body1Positions.push_back(b1Pos);

        // Parse Body 1 Velocity (x, y, z)
        std::array<double, 3> b1Vel = {
            std::stod(tokens[4]),
            std::stod(tokens[5]),
            std::stod(tokens[6])
        };
        rk4Solution.body1Velocities.push_back(b1Vel);

        // Parse Body 2 Position (x, y, z)
        std::array<double, 3> b2Pos = {
            std::stod(tokens[7]),
            std::stod(tokens[8]),
            std::stod(tokens[9])
        };
        rk4Solution.body2Positions.push_back(b2Pos);

        // Parse Body 2 Velocity (x, y, z)
        std::array<double, 3> b2Vel = {
            std::stod(tokens[10]),
            std::stod(tokens[11]),
            std::stod(tokens[12])
        };
        rk4Solution.body2Velocities.push_back(b2Vel);

        // First row contains initial conditions (needs 33 tokens total)
        if (firstRow && tokens.size() >= 33) {
            // Body 1 Initial Conditions
            initialConditions.body1Name = tokens[13];
            initialConditions.bodyMasses[0] = std::stod(tokens[14]);
            initialConditions.bodyRadii[0] = std::stod(tokens[15]);
            initialConditions.body1InitialPosition[0] = std::stod(tokens[16]);
            initialConditions.body1InitialPosition[1] = std::stod(tokens[17]);
            initialConditions.body1InitialPosition[2] = std::stod(tokens[18]);
            initialConditions.body1InitialVelocity[0] = std::stod(tokens[19]);
            initialConditions.body1InitialVelocity[1] = std::stod(tokens[20]);
            initialConditions.body1InitialVelocity[2] = std::stod(tokens[21]);

            // Body 2 Initial Conditions
            initialConditions.body2Name = tokens[22];
            initialConditions.bodyMasses[1] = std::stod(tokens[23]);
            initialConditions.bodyRadii[1] = std::stod(tokens[24]);
            initialConditions.body2InitialPosition[0] = std::stod(tokens[25]);
            initialConditions.body2InitialPosition[1] = std::stod(tokens[26]);
            initialConditions.body2InitialPosition[2] = std::stod(tokens[27]);
            initialConditions.body2InitialVelocity[0] = std::stod(tokens[28]);
            initialConditions.body2InitialVelocity[1] = std::stod(tokens[29]);
            initialConditions.body2InitialVelocity[2] = std::stod(tokens[30]);

            // Simulation Parameters
            initialConditions.timeSpan = std::stod(tokens[31]);
            initialConditions.timeStep = std::stod(tokens[32]);
            initialConditions.initTime = time;

            firstRow = false;
        }
    }

    file.close();

    // Check that solution has data
    if (rk4Solution.times.empty()) {
        std::cerr << "Error: No data rows found in file" << std::endl;
        return false;
    }

    return true;
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 
// Two Body CSV Write Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 

// Writes two body simulation data to CSV file
void CSVUtilities::writeTwoBodySimDataCSV(const TwoBodyIC& initialConditions, 
        const TwoBodySolution& rk4Solution, 
        const std::string& directory) {

    // Create directory if it doesn't exist
    SystemUtilities::createDirectory(directory);
    std::string filePath = makeCSVPath(directory, UniversalConstants::twoBodyFile);
    std::ofstream file(filePath);

    // Cannot open file
    if (!file.is_open()) {
        std::cerr << "Error: Could not open file " << filePath << std::endl;
        return;
    }

    // Write header
    file << UniversalConstants::twoBodyRK4Times +
        // Body 1 Position and Velocity
        "," + UniversalConstants::twoBodyRK4Body1PosX +
        "," + UniversalConstants::twoBodyRK4Body1PosY +
        "," + UniversalConstants::twoBodyRK4Body1PosZ +
        "," + UniversalConstants::twoBodyRK4Body1VelX +
        "," + UniversalConstants::twoBodyRK4Body1VelY +
        "," + UniversalConstants::twoBodyRK4Body1VelZ +
        // Body 2 Position and Velocity
        "," + UniversalConstants::twoBodyRK4Body2PosX +
        "," + UniversalConstants::twoBodyRK4Body2PosY +
        "," + UniversalConstants::twoBodyRK4Body2PosZ +
        "," + UniversalConstants::twoBodyRK4Body2VelX +
        "," + UniversalConstants::twoBodyRK4Body2VelY +
        "," + UniversalConstants::twoBodyRK4Body2VelZ +
        // Body 1 Initial Conditions
        "," + UniversalConstants::twoBodyBody1Name +
        "," + UniversalConstants::twoBodyBody1Mass +
        "," + UniversalConstants::twoBodyBody1Rad +
        "," + UniversalConstants::twoBodyBody1InitPosX +
        "," + UniversalConstants::twoBodyBody1InitPosY +
        "," + UniversalConstants::twoBodyBody1InitPosZ +
        "," + UniversalConstants::twoBodyBody1InitVelX +
        "," + UniversalConstants::twoBodyBody1InitVelY +
        "," + UniversalConstants::twoBodyBody1InitVelZ +
        // Body 2 Initial Conditions
        "," + UniversalConstants::twoBodyBody2Name +
        "," + UniversalConstants::twoBodyBody2Mass +
        "," + UniversalConstants::twoBodyBody2Rad +
        "," + UniversalConstants::twoBodyBody2InitPosX +
        "," + UniversalConstants::twoBodyBody2InitPosY +
        "," + UniversalConstants::twoBodyBody2InitPosZ +
        "," + UniversalConstants::twoBodyBody2InitVelX +
        "," + UniversalConstants::twoBodyBody2InitVelY +
        "," + UniversalConstants::twoBodyBody2InitVelZ +
        // Simulation Parameters
        "," + UniversalConstants::twoBodySimTimeSpan +
        "," + UniversalConstants::twoBodySimTimeStep + "\n";

    // Write first row with initial conditions
    file << rk4Solution.times[0] << ","
        // Body 1 Position and Velocity
        << rk4Solution.body1Positions[0][0] << ","
        << rk4Solution.body1Positions[0][1] << ","
        << rk4Solution.body1Positions[0][2] << ","
        << rk4Solution.body1Velocities[0][0] << ","
        << rk4Solution.body1Velocities[0][1] << ","
        << rk4Solution.body1Velocities[0][2] << ","
        // Body 2 Position and Velocity
        << rk4Solution.body2Positions[0][0] << ","
        << rk4Solution.body2Positions[0][1] << ","
        << rk4Solution.body2Positions[0][2] << ","
        << rk4Solution.body2Velocities[0][0] << ","
        << rk4Solution.body2Velocities[0][1] << ","
        << rk4Solution.body2Velocities[0][2] << ","
        // Body 1 Initial Conditions
        << initialConditions.body1Name << ","
        << initialConditions.bodyMasses.at(0) << ","
        << initialConditions.bodyRadii.at(0) << ","
        << initialConditions.body1InitialPosition[0] << ","
        << initialConditions.body1InitialPosition[1] << ","
        << initialConditions.body1InitialPosition[2] << ","
        << initialConditions.body1InitialVelocity[0] << ","
        << initialConditions.body1InitialVelocity[1] << ","
        << initialConditions.body1InitialVelocity[2] << ","
        // Body 2 Initial Conditions
        << initialConditions.body2Name << ","
        << initialConditions.bodyMasses.at(1) << ","
        << initialConditions.bodyRadii.at(1) << ","
        << initialConditions.body2InitialPosition[0] << ","
        << initialConditions.body2InitialPosition[1] << ","
        << initialConditions.body2InitialPosition[2] << ","
        << initialConditions.body2InitialVelocity[0] << ","
        << initialConditions.body2InitialVelocity[1] << ","
        << initialConditions.body2InitialVelocity[2] << ","
        // Simulation Parameters
        << initialConditions.timeSpan << ","
        << initialConditions.timeStep << "\n";

    // Write simulation data
    for (size_t i = 1; i < rk4Solution.times.size(); ++i) {
        file << rk4Solution.times[i] << ","
            // Body 1 Position and Velocity
            << rk4Solution.body1Positions[i][0] << ","
            << rk4Solution.body1Positions[i][1] << ","
            << rk4Solution.body1Positions[i][2] << ","
            << rk4Solution.body1Velocities[i][0] << ","
            << rk4Solution.body1Velocities[i][1] << ","
            << rk4Solution.body1Velocities[i][2] << ","
            // Body 2 Position and Velocity
            << rk4Solution.body2Positions[i][0] << ","
            << rk4Solution.body2Positions[i][1] << ","
            << rk4Solution.body2Positions[i][2] << ","
            << rk4Solution.body2Velocities[i][0] << ","
            << rk4Solution.body2Velocities[i][1] << ","
            << rk4Solution.body2Velocities[i][2] << "\n";
    }

    file.close();
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 
// Three Body CSV Read Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 

// Reads the three body simulation data from CSV file
bool CSVUtilities::readThreeBodySimDataCSV(const std::string& filepath,
        ThreeBodyIC& initialConditions,
        ThreeBodySolution& rk4Solution) {

    std::ifstream file(filepath);

    if (!file.is_open()) {
        std::cerr << "Error: Could not open file " << filepath << std::endl;
        return false;
    }

    std::string line;

    // Read and skip header line
    if (!std::getline(file, line)) {
        std::cerr << "Error: Empty file" << std::endl;
        return false;
    }

    // Clear solution vectors
    rk4Solution.times.clear();
    rk4Solution.body1Positions.clear();
    rk4Solution.body2Positions.clear();
    rk4Solution.body3Positions.clear();
    rk4Solution.body1Velocities.clear();
    rk4Solution.body2Velocities.clear();
    rk4Solution.body3Velocities.clear();

    bool firstRow = true;

    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::string item;
        std::vector<std::string> tokens;

        // Split by comma
        while (std::getline(ss, item, ',')) {
            tokens.push_back(item);
        }

        // Need at least time + 18 position/velocity values (1 + 9 + 9 = 19)
        if (tokens.size() < 19) continue;

        // Parse time
        double time = std::stod(tokens[0]);
        rk4Solution.times.push_back(time);

        // Parse Body 1 Position (x, y, z)
        std::array<double, 3> b1Pos = {
            std::stod(tokens[1]),
            std::stod(tokens[2]),
            std::stod(tokens[3])
        };
        rk4Solution.body1Positions.push_back(b1Pos);

        // Parse Body 1 Velocity (x, y, z)
        std::array<double, 3> b1Vel = {
            std::stod(tokens[4]),
            std::stod(tokens[5]),
            std::stod(tokens[6])
        };
        rk4Solution.body1Velocities.push_back(b1Vel);

        // Parse Body 2 Position (x, y, z)
        std::array<double, 3> b2Pos = {
            std::stod(tokens[7]),
            std::stod(tokens[8]),
            std::stod(tokens[9])
        };
        rk4Solution.body2Positions.push_back(b2Pos);

        // Parse Body 2 Velocity (x, y, z)
        std::array<double, 3> b2Vel = {
            std::stod(tokens[10]),
            std::stod(tokens[11]),
            std::stod(tokens[12])
        };
        rk4Solution.body2Velocities.push_back(b2Vel);

        // Parse Body 3 Position (x, y, z)
        std::array<double, 3> b3Pos = {
            std::stod(tokens[13]),
            std::stod(tokens[14]),
            std::stod(tokens[15])
        };
        rk4Solution.body3Positions.push_back(b3Pos);

        // Parse Body 3 Velocity (x, y, z)
        std::array<double, 3> b3Vel = {
            std::stod(tokens[16]),
            std::stod(tokens[17]),
            std::stod(tokens[18])
        };
        rk4Solution.body3Velocities.push_back(b3Vel);

        // First row contains initial conditions (needs 48 tokens total)
        if (firstRow && tokens.size() >= 48) {
            // Body 1 Initial Conditions
            initialConditions.body1Name = tokens[19];
            initialConditions.bodyMasses[0] = std::stod(tokens[20]);
            initialConditions.bodyRadii[0] = std::stod(tokens[21]);
            initialConditions.body1InitialPosition[0] = std::stod(tokens[22]);
            initialConditions.body1InitialPosition[1] = std::stod(tokens[23]);
            initialConditions.body1InitialPosition[2] = std::stod(tokens[24]);
            initialConditions.body1InitialVelocity[0] = std::stod(tokens[25]);
            initialConditions.body1InitialVelocity[1] = std::stod(tokens[26]);
            initialConditions.body1InitialVelocity[2] = std::stod(tokens[27]);

            // Body 2 Initial Conditions
            initialConditions.body2Name = tokens[28];
            initialConditions.bodyMasses[1] = std::stod(tokens[29]);
            initialConditions.bodyRadii[1] = std::stod(tokens[30]);
            initialConditions.body2InitialPosition[0] = std::stod(tokens[31]);
            initialConditions.body2InitialPosition[1] = std::stod(tokens[32]);
            initialConditions.body2InitialPosition[2] = std::stod(tokens[33]);
            initialConditions.body2InitialVelocity[0] = std::stod(tokens[34]);
            initialConditions.body2InitialVelocity[1] = std::stod(tokens[35]);
            initialConditions.body2InitialVelocity[2] = std::stod(tokens[36]);

            // Body 3 Initial Conditions
            initialConditions.body3Name = tokens[37];
            initialConditions.bodyMasses[2] = std::stod(tokens[38]);
            initialConditions.bodyRadii[2] = std::stod(tokens[39]);
            initialConditions.body3InitialPosition[0] = std::stod(tokens[40]);
            initialConditions.body3InitialPosition[1] = std::stod(tokens[41]);
            initialConditions.body3InitialPosition[2] = std::stod(tokens[42]);
            initialConditions.body3InitialVelocity[0] = std::stod(tokens[43]);
            initialConditions.body3InitialVelocity[1] = std::stod(tokens[44]);
            initialConditions.body3InitialVelocity[2] = std::stod(tokens[45]);

            // Simulation Parameters
            initialConditions.timeSpan = std::stod(tokens[46]);
            initialConditions.timeStep = std::stod(tokens[47]);
            initialConditions.initTime = time;

            firstRow = false;
        }
    }

    file.close();

    // Check that solution has data
    if (rk4Solution.times.empty()) {
        std::cerr << "Error: No data rows found in file" << std::endl;
        return false;
    }

    return true;
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 
// Three Body CSV Write Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 

// Writes three body simulation data to CSV file
void CSVUtilities::writeThreeBodySimDataCSV(const ThreeBodyIC& initialConditions, 
        const ThreeBodySolution& rk4Solution, 
        const std::string& directory) {

    // Create directory if it doesn't exist
    SystemUtilities::createDirectory(directory);
    std::string filePath = makeCSVPath(directory, UniversalConstants::threeBodyFile);
    std::ofstream file(filePath);

    // Cannot open file
    if (!file.is_open()) {
        std::cerr << "Error: Could not open file " << filePath << std::endl;
        return;
    }

    // Write header
    file << UniversalConstants::threeBodyRK4Times +
        // Body 1 Position and Velocity
        "," + UniversalConstants::threeBodyRK4Body1PosX +
        "," + UniversalConstants::threeBodyRK4Body1PosY +
        "," + UniversalConstants::threeBodyRK4Body1PosZ +
        "," + UniversalConstants::threeBodyRK4Body1VelX +
        "," + UniversalConstants::threeBodyRK4Body1VelY +
        "," + UniversalConstants::threeBodyRK4Body1VelZ +
        // Body 2 Position and Velocity
        "," + UniversalConstants::threeBodyRK4Body2PosX +
        "," + UniversalConstants::threeBodyRK4Body2PosY +
        "," + UniversalConstants::threeBodyRK4Body2PosZ +
        "," + UniversalConstants::threeBodyRK4Body2VelX +
        "," + UniversalConstants::threeBodyRK4Body2VelY +
        "," + UniversalConstants::threeBodyRK4Body2VelZ +
        // Body 3 Position and Velocity
        "," + UniversalConstants::threeBodyRK4Body3PosX +
        "," + UniversalConstants::threeBodyRK4Body3PosY +
        "," + UniversalConstants::threeBodyRK4Body3PosZ +
        "," + UniversalConstants::threeBodyRK4Body3VelX +
        "," + UniversalConstants::threeBodyRK4Body3VelY +
        "," + UniversalConstants::threeBodyRK4Body3VelZ +
        // Body 1 Initial Conditions
        "," + UniversalConstants::threeBodyBody1Name +
        "," + UniversalConstants::threeBodyBody1Mass +
        "," + UniversalConstants::threeBodyBody1Rad +
        "," + UniversalConstants::threeBodyBody1InitPosX +
        "," + UniversalConstants::threeBodyBody1InitPosY +
        "," + UniversalConstants::threeBodyBody1InitPosZ +
        "," + UniversalConstants::threeBodyBody1InitVelX +
        "," + UniversalConstants::threeBodyBody1InitVelY +
        "," + UniversalConstants::threeBodyBody1InitVelZ +
        // Body 2 Initial Conditions
        "," + UniversalConstants::threeBodyBody2Name +
        "," + UniversalConstants::threeBodyBody2Mass +
        "," + UniversalConstants::threeBodyBody2Rad +
        "," + UniversalConstants::threeBodyBody2InitPosX +
        "," + UniversalConstants::threeBodyBody2InitPosY +
        "," + UniversalConstants::threeBodyBody2InitPosZ +
        "," + UniversalConstants::threeBodyBody2InitVelX +
        "," + UniversalConstants::threeBodyBody2InitVelY +
        "," + UniversalConstants::threeBodyBody2InitVelZ +
        // Body 3 Initial Conditions
        "," + UniversalConstants::threeBodyBody3Name +
        "," + UniversalConstants::threeBodyBody3Mass +
        "," + UniversalConstants::threeBodyBody3Rad +
        "," + UniversalConstants::threeBodyBody3InitPosX +
        "," + UniversalConstants::threeBodyBody3InitPosY +
        "," + UniversalConstants::threeBodyBody3InitPosZ +
        "," + UniversalConstants::threeBodyBody3InitVelX +
        "," + UniversalConstants::threeBodyBody3InitVelY +
        "," + UniversalConstants::threeBodyBody3InitVelZ +
        // Simulation Parameters
        "," + UniversalConstants::threeBodySimTimeSpan +
        "," + UniversalConstants::threeBodySimTimeStep + "\n";

    // Write first row with initial conditions
    file << rk4Solution.times[0] << ","
        // Body 1 Position and Velocity
        << rk4Solution.body1Positions[0][0] << ","
        << rk4Solution.body1Positions[0][1] << ","
        << rk4Solution.body1Positions[0][2] << ","
        << rk4Solution.body1Velocities[0][0] << ","
        << rk4Solution.body1Velocities[0][1] << ","
        << rk4Solution.body1Velocities[0][2] << ","
        // Body 2 Position and Velocity
        << rk4Solution.body2Positions[0][0] << ","
        << rk4Solution.body2Positions[0][1] << ","
        << rk4Solution.body2Positions[0][2] << ","
        << rk4Solution.body2Velocities[0][0] << ","
        << rk4Solution.body2Velocities[0][1] << ","
        << rk4Solution.body2Velocities[0][2] << ","
        // Body 3 Position and Velocity
        << rk4Solution.body3Positions[0][0] << ","
        << rk4Solution.body3Positions[0][1] << ","
        << rk4Solution.body3Positions[0][2] << ","
        << rk4Solution.body3Velocities[0][0] << ","
        << rk4Solution.body3Velocities[0][1] << ","
        << rk4Solution.body3Velocities[0][2] << ","
        // Body 1 Initial Conditions
        << initialConditions.body1Name << ","
        << initialConditions.bodyMasses.at(0) << ","
        << initialConditions.bodyRadii.at(0) << ","
        << initialConditions.body1InitialPosition[0] << ","
        << initialConditions.body1InitialPosition[1] << ","
        << initialConditions.body1InitialPosition[2] << ","
        << initialConditions.body1InitialVelocity[0] << ","
        << initialConditions.body1InitialVelocity[1] << ","
        << initialConditions.body1InitialVelocity[2] << ","
        // Body 2 Initial Conditions
        << initialConditions.body2Name << ","
        << initialConditions.bodyMasses.at(1) << ","
        << initialConditions.bodyRadii.at(1) << ","
        << initialConditions.body2InitialPosition[0] << ","
        << initialConditions.body2InitialPosition[1] << ","
        << initialConditions.body2InitialPosition[2] << ","
        << initialConditions.body2InitialVelocity[0] << ","
        << initialConditions.body2InitialVelocity[1] << ","
        << initialConditions.body2InitialVelocity[2] << ","
        // Body 3 Initial Conditions
        << initialConditions.body3Name << ","
        << initialConditions.bodyMasses.at(2) << ","
        << initialConditions.bodyRadii.at(2) << ","
        << initialConditions.body3InitialPosition[0] << ","
        << initialConditions.body3InitialPosition[1] << ","
        << initialConditions.body3InitialPosition[2] << ","
        << initialConditions.body3InitialVelocity[0] << ","
        << initialConditions.body3InitialVelocity[1] << ","
        << initialConditions.body3InitialVelocity[2] << ","
        // Simulation Parameters
        << initialConditions.timeSpan << ","
        << initialConditions.timeStep << "\n";

    // Write simulation data
    for (size_t i = 1; i < rk4Solution.times.size(); ++i) {
        file << rk4Solution.times[i] << ","
            // Body 1 Position and Velocity
            << rk4Solution.body1Positions[i][0] << ","
            << rk4Solution.body1Positions[i][1] << ","
            << rk4Solution.body1Positions[i][2] << ","
            << rk4Solution.body1Velocities[i][0] << ","
            << rk4Solution.body1Velocities[i][1] << ","
            << rk4Solution.body1Velocities[i][2] << ","
            // Body 2 Position and Velocity
            << rk4Solution.body2Positions[i][0] << ","
            << rk4Solution.body2Positions[i][1] << ","
            << rk4Solution.body2Positions[i][2] << ","
            << rk4Solution.body2Velocities[i][0] << ","
            << rk4Solution.body2Velocities[i][1] << ","
            << rk4Solution.body2Velocities[i][2] << ","
            // Body 3 Position and Velocity
            << rk4Solution.body3Positions[i][0] << ","
            << rk4Solution.body3Positions[i][1] << ","
            << rk4Solution.body3Positions[i][2] << ","
            << rk4Solution.body3Velocities[i][0] << ","
            << rk4Solution.body3Velocities[i][1] << ","
            << rk4Solution.body3Velocities[i][2] << "\n";
    }
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 
// N-Body CSV Read Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 

// Reads N-body simulation data from a CSV file
bool CSVUtilities::readNBodySimDataCSV(const std::string& filepath,
        NBodyIC& initialConditions,
        NBodySolution& rk4Solution) {

    std::ifstream file(filepath);
    if (!file.is_open()) {
        std::cerr << "Error: Could not open file " << filepath << std::endl;
        return false;
    }

    std::string line;
    size_t numBodies = 0;
    double timeSpan = 0.0;
    double timeStep = 0.0;

    // Parse header comments to extract metadata
    while (std::getline(file, line) && line[0] == '#') {
        if (line.find("# N=") == 0) {
            numBodies = std::stoul(line.substr(4));
        } else if (line.find("# timeSpan=") == 0) {
            timeSpan = std::stod(line.substr(11));
        } else if (line.find("# timeStep=") == 0) {
            timeStep = std::stod(line.substr(11));
        } else if (line.find("# bodyNames=") == 0) {
            std::string namesStr = line.substr(12);
            std::stringstream ss(namesStr);
            std::string name;
            while (std::getline(ss, name, ',')) {
                initialConditions.bodyNames.push_back(name);
            }
        } else if (line.find("# bodyMasses=") == 0) {
            std::string massesStr = line.substr(13);
            std::stringstream ss(massesStr);
            std::string mass;
            while (std::getline(ss, mass, ',')) {
                initialConditions.bodyMasses.push_back(std::stod(mass));
            }
        } else if (line.find("# bodyRadii=") == 0) {
            std::string radiiStr = line.substr(12);
            std::stringstream ss(radiiStr);
            std::string radius;
            while (std::getline(ss, radius, ',')) {
                initialConditions.bodyRadii.push_back(std::stod(radius));
            }
        }
    }

    if (numBodies == 0) {
        std::cerr << "Error: Could not parse N (number of bodies) from CSV header" << std::endl;
        return false;
    }

    // Set simulation parameters
    initialConditions.timeSpan = timeSpan;
    initialConditions.timeStep = timeStep;
    rk4Solution.numBodies = numBodies;

    // Skip column header line (already read in the while loop above)
    // The 'line' variable now contains the column header

    // Read simulation data rows
    bool isFirstRow = true;
    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::string value;
        std::vector<double> rowValues;

        while (std::getline(ss, value, ',')) {
            rowValues.push_back(std::stod(value));
        }

        // Expected columns: time, x0,y0,z0, ..., xN-1,yN-1,zN-1, vx0,vy0,vz0, ..., vxN-1,vyN-1,vzN-1
        // Total: 1 + 3*N + 3*N = 1 + 6*N
        if (rowValues.size() < 1 + 6 * numBodies) {
            std::cerr << "Error: Row has insufficient columns" << std::endl;
            continue;
        }

        rk4Solution.times.push_back(rowValues[0]);

        std::vector<double> positions(3 * numBodies);
        std::vector<double> velocities(3 * numBodies);

        for (size_t i = 0; i < numBodies; ++i) {
            // Positions: columns 1 + 3*i, 1 + 3*i + 1, 1 + 3*i + 2
            positions[3 * i + 0] = rowValues[1 + 3 * i + 0];
            positions[3 * i + 1] = rowValues[1 + 3 * i + 1];
            positions[3 * i + 2] = rowValues[1 + 3 * i + 2];

            // Velocities: columns 1 + 3*N + 3*i, ...
            velocities[3 * i + 0] = rowValues[1 + 3 * numBodies + 3 * i + 0];
            velocities[3 * i + 1] = rowValues[1 + 3 * numBodies + 3 * i + 1];
            velocities[3 * i + 2] = rowValues[1 + 3 * numBodies + 3 * i + 2];
        }

        rk4Solution.positions.push_back(positions);
        rk4Solution.velocities.push_back(velocities);

        // Extract initial conditions from first row
        if (isFirstRow) {
            initialConditions.initTime = rowValues[0];
            initialConditions.initialPositions = positions;
            initialConditions.initialVelocities = velocities;
            isFirstRow = false;
        }
    }

    file.close();
    return true;
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 
// N-Body CSV Write Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 

// Writes N-body simulation data to a CSV file
void CSVUtilities::writeNBodySimDataCSV(const NBodyIC& initialConditions, 
        const NBodySolution& rk4Solution, 
        const std::string& directory) {

    // Create directory if it doesn't exist
    SystemUtilities::createDirectory(directory);
    std::string filePath = makeCSVPath(directory, UniversalConstants::nBodyFile);
    std::ofstream file(filePath);

    // Cannot open file
    if (!file.is_open()) {
        std::cerr << "Error: Could not open file " << filePath << std::endl;
        return;
    }

    size_t N = rk4Solution.numBodies;

    // Write header comments with metadata
    file << "# type=NBodySimData\n";
    file << "# N=" << N << "\n";
    file << "# timeSpan=" << initialConditions.timeSpan << "\n";
    file << "# timeStep=" << initialConditions.timeStep << "\n";

    // Write body names
    file << "# bodyNames=";
    for (size_t i = 0; i < N; ++i) {
        if (i > 0) file << ",";
        if (i < initialConditions.bodyNames.size()) {
            file << initialConditions.bodyNames[i];
        } else {
            file << "Body" << i;
        }
    }
    file << "\n";

    // Write body masses
    file << "# bodyMasses=";
    for (size_t i = 0; i < N; ++i) {
        if (i > 0) file << ",";
        file << initialConditions.bodyMasses[i];
    }
    file << "\n";

    // Write body radii
    file << "# bodyRadii=";
    for (size_t i = 0; i < N; ++i) {
        if (i > 0) file << ",";
        file << initialConditions.bodyRadii[i];
    }
    file << "\n";

    // Write column header
    file << UniversalConstants::nBodyRK4Times;

    // Position columns: x0,y0,z0, x1,y1,z1, ..., xN-1,yN-1,zN-1
    for (size_t i = 0; i < N; ++i) {
        file << ",x" << i << ",y" << i << ",z" << i;
    }

    // Velocity columns: vx0,vy0,vz0, vx1,vy1,vz1, ..., vxN-1,vyN-1,vzN-1
    for (size_t i = 0; i < N; ++i) {
        file << ",vx" << i << ",vy" << i << ",vz" << i;
    }
    file << "\n";

    // Write simulation data
    for (size_t t = 0; t < rk4Solution.times.size(); ++t) {
        file << rk4Solution.times[t];

        // Write positions for all bodies
        for (size_t i = 0; i < N; ++i) {
            file << "," << rk4Solution.positions[t][3 * i + 0]
                 << "," << rk4Solution.positions[t][3 * i + 1]
                 << "," << rk4Solution.positions[t][3 * i + 2];
        }

        // Write velocities for all bodies
        for (size_t i = 0; i < N; ++i) {
            file << "," << rk4Solution.velocities[t][3 * i + 0]
                 << "," << rk4Solution.velocities[t][3 * i + 1]
                 << "," << rk4Solution.velocities[t][3 * i + 2];
        }

        file << "\n";
    }

    file.close();
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
//                                                                               PYTHON UTILITIES
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PUBLIC METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 
// Python Interaction Utilities
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 

// Uses Python Inquirer to present a list of options and get user selection
std::string PythonUtilities::pythonInquirer(std::vector<std::string> options, const std::string& prompt) {
    // Create a temporary Python script
    std::string scriptPath = "temp_inquirer.py";
    std::ofstream scriptFile(scriptPath);
    
    scriptFile << "import inquirer\n\n";
    scriptFile << "questions = [\n";
    scriptFile << "    inquirer.List('selection',\n";
    scriptFile << "                  message='" << prompt << "',\n";
    scriptFile << "                  choices=[\n";
    for (const auto& option : options) {
        scriptFile << "                      '" << option << "',\n";
    }
    scriptFile << "                  ],\n";
    scriptFile << "              ),\n";
    scriptFile << "]\n\n";
    scriptFile << "answers = inquirer.prompt(questions)\n";
    scriptFile << "# Write result to output file\n";
    scriptFile << "with open('temp_inquirer_output.txt', 'w') as f:\n";
    scriptFile << "    f.write(answers['selection'])\n";
    
    scriptFile.close();
    
    // Execute the Python script with system() to provide TTY access
    std::string command = "python3 " + scriptPath;
    int exitCode = system(command.c_str());
    
    if (exitCode != 0) {
        std::cerr << "Error: Python script failed with exit code " << exitCode << std::endl;
        std::remove(scriptPath.c_str());
        return "";
    }
    
    // Read result from output file
    std::string outputPath = "temp_inquirer_output.txt";
    std::ifstream outputFile(outputPath);
    std::string result;
    
    if (outputFile.is_open()) {
        std::getline(outputFile, result);
        outputFile.close();
    } else {
        std::cerr << "Error: Could not read output file." << std::endl;
    }
    
    // Clean up temporary files
    std::remove(scriptPath.c_str());
    std::remove(outputPath.c_str());
    
    return result;
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
//                                                                               SYSTEM UTILITIES
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PUBLIC METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 
// Generic System Utilities
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 

// Clears the terminal screen
void SystemUtilities::clearTerminal() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
    return;
}

// Gets the directory of the executable
std::string SystemUtilities::getExecutableDir() {
    #ifdef _WIN32
        char buffer[MAX_PATH];
        GetModuleFileNameA(NULL, buffer, MAX_PATH);
        std::filesystem::path exePath = std::filesystem::path(buffer);
        return exePath.parent_path().string();
    #elif __APPLE__
        return std::filesystem::current_path().string();
    #else
        std::filesystem::path exePath = std::filesystem::canonical("/proc/self/exe");
        return exePath.parent_path().string();
    #endif
}

// Generates a timestamp string in "YYYY-MM-DD_HH-MM-SS-microseconds" format
std::string SystemUtilities::timeStamp() {
    using namespace std::chrono;
    auto now = system_clock::now();
    auto secs = system_clock::to_time_t(now);
    auto us  = duration_cast<microseconds>(now.time_since_epoch()) % 1000000;
    std::ostringstream ss;
    ss << std::put_time(std::localtime(&secs), "%Y-%m-%d_%H-%M-%S");
    ss << '-' << std::setw(6) << std::setfill('0') << us.count();
    return ss.str();
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 
// File And Directory Utilities
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 

// Creates a directory at the specified path
void SystemUtilities::createDirectory(const std::string& path) {
    std::filesystem::path execDir = getExecutableDir();
    std::filesystem::path fullPath = execDir / path;
    
    try {
        std::filesystem::create_directories(fullPath);
    } catch (const std::filesystem::filesystem_error& e) {
        std::cerr << "Error creating directory: " << e.what() << std::endl;
    }
}

// Check if a file exists
bool SystemUtilities::fileExists(const std::string& path) {
    return std::filesystem::exists(path);
}

// Check if a directory exists
bool SystemUtilities::directoryExists(const std::string& path) {
    std::filesystem::path execDir = getExecutableDir();
    std::filesystem::path fullPath = execDir / path;
    return std::filesystem::exists(fullPath) && std::filesystem::is_directory(fullPath);
}

// List subdirectories in a directory (returns names only, not full paths)
std::vector<std::string> SystemUtilities::listSubdirectories(const std::string& directory) {
    std::vector<std::string> subdirs;
    std::filesystem::path execDir = getExecutableDir();
    std::filesystem::path fullPath = execDir / directory;
    
    if (!std::filesystem::exists(fullPath) || !std::filesystem::is_directory(fullPath)) {
        return subdirs;
    }
    
    try {
        for (const auto& entry : std::filesystem::directory_iterator(fullPath)) {
            if (entry.is_directory()) {
                subdirs.push_back(entry.path().filename().string());
            }
        }
    } catch (const std::filesystem::filesystem_error& e) {
        std::cerr << "Error listing subdirectories: " << e.what() << std::endl;
    }
    
    // Sort alphabetically
    std::sort(subdirs.begin(), subdirs.end());
    
    return subdirs;
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 
// Random Number Generation Utilities
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- 

// Generates a random double in [min, max]
double SystemUtilities::getRandomDouble(double min, double max) {
    static std::random_device randomSeed;
    static std::mt19937 gen(randomSeed());
    std::uniform_real_distribution<> dis(min, max);
    return dis(gen);
}

// Generates a random integer in [min, max]
int SystemUtilities::getRandomInt(int min, int max) {
    static std::random_device randomSeed;
    static std::mt19937 gen(randomSeed());
    std::uniform_int_distribution<> dis(min, max);
    return dis(gen);
}
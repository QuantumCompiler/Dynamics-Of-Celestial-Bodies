#pragma once
#include <algorithm>
#include <chrono>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <random>
#include <sstream>
#include <string>
#include <vector>
#include "constants.h"
#include "rk4.h"

// CSV Utilities Class
class CSVUtilities {
    public:
        // CSV file and directory utilities
        static bool checkForEmptyDirectory(const std::string& directory);
        static void copyCSVFiles(const std::string& sourceDir, const std::string& destDir);
        static void copyRandomCSVFiles(const std::string& sourceDir, const std::string& destDir, int numFiles);
        static void emptyDirectory(const std::string& directory);
        static std::vector<std::string> listCSVFiles(const std::string& directory);
        static std::string makeCSVPath(const std::string& directory, const std::string& fileNameBase);
        static void moveCSVFiles(const std::string& sourceDir, const std::string& destDir);

        // Single Body CSV read methods
        static bool readSingleBodySimDataCSV(const std::string& filepath,
            SingleBodyIC& initialConditions,
            SingleBodySolution& rk4Solution);
        static bool readSingleBodyModelDataCSV(const std::string& filepath,
            SingleBodyIC& initialConditions,
            SingleBodySolution& modelSolution);
        static bool readSingleBodyEvaluationDataCSV(const std::string& filepath,
            SingleBodyIC& initialConditions,
            SingleBodySolution& rk4Solution,
            SingleBodySolution& modelSolution);

        // Single Body CSV write methods
        static void writeSingleBodySimDataCSV(const SingleBodyIC& initialConditions, 
            const SingleBodySolution rk4Solution, 
            const std::string& directory);
        static void writeSingleBodyModelDataCSV(const SingleBodyIC& initialConditions, 
            const SingleBodySolution& mlSolution, 
            const std::string& directory);
        static void writeSingleBodyEvaluationDataCSV(const SingleBodyIC& initialConditions, 
            const SingleBodySolution& rk4Solution, 
            const SingleBodySolution& mlSolution, 
            const std::string& directory);

        // Two body CSV read methods
        static bool readTwoBodySimDataCSV(const std::string& filepath,
            TwoBodyIC& initialConditions,
            TwoBodySolution& rk4Solution);

        // Two body CSV write methods
        static void writeTwoBodySimDataCSV(const TwoBodyIC& initialConditions, 
            const TwoBodySolution& rk4Solution, 
            const std::string& directory);

        // Three body CSV read methods
        static bool readThreeBodySimDataCSV(const std::string& filepath,
            ThreeBodyIC& initialConditions,
            ThreeBodySolution& rk4Solution);

        // Three body CSV write methods
        static void writeThreeBodySimDataCSV(const ThreeBodyIC& initialConditions, 
            const ThreeBodySolution& rk4Solution, 
            const std::string& directory);

        // N-body CSV read methods
        static bool readNBodySimDataCSV(const std::string& filepath,
            NBodyIC& initialConditions,
            NBodySolution& rk4Solution);

        // N-body CSV write methods
        static void writeNBodySimDataCSV(const NBodyIC& initialConditions, 
            const NBodySolution& rk4Solution, 
            const std::string& directory);
};

// Python Utilities Class
class PythonUtilities {
    public:
        // Python interaction utilities
        static std::string pythonInquirer(std::vector<std::string> options, const std::string& prompt);
};

// System Utilities Class
class SystemUtilities {
    public:
        // Generic system utilities
        static void clearTerminal();
        static std::string getExecutableDir();
        static std::string timeStamp();

        // File and directory utilities
        static void createDirectory(const std::string& path);
        static bool fileExists(const std::string& path);
        static bool directoryExists(const std::string& path);
        static std::vector<std::string> listSubdirectories(const std::string& directory);

        // Random number generation utilities
        static double getRandomDouble(double min, double max);
        static int getRandomInt(int min, int max);
};

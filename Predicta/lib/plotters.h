#pragma once
#include <Python.h>
#include <matplotlibcpp.h>
#include <vector>
#include <string>
#include <optional>
#include <iomanip>
#include <sstream>
#include "models.h"

namespace plt = matplotlibcpp;

// Plot parameters struct
struct SingleBodyPlotParameters {
    std::string xlabel;
    std::string ylabel;
    std::string title;
    std::string method;
    std::vector<double> xData;
    std::vector<double> yData;
};

// Two Body plot parameters struct
struct TwoBodyPlotParameters {
    std::string xlabel;
    std::string ylabel;
    std::string title;
    std::string method;
    std::vector<double> xData;
    std::vector<std::array<double, 3>> body1Data;
    std::vector<std::array<double, 3>> body2Data;
    bool isPos;
};

// Three Body plot parameters struct
struct ThreeBodyPlotParameters {
    std::string xlabel;
    std::string ylabel;
    std::string title;
    std::string method;
    std::vector<double> xData;
    std::vector<std::array<double, 3>> body1Data;
    std::vector<std::array<double, 3>> body2Data;
    std::vector<std::array<double, 3>> body3Data;
    bool isPos;
};

// N-Body plot parameters struct
struct NBodyPlotParameters {
    std::string xlabel;
    std::string ylabel;
    std::string title;
    std::string method;
    std::vector<double> xData;                              
    std::vector<std::vector<std::array<double, 3>>> bodyData;
    bool isPos;                                             
    std::optional<std::vector<std::string>> bodyLabels;
};

class Plotters {
    public:
        // Single Body plotting methods
        static void singleBodyPlot(const SingleBodyIC& initialConditions, const SingleBodyPlotParameters& params);
        static void singleBodyEvaluationPlot(const SingleBodyIC& initialConditions, const SingleBodyPlotParameters& rk4Params, const SingleBodyPlotParameters& modelParams);

        // Two Body plotting methods
        static void twoBodyPlot(const TwoBodyIC& initialConditions, const TwoBodyPlotParameters& params);

        // Three Body plotting methods
        static void threeBodyPlot(const ThreeBodyIC& initialConditions, const ThreeBodyPlotParameters& params);

        // N-Body plotting methods
        static void nBodyPlot(const NBodyIC& initialConditions, const NBodyPlotParameters& params);
        static void nBodyEvaluationPlot(const NBodyIC& initialConditions,
            const NBodyPlotParameters& rk4Params,
            const NBodyPlotParameters& modelParams);
};

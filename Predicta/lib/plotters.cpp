#include "plotters.h"

// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// PUBLIC METHODS
// ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// Single Body Plotting Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Single Body Plotting Method
void Plotters::singleBodyPlot(
    const SingleBodyIC& initialConditions,
    const SingleBodyPlotParameters& params
) {
    // Create figure
    plt::figure_size(1000, 600);
    
    // Plot the data
    plt::plot(params.xData, params.yData);
    
    // Set title with body name
    std::string fullTitle = params.title + " (" + initialConditions.bodyName + ")";
    plt::title(fullTitle);
    
    // Set axis labels
    plt::xlabel(params.xlabel);
    plt::ylabel(params.ylabel);
    
    // Build and display metadata text boxes
    std::string pythonCmd = "import matplotlib.pyplot as plt\n";
    
    // Build body info text box
    std::ostringstream bodyInfo;
    bodyInfo << "Body: " << initialConditions.bodyName << "\\n";
    bodyInfo << "Mass: " << std::scientific << std::setprecision(2) << initialConditions.bodyMass << " kg\\n";
    bodyInfo << "Radius: " << std::scientific << std::setprecision(2) << initialConditions.bodyRadius << " m";
    
    pythonCmd += "plt.gca().text(0.02, 0.98, '" + bodyInfo.str() + 
                "', transform=plt.gca().transAxes, fontsize=9, " +
                "verticalalignment='top', horizontalalignment='left', " +
                "bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))\n";
    
    // Build projectile info text box
    std::ostringstream projInfo;
    projInfo << "Initial Position: " << std::scientific << std::setprecision(2) << initialConditions.initialPosition << " m\\n";
    projInfo << "Initial Velocity: " << std::scientific << std::setprecision(2) << initialConditions.initialVelocity << " m/s";
    
    pythonCmd += "plt.gca().text(0.98, 0.98, '" + projInfo.str() + 
                "', transform=plt.gca().transAxes, fontsize=9, " +
                "verticalalignment='top', horizontalalignment='right', " +
                "bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))\n";
    
    // Build method info text box
    std::ostringstream methodInfo;
    methodInfo << "Method: " << params.method << "\\n";
    methodInfo << "Time Steps: " << params.xData.size() << "\\n";
    methodInfo << "Time Step: " << std::scientific << std::setprecision(2) << initialConditions.timeStep << " s";
    
    pythonCmd += "plt.gca().text(0.02, 0.02, '" + methodInfo.str() + 
                "', transform=plt.gca().transAxes, fontsize=9, " +
                "verticalalignment='bottom', horizontalalignment='left', " +
                "bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))\n";
    
    // Execute Python commands
    PyRun_SimpleString(pythonCmd.c_str());
    PyRun_SimpleString("plt.tight_layout()");
    
    // Show the plot
    plt::show();
}

// Single Body Evaluation Plotting Method
void Plotters::singleBodyEvaluationPlot(const SingleBodyIC& initialConditions, const SingleBodyPlotParameters& rk4Params, const SingleBodyPlotParameters& modelParams) 
{
    // Create figure
    plt::figure_size(1200, 700);
    
    // Plot both solutions
    plt::named_plot("RK4", rk4Params.xData, rk4Params.yData, "blue");
    plt::named_plot("ML Model", modelParams.xData, modelParams.yData, "red");
    
    // Set title with body name
    std::string fullTitle = rk4Params.title + " (" + initialConditions.bodyName + ")";
    plt::title(fullTitle);
    
    // Set axis labels
    plt::xlabel(rk4Params.xlabel);
    plt::ylabel(rk4Params.ylabel);
    plt::legend();
    
    // Build and display metadata text boxes
    std::string pythonCmd = "import matplotlib.pyplot as plt\n";
    
    // Build body info text box
    std::ostringstream bodyInfo;
    bodyInfo << "Body: " << initialConditions.bodyName << "\\n";
    bodyInfo << "Mass: " << std::scientific << std::setprecision(2) << initialConditions.bodyMass << " kg\\n";
    bodyInfo << "Radius: " << std::scientific << std::setprecision(2) << initialConditions.bodyRadius << " m";
    
    pythonCmd += "plt.gca().text(0.02, 0.98, '" + bodyInfo.str() + 
                "', transform=plt.gca().transAxes, fontsize=9, " +
                "verticalalignment='top', horizontalalignment='left', " +
                "bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))\n";
    
    // Build projectile info text box
    std::ostringstream projInfo;
    projInfo << "Initial Position: " << std::scientific << std::setprecision(2) << initialConditions.initialPosition << " m\\n";
    projInfo << "Initial Velocity: " << std::scientific << std::setprecision(2) << initialConditions.initialVelocity << " m/s";
    
    pythonCmd += "plt.gca().text(0.98, 0.98, '" + projInfo.str() + 
                "', transform=plt.gca().transAxes, fontsize=9, " +
                "verticalalignment='top', horizontalalignment='right', " +
                "bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))\n";
    
    // Build comparison info text box
    std::ostringstream compInfo;
    compInfo << "RK4 Steps: " << rk4Params.xData.size() << "\\n";
    compInfo << "Model Steps: " << modelParams.xData.size() << "\\n";
    compInfo << "Time Step: " << std::scientific << std::setprecision(2) << initialConditions.timeStep << " s";
    
    pythonCmd += "plt.gca().text(0.02, 0.02, '" + compInfo.str() + 
                "', transform=plt.gca().transAxes, fontsize=9, " +
                "verticalalignment='bottom', horizontalalignment='left', " +
                "bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))\n";
    
    // Execute Python commands
    PyRun_SimpleString(pythonCmd.c_str());
    PyRun_SimpleString("plt.tight_layout()");
    
    // Show the plot
    plt::show();
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// Two Body Plotting Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Two Body Plotting Method
void Plotters::twoBodyPlot(const TwoBodyIC& initialConditions, const TwoBodyPlotParameters& params) 
{
    // Create figure
    plt::figure_size(1000, 600);
    
    // Extract x, y, z components for each body
    std::vector<double> b1x, b1y, b1z, b2x, b2y, b2z;
    const auto& b1Data = params.body1Data;
    const auto& b2Data = params.body2Data;
    
    for (size_t i = 0; i < b1Data.size(); ++i) {
        b1x.push_back(b1Data[i][0]);
        b1y.push_back(b1Data[i][1]);
        b1z.push_back(b1Data[i][2]);
    }
    for (size_t i = 0; i < b2Data.size(); ++i) {
        b2x.push_back(b2Data[i][0]);
        b2y.push_back(b2Data[i][1]);
        b2z.push_back(b2Data[i][2]);
    }
    
    if (params.isPos) {
        // Position plot: X vs Y (orbital plot)
        plt::named_plot(initialConditions.body1Name, b1x, b1y, "b-");
        plt::named_plot(initialConditions.body2Name, b2x, b2y, "r-");
    } else {
        // Velocity plot: velocity components vs time
        plt::named_plot(initialConditions.body1Name + " X", params.xData, b1x, "b-");
        plt::named_plot(initialConditions.body1Name + " Y", params.xData, b1y, "b--");
        plt::named_plot(initialConditions.body1Name + " Z", params.xData, b1z, "b:");
        plt::named_plot(initialConditions.body2Name + " X", params.xData, b2x, "r-");
        plt::named_plot(initialConditions.body2Name + " Y", params.xData, b2y, "r--");
        plt::named_plot(initialConditions.body2Name + " Z", params.xData, b2z, "r:");
    }
    
    // Set title
    plt::title(params.title);
    
    // Set axis labels
    plt::xlabel(params.xlabel);
    plt::ylabel(params.ylabel);
    plt::legend();
    
    // Build and display metadata text boxes
    std::string pythonCmd = "import matplotlib.pyplot as plt\n";
    pythonCmd += "import warnings\n";
    pythonCmd += "warnings.filterwarnings('ignore', message='Creating legend with loc=\"best\" can be slow')\n\n";
    
    // Build body info text box
    std::ostringstream bodyInfo;
    bodyInfo << "Body 1: " << initialConditions.body1Name << "\\n";
    bodyInfo << "Mass: " << std::scientific << std::setprecision(2) << initialConditions.bodyMasses[0] << " kg\\n";
    bodyInfo << "Radius: " << std::scientific << std::setprecision(2) << initialConditions.bodyRadii[0] << " m\\n\\n";
    bodyInfo << "Body 2: " << initialConditions.body2Name << "\\n";
    bodyInfo << "Mass: " << std::scientific << std::setprecision(2) << initialConditions.bodyMasses[1] << " kg\\n";
    bodyInfo << "Radius: " << std::scientific << std::setprecision(2) << initialConditions.bodyRadii[1] << " m";

    pythonCmd += "plt.gca().text(0.02, 0.98, '" + bodyInfo.str() + 
                "', transform=plt.gca().transAxes, fontsize=9, " +
                "verticalalignment='top', horizontalalignment='left', " +
                "bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))\n";

    // Build method info text box
    std::ostringstream methodInfo;
    methodInfo << "Method: " << params.method << "\\n";
    methodInfo << "Time Steps: " << params.xData.size() << "\\n";
    methodInfo << "Time Step: " << std::scientific << std::setprecision(2) << initialConditions.timeStep << " s";

    pythonCmd += "plt.gca().text(0.02, 0.02, '" + methodInfo.str() + 
                "', transform=plt.gca().transAxes, fontsize=9, " +
                "verticalalignment='bottom', horizontalalignment='left', " +
                "bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))\n";

    // Execute Python commands
    PyRun_SimpleString(pythonCmd.c_str());
    PyRun_SimpleString("plt.tight_layout()");

    // Show the plot
    plt::show();
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// Three Body Plotting Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// Three Body Plotting Method
void Plotters::threeBodyPlot(const ThreeBodyIC& initialConditions, const ThreeBodyPlotParameters& params) 
{
    // Create figure
    plt::figure_size(1000, 600);
    
    // Extract x, y, z components for each body
    std::vector<double> b1x, b1y, b1z, b2x, b2y, b2z, b3x, b3y, b3z;
    const auto& b1Data = params.body1Data;
    const auto& b2Data = params.body2Data;
    const auto& b3Data = params.body3Data;
    
    for (size_t i = 0; i < b1Data.size(); ++i) {
        b1x.push_back(b1Data[i][0]);
        b1y.push_back(b1Data[i][1]);
        b1z.push_back(b1Data[i][2]);
    }
    for (size_t i = 0; i < b2Data.size(); ++i) {
        b2x.push_back(b2Data[i][0]);
        b2y.push_back(b2Data[i][1]);
        b2z.push_back(b2Data[i][2]);
    }
    for (size_t i = 0; i < b3Data.size(); ++i) {
        b3x.push_back(b3Data[i][0]);
        b3y.push_back(b3Data[i][1]);
        b3z.push_back(b3Data[i][2]);
    }
    
    if (params.isPos) {
        // Position plot: X vs Y (orbital plot)
        plt::named_plot(initialConditions.body1Name, b1x, b1y, "b-");
        plt::named_plot(initialConditions.body2Name, b2x, b2y, "g-");
        plt::named_plot(initialConditions.body3Name, b3x, b3y, "r-");
    } else {
        // Velocity plot: velocity components vs time
        plt::named_plot(initialConditions.body1Name + " X", params.xData, b1x, "b-");
        plt::named_plot(initialConditions.body1Name + " Y", params.xData, b1y, "b--");
        plt::named_plot(initialConditions.body1Name + " Z", params.xData, b1z, "b:");
        plt::named_plot(initialConditions.body2Name + " X", params.xData, b2x, "g-");
        plt::named_plot(initialConditions.body2Name + " Y", params.xData, b2y, "g--");
        plt::named_plot(initialConditions.body2Name + " Z", params.xData, b2z, "g:");
        plt::named_plot(initialConditions.body3Name + " X", params.xData, b3x, "r-");
        plt::named_plot(initialConditions.body3Name + " Y", params.xData, b3y, "r--");
        plt::named_plot(initialConditions.body3Name + " Z", params.xData, b3z, "r:");
    }
    
    // Set title
    plt::title(params.title);
    
    // Set axis labels
    plt::xlabel(params.xlabel);
    plt::ylabel(params.ylabel);
    plt::legend();
    
    // Build and display metadata text boxes
    std::string pythonCmd = "import matplotlib.pyplot as plt\n";
    pythonCmd += "import warnings\n";
    pythonCmd += "warnings.filterwarnings('ignore', message='Creating legend with loc=\"best\" can be slow')\n\n";
    
    // Build body info text box
    std::ostringstream bodyInfo;
    bodyInfo << "Body 1: " << initialConditions.body1Name << "\\n";
    bodyInfo << "Mass: " << std::scientific << std::setprecision(2) << initialConditions.bodyMasses[0] << " kg\\n";
    bodyInfo << "Radius: " << std::scientific << std::setprecision(2) << initialConditions.bodyRadii[0] << " m\\n\\n";
    bodyInfo << "Body 2: " << initialConditions.body2Name << "\\n";
    bodyInfo << "Mass: " << std::scientific << std::setprecision(2) << initialConditions.bodyMasses[1] << " kg\\n";
    bodyInfo << "Radius: " << std::scientific << std::setprecision(2) << initialConditions.bodyRadii[1] << " m\\n\\n";
    bodyInfo << "Body 3: " << initialConditions.body3Name << "\\n";
    bodyInfo << "Mass: " << std::scientific << std::setprecision(2) << initialConditions.bodyMasses[2] << " kg\\n";
    bodyInfo << "Radius: " << std::scientific << std::setprecision(2) << initialConditions.bodyRadii[2] << " m";

    pythonCmd += "plt.gca().text(0.02, 0.98, '" + bodyInfo.str() + 
                "', transform=plt.gca().transAxes, fontsize=9, " +
                "verticalalignment='top', horizontalalignment='left', " +
                "bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))\n";

    // Build method info text box
    std::ostringstream methodInfo;
    methodInfo << "Method: " << params.method << "\\n";
    methodInfo << "Time Steps: " << params.xData.size() << "\\n";
    methodInfo << "Time Step: " << std::scientific << std::setprecision(2) << initialConditions.timeStep << " s";

    pythonCmd += "plt.gca().text(0.02, 0.02, '" + methodInfo.str() + 
                "', transform=plt.gca().transAxes, fontsize=9, " +
                "verticalalignment='bottom', horizontalalignment='left', " +
                "bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))\n";

    // Execute Python commands
    PyRun_SimpleString(pythonCmd.c_str());
    PyRun_SimpleString("plt.tight_layout()");

    // Show the plot
    plt::show();
}

// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
// N-Body Plotting Methods
// ----- ----- ----- ----- ----- ----- ----- ----- ----- -----

// N-Body Plotting Method
void Plotters::nBodyPlot(const NBodyIC& initialConditions, const NBodyPlotParameters& params)
{
    size_t N = initialConditions.bodyMasses.size();

    // Validate params.bodyData.size() == N
    if (params.bodyData.size() != N) {
        std::cerr << "Error: bodyData size (" << params.bodyData.size() 
                << ") does not match number of bodies (" << N << ")" << std::endl;
        return;
    }

    // Validate each bodyData[i].size() == params.xData.size()
    for (size_t i = 0; i < N; ++i) {
        if (params.bodyData[i].size() != params.xData.size()) {
            std::cerr << "Error: bodyData[" << i << "] size (" << params.bodyData[i].size()
                    << ") does not match xData size (" << params.xData.size() << ")" << std::endl;
            return;
        }
    }

    // Create figure
    plt::figure_size(1000, 600);

    // Define color palette for bodies
    std::vector<std::string> colors = {"b", "g", "r", "c", "m", "y", "k"};

    // Extract and plot data for each body
    for (size_t i = 0; i < N; ++i) {
        std::vector<double> bx, by, bz;
        for (size_t t = 0; t < params.bodyData[i].size(); ++t) {
            bx.push_back(params.bodyData[i][t][0]);
            by.push_back(params.bodyData[i][t][1]);
            bz.push_back(params.bodyData[i][t][2]);
        }

        // Determine label for this body
        std::string label;
        if (params.bodyLabels.has_value() && i < params.bodyLabels->size()) {
            label = (*params.bodyLabels)[i];
        } else if (i < initialConditions.bodyNames.size()) {
            label = initialConditions.bodyNames[i];
        } else {
            label = "Body " + std::to_string(i);
        }

        std::string color = colors[i % colors.size()];

        if (params.isPos) {
            // Position plot: X vs Y (orbital plot)
            plt::named_plot(label, bx, by, color + "-");
        } else {
            // Velocity plot: velocity components vs time
            plt::named_plot(label + " X", params.xData, bx, color + "-");
            plt::named_plot(label + " Y", params.xData, by, color + "--");
            plt::named_plot(label + " Z", params.xData, bz, color + ":");
        }
    }

    // Set title
    plt::title(params.title);

    // Set axis labels
    plt::xlabel(params.xlabel);
    plt::ylabel(params.ylabel);
    plt::legend();
    plt::grid(false);

    // Build and display metadata text boxes
    std::string pythonCmd = "import matplotlib.pyplot as plt\n";
    pythonCmd += "import warnings\n";
    pythonCmd += "warnings.filterwarnings('ignore', message='Creating legend with loc=\"best\" can be slow')\n\n";

    // Build method info text box
    std::ostringstream methodInfo;
    methodInfo << "Method: " << params.method << "\\n";
    methodInfo << "Time Steps: " << params.xData.size() << "\\n";
    methodInfo << "Time Step: " << std::scientific << std::setprecision(2) << initialConditions.timeStep << " s";

    pythonCmd += "plt.gca().text(0.02, 0.02, '" + methodInfo.str() + 
                "', transform=plt.gca().transAxes, fontsize=9, " +
                "verticalalignment='bottom', horizontalalignment='left', " +
                "bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))\n";

    // Execute Python commands
    PyRun_SimpleString(pythonCmd.c_str());
    PyRun_SimpleString("plt.tight_layout()");

    // Show the plot
    plt::show();
}

// N-Body Evaluation Plotting Method
void Plotters::nBodyEvaluationPlot(const NBodyIC& initialConditions,
        const NBodyPlotParameters& rk4Params,
        const NBodyPlotParameters& modelParams)
{
    size_t N = initialConditions.bodyMasses.size();

    // Validate both param structs have the same N
    if (rk4Params.bodyData.size() != N || modelParams.bodyData.size() != N) {
        std::cerr << "Error: bodyData sizes do not match number of bodies (" << N << ")" << std::endl;
        return;
    }

    // Validate xData sizes match
    if (rk4Params.xData.size() != modelParams.xData.size()) {
        std::cerr << "Error: RK4 xData size (" << rk4Params.xData.size()
                << ") does not match Model xData size (" << modelParams.xData.size() << ")" << std::endl;
        return;
    }

    // Create figure
    plt::figure_size(1200, 700);

    // Define color palette for bodies
    std::vector<std::string> colors = {"b", "g", "r", "c", "m", "y", "k"};

    // Plot data for each body (RK4 solid, Model dashed)
    for (size_t i = 0; i < N; ++i) {
        std::vector<double> rk4_bx, rk4_by, model_bx, model_by;
        for (size_t t = 0; t < rk4Params.bodyData[i].size(); ++t) {
            rk4_bx.push_back(rk4Params.bodyData[i][t][0]);
            rk4_by.push_back(rk4Params.bodyData[i][t][1]);
        }
        for (size_t t = 0; t < modelParams.bodyData[i].size(); ++t) {
            model_bx.push_back(modelParams.bodyData[i][t][0]);
            model_by.push_back(modelParams.bodyData[i][t][1]);
        }

        // Determine label for this body
        std::string label;
        if (rk4Params.bodyLabels.has_value() && i < rk4Params.bodyLabels->size()) {
            label = (*rk4Params.bodyLabels)[i];
        } else if (i < initialConditions.bodyNames.size()) {
            label = initialConditions.bodyNames[i];
        } else {
            label = "Body " + std::to_string(i);
        }

        std::string color = colors[i % colors.size()];

        if (rk4Params.isPos) {
            // Position plot: X vs Y (orbital plot)
            plt::named_plot(label + " (RK4)", rk4_bx, rk4_by, color + "-");
            plt::named_plot(label + " (Model)", model_bx, model_by, color + "--");
        } else {
            // Velocity plot: velocity X component vs time
            plt::named_plot(label + " (RK4)", rk4Params.xData, rk4_bx, color + "-");
            plt::named_plot(label + " (Model)", modelParams.xData, model_bx, color + "--");
        }
    }

    // Set title
    std::string fullTitle = rk4Params.title + " - RK4 vs Model Comparison";
    plt::title(fullTitle);

    // Set axis labels
    plt::xlabel(rk4Params.xlabel);
    plt::ylabel(rk4Params.ylabel);
    plt::legend();
    plt::grid(false);

    // Build and display metadata text boxes
    std::string pythonCmd = "import matplotlib.pyplot as plt\n";
    pythonCmd += "import warnings\n";
    pythonCmd += "warnings.filterwarnings('ignore', message='Creating legend with loc=\"best\" can be slow')\n\n";

    // Build body info text box
    std::ostringstream bodyInfo;
    bodyInfo << "N = " << N << " Bodies\\n";
    for (size_t i = 0; i < std::min(N, size_t(3)); ++i) {
        std::string name = (i < initialConditions.bodyNames.size()) 
            ? initialConditions.bodyNames[i] : "Body " + std::to_string(i);
        bodyInfo << name << ": " << std::scientific << std::setprecision(2) 
                << initialConditions.bodyMasses[i] << " kg\\n";
    }
    if (N > 3) {
        bodyInfo << "... (" << (N - 3) << " more)";
    }

    pythonCmd += "plt.gca().text(0.02, 0.98, '" + bodyInfo.str() + 
                "', transform=plt.gca().transAxes, fontsize=9, " +
                "verticalalignment='top', horizontalalignment='left', " +
                "bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))\n";

    // Build comparison info text box
    std::ostringstream compInfo;
    compInfo << "RK4 Steps: " << rk4Params.xData.size() << "\\n";
    compInfo << "Model Steps: " << modelParams.xData.size() << "\\n";
    compInfo << "Time Step: " << std::scientific << std::setprecision(2) << initialConditions.timeStep << " s";

    pythonCmd += "plt.gca().text(0.02, 0.02, '" + compInfo.str() + 
                "', transform=plt.gca().transAxes, fontsize=9, " +
                "verticalalignment='bottom', horizontalalignment='left', " +
                "bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))\n";

    // Execute Python commands
    PyRun_SimpleString(pythonCmd.c_str());
    PyRun_SimpleString("plt.tight_layout()");

    // Show the plot
    plt::show();
}
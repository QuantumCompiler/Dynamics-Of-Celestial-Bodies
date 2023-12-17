from ModelFunctions import *

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### Canvas / Plot Window
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

""" ProjectileMotionCanvas - Class for projectile motion plots
    Member Functions:
        Constructor - Constructor for canvas with specific input parameters
        Plot - Plots the results from a projectile motion scenario
"""
class ProjectileMotionCanvas(FigureCanvasQTAgg):
    """ Constructor - Constructor for canvas with specific input parameters
        Input:
            parent - Parent class
            width - Width of canvas
            height - Height of canvas
            dpi - DPI of canvas
        Algorithm:
            * Create a figure with the width, height, and dpi from the input parameters
            * Create an axis and add it to the figure
            * Call the constructor for FigureCanvasQTAgg with the figure previously created
        Output:
            This function does not return a value
    """
    def __init__(self, parent=None, width=3, height=2, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvasQTAgg.__init__(self, fig)

    """ Plot - Plots the results from a projectile motion scenario
        Input:
            plotType - Integer that indicates the type of plot to be created
                0 - Position versus time 2D plot
                1 - Position versus time animation
                2 - Velocity versus time 2D plot
                3 - Velocity versus time animation
            obj - Array of values for a given object
                obj[0] - Mass of object in Kg
                obj[1] - Radius of object in m
            ic - Array of initial conditions for a projectile
                ic[0] - Initial vertical position in meters
                ic[1] - Initial vertical velocity in meters / second
            t0 - Initial time of model in seconds
            tn - Final time of model in seconds
            objName - Name of object
            projectileName - Name of projectile
        Algorithm:
            * Call the solver function for projectile motion
            * If the plotType is 0, plot the Position versus time 2D plot
                * Create the plot
                * Set the title, labels, and legend
                * Add the notes to the bottom of the plot
                * Draw the plot on the canvas
            * If the plotType is 1, plot the Position versus time animation
                * Create an array for the point and trail of the plot
                * Set the minimum and maximum for the axes in the plot
                * Create the initialize inner function
                * Create the animate inner function
                * Call the animation for the canvas
                * Set the title, labels, and legend
                * Add the notes to the bottom of the plot
                * Draw the animation on the canvas
            * If the plotType is 2, plot the Velocity versus time 2D plot
                * Create the plot
                * Set the title, labels, and legend
                * Add the notes to the bottom of the plot
                * Draw the plot on the canvas
            * If the plotType is 3, plot the Velocity versus time animation
                * Create an array for the point and trail of the plot
                * Set the minimum and maximum for the axes in the plot
                * Create the initialize inner function
                * Create the animate inner function
                * Call the animation for the canvas
                * Set the title, labels, and legend
                * Add the notes to the bottom of the plot
                * Draw the animation on the canvas
        Output:
            This function does not return a value
    """
    def Plot(self, plotType, obj, ic, t0, tn, objName, projectileName):
        # Call solver
        position, velocity, time = ProjectileMotionSolver(obj, ic, t0, tn)
        # Position Plot
        if (plotType == 0):
            # Clear axes
            self.axes.clear()
            # Plot
            self.axes.plot(time, position, '-', color = 'green', linewidth = 1, label = projectileName)
            # Title, labels, legend
            self.axes.set_title(f"Projectile Motion Plot Of Position Under The Influence Of {objName}", fontsize = TWODPLOTTITLE)
            self.axes.set_xlabel(f"Time In Seconds (s)", fontsize = TWODPLOTABELS)
            self.axes.set_ylabel(f"Vertical Position In (m)", fontsize = TWODPLOTABELS)
            self.axes.legend()
            # Notes
            self.figure.subplots_adjust(bottom=0.35)
            objNotes = f"Object: {objName}, Mass = {obj[0]} $(Kg)$, Radius = {obj[1]} $(m)$"
            initNotes = f"Initial Conditions: {projectileName}, Initial Vertical Position = {ic[0]} $(m)$, Initial Vertical Velocity = {ic[1]} $(m/s)$"
            finalNotes = f"Final Conditions: {projectileName}, Final Vertical Position = {round(position[-1],2)} $(m)$, Final Vertical Velocity = {round(velocity[-1],2)} $(m/s)$"
            timeNotes = f"Simulation From {t0} $(s)$ to {tn} $(s)$"
            self.figure.text(0.1, 0.05, objNotes + "\n" + initNotes + "\n" + finalNotes + "\n" + timeNotes, ha='left', va='bottom', fontsize=TWODNOTES)
            # Draw plot on canvas
            self.draw()
        # Position animation
        if (plotType == 1):
            # Clear axes
            self.axes.clear()
            # Arrays for point and trail
            projectile, = self.axes.plot([], [], 'o', color='green', markersize=2, label=projectileName)
            projectileTrail, = self.axes.plot([], [], '-', color='green', linewidth=1, alpha=0.5)
            # Max and min of axes
            self.axes.set_xlim(min(time) - 0.05 * max(time), 1.05 * max(time))
            self.axes.set_ylim(min(position) - 0.05 * max(position), 1.05 * max(position))
            # Initialize function
            def init():
                projectile.set_data([], [])
                projectileTrail.set_data([], [])
                return projectile, projectileTrail
            # Animation function
            def animate(k):
                projectile.set_data([time[k], position[k]])
                projectileTrail.set_data(time[:k+1], position[:k+1])
                return projectile, projectileTrail
            # Animation
            self.ani = FuncAnimation(self.figure, animate, init_func=init, frames=len(time), interval=1e-5, blit=True, repeat=True)
            # Title, labels, legend
            self.axes.set_title(f"Projectile Motion Animation Of Position Under The Influence Of {objName}", fontsize = TWODANIMTITLE)
            self.axes.set_xlabel(f"Time In Seconds (s)", fontsize = TWODANIMLABELS)
            self.axes.set_ylabel(f"Vertical Position In (m)", fontsize = TWODANIMLABELS)
            self.axes.legend()
            # Notes
            self.figure.subplots_adjust(bottom=0.35)
            objNotes = f"Object: {objName}, Mass = {obj[0]} $(Kg)$, Radius = {obj[1]} $(m)$"
            initNotes = f"Initial Conditions: {projectileName}, Initial Vertical Position = {ic[0]} $(m)$, Initial Vertical Velocity = {ic[1]} $(m/s)$"
            finalNotes = f"Final Conditions: {projectileName}, Final Vertical Position = {round(position[-1],2)} $(m)$, Final Vertical Velocity = {round(velocity[-1],2)} $(m/s)$"
            timeNotes = f"Simulation From {t0} $(s)$ to {tn} $(s)$"
            self.figure.text(0.1, 0.05, objNotes + "\n" + initNotes + "\n" + finalNotes + "\n" + timeNotes, ha='left', va='bottom', fontsize=TWODNOTES)
            # Draw animation on canvas
            self.draw()
        # Velocity plot
        if (plotType == 2):
            # Clear axes
            self.axes.clear()
            # Plot
            self.axes.plot(time, velocity, '-', color = 'green', linewidth = 1, label = projectileName)
            # Title, labels, legend
            self.axes.set_title(f"Projectile Motion Plot Of Velocity Under The Influence Of {objName}", fontsize = TWODPLOTTITLE)
            self.axes.set_xlabel(f"Time In Seconds (s)", fontsize = TWODPLOTABELS)
            self.axes.set_ylabel(f"Vertical Velocity In $(\\frac{{m}}{{s}})$", fontsize = TWODPLOTABELS)
            self.axes.legend()
            # Notes
            self.figure.subplots_adjust(bottom=0.35)
            objNotes = f"Object: {objName}, Mass = {obj[0]} $(Kg)$, Radius = {obj[1]} $(m)$"
            initNotes = f"Initial Conditions: {projectileName}, Initial Vertical Position = {ic[0]} $(m)$, Initial Vertical Velocity = {ic[1]} $(m/s)$"
            finalNotes = f"Final Conditions: {projectileName}, Final Vertical Position = {round(position[-1],2)} $(m)$, Final Vertical Velocity = {round(velocity[-1],2)} $(m/s)$"
            timeNotes = f"Simulation From {t0} $(s)$ to {tn} $(s)$"
            self.figure.text(0.1, 0.05, objNotes + "\n" + initNotes + "\n" + finalNotes + "\n" + timeNotes, ha='left', va='bottom', fontsize=TWODNOTES)
            # Draw plot on canvas
            self.draw()
        # Velocity animation
        if (plotType == 3):
            # Clear axes
            self.axes.clear()
            # Arrays for point and trail
            projectile, = self.axes.plot([], [], 'o', color='green', markersize=2, label=projectileName)
            projectileTrail, = self.axes.plot([], [], '-', color='green', linewidth=1, alpha=0.5)
            # Max and min of axes
            self.axes.set_xlim(min(time) - 0.05 * max(time), 1.05 * max(time))
            if (max(velocity) <= 0):
                self.axes.set_ylim(min(velocity) - 0.05 * max(velocity), 0.05 * abs(min(velocity)))
            else:
                self.axes.set_ylim(min(velocity) - 0.05 * max(velocity), 1.05 * max(velocity))
            # Initialize function
            def init():
                projectile.set_data([], [])
                projectileTrail.set_data([], [])
                return projectile, projectileTrail
            # Animation function
            def animate(k):
                projectile.set_data([time[k], velocity[k]])
                projectileTrail.set_data(time[:k+1], velocity[:k+1])
                return projectile, projectileTrail
            # Animation
            self.ani = FuncAnimation(self.figure, animate, init_func=init, frames=len(time), interval=1e-5, blit=True, repeat=True)
            # Title, labels, legend
            self.axes.set_title(f"Projectile Motion Animation Of Velocity Under The Influence Of {objName}", fontsize = TWODANIMTITLE)
            self.axes.set_xlabel(f"Time In Seconds (s)", fontsize = TWODANIMLABELS)
            self.axes.set_ylabel(f"Vertical Velocity In $(\\frac{{m}}{{s}})$", fontsize = TWODPLOTABELS)
            self.axes.legend()
            # Notes
            self.figure.subplots_adjust(bottom=0.35)
            objNotes = f"Object: {objName}, Mass = {obj[0]} $(Kg)$, Radius = {obj[1]} $(m)$"
            initNotes = f"Initial Conditions: {projectileName}, Initial Vertical Position = {ic[0]} $(m)$, Initial Vertical Velocity = {ic[1]} $(m/s)$"
            finalNotes = f"Final Conditions: {projectileName}, Final Vertical Position = {round(position[-1],2)} $(m)$, Final Vertical Velocity = {round(velocity[-1],2)} $(m/s)$"
            timeNotes = f"Simulation From {t0} $(s)$ to {tn} $(s)$"
            self.figure.text(0.1, 0.05, objNotes + "\n" + initNotes + "\n" + finalNotes + "\n" + timeNotes, ha='left', va='bottom', fontsize=TWODNOTES)
            # Draw animation on canvas
            self.draw()

""" ProjectileMotionPlotWindow - Class for projectile motion plot windows
    Member Functions:
        Constructor - Creates windows with specific input parameters
        closeEvent - Deletes plot canvas when window is closed
"""
class ProjectileMotionPlotWindow(QWidget):
    """ Constructor - Creates windows with specific input parameters
        Input:
            plotType - Integer that indicates the type of plot to be created
                0 - Position versus time 2D plot
                1 - Position versus time animation
                2 - Velocity versus time 2D plot
                3 - Velocity versus time animation
            obj - Array of values for a given object
                obj[0] - Mass of object in Kg
                obj[1] - Radius of object in m
            ic - Array of initial conditions for a projectile
                ic[0] - Initial vertical position in meters
                ic[1] - Initial vertical velocity in meters / second
            t0 - Initial time of model in seconds
            tn - Final time of model in seconds
            objName - Name of object
            projectileName - Name of projectile
            windowTitle - Title for window
        Algorithm:
            * Set the title of the window
            * Set the sizes of the window
            * Create the layout for the window
            * Create the canvas for the plot for the specific plot type
            * Generate the toolbar for the canvas
            * Add the widgets to the layout
            * Set the layout
        Output:
            This function does not return a value
    """
    def __init__(self, plotType, obj, ic, t0, tn, objName, projectileName, windowTitle):
        super().__init__()
        # Window title
        self.setWindowTitle(windowTitle)
        # Window sizes
        self.resize(800,500)
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        # Layout
        self.layout = QVBoxLayout()
        # Canvas for plot
        self.plotCanvas = ProjectileMotionCanvas(self, width=3, height=2, dpi=100)
        self.plotCanvas.Plot(plotType, obj, ic, t0, tn, objName, projectileName)
        # Tool bar
        self.toolBar = NavigationToolbar(self.plotCanvas, self)
        # Widget layout addition
        self.layout.addWidget(self.plotCanvas)
        self.layout.addWidget(self.toolBar)
        # Set layout
        self.setLayout(self.layout)

    """ closeEvent - Deletes plot canvas when window is closed
        Input:
            event - Object for the close event
        Algorithm:
            * Check if the window has the attributes "plotCanvas" and "ani"
            * Stop the animation if the window has an animation in it
            * Call the close event method
        Output:
            This function does not return a value
    """
    def closeEvent(self, event):
        if hasattr(self, 'plotCanvas') and hasattr(self.plotCanvas, 'ani'):
            self.plotCanvas.ani.event_source.stop()
        super().closeEvent(event)

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### Simulation Window
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

# Object Names
projMotCommonObjectDD = "Common Object Dropdown"
projMotCommonObjInitPos = "Common Object Projectile Initial Position"
projMotCommonObjInitVel = "Common Object Projectile Initial Velocity"
projMotCommonObjInitTime = "Common Object Initial Time"
projMotCommonObjFinalTime = "Common Object Final Time"
projMotCommonObjClearParamBtn = "Clear Common Parameters"
projMotCommonObjRandBtn = "Randomize Common Parameters"
projMotCustomObjMass = "Custom Object Mass"
projMotCustomObjRadius = "Custom Object Radius"
projMotCustomObjInitPos = "Custom Object Projectile Initial Position"
projMotCustomObjInitVel = "Custom Object Projectile Initial Velocity"
projMotCustomObjInitTime = "Custom Object Initial Time"
projMotCustomObjFinalTime = "Custom Object Final Time"
projMotCustomObjClearParamBtn = "Clear Custom Parameters"
projMotCustomObjRandBtn = "Randomize Custom Parameters"
projMotPosPlotCheck = "2D Position Plot Checkbox"
projMotPosAniCheck = "2D Position Animation Checkbox"
projMotVelPlotCheck = "2D Velocity Plot Checkbox"
projMotVelAniCheck = "2D Velocity Animation Checkbox"
projMotCBSelectAll = "Select All Projectile Motion Plots"
projMotCBUnselectAll = "Unselect All Projectile Motion Plots"
projMotCalculateBtn = "2D Calculate Button"
projMotClearBtn = "2D Clear Button"
projMotMainWinBtn = "Return Home"

""" ProjectileMotionWindow - Window for the projectile motion simulation
    Member Functions:

"""
class ProjectileMotionWindow(QWidget):
    """ Constructor - Constructs window with widgets and layouts of widgets
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Call the init ui function
        Output:
            This function does not return a value
    """
    # Main window signal
    mainWindowSignal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.InitUI()
        # # Widget sizes
        # headerSize = 20
        # comboBoxMinWidth = 200
        # comboBoxMinHeight = 25
        # textFieldMinWidth = 200
        # textFieldMinHeight = 25
        # buttonMinWidth = 175
        # buttonMinHeight = 35
        # # Title of Window
        # self.setWindowTitle("Projectile Motion Simulation")
        # # Height and Width of Window
        # self.resize(800,500)
        # self.setMinimumWidth(800)
        # self.setMinimumHeight(500)
        # # Layouts
        # mainLayout = QVBoxLayout()
        # ## Parameters layouts
        # parametersLayout = QHBoxLayout()
        # commonParametersLayout = QVBoxLayout()
        # customParametersLayout = QVBoxLayout()
        # customObjParametersLayout = QHBoxLayout()
        # ## Plot selection layouts
        # plotSelectionLayout = QVBoxLayout()
        # plotSelectionHeaderLayout = QHBoxLayout()
        # plotSelectionCBLayout = QHBoxLayout()
        # plotSelectionBtnLayout = QHBoxLayout()
        # # Main buttons layout
        # buttonLayout = QVBoxLayout()
        # buttonHeaderLayout = QHBoxLayout()
        # buttonMainBtnsLayout = QHBoxLayout()
        # # Margins
        # mainLayout.setContentsMargins(25,25,25,25)
        # ## Header
        # commonParametersHeader = QLabel("Common Parameters")
        # commonParametersHeaderFont = commonParametersHeader.font()
        # commonParametersHeaderFont.setPointSize(headerSize)
        # commonParametersHeader.setFont(commonParametersHeaderFont)
        # commonParametersHeader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        # commonParametersLayout.addWidget(commonParametersHeader)
        # ## Common Masses Dropdown
        # commonObjectsDropdown = QComboBox()
        # commonObjectsDropdown.setMinimumWidth(comboBoxMinWidth)
        # commonObjectsDropdown.setMinimumHeight(comboBoxMinHeight)
        # commonObjectsDropdown.addItems(["Select Common Object", "Sun", "Mercury", "Venus", "Earth", "Moon", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"])
        # commonObjectsDropdown.currentIndexChanged.connect(self.CommmonObjChanged)
        # commonObjectsDropdown.setObjectName(projMotCommonObjectDD)
        # commonParametersLayout.addWidget(commonObjectsDropdown)
        # ## Projectile Motion Initial Position
        # projectileInitialPosition1 = QLineEdit()
        # projectileInitialPosition1.setMinimumWidth(textFieldMinWidth)
        # projectileInitialPosition1.setMinimumHeight(textFieldMinHeight)
        # projectileInitialPosition1.setPlaceholderText("Enter Initial Position In (m)")
        # projectileInitialPosition1.setDisabled(True)
        # projectileInitialPosition1.setObjectName(projMotCommonObjInitPos)
        # commonParametersLayout.addWidget(projectileInitialPosition1)
        # ## Projectile Motion Initial Velocity
        # projectileInitialVelocity1 = QLineEdit()
        # projectileInitialVelocity1.setMinimumWidth(textFieldMinWidth)
        # projectileInitialVelocity1.setMinimumHeight(textFieldMinHeight)
        # projectileInitialVelocity1.setPlaceholderText("Enter Initial Velocity In (m/s)")
        # projectileInitialVelocity1.setDisabled(True)
        # projectileInitialVelocity1.setObjectName(projMotCommonObjInitVel)
        # commonParametersLayout.addWidget(projectileInitialVelocity1)
        # ## Initial Time Of Model
        # initialTime1 = QLineEdit()
        # initialTime1.setMinimumWidth(textFieldMinWidth)
        # initialTime1.setMinimumHeight(textFieldMinHeight)
        # initialTime1.setPlaceholderText("Enter Initial Time Of Model In (s)")
        # initialTime1.setDisabled(True)
        # initialTime1.setObjectName(projMotCommonObjInitTime)
        # commonParametersLayout.addWidget(initialTime1)
        # ## Final Time Of Model
        # finalTime1 = QLineEdit()
        # finalTime1.setMinimumWidth(textFieldMinWidth)
        # finalTime1.setMinimumHeight(textFieldMinHeight)
        # finalTime1.setPlaceholderText("Enter Final Time Of Model In (s)")
        # finalTime1.setDisabled(True)
        # finalTime1.setObjectName(projMotCommonObjFinalTime)
        # commonParametersLayout.addWidget(finalTime1)
        # ## Clear Parameters Button
        # commonParametersClearBtn = QPushButton("Clear Common Parameters")
        # commonParametersClearBtn.setMinimumWidth(buttonMinWidth)
        # commonParametersClearBtn.setMinimumHeight(buttonMinHeight)
        # commonParametersClearBtn.setDisabled(True)
        # commonParametersClearBtn.setObjectName(projMotCommonObjClearParamBtn)
        # commonParametersClearBtn.clicked.connect(self.ClearCommonParam)
        # commonParametersLayout.addWidget(commonParametersClearBtn)
        # ## Random Parameters Button
        # commonParametersRandomBtn = QPushButton("Randomize Parameters")
        # commonParametersRandomBtn.setMinimumWidth(buttonMinWidth)
        # commonParametersRandomBtn.setMinimumHeight(buttonMinHeight)
        # commonParametersRandomBtn.setObjectName(projMotCommonObjRandBtn)
        # commonParametersRandomBtn.clicked.connect(self.RandomCommon)
        # commonParametersLayout.addWidget(commonParametersRandomBtn)
        # # Custom Parameters
        # ## Header
        # customParametersHeader = QLabel("Custom Parameters")
        # customParametersHeaderFont = customParametersHeader.font()
        # customParametersHeaderFont.setPointSize(headerSize)
        # customParametersHeader.setFont(customParametersHeaderFont)
        # customParametersHeader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        # customParametersLayout.addWidget(customParametersHeader)
        # ## Mass
        # customObj = QLineEdit()
        # customObj.setMinimumHeight(textFieldMinHeight)
        # customObj.setPlaceholderText("Enter Mass Of Object In (Kg)")
        # customObj.textChanged.connect(self.CustomObjChanged)
        # customObj.setObjectName(projMotCustomObjMass)
        # customObjParametersLayout.addWidget(customObj)
        # ## Radius Of Mass
        # customRadius = QLineEdit()
        # customRadius.setMinimumHeight(textFieldMinHeight)
        # customRadius.setPlaceholderText("Enter Radius Of Mass In (m)")
        # customRadius.textChanged.connect(self.CustomObjChanged)
        # customRadius.setObjectName(projMotCustomObjRadius)
        # customObjParametersLayout.addWidget(customRadius)
        # customParametersLayout.addLayout(customObjParametersLayout)
        # ## Projectile Motion Initial Position
        # projectileInitialPosition2 = QLineEdit()
        # projectileInitialPosition2.setMinimumWidth(textFieldMinWidth)
        # projectileInitialPosition2.setMinimumHeight(textFieldMinHeight)
        # projectileInitialPosition2.setPlaceholderText("Enter Initial Position In (m)")
        # projectileInitialPosition2.setDisabled(True)
        # projectileInitialPosition2.setObjectName(projMotCustomObjInitPos)
        # customParametersLayout.addWidget(projectileInitialPosition2)
        # ## Projectile Motion Initial Velocity
        # projectileInitialVelocity2 = QLineEdit()
        # projectileInitialVelocity2.setMinimumWidth(textFieldMinWidth)
        # projectileInitialVelocity2.setMinimumHeight(textFieldMinHeight)
        # projectileInitialVelocity2.setPlaceholderText("Enter Initial Velocity In (m/s)")
        # projectileInitialVelocity2.setDisabled(True)
        # projectileInitialVelocity2.setObjectName(projMotCustomObjInitVel)
        # customParametersLayout.addWidget(projectileInitialVelocity2)
        # ## Initial Time Of Model
        # initialTime2 = QLineEdit()
        # initialTime2.setMinimumWidth(textFieldMinWidth)
        # initialTime2.setMinimumHeight(textFieldMinHeight)
        # initialTime2.setPlaceholderText("Enter Initial Time Of Model In (s)")
        # initialTime2.setDisabled(True)
        # initialTime2.setObjectName(projMotCustomObjInitTime)
        # customParametersLayout.addWidget(initialTime2)
        # ## Final Time Of Model
        # finalTime2 = QLineEdit()
        # finalTime2.setMinimumWidth(textFieldMinWidth)
        # finalTime2.setMinimumHeight(textFieldMinHeight)
        # finalTime2.setPlaceholderText("Enter Final Time Of Model In (s)")
        # finalTime2.setDisabled(True)
        # finalTime2.setObjectName(projMotCustomObjFinalTime)
        # customParametersLayout.addWidget(finalTime2)
        # ## Clear Parameters Button
        # customParametersClearBtn = QPushButton("Clear Custom Parameters")
        # customParametersClearBtn.setMinimumWidth(buttonMinWidth)
        # customParametersClearBtn.setMinimumHeight(buttonMinHeight)
        # customParametersClearBtn.setDisabled(True)
        # customParametersClearBtn.setObjectName(projMotCustomObjClearParamBtn)
        # customParametersClearBtn.clicked.connect(self.ClearCustomParam)
        # customParametersLayout.addWidget(customParametersClearBtn)
        # ## Random Parameters Button
        # customParametersRandomBtn = QPushButton("Randomize Parameters")
        # customParametersRandomBtn.setMinimumWidth(buttonMinWidth)
        # customParametersRandomBtn.setMinimumHeight(buttonMinHeight)
        # customParametersRandomBtn.setObjectName(projMotCustomObjRandBtn)
        # customParametersRandomBtn.clicked.connect(self.RandomCustom)
        # customParametersLayout.addWidget(customParametersRandomBtn)
        # # Parameters layouts layout addition
        # parametersLayout.addLayout(commonParametersLayout)
        # parametersLayout.addLayout(customParametersLayout)
        # # Plot Selection
        # plotSelectionHeader = QLabel("Choose Plot(s)")
        # plotSelectionHeaderFont = plotSelectionHeader.font()
        # plotSelectionHeaderFont.setPointSize(headerSize)
        # plotSelectionHeader.setFont(plotSelectionHeaderFont)
        # plotSelectionHeader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        # plotSelectionLayout.addWidget(plotSelectionHeader)
        # ## 2D Position Plot
        # projMotPosPlot = QCheckBox("2D Position Plot")
        # projMotPosPlot.setDisabled(True)
        # projMotPosPlot.setObjectName(projMotPosPlotCheck)
        # plotSelectionCBLayout.addWidget(projMotPosPlot)
        # ## 2D Position Animation
        # projMotPosAni = QCheckBox("2D Position Animation")
        # projMotPosAni.setDisabled(True)
        # projMotPosAni.setObjectName(projMotPosAniCheck)
        # plotSelectionCBLayout.addWidget(projMotPosAni)
        # ## 2D Velocity Plot
        # projMotVelPlot = QCheckBox("2D Velocity Plot")
        # projMotVelPlot.setDisabled(True)
        # projMotVelPlot.setObjectName(projMotVelPlotCheck)
        # plotSelectionCBLayout.addWidget(projMotVelPlot)
        # ## 2D Velocity Animation
        # projMotVelAni = QCheckBox("2D Velocity Animation")
        # projMotVelAni.setDisabled(True)
        # projMotVelAni.setObjectName(projMotVelAniCheck)
        # plotSelectionCBLayout.addWidget(projMotVelAni)
        # ## Select all plots
        # selectAllPlotsBtn = QPushButton("Select All Plots")
        # selectAllPlotsBtn.setMinimumWidth(buttonMinWidth)
        # selectAllPlotsBtn.setMinimumHeight(buttonMinHeight)
        # selectAllPlotsBtn.setDisabled(True)
        # selectAllPlotsBtn.setObjectName(projMotCBSelectAll)
        # selectAllPlotsBtn.clicked.connect(self.SelectAllPlots)
        # plotSelectionBtnLayout.addWidget(selectAllPlotsBtn)
        # ## Unselect all plots
        # unselectAllPlotsBtn = QPushButton("Unselect All Plots")
        # unselectAllPlotsBtn.setMinimumWidth(buttonMinWidth)
        # unselectAllPlotsBtn.setMinimumHeight(buttonMinHeight)
        # unselectAllPlotsBtn.setDisabled(True)
        # unselectAllPlotsBtn.setObjectName(projMotCBUnselectAll)
        # unselectAllPlotsBtn.clicked.connect(self.UnselectAllPlots)
        # plotSelectionBtnLayout.addWidget(unselectAllPlotsBtn)
        # ## Plot selection layouts layout addition
        # plotSelectionLayout.addLayout(plotSelectionHeaderLayout)
        # plotSelectionLayout.addLayout(plotSelectionCBLayout)
        # plotSelectionLayout.addLayout(plotSelectionBtnLayout)
        # # Buttons
        # buttonsHeader = QLabel("Calculate / Clear Selection")
        # buttonsHeaderFont = buttonsHeader.font()
        # buttonsHeaderFont.setPointSize(20)
        # buttonsHeader.setFont(buttonsHeaderFont)
        # buttonsHeader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        # buttonHeaderLayout.addWidget(buttonsHeader)
        # ## Calculate Button
        # calculateButton = QPushButton("Calculate")
        # calculateButton.setMinimumWidth(buttonMinWidth)
        # calculateButton.setMinimumHeight(buttonMinHeight)
        # calculateButton.setDisabled(True)
        # calculateButton.setObjectName(projMotCalculateBtn)
        # calculateButton.clicked.connect(self.OpenPlot)
        # buttonMainBtnsLayout.addWidget(calculateButton)
        # ## Clear Button
        # clearButton = QPushButton("Clear")
        # clearButton.setMinimumWidth(buttonMinWidth)
        # clearButton.setMinimumHeight(buttonMinHeight)
        # clearButton.setDisabled(True)
        # clearButton.setObjectName(projMotClearBtn)
        # clearButton.clicked.connect(self.ClearAllInputs)
        # buttonMainBtnsLayout.addWidget(clearButton)
        # ## Main Window Button
        # mainWindowButton = QPushButton("Return Home")
        # mainWindowButton.setMinimumWidth(buttonMinWidth)
        # mainWindowButton.setMinimumHeight(buttonMinHeight)
        # mainWindowButton.setObjectName(projMotMainWinBtn)
        # mainWindowButton.clicked.connect(self.ReturnHome)
        # buttonMainBtnsLayout.addWidget(mainWindowButton)
        # ## Button layouts layout addition
        # buttonLayout.addLayout(buttonHeaderLayout)
        # buttonLayout.addLayout(buttonMainBtnsLayout)
        # # Main layout widget addition
        # mainLayout.addLayout(parametersLayout)
        # mainLayout.addLayout(plotSelectionLayout)
        # mainLayout.addLayout(buttonLayout)
        # # Add layouts
        # self.setLayout(mainLayout)

    """ Calculate - Assigns parameters of input fields to be fed to the projectile motion solver
        Input:
            There are not unique input parameters for this function
        Algorithm:
            * Grab the children from the parameters and plot selection input fields
            * Create parameters that are to be returned from the calculation
            * Check if the common field parameters are the only parameters entered
                * Get the values from the children in the input fields
                * Assign the proper values to obj for the parameter that was selected
                    * obj[0] - Object's mass
                    * obj[1] - Object's radius
                * Assign the return parameters to the other input fields
                    * ic[0] - Projectile's initial vertical position
                    * ic[1] - Projectile's initial vertical velocity
            * Check if the custom field parameters are the only parameters entered
                * Get the values from the children in the input fields
                * Assign the return parameters to the input fields
            * Otherwise, create a dialog box that tells the user they have incorrectly entered parameters
            * Return the parameters to be fed to the model
        Output:
            obj - Array of object parameters
                obj[0] - Object's mass
                obj[1] - Object's radius
            ic - Array of initial conditions of projectile
                ic[0] - Initial vertical position
                ic[1] - Initial vertical velocity
            initTime - Initial time of model
            finTime - Final time of model
            objectName - Name of object
    """
    def Calculate(self):
        # Grab children from input fields
        children = self.GrabChildren()
        # Parameters to be fed into solver
        obj = []
        objName = ""
        ic = []
        initPos = 0
        initVel = 0
        initTime = 0
        finTime = 0
        commonEntered = (any(isinstance(widget, QComboBox) and widget.currentText() != "Select Common Object" for widget in children[0]) and all(isinstance(widget, QLineEdit) and widget.text() != "" for widget in children[0][1:5]))
        customEntered = (all(isinstance(widget, QLineEdit) and widget.text() != "" for widget in children[1][0:6]))
        # Common field entered, custom not
        if (commonEntered):
            objectSelection = children[0][0].currentText()
            initialPos = float(children[0][1].text())
            initialVel = float(children[0][2].text())
            initialTime = float(children[0][3].text())
            finalTime = float(children[0][4].text())
            # Assign object parameters
            if (objectSelection == "Sun"):
                obj.append(MSUN)
                obj.append(RSUN)
            elif (objectSelection == "Mercury"):
                obj.append(MMERCURY)
                obj.append(RMERCURY)
            elif (objectSelection == "Venus"):
                obj.append(MVENUS)
                obj.append(RVENUS)
            elif (objectSelection == "Earth"):
                obj.append(MEARTH)
                obj.append(REARTH)
            elif (objectSelection == "Moon"):
                obj.append(MMOON)
                obj.append(RMOON)
            elif (objectSelection == "Mars"):
                obj.append(MMARS)
                obj.append(RMARS)
            elif (objectSelection == "Jupiter"):
                obj.append(MJUPITER)
                obj.append(RJUPITER)
            elif (objectSelection == "Saturn"):
                obj.append(MSATURN)
                obj.append(RSATURN)
            elif (objectSelection == "Uranus"):
                obj.append(MURANUS)
                obj.append(RURANUS)
            elif (objectSelection == "Neptune"):
                obj.append(MNEPTUNE)
                obj.append(RNEPTUNE)
            elif (objectSelection == "Pluto"):
                obj.append(MPLUTO)
                obj.append(RPLUTO)
            objName = objectSelection
            # Assign return values to input field values
            initPos = initialPos
            initVel = initialVel
            ic.append(initPos)
            ic.append(initVel)
            initTime = initialTime
            finTime = finalTime
            return obj, ic, initTime, finTime, objName
        # Custom field entered, common not
        elif (commonEntered == False and customEntered == True):
            # Convert input fields to correct data type
            objectMass = float(children[1][0].text())
            objectRadius = float(children[1][1].text())
            initialPos = float(children[1][2].text())
            initialVel = float(children[1][3].text())
            initialTime = float(children[1][4].text())
            finalTime = float(children[1][5].text())
            # Assign object parameters
            obj.append(objectMass)
            obj.append(objectRadius)
            objName = "Arbitrary Mass"
            # Assign return values to input field values
            initPos = initialPos
            initVel = initialVel
            ic.append(initPos)
            ic.append(initVel)
            initTime = initialTime
            finTime = finalTime
            return obj, ic, initTime, finTime, objName
        # Invalid entries
        else:
            dialogBox = QDialog(self)
            dialogBox.setWindowTitle("Invalid Entries")
            dialogBox.setFixedSize(400, 75)
            warningLabel = QLabel("Please enter in all values in the given fields.", dialogBox)
            warningFont = warningLabel.font()
            warningFont.setPointSize(13)
            warningLabel.setFont(warningFont)
            warningLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            layout = QVBoxLayout()
            layout.addWidget(warningLabel)
            dialogBox.setLayout(layout)
            dialogBox.exec()
            return None, None, None, None, None
    
    """ ClearAllInputs - Clears all the inputs of the window
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Call the member functions for all of the input fields
        Output:
            This function does not return a value
    """
    def ClearAllInputs(self):
        # Call functions
        self.ClearCommonParam()
        self.ClearCustomParam()
        self.UnselectAllPlots()

    """ ClearCommonParam - Clears the common parameters input fields
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab the children of the common parameters input fields
            * Reset the common parameter children
            * Reset the custom parameter children
            * Enable / Disable common parameter children
            * Enable / Disable custom parameter children
            * Disable the Plot selection / Main buttons children
        Output:
            This function does not return a value
    """
    def ClearCommonParam(self):
        # Grab children
        children = self.GrabChildren()
        # Reset common parameters
        for widget in children[0]:
            if isinstance(widget, QComboBox):
                widget.setCurrentIndex(0)
            if isinstance(widget, QLineEdit):
                widget.setText("")
        # Reset custom parameters
        for widget in children[1]:
            if isinstance(widget, QLineEdit):
                widget.setText("")
        # Enable / Disable children
        ## Common parameters children
        for widget in children[0]:
            if ((widget.objectName() == projMotCommonObjectDD) or (widget.objectName() == projMotCommonObjRandBtn)):
                if isinstance(widget, QComboBox):
                    widget.setCurrentIndex(0)
                widget.setEnabled(True)
            else:
                if isinstance(widget, QLineEdit):
                    widget.setText("")
                widget.setDisabled(True)
        ## Custom parameters children
        for widget in children[1]:
            if ((widget.objectName() == projMotCustomObjMass) or (widget.objectName() == projMotCustomObjRadius) or (widget.objectName() == projMotCustomObjRandBtn)):
                if isinstance(widget, QLineEdit):
                    widget.setText("")
                widget.setEnabled(True)
            else:
                if isinstance(widget, QLineEdit):
                    widget.setText("")
                widget.setDisabled(True)
        ## Plot selection / Main buttons children
        for widgets in children[2:]:
            for widget in widgets:
                widget.setDisabled(True)

    """ ClearCustomParam - Clears the custom parameters input fields
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab the children of the common parameters input fields
            * Reset the common parameter children
            * Reset the custom parameter children
            * Enable / Disable common parameter children
            * Enable / Disable custom parameter children
            * Disable the Plot selection / Main buttons children
        Output:
            This function does not return a value
    """
    def ClearCustomParam(self):
        # Grab children
        children = self.GrabChildren()
        # Reset common parameters
        for widget in children[0]:
            if isinstance(widget, QComboBox):
                widget.setCurrentIndex(0)
            if isinstance(widget, QLineEdit):
                widget.setText("")
        # Reset custom parameters
        for widget in children[1]:
            if isinstance(widget, QLineEdit):
                widget.setText("")
        # Enable / Disable children
        ## Common parameters children
        for widget in children[0]:
            if ((widget.objectName() == projMotCommonObjectDD) or (widget.objectName() == projMotCommonObjRandBtn)):
                if isinstance(widget, QComboBox):
                    widget.setCurrentIndex(0)
                widget.setEnabled(True)
            else:
                if isinstance(widget, QLineEdit):
                    widget.setText("")
                widget.setDisabled(True)
        ## Custom parameters children
        for widget in children[1]:
            if ((widget.objectName() == projMotCustomObjMass) or (widget.objectName() == projMotCustomObjRadius) or (widget.objectName() == projMotCustomObjRandBtn)):
                if isinstance(widget, QLineEdit):
                    widget.setText("")
                widget.setEnabled(True)
            else:
                if isinstance(widget, QLineEdit):
                    widget.setText("")
                widget.setDisabled(True)
        ## Plot selection / Main buttons children
        for widgets in children[2:]:
            for widget in widgets:
                if isinstance(widget, QCheckBox):
                    widget.setChecked(False)
                widget.setDisabled(True)

    """ CommmonObjChanged - Enables / Disables and resets children based on index of the combo box
        Input:
            index - Index of the common object combo box
        Algorithm:
            * Grab the children from the window
            * If the combo box index is currently zero
                * Disable and reset the common parameters children
                * Disable and reset the custom parameters children
                * Disable and reset the Plot selection / Main buttons children
            * If the combo box is another index
                * Enable the common parameters children
                * Disable and reset the custom parameters children
                * Enable the Plot selection / Main buttons children
        Output:
            This function does not return a value
    """
    def CommmonObjChanged(self, index):
        # Grab children
        children = self.GrabChildren()
        # Index zero
        if (index == 0):
            ## Reset common
            for widget in children[0]:
                if isinstance(widget, QLineEdit):
                    widget.setText("")
                    widget.setDisabled(True)
                if isinstance(widget, QPushButton):
                    if (widget.objectName() == projMotCommonObjRandBtn):
                        widget.setEnabled(True)
                    else:
                        widget.setDisabled(True)
            ## Reset custom 
            for widget in children[1]:
                if isinstance(widget, QLineEdit):
                    widget.setText("")
                    if ((widget.objectName() == projMotCustomObjMass) or (widget.objectName() == projMotCustomObjRadius)):
                        widget.setEnabled(True)
                    else:
                        widget.setDisabled(True)
                if isinstance(widget, QPushButton):
                    if (widget.objectName() == projMotCustomObjRandBtn):
                        widget.setEnabled(True)
                    else:
                        widget.setDisabled(True)
            ## Reset Plot selection / Main buttons 
            for widgets in children[2:]:
                for widget in widgets:
                    if isinstance(widget, QCheckBox):
                        widget.setChecked(False)
                    widget.setDisabled(True)
        # Other index
        else:
            ## Enable common
            for widget in children[0]:
                widget.setEnabled(True)
            ## Disable custom
            for widget in children[1]:
                if isinstance(widget, QLineEdit):
                    widget.setText("")
                widget.setDisabled(True)
            ## Enable Plot selection / Main buttons
            for widgets in children[2:]:
                for widget in widgets:
                    widget.setEnabled(True)

    """ CustomObjChanged - Enables / Disables and resets children based on the value of children in custom parameters
        Input:
            There are not unique input parameters for this function
        Algorithm:
            * Grab the children from the window
            * Check if custom object mass and custom object radius are both empty
                * If they are, reset the children of the window to their default state
            * If one or the other is not empty
                * Reset and disable the common parameter children
                * Enable the custom parameter, Plot selection, and main buttons children
        Output:
            This function does not return a value
    """
    def CustomObjChanged(self):
        # Grab children
        children = self.GrabChildren()
        # Check for empty fields
        if (children[1][0].text() == "" and children[1][1].text() == ""):
            # Clear common
            self.ClearCommonParam()
            # Clear custom
            self.ClearCustomParam()
        # Field(s) are not empty
        else:
            # Disable common
            for widget in children[0]:
                if isinstance(widget, QComboBox):
                    widget.setCurrentIndex(0)
                if isinstance(widget, QLineEdit):
                    widget.setText("")
                widget.setDisabled(True)
            # Enable custom, Plot selection, Main buttons
            for widgets in children[1:]:
                for widget in widgets:
                    widget.setEnabled(True)

    """ GrabChildren - Grabs the children from the main window
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab the children from the common object fields, and create an array for them
            * Grab the children from the custom object fields, and create an array for them
            * Grab the children from the plot selection fields, and create an array for them
            * Grab the children from the main window fields, and create an array for them
            * Return the previous arrays
        Output:
            commonArr - Array of common object field children
                commonArr[0] - Common object combo box
                commonArr[1] - Common object initial position text field
                commonArr[2] - Common object initial velocity text field
                commonArr[3] - Common object initial time text field
                commonArr[4] - Common object final time text field
                commonArr[5] - Common object clear parameters button
                commonArr[6] - Common object random parameters button
            customArr - Array of custom object field children
                customArr[0] - Custom object mass text field
                customArr[1] - Custom object radius text field
                customArr[2] - Custom object initial position text field
                customArr[3] - Custom object initial velocity text field
                customArr[4] - Custom object initial time text field
                customArr[5] - Custom object final time text field
                customArr[6] - Custom object clear parameters button
                customArr[7] - Custom object random parameters button
            checkBoxArr - Array of plot selection field children
                checkBoxArr[0] - 2D position plot checkbox
                checkBoxArr[1] - 2D position animation checkbox
                checkBoxArr[2] - 2D velocity plot checkbox
                checkBoxArr[3] - 2D velocity animation checkbox
                checkBoxArr[4] - Select all plot checkboxes button
                checkBoxArr[6] - Unselect all plot checkboxes button
            mainButtonArr - Array of main buttons field children
                mainButtonArr[0] - Calculate button
                mainButtonArr[1] - Clear all fields button
    """
    def GrabChildren(self):
        # Grab children
        ## Common object children
        commonObjDD = self.findChild(QComboBox, projMotCommonObjectDD)
        commonObjInitPos = self.findChild(QLineEdit, projMotCommonObjInitPos)
        commonObjInitVel = self.findChild(QLineEdit, projMotCommonObjInitVel)
        commonObjInitTime = self.findChild(QLineEdit, projMotCommonObjInitTime)
        commonObjFinalTime = self.findChild(QLineEdit, projMotCommonObjFinalTime)
        commonObjClearButton = self.findChild(QPushButton, projMotCommonObjClearParamBtn)
        commonObjRandButton = self.findChild(QPushButton, projMotCommonObjRandBtn)
        commonArr = [commonObjDD, commonObjInitPos, commonObjInitVel, commonObjInitTime, commonObjFinalTime, commonObjClearButton, commonObjRandButton]
        ## Custom object children
        customObjMass = self.findChild(QLineEdit, projMotCustomObjMass)
        customObjRadius = self.findChild(QLineEdit, projMotCustomObjRadius)
        customObjInitPos = self.findChild(QLineEdit, projMotCustomObjInitPos)
        customObjInitVel = self.findChild(QLineEdit, projMotCustomObjInitVel)
        customObjInitTime = self.findChild(QLineEdit, projMotCustomObjInitTime)
        customObjFinalTime = self.findChild(QLineEdit, projMotCustomObjFinalTime)
        customObjClearButton = self.findChild(QPushButton, projMotCustomObjClearParamBtn)
        customObjRandButton = self.findChild(QPushButton, projMotCustomObjRandBtn)
        customArr = [customObjMass, customObjRadius, customObjInitPos, customObjInitVel, customObjInitTime, customObjFinalTime, customObjClearButton, customObjRandButton]
        ## Plot selection children
        posPlotCheck = self.findChild(QCheckBox, projMotPosPlotCheck)
        posAniCheck = self.findChild(QCheckBox, projMotPosAniCheck)
        velPlotCheck = self.findChild(QCheckBox, projMotVelPlotCheck)
        velAniCheck = self.findChild(QCheckBox, projMotVelAniCheck)
        selectAllPlotsButton = self.findChild(QPushButton, projMotCBSelectAll)
        unselectAllPlotsButton = self.findChild(QPushButton, projMotCBUnselectAll)
        checkBoxArr = [posPlotCheck, posAniCheck, velPlotCheck, velAniCheck, selectAllPlotsButton, unselectAllPlotsButton]
        ## Main button children
        calcButton = self.findChild(QPushButton, projMotCalculateBtn)
        clearButton = self.findChild(QPushButton, projMotClearBtn)
        mainButtonArr = [calcButton, clearButton]
        return commonArr, customArr, checkBoxArr, mainButtonArr

    def InitUI(self):
        # Object names
        objSelCBName = "Object Selection Combo Box"
        objSelMassLEName = "Object's Mass"
        objSelRadLEName = "Object's Radius"
        objSelName = "Object's Name"
        objSelClearBtnName = "Clear Object Parameters"
        objSelRandBtnName = "Randomize Object Parameters"
        icInitPosName = "Initial Position"
        icInitVelName = "Initial Velocity"
        icTimeSpanName = "Time Span"
        icProjName = "Projectile's Name"
        icClearBtnName = "Clear Initial Conditions"
        icRandBtnName = "Randomize Initial Conditions"
        plotSelPosPlotCBName = "2D Position Plot"
        plotSelPosAniCBName = "2D Position Animation"
        plotSelVelPlotCBName = "2D Velocity Plot"
        plotSelVelAniCBName = "2D Velocity Animation"
        plotSelSelAllBtnName = "Select All Plots"
        plotSelUnselAllBtnName = "Unselect All Plots"
        calcBtnName = "Calculate"
        clearBtnName = "Clear"
        randomBtnName = "Random"
        homeBtnName = "Home"
        # Widget sizes
        headerSize = 20
        comboBoxMinWidth = 200
        comboBoxMinHeight = 25
        lineEditMinWidth = 200
        lineEditMinHeight = 25
        buttonMinWidth = 200
        buttonMinHeight = 35
        # Combo box items
        selectObjectCB = "Select Object:"
        arbitraryObjectCB = "Arbitrary Object"
        sunCB = "Sun"
        mercCB = "Mercury"
        venCB = "Venus"
        earCB = "Earth"
        moonCB = "Moon"
        marsCB = "Mars"
        jupCB = "Jupiter"
        satCB = "Saturn"
        uraCB = "Uranus"
        nepCB = "Neptune"
        pluCB = "Pluto"
        cbItems = [selectObjectCB, arbitraryObjectCB, sunCB, mercCB, venCB, earCB, moonCB, marsCB, jupCB, satCB, uraCB, nepCB, pluCB]
        # Title of Window
        self.setWindowTitle("Projectile Motion Simulation")
        # Height and Width of Window
        self.resize(800,500)
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        # Layouts
        ## Main layout
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(25,25,25,25)
        mainLayout.setSpacing(20)
        ## Parameters layout
        parametersLayout = QHBoxLayout()
        parametersLayout.setContentsMargins(5,5,5,5)
        parametersLayout.setSpacing(10)
        ## Object selection layout
        objSelLayout = QVBoxLayout()
        objSelLayout.setContentsMargins(0,0,0,0)
        objSelLayout.setSpacing(5)
        ## Initial conditions layout
        icLayout = QVBoxLayout()
        icLayout.setContentsMargins(0,0,0,0)
        icLayout.setSpacing(5)
        ## Plot selection layout
        plotSelLayout = QVBoxLayout()
        plotSelLayout.setContentsMargins(0,0,0,0)
        plotSelLayout.setSpacing(5)
        ## Plot checkboxes layout
        plotCheckLayout = QHBoxLayout()
        plotCheckLayout.setContentsMargins(0,0,0,0)
        plotCheckLayout.setSpacing(5)
        ## Plot selection buttons layout
        plotButtonLayout = QHBoxLayout()
        plotButtonLayout.setContentsMargins(0,0,0,0)
        plotButtonLayout.setSpacing(5)
        ## Main buttons layout
        mainButtonsLayout = QVBoxLayout()
        mainButtonsLayout.setContentsMargins(0,0,0,0)
        mainButtonsLayout.setSpacing(5)
        ## Main buttons button layout
        mainButtonsBtnLayout = QHBoxLayout()
        mainButtonsBtnLayout.setContentsMargins(0,0,0,0)
        mainButtonsBtnLayout.setSpacing(5)
        ###################################
        ##### Object selection widgets
        ###################################
        ### Object selection header
        objSelHeader = QLabel("Object Selection")
        objSelLayout.addWidget(objSelHeader, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Object selection combo box
        objSelCB = QComboBox()
        objSelCB.setObjectName(objSelCBName)
        objSelCB.setMinimumWidth(comboBoxMinWidth)
        objSelCB.setMinimumHeight(comboBoxMinHeight)
        objSelCB.addItems(cbItems)
        objSelLayout.addWidget(objSelCB, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Object selection mass line edit
        objSelMassLE = QLineEdit()
        objSelMassLE.setObjectName(objSelMassLEName)
        objSelMassLE.setMinimumWidth(lineEditMinWidth)
        objSelMassLE.setMinimumHeight(lineEditMinHeight)
        objSelMassLE.setPlaceholderText("Enter mass of object in (Kg)")
        objSelLayout.addWidget(objSelMassLE, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Object selection radius line edit
        objSelRadLE = QLineEdit()
        objSelRadLE.setObjectName(objSelRadLEName)
        objSelRadLE.setMinimumWidth(lineEditMinWidth)
        objSelRadLE.setMinimumHeight(lineEditMinHeight)
        objSelRadLE.setPlaceholderText("Enter radius of object in (m)")
        objSelLayout.addWidget(objSelRadLE, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Object selection name line edit
        objSelNameLE = QLineEdit()
        objSelNameLE.setObjectName(objSelName)
        objSelNameLE.setMinimumWidth(lineEditMinWidth)
        objSelNameLE.setMinimumHeight(lineEditMinHeight)
        objSelNameLE.setPlaceholderText("Enter name of object")
        objSelLayout.addWidget(objSelNameLE, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Object selection clear parameters button
        objSelClearBtn = QPushButton("Clear Parameters")
        objSelClearBtn.setObjectName(objSelClearBtnName)
        objSelClearBtn.setMinimumWidth(buttonMinWidth)
        objSelClearBtn.setMinimumHeight(buttonMinHeight)
        objSelLayout.addWidget(objSelClearBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Object selection randomize parameters button
        objSelRandBtn = QPushButton("Random Object")
        objSelRandBtn.setObjectName(objSelRandBtnName)
        objSelRandBtn.setMinimumWidth(buttonMinWidth)
        objSelRandBtn.setMinimumHeight(buttonMinHeight)
        objSelLayout.addWidget(objSelRandBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ###################################
        ##### Initial conditions widgets
        ###################################
        ### Initial conditions header
        icHeader = QLabel("Projectile Initial Conditions")
        icLayout.addWidget(icHeader, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Initial conditions initial position line edit
        icInitPosLE = QLineEdit()
        icInitPosLE.setObjectName(icInitPosName)
        icInitPosLE.setMinimumWidth(lineEditMinWidth)
        icInitPosLE.setMinimumHeight(lineEditMinHeight)
        icInitPosLE.setPlaceholderText("Enter initial position in (m)")
        icLayout.addWidget(icInitPosLE, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Initial conditions initial velocity line edit
        icInitVelLE = QLineEdit()
        icInitVelLE.setObjectName(icInitVelName)
        icInitVelLE.setMinimumWidth(lineEditMinWidth)
        icInitVelLE.setMinimumHeight(lineEditMinHeight)
        icInitVelLE.setPlaceholderText("Enter initial velocity in (m/s)")
        icLayout.addWidget(icInitVelLE, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Initial conditions time span line edit
        icTimeSpanLE = QLineEdit()
        icTimeSpanLE.setObjectName(icTimeSpanName)
        icTimeSpanLE.setMinimumWidth(lineEditMinWidth)
        icTimeSpanLE.setMinimumHeight(lineEditMinHeight)
        icTimeSpanLE.setPlaceholderText("Enter time span of model in (s)")
        icLayout.addWidget(icTimeSpanLE, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Initial conditions projectile name line edit
        icProjNameLE = QLineEdit()
        icProjNameLE.setObjectName(icProjName)
        icProjNameLE.setMinimumWidth(lineEditMinWidth)
        icProjNameLE.setMinimumHeight(lineEditMinHeight)
        icProjNameLE.setPlaceholderText("Enter name of projectile")
        icLayout.addWidget(icProjNameLE, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Initial conditions clear parameters button
        icClearBtn = QPushButton("Clear Parameters")
        icClearBtn.setObjectName(icClearBtnName)
        icClearBtn.setMinimumWidth(buttonMinWidth)
        icClearBtn.setMinimumHeight(buttonMinHeight)
        icLayout.addWidget(icClearBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Initial conditions random parameters button
        icRandBtn = QPushButton("Random Initial Conditions")
        icRandBtn.setObjectName(icRandBtnName)
        icRandBtn.setMinimumWidth(buttonMinWidth)
        icRandBtn.setMinimumHeight(buttonMinHeight)
        icLayout.addWidget(icRandBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Parameters layout layouts addition
        parametersLayout.addLayout(objSelLayout)
        parametersLayout.addLayout(icLayout)
        ###################################
        ##### Plot selection widgets
        ###################################
        ### Plot selection header
        plotSelHeader = QLabel("Select Plot(s)")
        plotSelLayout.addWidget(plotSelHeader, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Plot selection checkboxes
        #### 2D Position Plot
        plotSelPosPlotCB = QCheckBox("2D Position Plot")
        plotSelPosPlotCB.setObjectName(plotSelPosPlotCBName)
        plotCheckLayout.addWidget(plotSelPosPlotCB)
        #### 2D Position Animation
        plotSelPosAniCB = QCheckBox("2D Position Animation")
        plotSelPosAniCB.setObjectName(plotSelPosAniCBName)
        plotCheckLayout.addWidget(plotSelPosAniCB)
        #### 2D Velocity Plot
        plotSelVelPlotCB = QCheckBox("2D Velocity Plot")
        plotSelVelPlotCB.setObjectName(plotSelVelPlotCBName)
        plotCheckLayout.addWidget(plotSelVelPlotCB)
        #### 2D Velocity Animation
        plotSelVelAniCB = QCheckBox("2D Velocity Animation")
        plotSelVelAniCB.setObjectName(plotSelVelAniCBName)
        plotCheckLayout.addWidget(plotSelVelAniCB)
        ### Plot selection select all button
        plotSelSelAllBtn = QPushButton("Select All Plots")
        plotSelSelAllBtn.setObjectName(plotSelSelAllBtnName)
        plotSelSelAllBtn.setMinimumWidth(buttonMinWidth)
        plotSelSelAllBtn.setMinimumHeight(buttonMinHeight)
        plotButtonLayout.addWidget(plotSelSelAllBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Plot selection unselect all button
        plotSelUnselAllBtn = QPushButton("Unselect All Plots")
        plotSelUnselAllBtn.setObjectName(plotSelUnselAllBtnName)
        plotSelUnselAllBtn.setMinimumWidth(buttonMinWidth)
        plotSelUnselAllBtn.setMinimumHeight(buttonMinHeight)
        plotButtonLayout.addWidget(plotSelUnselAllBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Plot selection layout layouts addition
        plotSelLayout.addLayout(plotCheckLayout)
        plotSelLayout.addLayout(plotButtonLayout)
        ###################################
        ##### Main Buttons
        ###################################
        ## Main buttons header
        mainButtonsHeader = QLabel("Calculate / Clear All / Randomize All / Return Home")
        mainButtonsLayout.addWidget(mainButtonsHeader, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Main buttons calculate button
        calculateBtn = QPushButton("Calculate")
        calculateBtn.setObjectName(calcBtnName)
        calculateBtn.setMinimumWidth(buttonMinWidth - 50)
        calculateBtn.setMinimumHeight(buttonMinHeight)
        mainButtonsBtnLayout.addWidget(calculateBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Main buttons clear button
        clearBtn = QPushButton("Clear All")
        clearBtn.setObjectName(clearBtnName)
        clearBtn.setMinimumWidth(buttonMinWidth - 50)
        clearBtn.setMinimumHeight(buttonMinHeight)
        mainButtonsBtnLayout.addWidget(clearBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Main buttons random button
        randomBtn = QPushButton("Randomize All")
        randomBtn.setObjectName(randomBtnName)
        randomBtn.setMinimumWidth(buttonMinWidth - 50)
        randomBtn.setMinimumHeight(buttonMinHeight)
        mainButtonsBtnLayout.addWidget(randomBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Main buttons home button
        homeBtn = QPushButton("Return Home")
        homeBtn.setObjectName(homeBtnName)
        homeBtn.setMinimumWidth(buttonMinWidth - 50)
        homeBtn.setMinimumHeight(buttonMinHeight)
        mainButtonsBtnLayout.addWidget(homeBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Main buttons layout layouts addition
        mainButtonsLayout.addLayout(mainButtonsBtnLayout)
        # Add layouts
        mainLayout.addLayout(parametersLayout)
        mainLayout.addLayout(plotSelLayout)
        mainLayout.addLayout(mainButtonsLayout)
        # Spacers
        spacer = QSpacerItem(0, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        mainLayout.addSpacerItem(spacer)
        # Set layout
        self.setLayout(mainLayout)

    """ OpenPlot - Opens a window for a given plot
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Call the calculate member function
            * Grab the children for the checkboxes
            * Check for if a specific checkbox checked
                * If it is, create a canvas with the parameters returned from Calculate for the type of plot
                    * 0 - 2D Position versus time plot
                    * 1 - 2D Position versus time animation
                    * 2 - 2D Velocity versus time plot
                    * 3 - 2D Velocity versus time animation
                * If no boxes are checked, generate a dialog window that tells the user they need to select a plot
        Output:
            This function does not return a value
    """
    def OpenPlot(self):
        # Call calculate
        calc = self.Calculate()
        # Check for not none
        if all(values is not None for values in calc):        
            # Grab children
            children = self.GrabChildren()
            # Position Plot
            if (children[2][0].isChecked() == True):
                self.posPlot = ProjectileMotionPlotWindow(0, calc[0], calc[1], calc[2], calc[3], calc[4], "Projectile", "Projectile Motion Plot: Position Vs. Time")
                self.posPlot.show()
            # Position Animation
            if (children[2][1].isChecked() == True):
                self.posAni = ProjectileMotionPlotWindow(1, calc[0], calc[1], calc[2], calc[3], calc[4], "Projectile", "Projectile Motion Animation: Position Vs. Time")
                self.posAni.show()
            # Velocity Plot
            if (children[2][2].isChecked() == True):
                self.velPlot = ProjectileMotionPlotWindow(2, calc[0], calc[1], calc[2], calc[3], calc[4], "Projectile", "Projectile Motion Plot: Velocity Vs. Time")
                self.velPlot.show()
            # Velocity Animation
            if (children[2][3].isChecked() == True):
                self.velAni = ProjectileMotionPlotWindow(3, calc[0], calc[1], calc[2], calc[3], calc[4], "Projectile", "Projectile Motion Animation: Velocity Vs. Time")
                self.velAni.show()
            # No boxes checked
            if (children[2][0].isChecked() == False and children[2][1].isChecked() == False and children[2][2].isChecked() == False and children[2][3].isChecked() == False):
                dialogBox = QDialog(self)
                dialogBox.setWindowTitle("Invalid Entries")
                dialogBox.setFixedSize(400, 75)
                warningLabel = QLabel("Please select plot(s) for entered input values.", dialogBox)
                warningFont = warningLabel.font()
                warningFont.setPointSize(13)
                warningLabel.setFont(warningFont)
                warningLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
                layout = QVBoxLayout()
                layout.addWidget(warningLabel)
                dialogBox.setLayout(layout)
                dialogBox.exec()

    """ RandomCommon - Generates random parameters for a common object simulation
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab all children from the window
            * Enable the common object children
            * Clear and disable the custom object children
            * Enable all the plot selection widgets
            * Enable the main buttons
            * Calculate a random object from the choices in combo box and set the combo box to that entry
            * Calculate a random initial position, round it, and set the text field to that value
            * Calculate a random initial velocity, round it, and set the text field to that value
            * Set the initial time of the model to 0
            * Calculate a random final time of the model, round it, and set the text field to that value
        Output:
            This function does not return a value
    """
    def RandomCommon(self):
        # Grab children
        children = self.GrabChildren()
        # Enable / Disable children
        ## Common object children
        for widget in children[0]:
            widget.setEnabled(True)
        ## Custom object children
        for widget in children[1]:
            if isinstance(widget, QLineEdit):
                widget.setText("")
            widget.setDisabled(True)
        ## Plot selection / Main buttons children
        for widgets in children[2:]:
            for widget in widgets:
                widget.setEnabled(True)
        # Random object
        randObj = random.randrange(1,11)
        children[0][0].setCurrentIndex(randObj)
        # Random Position
        randPos = random.uniform(0.0, 1000.0)
        randPos = round(randPos,2)
        children[0][1].setText(str(randPos))
        # Random Velocity
        randVel = random.uniform(-200.0, 200.0)
        randVel = round(randVel,2)
        children[0][2].setText(str(randVel))
        # Initial Time
        children[0][3].setText(str(0))
        # Random Final Time
        randFinTime = random.uniform(1.0, 30.0)
        randFinTime = round(randFinTime,2)
        children[0][4].setText(str(randFinTime))

    """ RandomCustom - Generates random parameters for a custom object simulation
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab all children from the window
            * Enable the custom object children
            * Clear and disable the common object children
            * Enable all the plot selection widgets
            * Enable the main buttons
            * Calculate a random mass, round it, and set the text field to that value
            * Calculate a random radius, round it, and set the text field to that value
            * Calculate a random initial position, round it, and set the text field to that value
            * Calculate a random initial velocity, round it, and set the text field to that value
            * Set the initial time of the model to 0
            * Calculate a random final time of the model, round it, and set the text field to that value
        Output:
            This function does not return a value
    """
    def RandomCustom(self):
        # Grab children
        children = self.GrabChildren()
        # Enable / Disable children
        for widget in children[0]:
            if isinstance(widget, QComboBox):
                widget.setCurrentIndex(0)
            if isinstance(widget, QLineEdit):
                widget.setText("")
            widget.setDisabled(True)
        for widgets in children[1:]:
            for widget in widgets:
                widget.setEnabled(True)
        # Random Mass
        randMass = random.uniform(0.5 * MPLUTO, 10.0 * MSUN)
        randMass = round(randMass,2)
        children[1][0].setText(str(randMass))
        # Random Radius
        randRad = random.uniform(0.5 * RPLUTO, 10.0 * RSUN)
        randRad = round(randRad,2)
        children[1][1].setText(str(randRad))
        # Random Position
        randPos = random.uniform(0.0, 1000.0)
        randPos = round(randPos,2)
        children[1][2].setText(str(randPos))
        # Random Velocity
        randVel = random.uniform(-200.0, 200.0)
        randVel = round(randVel,2)
        children[1][3].setText(str(randVel))
        # Initial Time
        children[1][4].setText(str(0))
        # Random Final Time
        randFinTime = random.uniform(1.0, 30.0)
        randFinTime = round(randFinTime,2)
        children[1][5].setText(str(randFinTime))

    """ ReturnHome - Returns home and closes the current window
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Emit the signal that was created with the class
            * Close the window
        Output:
            This function does not return a values
    """
    def ReturnHome(self):
        # Emit signal
        self.mainWindowSignal.emit()
        # Close current window
        self.close()

    """ SelectAllPlots - Selects all plot options
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab the checkbox children
            * Create an array for the checkbox children
            * Set all the children to checked
        Output:
            This function does not return a value
    """
    def SelectAllPlots(self):
        # Grab children
        posPlotCheck = self.findChild(QCheckBox, projMotPosPlotCheck)
        posAniCheck = self.findChild(QCheckBox, projMotPosAniCheck)
        velPlotCheck = self.findChild(QCheckBox, projMotVelPlotCheck)
        velAniCheck = self.findChild(QCheckBox, projMotVelAniCheck)
        # Boxes array
        arr = [posPlotCheck, posAniCheck, velPlotCheck, velAniCheck]
        # Set to checked
        for i in range(len(arr)):
            arr[i].setChecked(True)
    
    """ UnselectAllPlots - Unselects all plot options
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab the checkbox children
            * Create an array for the checkbox children
            * Set all the children to unchecked
        Output:
            This function does not return a value
    """
    def UnselectAllPlots(self):
        posPlotCheck = self.findChild(QCheckBox, projMotPosPlotCheck)
        posAniCheck = self.findChild(QCheckBox, projMotPosAniCheck)
        velPlotCheck = self.findChild(QCheckBox, projMotVelPlotCheck)
        velAniCheck = self.findChild(QCheckBox, projMotVelAniCheck)
        arr = [posPlotCheck, posAniCheck, velPlotCheck, velAniCheck]
        for i in range(len(arr)):
            arr[i].setChecked(False)

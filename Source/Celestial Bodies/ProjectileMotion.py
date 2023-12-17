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
# projMotCommonObjectDD = "Common Object Dropdown"
# projMotCommonObjInitPos = "Common Object Projectile Initial Position"
# projMotCommonObjInitVel = "Common Object Projectile Initial Velocity"
# projMotCommonObjInitTime = "Common Object Initial Time"
# projMotCommonObjFinalTime = "Common Object Final Time"
# projMotCommonObjClearParamBtn = "Clear Common Parameters"
# projMotCommonObjRandBtn = "Randomize Common Parameters"
# projMotCustomObjMass = "Custom Object Mass"
# projMotCustomObjRadius = "Custom Object Radius"
# projMotCustomObjInitPos = "Custom Object Projectile Initial Position"
# projMotCustomObjInitVel = "Custom Object Projectile Initial Velocity"
# projMotCustomObjInitTime = "Custom Object Initial Time"
# projMotCustomObjFinalTime = "Custom Object Final Time"
# projMotCustomObjClearParamBtn = "Clear Custom Parameters"
# projMotCustomObjRandBtn = "Randomize Custom Parameters"
# projMotPosPlotCheck = "2D Position Plot Checkbox"
# projMotPosAniCheck = "2D Position Animation Checkbox"
# projMotVelPlotCheck = "2D Velocity Plot Checkbox"
# projMotVelAniCheck = "2D Velocity Animation Checkbox"
# projMotCBSelectAll = "Select All Projectile Motion Plots"
# projMotCBUnselectAll = "Unselect All Projectile Motion Plots"
# projMotCalculateBtn = "2D Calculate Button"
# projMotClearBtn = "2D Clear Button"
# projMotMainWinBtn = "Return Home"

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

    """ ClearIC - Clear initial conditions parameters
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab the children from the fields
            * Iterate over the widgets in the initial conditions fields
                * Clear the line edits
                * Set the clear button to disabled
        Output:
            This function does not return a value
    """
    def ClearIC(self):
        # Grab children
        children = self.GrabChildren()
        # Iterate over widgets
        for widget in children[1]:
            if isinstance(widget, QLineEdit):
                widget.setText("")
                widget.setDisabled(True)
            elif isinstance(widget, QPushButton):
                if (widget == children[1][4]):
                    widget.setDisabled(True)

    """ ClearObj - Clear object field parameters
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab the children from the fields
            * Iterate over the widgets in the object selection fields
                * Set the combo box index to 0
                * Clear the line edits
                * Set the clear button to disabled
        Output:
            This function does not return a value
    """
    def ClearObj(self):
        # Grab children
        children = self.GrabChildren()
        # Iterate over widgets
        for widget in children[0]:
            if isinstance(widget, QComboBox):
                widget.setCurrentIndex(0)
            elif isinstance(widget, QLineEdit):
                widget.setText("")
                widget.setDisabled(True)
            elif isinstance(widget, QPushButton):
                if (widget == children[0][4]):
                    widget.setDisabled(True)
    
    """ GrabChildren - Grabs the children from the window
        Input:
            There are no unique input parameters for this function
        Algorithm:
            * Grab object selection children, add them to an array
            * Grab initial condition children, add them to an array
            * Grab plot selection children, add them to an array
            * Grab main button children, add them to an array
        Output:
            objArr - Array of object selection fields / buttons
                objArr[0] - Object selection combo box
                objArr[1] - Object selection mass line edit
                objArr[2] - Object selection radius line edit
                objArr[3] - Object selection name
                objArr[4] - Object selection clear parameters button
                objArr[5] - Object selection random parameters button
            icArr - Array of initial conditions fields / buttons
                icArr[0] - Initial condition initial vertical position line edit
                icArr[1] - Initial condition initial vertical velocity line edit
                icArr[2] - Initial condition time span line edit
                icArr[3] - Initial condition projectile name line edit
                icArr[4] - Initial condition clear parameters button
                icArr[5] - Initial condition random parameters button
            plotSelection - Array of plot selection check boxes / buttons
                plotSelection[0] - Plot selection 2D position plot check box
                plotSelection[1] - Plot selection 2D position animation check box
                plotSelection[2] - Plot selection 2D velocity plot check box
                plotSelection[3] - Plot selection 2D velocity animation check box
                plotSelection[4] - Plot selection select all button
                plotSelection[5] - Plot selection unselect all button
            mainButtons - Array of main button buttons
                mainButtons[0] - Main buttons calculate button
                mainButtons[1] - Main buttons clear button
                mainButtons[2] - Main buttons randomize button
                mainButtons[3] - Main buttons home button
    """
    def GrabChildren(self):
        # Object selection children
        objCB = self.findChild(QComboBox, objSelCBName)
        objMass = self.findChild(QLineEdit, objSelMassLEName)
        objRad = self.findChild(QLineEdit, objSelRadLEName)
        objName = self.findChild(QLineEdit, objSelName)
        objClear = self.findChild(QPushButton, objSelClearBtnName)
        objRand = self.findChild(QPushButton, objSelRandBtnName)
        objArr = [objCB, objMass, objRad, objName, objClear, objRand]
        # Initial condition children
        icInitPos = self.findChild(QLineEdit, icInitPosName)
        icInitVel = self.findChild(QLineEdit, icInitVelName)
        icTimeSpan = self.findChild(QLineEdit, icTimeSpanName)
        projName = self.findChild(QLineEdit, icProjName)
        icClear = self.findChild(QPushButton, icClearBtnName)
        icRand = self.findChild(QPushButton, icRandBtnName)
        icArr = [icInitPos, icInitVel, icTimeSpan, projName, icClear, icRand]
        # Plot selection children
        posPlot = self.findChild(QCheckBox, plotSelPosPlotCBName)
        posAni = self.findChild(QCheckBox, plotSelPosAniCBName)
        velPlot = self.findChild(QCheckBox, plotSelVelPlotCBName)
        velAni = self.findChild(QCheckBox, plotSelVelAniCBName)
        selAll = self.findChild(QPushButton, plotSelSelAllBtnName)
        unSelAll = self.findChild(QPushButton, plotSelUnselAllBtnName)
        plotSelection = [posPlot, posAni, velPlot, velAni, selAll, unSelAll]
        # Main button children
        calc = self.findChild(QPushButton, calcBtnName)
        clear = self.findChild(QPushButton, clearBtnName)
        rand = self.findChild(QPushButton, randomBtnName)
        home = self.findChild(QPushButton, homeBtnName)
        mainButtons = [calc, clear, rand, home]
        return objArr, icArr, plotSelection, mainButtons
        
    def InitUI(self):
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
        objSelMassLE.setDisabled(True)
        objSelLayout.addWidget(objSelMassLE, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Object selection radius line edit
        objSelRadLE = QLineEdit()
        objSelRadLE.setObjectName(objSelRadLEName)
        objSelRadLE.setMinimumWidth(lineEditMinWidth)
        objSelRadLE.setMinimumHeight(lineEditMinHeight)
        objSelRadLE.setPlaceholderText("Enter radius of object in (m)")
        objSelRadLE.setDisabled(True)
        objSelLayout.addWidget(objSelRadLE, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Object selection name line edit
        objSelNameLE = QLineEdit()
        objSelNameLE.setObjectName(objSelName)
        objSelNameLE.setMinimumWidth(lineEditMinWidth)
        objSelNameLE.setMinimumHeight(lineEditMinHeight)
        objSelNameLE.setPlaceholderText("Enter name of object")
        objSelNameLE.setDisabled(True)
        objSelLayout.addWidget(objSelNameLE, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Object selection clear parameters button
        objSelClearBtn = QPushButton("Clear Parameters")
        objSelClearBtn.setObjectName(objSelClearBtnName)
        objSelClearBtn.setMinimumWidth(buttonMinWidth)
        objSelClearBtn.setMinimumHeight(buttonMinHeight)
        objSelClearBtn.setDisabled(True)
        objSelClearBtn.clicked.connect(self.ClearObj)
        objSelLayout.addWidget(objSelClearBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Object selection randomize parameters button
        objSelRandBtn = QPushButton("Random Object")
        objSelRandBtn.setObjectName(objSelRandBtnName)
        objSelRandBtn.setMinimumWidth(buttonMinWidth)
        objSelRandBtn.setMinimumHeight(buttonMinHeight)
        objSelRandBtn.clicked.connect(self.RandomObj)
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
        icInitPosLE.setDisabled(True)
        icLayout.addWidget(icInitPosLE, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Initial conditions initial velocity line edit
        icInitVelLE = QLineEdit()
        icInitVelLE.setObjectName(icInitVelName)
        icInitVelLE.setMinimumWidth(lineEditMinWidth)
        icInitVelLE.setMinimumHeight(lineEditMinHeight)
        icInitVelLE.setPlaceholderText("Enter initial velocity in (m/s)")
        icInitVelLE.setDisabled(True)
        icLayout.addWidget(icInitVelLE, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Initial conditions time span line edit
        icTimeSpanLE = QLineEdit()
        icTimeSpanLE.setObjectName(icTimeSpanName)
        icTimeSpanLE.setMinimumWidth(lineEditMinWidth)
        icTimeSpanLE.setMinimumHeight(lineEditMinHeight)
        icTimeSpanLE.setPlaceholderText("Enter time span of model in (s)")
        icTimeSpanLE.setDisabled(True)
        icLayout.addWidget(icTimeSpanLE, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Initial conditions projectile name line edit
        icProjNameLE = QLineEdit()
        icProjNameLE.setObjectName(icProjName)
        icProjNameLE.setMinimumWidth(lineEditMinWidth)
        icProjNameLE.setMinimumHeight(lineEditMinHeight)
        icProjNameLE.setPlaceholderText("Enter name of projectile")
        icProjNameLE.setDisabled(True)
        icLayout.addWidget(icProjNameLE, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Initial conditions clear parameters button
        icClearBtn = QPushButton("Clear Parameters")
        icClearBtn.setObjectName(icClearBtnName)
        icClearBtn.setMinimumWidth(buttonMinWidth)
        icClearBtn.setMinimumHeight(buttonMinHeight)
        icClearBtn.setDisabled(True)
        icClearBtn.clicked.connect(self.ClearIC)
        icLayout.addWidget(icClearBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Initial conditions random parameters button
        icRandBtn = QPushButton("Random Initial Conditions")
        icRandBtn.setObjectName(icRandBtnName)
        icRandBtn.setMinimumWidth(buttonMinWidth)
        icRandBtn.setMinimumHeight(buttonMinHeight)
        icRandBtn.clicked.connect(self.RandomIC)
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
        plotSelPosPlotCB.setDisabled(True)
        plotCheckLayout.addWidget(plotSelPosPlotCB)
        #### 2D Position Animation
        plotSelPosAniCB = QCheckBox("2D Position Animation")
        plotSelPosAniCB.setObjectName(plotSelPosAniCBName)
        plotSelPosAniCB.setDisabled(True)
        plotCheckLayout.addWidget(plotSelPosAniCB)
        #### 2D Velocity Plot
        plotSelVelPlotCB = QCheckBox("2D Velocity Plot")
        plotSelVelPlotCB.setObjectName(plotSelVelPlotCBName)
        plotSelVelPlotCB.setDisabled(True)
        plotCheckLayout.addWidget(plotSelVelPlotCB)
        #### 2D Velocity Animation
        plotSelVelAniCB = QCheckBox("2D Velocity Animation")
        plotSelVelAniCB.setObjectName(plotSelVelAniCBName)
        plotSelVelAniCB.setDisabled(True)
        plotCheckLayout.addWidget(plotSelVelAniCB)
        ### Plot selection select all button
        plotSelSelAllBtn = QPushButton("Select All Plots")
        plotSelSelAllBtn.setObjectName(plotSelSelAllBtnName)
        plotSelSelAllBtn.setMinimumWidth(buttonMinWidth)
        plotSelSelAllBtn.setMinimumHeight(buttonMinHeight)
        plotSelSelAllBtn.setDisabled(True)
        plotButtonLayout.addWidget(plotSelSelAllBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Plot selection unselect all button
        plotSelUnselAllBtn = QPushButton("Unselect All Plots")
        plotSelUnselAllBtn.setObjectName(plotSelUnselAllBtnName)
        plotSelUnselAllBtn.setMinimumWidth(buttonMinWidth)
        plotSelUnselAllBtn.setMinimumHeight(buttonMinHeight)
        plotSelUnselAllBtn.setDisabled(True)
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
        calculateBtn.setDisabled(True)
        mainButtonsBtnLayout.addWidget(calculateBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Main buttons clear button
        clearBtn = QPushButton("Clear All")
        clearBtn.setObjectName(clearBtnName)
        clearBtn.setMinimumWidth(buttonMinWidth - 50)
        clearBtn.setMinimumHeight(buttonMinHeight)
        clearBtn.setDisabled(True)
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
        homeBtn.clicked.connect(self.ReturnHome)
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

    """ RandomIC - Randomizes initial conditions
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab children from text fields
            * Rename children for the object selection
            * Generate random values for the initial conditions fields
            * Enable children in the object selection and initial conditions fields
        Output:
            This function does not return a value
    """
    def RandomIC(self):
        # Grab children
        children = self.GrabChildren()
        # Rename children
        initPos = children[1][0]
        initVel = children[1][1]
        timeSpan = children[1][2]
        projName = children[1][3]
        # Randomize children values
        initPos.setText(str(round(random.uniform(random.uniform(-2000, 0), random.uniform(0, 2000)), 2)))
        initVel.setText(str(round(random.uniform(random.uniform(-1000, 0), random.uniform(0, 1000)), 2)))
        timeSpan.setText(str(random.randint(random.randint(5, 15), random.randint(15, 30))))
        projName.setText(str("Projectile"))
        for widgets in children[0:2]:
            for widget in widgets:
                widget.setEnabled(True)

    """ RandomObj - Randomizes object selection parameters
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab children from text fields
            * Rename children for the object selection
            * Generate a random integer
            * If it is divisible by 2
                * Generate random parameters from common objects
            * If it is not
                * Generate arbitrary random parameters for custom objects
            * Enable children in the object selection and initial conditions fields
        Output:
            This function does not return a value
    """
    def RandomObj(self):
        # Grab children
        children = self.GrabChildren()
        # Rename children
        comboBox = children[0][0]
        massLE = children[0][1]
        radiusLE = children[0][2]
        objName = children[0][3]
        # Generate random integer
        randVal = random.randint(0,1000000)
        # Generate random common parameters
        if (randVal % 2 == 0):
            for widget in children[0]:
                if isinstance(widget, QComboBox):
                    widget.setCurrentIndex(0)
                elif isinstance(widget, QLineEdit):
                    widget.setText("")
            cbIndex = random.randint(2, 12)
            comboBox.setCurrentIndex(cbIndex)
            massLE.setText(str(MASSESARR[cbIndex - 2]))
            radiusLE.setText(str(RADIUSARR[cbIndex - 2]))
            objName.setText(str(comboBox.currentText()))
        # Generate random custom parameters
        else:
            for widget in children[0]:
                if isinstance(widget, QComboBox):
                    widget.setCurrentIndex(0)
                elif isinstance(widget, QLineEdit):
                    widget.setText("")
            cbIndex = random.randint(2, 12)
            comboBox.setCurrentIndex(1)
            massLE.setText(str(round(random.uniform(random.uniform(0.01,0.99) * MASSESARR[cbIndex - 2], random.uniform(1.00, 10.0) * MASSESARR[cbIndex - 2]), 2)))
            radiusLE.setText(str(round(random.uniform(random.uniform(0.01,0.99) * RADIUSARR[cbIndex - 2], random.uniform(1.00, 10.0) * RADIUSARR[cbIndex - 2]), 2)))
            objName.setText(str(comboBox.currentText()))
        # Enable children
        for widgets in children[0:2]:
            for widget in widgets:
                widget.setEnabled(True)

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

    # """ Calculate - Assigns parameters of input fields to be fed to the projectile motion solver
    #     Input:
    #         There are not unique input parameters for this function
    #     Algorithm:
    #         * Grab the children from the parameters and plot selection input fields
    #         * Create parameters that are to be returned from the calculation
    #         * Check if the common field parameters are the only parameters entered
    #             * Get the values from the children in the input fields
    #             * Assign the proper values to obj for the parameter that was selected
    #                 * obj[0] - Object's mass
    #                 * obj[1] - Object's radius
    #             * Assign the return parameters to the other input fields
    #                 * ic[0] - Projectile's initial vertical position
    #                 * ic[1] - Projectile's initial vertical velocity
    #         * Check if the custom field parameters are the only parameters entered
    #             * Get the values from the children in the input fields
    #             * Assign the return parameters to the input fields
    #         * Otherwise, create a dialog box that tells the user they have incorrectly entered parameters
    #         * Return the parameters to be fed to the model
    #     Output:
    #         obj - Array of object parameters
    #             obj[0] - Object's mass
    #             obj[1] - Object's radius
    #         ic - Array of initial conditions of projectile
    #             ic[0] - Initial vertical position
    #             ic[1] - Initial vertical velocity
    #         initTime - Initial time of model
    #         finTime - Final time of model
    #         objectName - Name of object
    # """
    # def Calculate(self):
    #     # Grab children from input fields
    #     children = self.GrabChildren()
    #     # Parameters to be fed into solver
    #     obj = []
    #     objName = ""
    #     ic = []
    #     initPos = 0
    #     initVel = 0
    #     initTime = 0
    #     finTime = 0
    #     commonEntered = (any(isinstance(widget, QComboBox) and widget.currentText() != "Select Common Object" for widget in children[0]) and all(isinstance(widget, QLineEdit) and widget.text() != "" for widget in children[0][1:5]))
    #     customEntered = (all(isinstance(widget, QLineEdit) and widget.text() != "" for widget in children[1][0:6]))
    #     # Common field entered, custom not
    #     if (commonEntered):
    #         objectSelection = children[0][0].currentText()
    #         initialPos = float(children[0][1].text())
    #         initialVel = float(children[0][2].text())
    #         initialTime = float(children[0][3].text())
    #         finalTime = float(children[0][4].text())
    #         # Assign object parameters
    #         if (objectSelection == "Sun"):
    #             obj.append(MSUN)
    #             obj.append(RSUN)
    #         elif (objectSelection == "Mercury"):
    #             obj.append(MMERCURY)
    #             obj.append(RMERCURY)
    #         elif (objectSelection == "Venus"):
    #             obj.append(MVENUS)
    #             obj.append(RVENUS)
    #         elif (objectSelection == "Earth"):
    #             obj.append(MEARTH)
    #             obj.append(REARTH)
    #         elif (objectSelection == "Moon"):
    #             obj.append(MMOON)
    #             obj.append(RMOON)
    #         elif (objectSelection == "Mars"):
    #             obj.append(MMARS)
    #             obj.append(RMARS)
    #         elif (objectSelection == "Jupiter"):
    #             obj.append(MJUPITER)
    #             obj.append(RJUPITER)
    #         elif (objectSelection == "Saturn"):
    #             obj.append(MSATURN)
    #             obj.append(RSATURN)
    #         elif (objectSelection == "Uranus"):
    #             obj.append(MURANUS)
    #             obj.append(RURANUS)
    #         elif (objectSelection == "Neptune"):
    #             obj.append(MNEPTUNE)
    #             obj.append(RNEPTUNE)
    #         elif (objectSelection == "Pluto"):
    #             obj.append(MPLUTO)
    #             obj.append(RPLUTO)
    #         objName = objectSelection
    #         # Assign return values to input field values
    #         initPos = initialPos
    #         initVel = initialVel
    #         ic.append(initPos)
    #         ic.append(initVel)
    #         initTime = initialTime
    #         finTime = finalTime
    #         return obj, ic, initTime, finTime, objName
    #     # Custom field entered, common not
    #     elif (commonEntered == False and customEntered == True):
    #         # Convert input fields to correct data type
    #         objectMass = float(children[1][0].text())
    #         objectRadius = float(children[1][1].text())
    #         initialPos = float(children[1][2].text())
    #         initialVel = float(children[1][3].text())
    #         initialTime = float(children[1][4].text())
    #         finalTime = float(children[1][5].text())
    #         # Assign object parameters
    #         obj.append(objectMass)
    #         obj.append(objectRadius)
    #         objName = "Arbitrary Mass"
    #         # Assign return values to input field values
    #         initPos = initialPos
    #         initVel = initialVel
    #         ic.append(initPos)
    #         ic.append(initVel)
    #         initTime = initialTime
    #         finTime = finalTime
    #         return obj, ic, initTime, finTime, objName
    #     # Invalid entries
    #     else:
    #         dialogBox = QDialog(self)
    #         dialogBox.setWindowTitle("Invalid Entries")
    #         dialogBox.setFixedSize(400, 75)
    #         warningLabel = QLabel("Please enter in all values in the given fields.", dialogBox)
    #         warningFont = warningLabel.font()
    #         warningFont.setPointSize(13)
    #         warningLabel.setFont(warningFont)
    #         warningLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    #         layout = QVBoxLayout()
    #         layout.addWidget(warningLabel)
    #         dialogBox.setLayout(layout)
    #         dialogBox.exec()
    #         return None, None, None, None, None
    
    # """ ClearAllInputs - Clears all the inputs of the window
    #     Input:
    #         This function does not have any unique input parameters
    #     Algorithm:
    #         * Call the member functions for all of the input fields
    #     Output:
    #         This function does not return a value
    # """
    # def ClearAllInputs(self):
    #     # Call functions
    #     self.ClearCommonParam()
    #     self.ClearCustomParam()
    #     self.UnselectAllPlots()

    # """ CommmonObjChanged - Enables / Disables and resets children based on index of the combo box
    #     Input:
    #         index - Index of the common object combo box
    #     Algorithm:
    #         * Grab the children from the window
    #         * If the combo box index is currently zero
    #             * Disable and reset the common parameters children
    #             * Disable and reset the custom parameters children
    #             * Disable and reset the Plot selection / Main buttons children
    #         * If the combo box is another index
    #             * Enable the common parameters children
    #             * Disable and reset the custom parameters children
    #             * Enable the Plot selection / Main buttons children
    #     Output:
    #         This function does not return a value
    # """
    # def CommmonObjChanged(self, index):
    #     # Grab children
    #     children = self.GrabChildren()
    #     # Index zero
    #     if (index == 0):
    #         ## Reset common
    #         for widget in children[0]:
    #             if isinstance(widget, QLineEdit):
    #                 widget.setText("")
    #                 widget.setDisabled(True)
    #             if isinstance(widget, QPushButton):
    #                 if (widget.objectName() == projMotCommonObjRandBtn):
    #                     widget.setEnabled(True)
    #                 else:
    #                     widget.setDisabled(True)
    #         ## Reset custom 
    #         for widget in children[1]:
    #             if isinstance(widget, QLineEdit):
    #                 widget.setText("")
    #                 if ((widget.objectName() == projMotCustomObjMass) or (widget.objectName() == projMotCustomObjRadius)):
    #                     widget.setEnabled(True)
    #                 else:
    #                     widget.setDisabled(True)
    #             if isinstance(widget, QPushButton):
    #                 if (widget.objectName() == projMotCustomObjRandBtn):
    #                     widget.setEnabled(True)
    #                 else:
    #                     widget.setDisabled(True)
    #         ## Reset Plot selection / Main buttons 
    #         for widgets in children[2:]:
    #             for widget in widgets:
    #                 if isinstance(widget, QCheckBox):
    #                     widget.setChecked(False)
    #                 widget.setDisabled(True)
    #     # Other index
    #     else:
    #         ## Enable common
    #         for widget in children[0]:
    #             widget.setEnabled(True)
    #         ## Disable custom
    #         for widget in children[1]:
    #             if isinstance(widget, QLineEdit):
    #                 widget.setText("")
    #             widget.setDisabled(True)
    #         ## Enable Plot selection / Main buttons
    #         for widgets in children[2:]:
    #             for widget in widgets:
    #                 widget.setEnabled(True)

    # """ OpenPlot - Opens a window for a given plot
    #     Input:
    #         This function does not have any unique input parameters
    #     Algorithm:
    #         * Call the calculate member function
    #         * Grab the children for the checkboxes
    #         * Check for if a specific checkbox checked
    #             * If it is, create a canvas with the parameters returned from Calculate for the type of plot
    #                 * 0 - 2D Position versus time plot
    #                 * 1 - 2D Position versus time animation
    #                 * 2 - 2D Velocity versus time plot
    #                 * 3 - 2D Velocity versus time animation
    #             * If no boxes are checked, generate a dialog window that tells the user they need to select a plot
    #     Output:
    #         This function does not return a value
    # """
    # def OpenPlot(self):
    #     # Call calculate
    #     calc = self.Calculate()
    #     # Check for not none
    #     if all(values is not None for values in calc):        
    #         # Grab children
    #         children = self.GrabChildren()
    #         # Position Plot
    #         if (children[2][0].isChecked() == True):
    #             self.posPlot = ProjectileMotionPlotWindow(0, calc[0], calc[1], calc[2], calc[3], calc[4], "Projectile", "Projectile Motion Plot: Position Vs. Time")
    #             self.posPlot.show()
    #         # Position Animation
    #         if (children[2][1].isChecked() == True):
    #             self.posAni = ProjectileMotionPlotWindow(1, calc[0], calc[1], calc[2], calc[3], calc[4], "Projectile", "Projectile Motion Animation: Position Vs. Time")
    #             self.posAni.show()
    #         # Velocity Plot
    #         if (children[2][2].isChecked() == True):
    #             self.velPlot = ProjectileMotionPlotWindow(2, calc[0], calc[1], calc[2], calc[3], calc[4], "Projectile", "Projectile Motion Plot: Velocity Vs. Time")
    #             self.velPlot.show()
    #         # Velocity Animation
    #         if (children[2][3].isChecked() == True):
    #             self.velAni = ProjectileMotionPlotWindow(3, calc[0], calc[1], calc[2], calc[3], calc[4], "Projectile", "Projectile Motion Animation: Velocity Vs. Time")
    #             self.velAni.show()
    #         # No boxes checked
    #         if (children[2][0].isChecked() == False and children[2][1].isChecked() == False and children[2][2].isChecked() == False and children[2][3].isChecked() == False):
    #             dialogBox = QDialog(self)
    #             dialogBox.setWindowTitle("Invalid Entries")
    #             dialogBox.setFixedSize(400, 75)
    #             warningLabel = QLabel("Please select plot(s) for entered input values.", dialogBox)
    #             warningFont = warningLabel.font()
    #             warningFont.setPointSize(13)
    #             warningLabel.setFont(warningFont)
    #             warningLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    #             layout = QVBoxLayout()
    #             layout.addWidget(warningLabel)
    #             dialogBox.setLayout(layout)
    #             dialogBox.exec()

    # """ SelectAllPlots - Selects all plot options
    #     Input:
    #         This function does not have any unique input parameters
    #     Algorithm:
    #         * Grab the checkbox children
    #         * Create an array for the checkbox children
    #         * Set all the children to checked
    #     Output:
    #         This function does not return a value
    # """
    # def SelectAllPlots(self):
    #     # Grab children
    #     posPlotCheck = self.findChild(QCheckBox, projMotPosPlotCheck)
    #     posAniCheck = self.findChild(QCheckBox, projMotPosAniCheck)
    #     velPlotCheck = self.findChild(QCheckBox, projMotVelPlotCheck)
    #     velAniCheck = self.findChild(QCheckBox, projMotVelAniCheck)
    #     # Boxes array
    #     arr = [posPlotCheck, posAniCheck, velPlotCheck, velAniCheck]
    #     # Set to checked
    #     for i in range(len(arr)):
    #         arr[i].setChecked(True)
    
    # """ UnselectAllPlots - Unselects all plot options
    #     Input:
    #         This function does not have any unique input parameters
    #     Algorithm:
    #         * Grab the checkbox children
    #         * Create an array for the checkbox children
    #         * Set all the children to unchecked
    #     Output:
    #         This function does not return a value
    # """
    # def UnselectAllPlots(self):
    #     posPlotCheck = self.findChild(QCheckBox, projMotPosPlotCheck)
    #     posAniCheck = self.findChild(QCheckBox, projMotPosAniCheck)
    #     velPlotCheck = self.findChild(QCheckBox, projMotVelPlotCheck)
    #     velAniCheck = self.findChild(QCheckBox, projMotVelAniCheck)
    #     arr = [posPlotCheck, posAniCheck, velPlotCheck, velAniCheck]
    #     for i in range(len(arr)):
    #         arr[i].setChecked(False)

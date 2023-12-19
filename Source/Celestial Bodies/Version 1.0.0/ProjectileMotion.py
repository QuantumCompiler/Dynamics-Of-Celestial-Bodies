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
            minPos = min(position)
            maxPos = max(position)
            self.axes.set_xlim(-0.05 * max(time), 1.05 * max(time))
            if (minPos < 0):
                self.axes.set_ylim(1.05 * minPos, 1.05 * maxPos)
            elif (minPos == 0):
                self.axes.set_ylim(-0.05 * maxPos, 1.05 * maxPos)
            else:
                self.axes.set_ylim(-0.05 * minPos, 1.05 * maxPos)
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
            # Max and min of axes
            minVel = min(velocity)
            maxVel = max(velocity)
            self.axes.set_xlim(-0.05 * max(time), 1.05 * max(time))
            if (minVel < 0):
                self.axes.set_ylim(1.05 * minVel, 1.05 * maxVel)
            elif (minVel == 0):
                self.axes.set_ylim(-0.05 * maxVel, 1.05 * maxVel)
            else:
                self.axes.set_ylim(-0.05 * minVel, 1.05 * maxVel)
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
        self.setMinimumHeight(400)
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
        
""" ProjectileMotionWindow - Window for the projectile motion simulation
    Member Functions:
        Constructor - Constructs window with widgets and layouts of widgets
        Calculate - Generates the plots for projectile motion
        CheckAllCB - Check all checkboxes
        CheckAllInputs - Check if all necessary inputs have been entered
        ClearAll - Clears all input fields
        ClearIC - Clear initial conditions parameters
        ClearObj - Clear object field parameters
        GrabChildren - Grabs the children from the window
        InitUI - Initializes UI with layouts and widgets
        IsNum - Checks to see if an input is able to be converted to a number
        IsPositive - Checks if a number is positive
        ObjectOnChange - Modifies input parameters based upon field values
        RandomAll - Randomize all input fields
        RandomCB - Randomizes checkboxes to be selected
        RandomIC - Randomizes initial conditions
        RandomObj - Randomizes object selection parameters
        ReturnHome - Returns home and closes the current window
        UnselectAllCB - Unselect all checkboxes
"""
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
plotSelRandBtnName = "Select Random Check Boxes"
plotSelUnselAllBtnName = "Unselect All Plots"
calcBtnName = "Calculate"
clearBtnName = "Clear"
randomBtnName = "Random"
homeBtnName = "Home"

class ProjectileMotionWindow(QWidget):
    """ Constructor - Constructs window with widgets and layouts of widgets
        Input:
            mainWindow - The main window of the application
        Algorithm:
            * Call the init ui function
        Output:
            This function does not return a value
    """
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.InitUI()

    """ Calculate - Generates the plots for projectile motion
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab children from the fields
            * Grab input fields from window
            * Add some of the values to arrays
            * Generate plots depending upon what checkboxes are checked
        Output:
            This function does not return a value
    """
    def Calculate(self):
        # Grab children
        children = self.GrabChildren()
        # Values from fields
        objSel = []
        icSel = []
        # Valid object selection
        for widget in children[0][1:3]:
            widVal1 = self.IsNum(widget.text())
            if (widVal1 == True):
                widVal2 = self.IsPositive(float(str(widget.text())))
                objSel.append(widVal2)
            else:
                objSel.append(widVal)
        # Valid initial conditions
        for widget in children[1][0:3]:
            widVal1 = self.IsNum(widget.text())
            if (widVal1 == True):
                if (widget == children[1][2]):
                    widVal2 = self.IsPositive(float(str(widget.text())))
                    icSel.append(widVal2)
                else:
                    continue
            else:
                icSel.append(widVal1)
        objects = all(val == True for val in objSel)
        initialCondtions = all(val == True for val in icSel)
        # Valid inputs
        if (objects and initialCondtions):
            mass = float(str(children[0][1].text()))
            radius = float(str(children[0][2].text()))
            objName = str(children[0][3].text())
            initPos = float(str(children[1][0].text()))
            initVel = float(str(children[1][1].text()))
            timeSpan = float(str(children[1][2].text()))
            projName = str(children[1][3].text())
            posPlot = children[2][0]
            posAni = children[2][1]
            velPlot = children[2][2]
            velAni = children[2][3]
            # Casting values for functions
            objArr = [mass, radius]
            icArr = [initPos, initVel]
            # Plot(s)
            if (posPlot.isChecked() == True):
                self.posPlot = ProjectileMotionPlotWindow(0, objArr, icArr, 0, timeSpan, objName, projName, "Projectile Motion Plot: Position Vs. Time")
                self.posPlot.show()
            if (posAni.isChecked() == True):
                self.posAni = ProjectileMotionPlotWindow(1, objArr, icArr, 0, timeSpan, objName, projName, "Projectile Motion Animation: Position Vs. Time")
                self.posAni.show()
            if (velPlot.isChecked() == True):
                self.velPlot = ProjectileMotionPlotWindow(2, objArr, icArr, 0, timeSpan, objName, projName, "Projectile Motion Plot: Velocity Vs. Time")
                self.velPlot.show()
            if (velAni.isChecked() == True):
                self.velAni = ProjectileMotionPlotWindow(3, objArr, icArr, 0, timeSpan, objName, projName, "Projectile Motion Animation: Velocity Vs. Time")
                self.velAni.show()
        # Invalid inputs
        else:
            if (objects == False):
                dialogBox = QDialog(self)
                dialogBox.setWindowTitle("Invalid Object")
                dialogBox.setFixedSize(400, 75)
                warningLabel = QLabel("Please enter positive values in the object selection field.", dialogBox)
                warningFont = warningLabel.font()
                warningFont.setPointSize(13)
                warningLabel.setFont(warningFont)
                warningLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
                layout = QVBoxLayout()
                layout.addWidget(warningLabel)
                dialogBox.setLayout(layout)
                dialogBox.exec()
            if (initialCondtions == False):
                dialogBox = QDialog(self)
                dialogBox.setWindowTitle("Invalid Initial Conditions")
                dialogBox.setFixedSize(400, 75)
                warningLabel = QLabel("Please enter a positive nonzero time span.", dialogBox)
                warningFont = warningLabel.font()
                warningFont.setPointSize(13)
                warningLabel.setFont(warningFont)
                warningLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
                layout = QVBoxLayout()
                layout.addWidget(warningLabel)
                dialogBox.setLayout(layout)
                dialogBox.exec()

    """ CheckAllCB - Check all checkboxes
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab all the children from the fields
            * Set all checkboxes to checked
        Output:
            This function does not return a value
    """
    def CheckAllCB(self):
        # Grab children
        children = self.GrabChildren()
        # Set CBs to true
        for widget in children[2][0:5]:
            widget.setChecked(True)

    """ CheckAllInputs - Check if all necessary inputs have been entered
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab the children from the input fields
            * Check for valid inputs in combo box, object selection, initial conditions, and check boxes
            * Enable fields as previous fields are fully complete
        Output:
            This function does not return a value
    """
    def CheckAllInputs(self):
        # Grab children
        children = self.GrabChildren()
        # Valid inputs
        comboBoxValid = children[0][0].currentIndex() != 0
        objectSelValid = all(isinstance(widget, QLineEdit) and widget.text() != "" for widget in children[0][1:4])
        initConValid = all(isinstance(widget, QLineEdit) and widget.text() != "" for widget in children[1][0:4])
        checkBoxValid = any(isinstance(widget, QCheckBox) and widget.isChecked() == True for widget in children[2][0:5])
        # Combo box invalid
        if (comboBoxValid == False):
            self.ClearObj()
            self.ClearIC()
            self.UnselectAllCB()
            for widget in children[0]:
                if (widget == children[0][0] or widget == children[0][-1]):
                    widget.setEnabled(True)
                else:
                    widget.setDisabled(True)
            for widget in children[1]:
                if (widget == children[1][-1]):
                    widget.setEnabled(True)
                else:
                    widget.setDisabled(True)
        # Object selection valid
        if (objectSelValid == True):
            for widget in children[1]:
                widget.setEnabled(True)
        else:
            for widget in children[1]:
                if (widget != children[1][-1]):
                    widget.setDisabled(True)
                else:
                    widget.setEnabled(True)
        # Object selection and initial conditions valid
        if (objectSelValid == True and initConValid == True):
            for widget in children[2]:
                widget.setEnabled(True)
        elif (objectSelValid == False):
            self.UnselectAllCB()
            for widget in children[1]:
                if (widget != children[1][-1]):
                    widget.setDisabled(True)
                else:
                    widget.setEnabled(True)
            for widget in children[2]:
                widget.setDisabled(True)
        elif (initConValid == False):
            self.UnselectAllCB()
            for widget in children[2]:
                widget.setDisabled(True)
        # All fields valid
        if (objectSelValid == True and initConValid == True and checkBoxValid == True):
            children[3][0].setEnabled(True)
        else:
            children[3][0].setDisabled(True)

    """ ClearAll - Clears all input fields
        Input:
            There are not unique input parameters in this function
        Algorithm:
            * Call inner functions
        Output:
            This function does not return a value
    """
    def ClearAll(self):
        self.UnselectAllCB()
        self.ClearIC()
        self.ClearObj()

    """ ClearIC - Clear initial conditions parameters
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab the children from the fields
            * Iterate over the widgets in the initial conditions fields
                * Clear the line edits
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

    """ ClearObj - Clear object field parameters
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab the children from the fields
            * Iterate over the widgets in the object selection fields
                * Set the combo box index to 0
                * Clear the line edits
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
                plotSelection[5] - Plot selection random all button
                plotSelection[6] - Plot selection unselect all button
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
        randAll = self.findChild(QPushButton, plotSelRandBtnName)
        unSelAll = self.findChild(QPushButton, plotSelUnselAllBtnName)
        plotSelection = [posPlot, posAni, velPlot, velAni, selAll, randAll, unSelAll]
        # Main button children
        calc = self.findChild(QPushButton, calcBtnName)
        clear = self.findChild(QPushButton, clearBtnName)
        rand = self.findChild(QPushButton, randomBtnName)
        home = self.findChild(QPushButton, homeBtnName)
        mainButtons = [calc, clear, rand, home]
        return objArr, icArr, plotSelection, mainButtons
        
    """ InitUI - Initializes UI with layouts and widgets
        Input:
            There are no unique input parameters for this function
        Algorithm:
            * Set size of window and title
            * Create layouts
            * Create widgets for each layout
            * Add widgets to layouts
            * Add layouts to main layout
            * Set the main layout
        Output:
            This function does not return a value
    """
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
        ###################################
        ##### Layouts
        ###################################
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
        objSelCB.currentIndexChanged.connect(self.ObjectOnChange)
        objSelCB.currentIndexChanged.connect(self.CheckAllInputs)
        objSelLayout.addWidget(objSelCB, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Object selection mass line edit
        objSelMassLE = QLineEdit()
        objSelMassLE.setObjectName(objSelMassLEName)
        objSelMassLE.setMinimumWidth(lineEditMinWidth)
        objSelMassLE.setMinimumHeight(lineEditMinHeight)
        objSelMassLE.setPlaceholderText("Enter mass of object in (Kg)")
        objSelMassLE.setDisabled(True)
        objSelMassLE.textChanged.connect(self.CheckAllInputs)
        objSelLayout.addWidget(objSelMassLE, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Object selection radius line edit
        objSelRadLE = QLineEdit()
        objSelRadLE.setObjectName(objSelRadLEName)
        objSelRadLE.setMinimumWidth(lineEditMinWidth)
        objSelRadLE.setMinimumHeight(lineEditMinHeight)
        objSelRadLE.setPlaceholderText("Enter radius of object in (m)")
        objSelRadLE.setDisabled(True)
        objSelRadLE.textChanged.connect(self.CheckAllInputs)
        objSelLayout.addWidget(objSelRadLE, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Object selection name line edit
        objSelNameLE = QLineEdit()
        objSelNameLE.setObjectName(objSelName)
        objSelNameLE.setMinimumWidth(lineEditMinWidth)
        objSelNameLE.setMinimumHeight(lineEditMinHeight)
        objSelNameLE.setPlaceholderText("Enter name of object")
        objSelNameLE.setDisabled(True)
        objSelNameLE.textChanged.connect(self.CheckAllInputs)
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
        icInitPosLE.textChanged.connect(self.CheckAllInputs)
        icLayout.addWidget(icInitPosLE, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Initial conditions initial velocity line edit
        icInitVelLE = QLineEdit()
        icInitVelLE.setObjectName(icInitVelName)
        icInitVelLE.setMinimumWidth(lineEditMinWidth)
        icInitVelLE.setMinimumHeight(lineEditMinHeight)
        icInitVelLE.setPlaceholderText("Enter initial velocity in (m/s)")
        icInitVelLE.setDisabled(True)
        icInitVelLE.textChanged.connect(self.CheckAllInputs)
        icLayout.addWidget(icInitVelLE, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Initial conditions time span line edit
        icTimeSpanLE = QLineEdit()
        icTimeSpanLE.setObjectName(icTimeSpanName)
        icTimeSpanLE.setMinimumWidth(lineEditMinWidth)
        icTimeSpanLE.setMinimumHeight(lineEditMinHeight)
        icTimeSpanLE.setPlaceholderText("Enter time span of model in (s)")
        icTimeSpanLE.setDisabled(True)
        icTimeSpanLE.textChanged.connect(self.CheckAllInputs)
        icLayout.addWidget(icTimeSpanLE, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Initial conditions projectile name line edit
        icProjNameLE = QLineEdit()
        icProjNameLE.setObjectName(icProjName)
        icProjNameLE.setMinimumWidth(lineEditMinWidth)
        icProjNameLE.setMinimumHeight(lineEditMinHeight)
        icProjNameLE.setPlaceholderText("Enter name of projectile")
        icProjNameLE.setDisabled(True)
        icProjNameLE.textChanged.connect(self.CheckAllInputs)
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
        plotSelPosPlotCB.stateChanged.connect(self.CheckAllInputs)
        plotCheckLayout.addWidget(plotSelPosPlotCB)
        #### 2D Position Animation
        plotSelPosAniCB = QCheckBox("2D Position Animation")
        plotSelPosAniCB.setObjectName(plotSelPosAniCBName)
        plotSelPosAniCB.setDisabled(True)
        plotSelPosAniCB.stateChanged.connect(self.CheckAllInputs)
        plotCheckLayout.addWidget(plotSelPosAniCB)
        #### 2D Velocity Plot
        plotSelVelPlotCB = QCheckBox("2D Velocity Plot")
        plotSelVelPlotCB.setObjectName(plotSelVelPlotCBName)
        plotSelVelPlotCB.setDisabled(True)
        plotSelVelPlotCB.stateChanged.connect(self.CheckAllInputs)
        plotCheckLayout.addWidget(plotSelVelPlotCB)
        #### 2D Velocity Animation
        plotSelVelAniCB = QCheckBox("2D Velocity Animation")
        plotSelVelAniCB.setObjectName(plotSelVelAniCBName)
        plotSelVelAniCB.setDisabled(True)
        plotSelVelAniCB.stateChanged.connect(self.CheckAllInputs)
        plotCheckLayout.addWidget(plotSelVelAniCB)
        ### Plot selection select all button
        plotSelSelAllBtn = QPushButton("Select All Plots")
        plotSelSelAllBtn.setObjectName(plotSelSelAllBtnName)
        plotSelSelAllBtn.setMinimumWidth(buttonMinWidth)
        plotSelSelAllBtn.setMinimumHeight(buttonMinHeight)
        plotSelSelAllBtn.setDisabled(True)
        plotSelSelAllBtn.clicked.connect(self.CheckAllCB)
        plotButtonLayout.addWidget(plotSelSelAllBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Plot selection randomize button
        plotSelRandBtn = QPushButton("Random Plots")
        plotSelRandBtn.setObjectName(plotSelRandBtnName)
        plotSelRandBtn.setMinimumWidth(buttonMinWidth)
        plotSelRandBtn.setMinimumHeight(buttonMinHeight)
        plotSelRandBtn.setDisabled(True)
        plotSelRandBtn.clicked.connect(self.RandomCB)
        plotButtonLayout.addWidget(plotSelRandBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ### Plot selection unselect all button
        plotSelUnselAllBtn = QPushButton("Unselect All Plots")
        plotSelUnselAllBtn.setObjectName(plotSelUnselAllBtnName)
        plotSelUnselAllBtn.setMinimumWidth(buttonMinWidth)
        plotSelUnselAllBtn.setMinimumHeight(buttonMinHeight)
        plotSelUnselAllBtn.setDisabled(True)
        plotSelUnselAllBtn.clicked.connect(self.UnselectAllCB)
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
        calculateBtn.clicked.connect(self.Calculate)
        mainButtonsBtnLayout.addWidget(calculateBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Main buttons clear button
        clearBtn = QPushButton("Clear All")
        clearBtn.setObjectName(clearBtnName)
        clearBtn.setMinimumWidth(buttonMinWidth - 50)
        clearBtn.setMinimumHeight(buttonMinHeight)
        clearBtn.clicked.connect(self.ClearAll)
        mainButtonsBtnLayout.addWidget(clearBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Main buttons random button
        randomBtn = QPushButton("Random All")
        randomBtn.setObjectName(randomBtnName)
        randomBtn.setMinimumWidth(buttonMinWidth - 50)
        randomBtn.setMinimumHeight(buttonMinHeight)
        randomBtn.clicked.connect(self.RandomAll)
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
        ###################################
        ##### Spacers / Set Layout
        ###################################
        # Add layouts
        mainLayout.addLayout(parametersLayout)
        mainLayout.addLayout(plotSelLayout)
        mainLayout.addLayout(mainButtonsLayout)
        # Spacers
        spacer = QSpacerItem(0, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        mainLayout.addSpacerItem(spacer)
        # Set layout
        self.setLayout(mainLayout)

    """ IsNum - Checks to see if an input is able to be converted to a number
        Input:
            string - String value that is trying to be converted to a float
        Algorithm:
            * Try the conversion, if it succeeds, return true
            * Otherwise, return false
        Output:
            This function returns a boolean value for if a value has been successfully converted
    """
    def IsNum(self, string):
        # Try conversion
        try:
            float(string)
            return True
        # Conversion failed
        except ValueError:
            return False

    """ IsPositive - Checks if a number is positive
        Input:
            value - Value that is being checked
        Algorithm:
            * If the value is non zero and positive, return True
            * Otherwise, return False
        Output:
            This function returns a boolean value for if a number is positive
    """
    def IsPositive(self, value):
        if (value > 0):
            return True
        else:
            return False

    """ ObjectOnChange - Modifies input parameters based upon field values
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab children from fields
            * If the combo box is set to the default value
                * Clear the inputs
            * Otherwise
                * Enable all the children
        Output:
            This function does not return a value
    """
    def ObjectOnChange(self):
        # Grab children
        children = self.GrabChildren()
        # Combo box set to default
        if (children[0][0].currentIndex() == 0):
            self.ClearObj()
        # Combo box not set to default
        else:
            currentIndex = children[0][0].currentIndex()
            for widget in children[0]:
                widget.setEnabled(True)
            if (currentIndex != 1):
                children[0][1].setText(str(round(MASSESARR[currentIndex - 2], 2)))
                children[0][2].setText(str(round(RADIUSARR[currentIndex - 2], 2)))
            else:
                children[0][1].setText("")
                children[0][2].setText("")
            children[0][3].setText(str(children[0][0].currentText()))

    """ RandomAll - Randomize all input fields
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Call inner functions
        Output:
            This function does not return a value
    """
    def RandomAll(self):
        # Randomize inner functions
        self.RandomObj()
        self.RandomIC()
        self.RandomCB()

    """ RandomCB - Randomizes checkboxes to be selected
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab children from fields
            * Generate boolean array
            * Iterate over checkboxes
                * If the random integer modulo 2 is 0
                    * Check the current box, add the boolean to the array
                * If otherwise
                    * Don't check the current box, add the boolean to the array
            * Check if all booleans in array are false
                * If they are, choose a random box to check
        Output:
            This function does not return a value
    """
    def RandomCB(self):
        # Grab children
        children = self.GrabChildren()
        # Randomize checkboxes
        boolArr = []
        for widget in children[2][0:4]:
            randInt = random.randint(1,100)
            if (randInt % 2 == 0):
                widget.setChecked(True)
                boolArr.append(True)
            else:
                widget.setChecked(False)
                boolArr.append(False)
        allFalse = all(vals == False for vals in boolArr)
        if (allFalse == True):
            randInt = random.randint(0,3)
            children[2][randInt].setChecked(True)

    """ RandomIC - Randomizes initial conditions
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab children from text fields
            * Rename children for the object selection
            * Generate random values for the initial conditions fields
            * Enable children in the initial conditions fields
        Output:
            This function does not return a value
    """
    def RandomIC(self):
        # Grab children
        children = self.GrabChildren()
        # Valid inputs
        comboBoxValid = children[0][0].currentIndex() != 0
        objectSelValid = all(isinstance(widget, QLineEdit) and widget.text() != "" for widget in children[0][1:4])
        # Rename children
        initPos = children[1][0]
        initVel = children[1][1]
        timeSpan = children[1][2]
        projName = children[1][3]
        # Randomize children values
        if (comboBoxValid == True and objectSelValid == True):
            initPos.setText(str(round(random.uniform(random.uniform(-2000, 0), random.uniform(0, 2000)), 2)))
            initVel.setText(str(round(random.uniform(random.uniform(-1000, 0), random.uniform(0, 1000)), 2)))
            timeSpan.setText(str(random.randint(random.randint(5, 15), random.randint(15, 30))))
            projName.setText(str("Projectile"))
            # Enable initial conditions
            for widget in children[1]:
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

    """ ReturnHome - Returns home and closes the current window
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Open the main window
            * Close the window
        Output:
            This function does not return a values
    """
    def ReturnHome(self):
        self.mainWindow.show()
        self.close()

    """ UnselectAllCB - Unselect all checkboxes
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab all the children from the fields
            * Uncheck all checkboxes
        Output:
            This function does not return a value
    """
    def UnselectAllCB(self):
        # Grab children
        children = self.GrabChildren()
        # Uncheck all CBs
        for widget in children[2][0:5]:
            widget.setChecked(False)
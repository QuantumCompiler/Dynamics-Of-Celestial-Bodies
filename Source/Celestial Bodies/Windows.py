from WindowFunctions import *

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### Main Window
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

# Object Names
ProjectileMotionObjName = "2D Force Button"
TwoBodyObjName = "2 Body Button"
ThreeBodyObjName = "3 Body Button"

""" MainWindow - Main window for application
    Member Functions:
        Constructor - Creates window with widgets and layouts
        CenterWidgetHoriz - Centers a widget horizontally
        OpenProjectileMotionWindow - Opens the projectile motion window
        OpenTwoBodyWindow - Opens the 2 body window
        OpenThreeBodyWindow - Opens the 3 body window
        ResizeEvent - Centers widgets horizontally when window is resized
"""
class MainWindow(QMainWindow):
    """ Constructor - Creates window with widgets and layouts
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Set the title of the window
            * Set the height and width of the window
            * Create the label for the header of the window
            * Create the button for the projectile motion window
            * Create the button for the 2 Body window
            * Create the button for the 3 Body Window
            * Create an empty second window for the other windows
        Output:
            This function does not return a value
    """
    def __init__(self):
        super().__init__()
        # Title of Window
        self.setWindowTitle("Celestial Bodies")
        # Height and Width of Window
        self.resize(800,500)
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        # Header label
        self.headerLabel = QLabel("Choose A Simulation", self)
        self.CenterWidgetHoriz(self.headerLabel)
        headerFont = self.headerLabel.font()
        headerFont.setPointSize(50)
        self.headerLabel.setFont(headerFont)
        self.headerLabel.adjustSize()
        self.headerLabel.move((self.size().width() - self.headerLabel.size().width()) // 2, int(0.05 * self.size().height()))
        # Projectile Motion Button
        self.ProjectileMotionBtn = QPushButton("Projectile Motion", self)
        self.ProjectileMotionBtn.setFixedSize(400, 50)
        self.ProjectileMotionBtn.setObjectName(ProjectileMotionObjName)
        self.ProjectileMotionBtn.clicked.connect(self.OpenProjectileMotionWindow)
        self.CenterWidgetHoriz(self.ProjectileMotionBtn)
        self.ProjectileMotionBtn.move(self.ProjectileMotionBtn.pos().x(), 6 * self.headerLabel.pos().y())
        # 2 Body Button
        self.TwoBodyBtn = QPushButton("2 Body Simulation", self)
        self.TwoBodyBtn.setFixedSize(400, 50)
        self.TwoBodyBtn.setObjectName(TwoBodyObjName)
        self.TwoBodyBtn.clicked.connect(self.OpenTwoBodyWindow)
        self.CenterWidgetHoriz(self.TwoBodyBtn)
        self.TwoBodyBtn.move(self.TwoBodyBtn.pos().x(), self.ProjectileMotionBtn.pos().y() + 50)
        # 3 Body Button
        self.ThreeBodyBtn = QPushButton("3 Body Simulation", self)
        self.ThreeBodyBtn.setFixedSize(400, 50)
        self.ThreeBodyBtn.setObjectName(ThreeBodyObjName)
        self.ThreeBodyBtn.clicked.connect(self.OpenThreeBodyWindow)
        self.CenterWidgetHoriz(self.ThreeBodyBtn)
        self.ThreeBodyBtn.move(self.ThreeBodyBtn.pos().x(), self.TwoBodyBtn.pos().y() + 50)
        # Second window
        self.secondWindow = None
        
    """ CenterWidgetHoriz - Centers a widget horizontally
        Input:
            widget - Qt widget that is to be centered on the window
        Algorithm:
            * Retrieve the current window width
            * Get the width of the widget
            * Get the y position of the widget
            * Center the widget in the window
            * Move the widget to the center of the window
        Output:
            This function does not return a value
    """
    def CenterWidgetHoriz(self, widget):
        windowWidth = self.size().width()
        widgetWidth = widget.size().width()
        widgetYPos = widget.pos().y()
        horizCenter = (windowWidth - widgetWidth) // 2
        widget.move(horizCenter, widgetYPos)

    """ OpenProjectileMotionWindow - Opens the projectile motion window
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Make sure the current window is not the second window made in the constructor
            * Set the second window to the projectile motion window
            * Connect to the main window signal made in the Projectile motion class
            * Open the second window
            * Hide the main window
        Output:
            This function does not return a value
    """
    def OpenProjectileMotionWindow(self):
        if not self.secondWindow:
            self.secondWindow = ProjectileMotionWindow()
        self.secondWindow.mainWindowSignal.connect(self.show)
        self.secondWindow.show()
        self.hide()

    """ OpenTwoBodyWindow - Opens the 2 body window
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Make sure the current window is not the second window made in the constructor
            * Set the second window to the 2 body window
            * Open the second window
            * Hide the main window
        Output:
            This function does not return a value
    """
    def OpenTwoBodyWindow(self):
        if not self.secondWindow:
            self.secondWindow = TwoBodyWindow()
        self.secondWindow.show()
        self.hide()

    """ OpenThreeBodyWindow - Opens the 3 body window
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Make sure the current window is not the second window made in the constructor
            * Set the second window to the 3 body window
            * Open the second window
            * Hide the main window
        Output:
            This function does not return a value
    """
    def OpenThreeBodyWindow(self):
        if not self.secondWindow:
            self.secondWindow = ThreeBodyWindow()
        self.secondWindow.show()
        self.hide()

    """ ResizeEvent - Centers widgets horizontally when window is resized
        Input:
            event - Object for the resize of a window
        Algorithm:
            * Call the center widget method for all the widgets in the window
            * Call the resize event for the window
        Output:
            This function does not return a value
    """
    def ResizeEvent(self, event):
        self.CenterWidgetHoriz(self.headerLabel)
        self.CenterWidgetHoriz(self.ProjectileMotionBtn)
        self.CenterWidgetHoriz(self.TwoBodyBtn)
        self.CenterWidgetHoriz(self.ThreeBodyBtn)
        super().ResizeEvent(event)

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### Projectile Motion Window
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
        Constructor - Constructs window with widgets and layouts of widgets
        Calculate - Assigns parameters of input fields to be fed to the projectile motion solver
        ClearAllInputs - Clears all the inputs of the window
        ClearCommonParam - Clears the common parameters input fields
        ClearCustomParam - Clears the custom parameters input fields
        CommmonObjChanged - Enables / Disables and resets children based on index of the combo box
        CustomObjChanged - Enables / Disables and resets children based on the value of children in custom parameters
        GrabChildren - Grabs the children from the main window
        OpenPlot - Opens a window for a given plot
        RandomCommon - Generates random parameters for a common object simulation
        RandomCustom - Generates random parameters for a custom object simulation
        ReturnHome - Returns home and closes the current window
        SelectAllPlots - Selects all plot options
        UnselectAllPlots - Unselects all plot options
"""
class ProjectileMotionWindow(QWidget):
    """ Constructor - Constructs window with widgets and layouts of widgets
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Create a signal for the main window
            * Set the title of the window
            * Set the height and width of the window
            * Create the layouts for the window
            * Create the common mass parameters header
            * Create the common masses drop down
            * Create the common masses initial position text field
            * Create the common masses initial velocity text field
            * Create the common masses initial time text field
            * Create the common masses final time text field
            * Create the common masses clear button
            * Create the common masses random button
            * Create the custom masses parameters header
            * Create the custom masses mass text field
            * Create the custom masses radius text field
            * Create the custom masses initial position text field
            * Create the custom masses initial velocity text field
            * Create the custom masses initial time text field
            * Create the custom masses final time text field
            * Create the custom masses clear button
            * Create the custom masses random button
            * Add the common and custom parameters layouts to the parameters layout
            * Create the plot selection header
            * Create the plot selection check boxes
            * Create the plot selection buttons
            * Add the plot selection layouts to the plot selection layout
            * Create the buttons header
            * Create the calculate button
            * Create the clear button
            * Create the main window button
            * Add the button layouts to the button layout
            * Add the parameters, plot selection, and button layouts to the main layout
            * Set the main layout to main layout
        Output:
            This function does not return a value
    """
    # Main window signal
    mainWindowSignal = pyqtSignal()
    def __init__(self):
        # Widget sizes
        headerSize = 20
        comboBoxMinWidth = 200
        comboBoxMinHeight = 25
        textFieldMinWidth = 200
        textFieldMinHeight = 25
        buttonMinWidth = 175
        buttonMinHeight = 35
        super().__init__()
        # Title of Window
        self.setWindowTitle("Projectile Motion Simulation")
        # Height and Width of Window
        self.resize(800,500)
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        # Layouts
        mainLayout = QVBoxLayout()
        ## Parameters layouts
        parametersLayout = QHBoxLayout()
        commonParametersLayout = QVBoxLayout()
        customParametersLayout = QVBoxLayout()
        customObjParametersLayout = QHBoxLayout()
        ## Plot selection layouts
        plotSelectionLayout = QVBoxLayout()
        plotSelectionHeaderLayout = QHBoxLayout()
        plotSelectionCBLayout = QHBoxLayout()
        plotSelectionBtnLayout = QHBoxLayout()
        # Main buttons layout
        buttonLayout = QVBoxLayout()
        buttonHeaderLayout = QHBoxLayout()
        buttonMainBtnsLayout = QHBoxLayout()
        # Margins
        mainLayout.setContentsMargins(25,25,25,25)
        ## Header
        commonParametersHeader = QLabel("Common Parameters")
        commonParametersHeaderFont = commonParametersHeader.font()
        commonParametersHeaderFont.setPointSize(headerSize)
        commonParametersHeader.setFont(commonParametersHeaderFont)
        commonParametersHeader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        commonParametersLayout.addWidget(commonParametersHeader)
        ## Common Masses Dropdown
        commonObjectsDropdown = QComboBox()
        commonObjectsDropdown.setMinimumWidth(comboBoxMinWidth)
        commonObjectsDropdown.setMinimumHeight(comboBoxMinHeight)
        commonObjectsDropdown.addItems(["Select Common Object", "Sun", "Mercury", "Venus", "Earth", "Moon", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"])
        commonObjectsDropdown.currentIndexChanged.connect(self.CommmonObjChanged)
        commonObjectsDropdown.setObjectName(projMotCommonObjectDD)
        commonParametersLayout.addWidget(commonObjectsDropdown)
        ## Projectile Motion Initial Position
        projectileInitialPosition1 = QLineEdit()
        projectileInitialPosition1.setMinimumWidth(textFieldMinWidth)
        projectileInitialPosition1.setMinimumHeight(textFieldMinHeight)
        projectileInitialPosition1.setPlaceholderText("Enter Initial Position In (m)")
        projectileInitialPosition1.setDisabled(True)
        projectileInitialPosition1.setObjectName(projMotCommonObjInitPos)
        commonParametersLayout.addWidget(projectileInitialPosition1)
        ## Projectile Motion Initial Velocity
        projectileInitialVelocity1 = QLineEdit()
        projectileInitialVelocity1.setMinimumWidth(textFieldMinWidth)
        projectileInitialVelocity1.setMinimumHeight(textFieldMinHeight)
        projectileInitialVelocity1.setPlaceholderText("Enter Initial Velocity In (m/s)")
        projectileInitialVelocity1.setDisabled(True)
        projectileInitialVelocity1.setObjectName(projMotCommonObjInitVel)
        commonParametersLayout.addWidget(projectileInitialVelocity1)
        ## Initial Time Of Model
        initialTime1 = QLineEdit()
        initialTime1.setMinimumWidth(textFieldMinWidth)
        initialTime1.setMinimumHeight(textFieldMinHeight)
        initialTime1.setPlaceholderText("Enter Initial Time Of Model In (s)")
        initialTime1.setDisabled(True)
        initialTime1.setObjectName(projMotCommonObjInitTime)
        commonParametersLayout.addWidget(initialTime1)
        ## Final Time Of Model
        finalTime1 = QLineEdit()
        finalTime1.setMinimumWidth(textFieldMinWidth)
        finalTime1.setMinimumHeight(textFieldMinHeight)
        finalTime1.setPlaceholderText("Enter Final Time Of Model In (s)")
        finalTime1.setDisabled(True)
        finalTime1.setObjectName(projMotCommonObjFinalTime)
        commonParametersLayout.addWidget(finalTime1)
        ## Clear Parameters Button
        commonParametersClearBtn = QPushButton("Clear Common Parameters")
        commonParametersClearBtn.setMinimumWidth(buttonMinWidth)
        commonParametersClearBtn.setMinimumHeight(buttonMinHeight)
        commonParametersClearBtn.setDisabled(True)
        commonParametersClearBtn.setObjectName(projMotCommonObjClearParamBtn)
        commonParametersClearBtn.clicked.connect(self.ClearCommonParam)
        commonParametersLayout.addWidget(commonParametersClearBtn)
        ## Random Parameters Button
        commonParametersRandomBtn = QPushButton("Randomize Parameters")
        commonParametersRandomBtn.setMinimumWidth(buttonMinWidth)
        commonParametersRandomBtn.setMinimumHeight(buttonMinHeight)
        commonParametersRandomBtn.setObjectName(projMotCommonObjRandBtn)
        commonParametersRandomBtn.clicked.connect(self.RandomCommon)
        commonParametersLayout.addWidget(commonParametersRandomBtn)
        # Custom Parameters
        ## Header
        customParametersHeader = QLabel("Custom Parameters")
        customParametersHeaderFont = customParametersHeader.font()
        customParametersHeaderFont.setPointSize(headerSize)
        customParametersHeader.setFont(customParametersHeaderFont)
        customParametersHeader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        customParametersLayout.addWidget(customParametersHeader)
        ## Mass
        customObj = QLineEdit()
        customObj.setMinimumHeight(textFieldMinHeight)
        customObj.setPlaceholderText("Enter Mass Of Object In (Kg)")
        customObj.textChanged.connect(self.CustomObjChanged)
        customObj.setObjectName(projMotCustomObjMass)
        customObjParametersLayout.addWidget(customObj)
        ## Radius Of Mass
        customRadius = QLineEdit()
        customRadius.setMinimumHeight(textFieldMinHeight)
        customRadius.setPlaceholderText("Enter Radius Of Mass In (m)")
        customRadius.textChanged.connect(self.CustomObjChanged)
        customRadius.setObjectName(projMotCustomObjRadius)
        customObjParametersLayout.addWidget(customRadius)
        customParametersLayout.addLayout(customObjParametersLayout)
        ## Projectile Motion Initial Position
        projectileInitialPosition2 = QLineEdit()
        projectileInitialPosition2.setMinimumWidth(textFieldMinWidth)
        projectileInitialPosition2.setMinimumHeight(textFieldMinHeight)
        projectileInitialPosition2.setPlaceholderText("Enter Initial Position In (m)")
        projectileInitialPosition2.setDisabled(True)
        projectileInitialPosition2.setObjectName(projMotCustomObjInitPos)
        customParametersLayout.addWidget(projectileInitialPosition2)
        ## Projectile Motion Initial Velocity
        projectileInitialVelocity2 = QLineEdit()
        projectileInitialVelocity2.setMinimumWidth(textFieldMinWidth)
        projectileInitialVelocity2.setMinimumHeight(textFieldMinHeight)
        projectileInitialVelocity2.setPlaceholderText("Enter Initial Velocity In (m/s)")
        projectileInitialVelocity2.setDisabled(True)
        projectileInitialVelocity2.setObjectName(projMotCustomObjInitVel)
        customParametersLayout.addWidget(projectileInitialVelocity2)
        ## Initial Time Of Model
        initialTime2 = QLineEdit()
        initialTime2.setMinimumWidth(textFieldMinWidth)
        initialTime2.setMinimumHeight(textFieldMinHeight)
        initialTime2.setPlaceholderText("Enter Initial Time Of Model In (s)")
        initialTime2.setDisabled(True)
        initialTime2.setObjectName(projMotCustomObjInitTime)
        customParametersLayout.addWidget(initialTime2)
        ## Final Time Of Model
        finalTime2 = QLineEdit()
        finalTime2.setMinimumWidth(textFieldMinWidth)
        finalTime2.setMinimumHeight(textFieldMinHeight)
        finalTime2.setPlaceholderText("Enter Final Time Of Model In (s)")
        finalTime2.setDisabled(True)
        finalTime2.setObjectName(projMotCustomObjFinalTime)
        customParametersLayout.addWidget(finalTime2)
        ## Clear Parameters Button
        customParametersClearBtn = QPushButton("Clear Custom Parameters")
        customParametersClearBtn.setMinimumWidth(buttonMinWidth)
        customParametersClearBtn.setMinimumHeight(buttonMinHeight)
        customParametersClearBtn.setDisabled(True)
        customParametersClearBtn.setObjectName(projMotCustomObjClearParamBtn)
        customParametersClearBtn.clicked.connect(self.ClearCustomParam)
        customParametersLayout.addWidget(customParametersClearBtn)
        ## Random Parameters Button
        customParametersRandomBtn = QPushButton("Randomize Parameters")
        customParametersRandomBtn.setMinimumWidth(buttonMinWidth)
        customParametersRandomBtn.setMinimumHeight(buttonMinHeight)
        customParametersRandomBtn.setObjectName(projMotCustomObjRandBtn)
        customParametersRandomBtn.clicked.connect(self.RandomCustom)
        customParametersLayout.addWidget(customParametersRandomBtn)
        # Parameters layouts layout addition
        parametersLayout.addLayout(commonParametersLayout)
        parametersLayout.addLayout(customParametersLayout)
        # Plot Selection
        plotSelectionHeader = QLabel("Choose Plot(s)")
        plotSelectionHeaderFont = plotSelectionHeader.font()
        plotSelectionHeaderFont.setPointSize(headerSize)
        plotSelectionHeader.setFont(plotSelectionHeaderFont)
        plotSelectionHeader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        plotSelectionLayout.addWidget(plotSelectionHeader)
        ## 2D Position Plot
        projMotPosPlot = QCheckBox("2D Position Plot")
        projMotPosPlot.setDisabled(True)
        projMotPosPlot.setObjectName(projMotPosPlotCheck)
        plotSelectionCBLayout.addWidget(projMotPosPlot)
        ## 2D Position Animation
        projMotPosAni = QCheckBox("2D Position Animation")
        projMotPosAni.setDisabled(True)
        projMotPosAni.setObjectName(projMotPosAniCheck)
        plotSelectionCBLayout.addWidget(projMotPosAni)
        ## 2D Velocity Plot
        projMotVelPlot = QCheckBox("2D Velocity Plot")
        projMotVelPlot.setDisabled(True)
        projMotVelPlot.setObjectName(projMotVelPlotCheck)
        plotSelectionCBLayout.addWidget(projMotVelPlot)
        ## 2D Velocity Animation
        projMotVelAni = QCheckBox("2D Velocity Animation")
        projMotVelAni.setDisabled(True)
        projMotVelAni.setObjectName(projMotVelAniCheck)
        plotSelectionCBLayout.addWidget(projMotVelAni)
        ## Select all plots
        selectAllPlotsBtn = QPushButton("Select All Plots")
        selectAllPlotsBtn.setMinimumWidth(buttonMinWidth)
        selectAllPlotsBtn.setMinimumHeight(buttonMinHeight)
        selectAllPlotsBtn.setDisabled(True)
        selectAllPlotsBtn.setObjectName(projMotCBSelectAll)
        selectAllPlotsBtn.clicked.connect(self.SelectAllPlots)
        plotSelectionBtnLayout.addWidget(selectAllPlotsBtn)
        ## Unselect all plots
        unselectAllPlotsBtn = QPushButton("Unselect All Plots")
        unselectAllPlotsBtn.setMinimumWidth(buttonMinWidth)
        unselectAllPlotsBtn.setMinimumHeight(buttonMinHeight)
        unselectAllPlotsBtn.setDisabled(True)
        unselectAllPlotsBtn.setObjectName(projMotCBUnselectAll)
        unselectAllPlotsBtn.clicked.connect(self.UnselectAllPlots)
        plotSelectionBtnLayout.addWidget(unselectAllPlotsBtn)
        ## Plot selection layouts layout addition
        plotSelectionLayout.addLayout(plotSelectionHeaderLayout)
        plotSelectionLayout.addLayout(plotSelectionCBLayout)
        plotSelectionLayout.addLayout(plotSelectionBtnLayout)
        # Buttons
        buttonsHeader = QLabel("Calculate / Clear Selection")
        buttonsHeaderFont = buttonsHeader.font()
        buttonsHeaderFont.setPointSize(20)
        buttonsHeader.setFont(buttonsHeaderFont)
        buttonsHeader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        buttonHeaderLayout.addWidget(buttonsHeader)
        ## Calculate Button
        calculateButton = QPushButton("Calculate")
        calculateButton.setMinimumWidth(buttonMinWidth)
        calculateButton.setMinimumHeight(buttonMinHeight)
        calculateButton.setDisabled(True)
        calculateButton.setObjectName(projMotCalculateBtn)
        calculateButton.clicked.connect(self.OpenPlot)
        buttonMainBtnsLayout.addWidget(calculateButton)
        ## Clear Button
        clearButton = QPushButton("Clear")
        clearButton.setMinimumWidth(buttonMinWidth)
        clearButton.setMinimumHeight(buttonMinHeight)
        clearButton.setDisabled(True)
        clearButton.setObjectName(projMotClearBtn)
        clearButton.clicked.connect(self.ClearAllInputs)
        buttonMainBtnsLayout.addWidget(clearButton)
        ## Main Window Button
        mainWindowButton = QPushButton("Return Home")
        mainWindowButton.setMinimumWidth(buttonMinWidth)
        mainWindowButton.setMinimumHeight(buttonMinHeight)
        mainWindowButton.setObjectName(projMotMainWinBtn)
        mainWindowButton.clicked.connect(self.ReturnHome)
        buttonMainBtnsLayout.addWidget(mainWindowButton)
        ## Button layouts layout addition
        buttonLayout.addLayout(buttonHeaderLayout)
        buttonLayout.addLayout(buttonMainBtnsLayout)
        # Main layout widget addition
        mainLayout.addLayout(parametersLayout)
        mainLayout.addLayout(plotSelectionLayout)
        mainLayout.addLayout(buttonLayout)
        # Add layouts
        self.setLayout(mainLayout)

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

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### Two Body Window
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####

""" TwoBodyWindow - Window for the two body simulation
    Member Functions:
        Constructor - 
"""
class TwoBodyWindow(QWidget):
    """ Constructor - Constructs window with widgets and layouts of widgets
    
    """
    mainWindowSignal = pyqtSignal()
    def __init__(self):
        super().__init__()
        # Title of Window
        self.setWindowTitle("2 Body Simulation")
        # Height and Width of Window
        self.resize(800,500)
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        # Layouts
        mainLayout = QVBoxLayout()
        # Main layout widget addition
        # Add layouts
        self.setLayout(mainLayout)

    def Calculate(self):
        return

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### Three Body Window
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####
        
class ThreeBodyWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Title of Window
        self.setWindowTitle("3 Body Simulation")
        # Height and Width of Window
        self.resize(800,500)
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        # Layouts
        mainLayout = QVBoxLayout()
        # Center Column Header
        centerColumnHeader = QLabel("Parameters")
        centerColumnHeaderFont = centerColumnHeader.font()
        centerColumnHeaderFont.setPointSize(30)
        centerColumnHeader.setFont(centerColumnHeaderFont)
        centerColumnHeader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        mainLayout.addWidget(centerColumnHeader, Qt.AlignmentFlag.AlignHCenter)
        # Add layouts
        self.setLayout(mainLayout)

""" RunProgram - Runs the program from the main window
    Input:
        There are no input parameters for this function
    Algorithm:
        * Create an application instance of QApplication with sys.argv
        * Create a window object
        * Show the window
        * Exit system
    Output:
        This program does not return a value
"""
def RunProgram():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
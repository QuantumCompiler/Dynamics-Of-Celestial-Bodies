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
projMotCommonObjectDropDownBtnName = "Common Object Dropdown"
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
        commonObjectsDropdown.setObjectName(projMotCommonObjectDropDownBtnName)
        commonParametersLayout.addWidget(commonObjectsDropdown)
        ## Projectile Motion Initial Position
        projectileInitialPosition1 = QLineEdit()
        projectileInitialPosition1.setMinimumWidth(textFieldMinWidth)
        projectileInitialPosition1.setMinimumHeight(textFieldMinHeight)
        projectileInitialPosition1.setPlaceholderText("Enter Initial Position In (m)")
        projectileInitialPosition1.setObjectName(projMotCommonObjInitPos)
        commonParametersLayout.addWidget(projectileInitialPosition1)
        ## Projectile Motion Initial Velocity
        projectileInitialVelocity1 = QLineEdit()
        projectileInitialVelocity1.setMinimumWidth(textFieldMinWidth)
        projectileInitialVelocity1.setMinimumHeight(textFieldMinHeight)
        projectileInitialVelocity1.setPlaceholderText("Enter Initial Velocity In (m/s)")
        projectileInitialVelocity1.setObjectName(projMotCommonObjInitVel)
        commonParametersLayout.addWidget(projectileInitialVelocity1)
        ## Initial Time Of Model
        initialTime1 = QLineEdit()
        initialTime1.setMinimumWidth(textFieldMinWidth)
        initialTime1.setMinimumHeight(textFieldMinHeight)
        initialTime1.setPlaceholderText("Enter Initial Time Of Model In (s)")
        initialTime1.setObjectName(projMotCommonObjInitTime)
        commonParametersLayout.addWidget(initialTime1)
        ## Final Time Of Model
        finalTime1 = QLineEdit()
        finalTime1.setMinimumWidth(textFieldMinWidth)
        finalTime1.setMinimumHeight(textFieldMinHeight)
        finalTime1.setPlaceholderText("Enter Final Time Of Model In (s)")
        finalTime1.setObjectName(projMotCommonObjFinalTime)
        commonParametersLayout.addWidget(finalTime1)
        ## Clear Parameters Button
        commonParametersClearBtn = QPushButton("Clear Common Parameters")
        commonParametersClearBtn.setMinimumWidth(buttonMinWidth)
        commonParametersClearBtn.setMinimumHeight(buttonMinHeight)
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
        customObj.setObjectName(projMotCustomObjMass)
        customObjParametersLayout.addWidget(customObj)
        ## Radius Of Mass
        customRadius = QLineEdit()
        customRadius.setMinimumHeight(textFieldMinHeight)
        customRadius.setPlaceholderText("Enter Radius Of Mass In (m)")
        customRadius.setObjectName(projMotCustomObjRadius)
        customObjParametersLayout.addWidget(customRadius)
        customParametersLayout.addLayout(customObjParametersLayout)
        ## Projectile Motion Initial Position
        projectileInitialPosition2 = QLineEdit()
        projectileInitialPosition2.setMinimumWidth(textFieldMinWidth)
        projectileInitialPosition2.setMinimumHeight(textFieldMinHeight)
        projectileInitialPosition2.setPlaceholderText("Enter Initial Position In (m)")
        projectileInitialPosition2.setObjectName(projMotCustomObjInitPos)
        customParametersLayout.addWidget(projectileInitialPosition2)
        ## Projectile Motion Initial Velocity
        projectileInitialVelocity2 = QLineEdit()
        projectileInitialVelocity2.setMinimumWidth(textFieldMinWidth)
        projectileInitialVelocity2.setMinimumHeight(textFieldMinHeight)
        projectileInitialVelocity2.setPlaceholderText("Enter Initial Velocity In (m/s)")
        projectileInitialVelocity2.setObjectName(projMotCustomObjInitVel)
        customParametersLayout.addWidget(projectileInitialVelocity2)
        ## Initial Time Of Model
        initialTime2 = QLineEdit()
        initialTime2.setMinimumWidth(textFieldMinWidth)
        initialTime2.setMinimumHeight(textFieldMinHeight)
        initialTime2.setPlaceholderText("Enter Initial Time Of Model In (s)")
        initialTime2.setObjectName(projMotCustomObjInitTime)
        customParametersLayout.addWidget(initialTime2)
        ## Final Time Of Model
        finalTime2 = QLineEdit()
        finalTime2.setMinimumWidth(textFieldMinWidth)
        finalTime2.setMinimumHeight(textFieldMinHeight)
        finalTime2.setPlaceholderText("Enter Final Time Of Model In (s)")
        finalTime2.setObjectName(projMotCustomObjFinalTime)
        customParametersLayout.addWidget(finalTime2)
        ## Clear Parameters Button
        customParametersClearBtn = QPushButton("Clear Custom Parameters")
        customParametersClearBtn.setMinimumWidth(buttonMinWidth)
        customParametersClearBtn.setMinimumHeight(buttonMinHeight)
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
        projMotPosPlot.setObjectName(projMotPosPlotCheck)
        plotSelectionCBLayout.addWidget(projMotPosPlot)
        ## 2D Position Animation
        projMotPosAni = QCheckBox("2D Position Animation")
        projMotPosAni.setObjectName(projMotPosAniCheck)
        plotSelectionCBLayout.addWidget(projMotPosAni)
        ## 2D Velocity Plot
        projMotVelPlot = QCheckBox("2D Velocity Plot")
        projMotVelPlot.setObjectName(projMotVelPlotCheck)
        plotSelectionCBLayout.addWidget(projMotVelPlot)
        ## 2D Velocity Animation
        projMotVelAni = QCheckBox("2D Velocity Animation")
        projMotVelAni.setObjectName(projMotVelAniCheck)
        plotSelectionCBLayout.addWidget(projMotVelAni)
        ## Select all plots
        selectAllPlotsBtn = QPushButton("Select All Plots")
        selectAllPlotsBtn.setMinimumWidth(buttonMinWidth)
        selectAllPlotsBtn.setMinimumHeight(buttonMinHeight)
        selectAllPlotsBtn.setObjectName(projMotCBSelectAll)
        selectAllPlotsBtn.clicked.connect(self.SelectAllPlots)
        plotSelectionBtnLayout.addWidget(selectAllPlotsBtn)
        ## Unselect all plots
        unselectAllPlotsBtn = QPushButton("Unselect All Plots")
        unselectAllPlotsBtn.setMinimumWidth(buttonMinWidth)
        unselectAllPlotsBtn.setMinimumHeight(buttonMinHeight)
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
        calculateButton.setObjectName(projMotCalculateBtn)
        calculateButton.clicked.connect(self.OpenPlot)
        buttonMainBtnsLayout.addWidget(calculateButton)
        ## Clear Button
        clearButton = QPushButton("Clear")
        clearButton.setMinimumWidth(buttonMinWidth)
        clearButton.setMinimumHeight(buttonMinHeight)
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
        commonObjDD = self.findChild(QComboBox, projMotCommonObjectDropDownBtnName)
        commonObjInitPos = self.findChild(QLineEdit, projMotCommonObjInitPos)
        commonObjInitVel = self.findChild(QLineEdit, projMotCommonObjInitVel)
        commonObjInitTime = self.findChild(QLineEdit, projMotCommonObjInitTime)
        commonObjFinalTime = self.findChild(QLineEdit, projMotCommonObjFinalTime)
        customObjMass = self.findChild(QLineEdit, projMotCustomObjMass)
        customObjRadius = self.findChild(QLineEdit, projMotCustomObjRadius)
        customObjInitPos = self.findChild(QLineEdit, projMotCustomObjInitPos)
        customObjInitVel = self.findChild(QLineEdit, projMotCustomObjInitVel)
        customObjInitTime = self.findChild(QLineEdit, projMotCustomObjInitTime)
        customObjFinalTime = self.findChild(QLineEdit, projMotCustomObjFinalTime)
        # Parameters to be fed into solver
        obj = []
        objName = ""
        ic = []
        initPos = 0
        initVel = 0
        initTime = 0
        finTime = 0
        # Common field entered, custom not
        if ((customObjMass.text() == "" and customObjRadius.text() == "" and customObjInitPos.text() == "" and customObjInitVel.text() == "" and customObjInitTime.text() == "" and customObjFinalTime.text() == "") 
            and (commonObjDD.currentText() != "Select Common Object" and commonObjInitPos.text() != "" and commonObjInitVel.text() != "" and commonObjInitTime.text() != "" and commonObjFinalTime.text())):
            # Convert input fields to correct data type
            objectSelection = commonObjDD.currentText()
            initialPos = float(commonObjInitPos.text())
            initialVel = float(commonObjInitVel.text())
            initialTime = float(commonObjInitTime.text())
            finalTime = float(commonObjFinalTime.text())
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
        # Custom field entered, common not
        elif ((customObjMass.text() != "" and customObjRadius.text() != "" and customObjInitPos.text() != "" and customObjInitVel.text() != "" and customObjInitTime.text() != "" and customObjFinalTime.text() != "") 
            and (commonObjInitPos.text() == "" and commonObjInitVel.text() == "" and commonObjInitTime.text() == "" and commonObjFinalTime.text() == "")):
            # Convert input fields to correct data type
            objectMass = float(customObjMass.text())
            objectRadius = float(customObjRadius.text())
            initialPos = float(customObjInitPos.text())
            initialVel = float(customObjInitVel.text())
            initialTime = float(customObjInitTime.text())
            finalTime = float(customObjFinalTime.text())
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
        # Invalid entries
        else:
            dialogBox = QDialog(self)
            dialogBox.setWindowTitle("Invalid Entries")
            dialogBox.setFixedSize(400, 75)
            warningLabel = QLabel("Please enter in values into one parameter field or the other.", dialogBox)
            warningFont = warningLabel.font()
            warningFont.setPointSize(13)
            warningLabel.setFont(warningFont)
            warningLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            layout = QVBoxLayout()
            layout.addWidget(warningLabel)
            dialogBox.setLayout(layout)
            dialogBox.exec()
        return obj, ic, initTime, finTime, objName
    
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
            * Create an array for the text fields
            * Reset all children to their default values
        Output:
            This function does not return a value
    """
    def ClearCommonParam(self):
        # Grab children
        commonObjDD = self.findChild(QComboBox, projMotCommonObjectDropDownBtnName)
        commonObjInitPos = self.findChild(QLineEdit, projMotCommonObjInitPos)
        commonObjInitVel = self.findChild(QLineEdit, projMotCommonObjInitVel)
        commonObjInitTime = self.findChild(QLineEdit, projMotCommonObjInitTime)
        commonObjFinalTime = self.findChild(QLineEdit, projMotCommonObjFinalTime)
        # Fields array
        arr = [commonObjInitPos, commonObjInitVel, commonObjInitTime, commonObjFinalTime]
        # Reset 
        commonObjDD.setCurrentIndex(0)
        for i in range(len(arr)):
            arr[i].clear()

    """ ClearCustomParam - Clears the custom parameters input fields
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab the children of the custom parameters input fields
            * Create an array for the text fields
            * Reset all children to their default values
        Output:
            This function does not return a value
    """
    def ClearCustomParam(self):
        # Grab children
        customObjMass = self.findChild(QLineEdit, projMotCustomObjMass)
        customObjRadius = self.findChild(QLineEdit, projMotCustomObjRadius)
        customObjInitPos = self.findChild(QLineEdit, projMotCustomObjInitPos)
        customObjInitVel = self.findChild(QLineEdit, projMotCustomObjInitVel)
        customObjInitTime = self.findChild(QLineEdit, projMotCustomObjInitTime)
        customObjFinalTime = self.findChild(QLineEdit, projMotCustomObjFinalTime)
        # Fields array
        arr = [customObjMass, customObjRadius, customObjInitPos, customObjInitVel, customObjInitTime, customObjFinalTime]
        # Reset 
        for i in range(len(arr)):
            arr[i].clear()

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
        # Grab checkbox children
        posPlotCheck = self.findChild(QCheckBox, projMotPosPlotCheck)
        posAniCheck = self.findChild(QCheckBox, projMotPosAniCheck)
        velPlotCheck = self.findChild(QCheckBox, projMotVelPlotCheck)
        velAniCheck = self.findChild(QCheckBox, projMotVelAniCheck)
        # Position Plot
        if (posPlotCheck.isChecked() == True):
            self.posPlot = ProjectileMotionPlotWindow(0, calc[0], calc[1], calc[2], calc[3], calc[4], "Projectile", "Projectile Motion Plot: Position Vs. Time")
            self.posPlot.show()
        # Position Animation
        if (posAniCheck.isChecked() == True):
            self.posAni = ProjectileMotionPlotWindow(1, calc[0], calc[1], calc[2], calc[3], calc[4], "Projectile", "Projectile Motion Animation: Position Vs. Time")
            self.posAni.show()
        # Velocity Plot
        if (velPlotCheck.isChecked() == True):
            self.velPlot = ProjectileMotionPlotWindow(2, calc[0], calc[1], calc[2], calc[3], calc[4], "Projectile", "Projectile Motion Plot: Velocity Vs. Time")
            self.velPlot.show()
        # Velocity Animation
        if (velAniCheck.isChecked() == True):
            self.velAni = ProjectileMotionPlotWindow(3, calc[0], calc[1], calc[2], calc[3], calc[4], "Projectile", "Projectile Motion Animation: Velocity Vs. Time")
            self.velAni.show()
        # No boxes checked
        if (posPlotCheck.isChecked() == False and posAniCheck.isChecked() == False and velPlotCheck.isChecked() == False and velAniCheck.isChecked() == False):
            dialogBox = QDialog(self)
            dialogBox.setWindowTitle("Invalid Entries")
            dialogBox.setFixedSize(400, 75)
            warningLabel = QLabel("Please select plot(s) for entered input parameters.", dialogBox)
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
            * Grab the common object children
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
        commonObjDD = self.findChild(QComboBox, projMotCommonObjectDropDownBtnName)
        commonObjInitPos = self.findChild(QLineEdit, projMotCommonObjInitPos)
        commonObjInitVel = self.findChild(QLineEdit, projMotCommonObjInitVel)
        commonObjInitTime = self.findChild(QLineEdit, projMotCommonObjInitTime)
        commonObjFinalTime = self.findChild(QLineEdit, projMotCommonObjFinalTime)
        # Random object
        randObj = random.randrange(1,11)
        commonObjDD.setCurrentIndex(randObj)
        # Random Position
        randPos = random.uniform(0.0, 1000.0)
        randPos = round(randPos,2)
        commonObjInitPos.setText(str(randPos))
        # Random Velocity
        randVel = random.uniform(-200.0, 200.0)
        randVel = round(randVel,2)
        commonObjInitVel.setText(str(randVel))
        # Initial Time
        commonObjInitTime.setText(str(0))
        # Random Final Time
        randFinTime = random.uniform(1.0, 30.0)
        randFinTime = round(randFinTime,2)
        commonObjFinalTime.setText(str(randFinTime))

    """ RandomCustom - Generates random parameters for a custom object simulation
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab the custom object children
            * Calculate a random mass for the custom object, round it, and set the text field to that value
            * Calculate a random radius for the custom object, round it, and set the text field to that value
            * Calculate a random initial position, round it, and set the text field to that value
            * Calculate a random initial velocity, round it, and set the text field to that value
            * Set the initial time of the model to 0
            * Calculate a random final time of the model, round it, and set the text field to that value
        Output:
            This function does not return a value
    """
    def RandomCustom(self):
        # Grab children
        customObjMass = self.findChild(QLineEdit, projMotCustomObjMass)
        customObjRadius = self.findChild(QLineEdit, projMotCustomObjRadius)
        customObjInitPos = self.findChild(QLineEdit, projMotCustomObjInitPos)
        customObjInitVel = self.findChild(QLineEdit, projMotCustomObjInitVel)
        customObjInitTime = self.findChild(QLineEdit, projMotCustomObjInitTime)
        customObjFinalTime = self.findChild(QLineEdit, projMotCustomObjFinalTime)
        # Random Mass
        randMass = random.uniform(0.5 * MPLUTO, 10.0 * MSUN)
        randMass = round(randMass,2)
        customObjMass.setText(str(randMass))
        # Random Radius
        randRad = random.uniform(0.5 * RPLUTO, 10.0 * RSUN)
        randRad = round(randRad,2)
        customObjRadius.setText(str(randRad))
        # Random Position
        randPos = random.uniform(0.0, 1000.0)
        randPos = round(randPos,2)
        customObjInitPos.setText(str(randPos))
        # Random Velocity
        randVel = random.uniform(-200.0, 200.0)
        randVel = round(randVel,2)
        customObjInitVel.setText(str(randVel))
        # Initial Time
        customObjInitTime.setText(str(0))
        # Random Final Time
        randFinTime = random.uniform(1.0, 30.0)
        randFinTime = round(randFinTime,2)
        customObjFinalTime.setText(str(randFinTime))

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

class TwoBodyWindow(QWidget):
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
        # Center Column Header
        centerColumnHeader = QLabel("Parameters")
        centerColumnHeaderFont = centerColumnHeader.font()
        centerColumnHeaderFont.setPointSize(30)
        centerColumnHeader.setFont(centerColumnHeaderFont)
        centerColumnHeader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        mainLayout.addWidget(centerColumnHeader, Qt.AlignmentFlag.AlignHCenter)
        # Add layouts
        self.setLayout(mainLayout)

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
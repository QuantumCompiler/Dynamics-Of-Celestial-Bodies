from WindowFunctions import *

# Widget Names 
HeaderLabel = "Choose A Simulation"
TwoDForceLabel = "2D Force"
TwoBodyLabel = "2 Body Simulation"
ThreeBodyLabel = "3 Body Simulation"

# Object Names
TwoDForceObjName = "2D Force Button"
TwoBodyObjName = "2 Body Button"
ThreeBodyObjName = "3 Body Button"

class MainWindow(QMainWindow):
    # Constructor
    def __init__(self):
        super().__init__()
        # Title of Window
        self.setWindowTitle("Celestial Bodies")
        # Height and Width of Window
        self.resize(800,500)
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        # Header label
        self.headerLabel = QLabel(HeaderLabel, self)
        self.centerWidgetHoriz(self.headerLabel)
        headerFont = self.headerLabel.font()
        headerFont.setPointSize(50)
        self.headerLabel.setFont(headerFont)
        self.headerLabel.adjustSize()
        self.headerLabel.move((self.size().width() - self.headerLabel.size().width()) // 2, int(0.05 * self.size().height()))
        # 2 Body Button
        self.TwoDForceBtn = QPushButton(TwoDForceLabel, self)
        self.TwoDForceBtn.setFixedSize(400, 50)
        self.TwoDForceBtn.setObjectName(TwoDForceObjName)
        self.TwoDForceBtn.clicked.connect(self.OpenTwoDForceWindow)
        self.centerWidgetHoriz(self.TwoDForceBtn)
        self.TwoDForceBtn.move(self.TwoDForceBtn.pos().x(), 6 * self.headerLabel.pos().y())
        # 2 Body Button
        self.TwoBodyBtn = QPushButton(TwoBodyLabel, self)
        self.TwoBodyBtn.setFixedSize(400, 50)
        self.TwoBodyBtn.setObjectName(TwoBodyObjName)
        self.TwoBodyBtn.clicked.connect(self.OpenTwoBodyWindow)
        self.centerWidgetHoriz(self.TwoBodyBtn)
        self.TwoBodyBtn.move(self.TwoBodyBtn.pos().x(), self.TwoDForceBtn.pos().y() + 50)
        # 3 Body Button
        self.ThreeBodyBtn = QPushButton(ThreeBodyLabel, self)
        self.ThreeBodyBtn.setFixedSize(400, 50)
        self.ThreeBodyBtn.setObjectName(ThreeBodyObjName)
        self.ThreeBodyBtn.clicked.connect(self.OpenThreeBodyWindow)
        self.centerWidgetHoriz(self.ThreeBodyBtn)
        self.ThreeBodyBtn.move(self.ThreeBodyBtn.pos().x(), self.TwoBodyBtn.pos().y() + 50)
        self.secondWindow = None
        
    def centerWidgetHoriz(self, widget):
        windowWidth = self.size().width()
        widgetWidth = widget.size().width()
        widgetYPos = widget.pos().y()
        horizCenter = (windowWidth - widgetWidth) // 2
        widget.move(horizCenter, widgetYPos)

    def resizeEvent(self, event):
        self.centerWidgetHoriz(self.headerLabel)
        self.centerWidgetHoriz(self.TwoDForceBtn)
        self.centerWidgetHoriz(self.TwoBodyBtn)
        self.centerWidgetHoriz(self.ThreeBodyBtn)
        super().resizeEvent(event)

    def OpenTwoDForceWindow(self):
        if not self.secondWindow:
            self.secondWindow = TwoDForceWindow()
        self.secondWindow.show()
        self.close()

    def OpenTwoBodyWindow(self):
        if not self.secondWindow:
            self.secondWindow = TwoBodyWindow()
        self.secondWindow.show()
        self.close()

    def OpenThreeBodyWindow(self):
        if not self.secondWindow:
            self.secondWindow = ThreeBodyWindow()
        self.secondWindow.show()
        self.close()

# 2D Force Window Widget Attributes

# Object Names
twoDCommonObjectDropDownBtnName = "Common Object Dropdown"
twoDCommonObjInitPos = "Common Object Projectile Initial Position"
twoDCommonObjInitVel = "Common Object Projectile Initial Velocity"
twoDCommonObjInitTime = "Common Object Initial Time"
twoDCommonObjFinalTime = "Common Object Final Time"
twoDCustomObjMass = "Custom Object Mass"
twoDCustomObjRadius = "Custom Object Radius"
twoDCustomObjInitPos = "Custom Object Projectile Initial Position"
twoDCustomObjInitVel = "Custom Object Projectile Initial Velocity"
twoDCustomObjInitTime = "Custom Object Initial Time"
twoDCustomObjFinalTime = "Custom Object Final Time"
twoDPosPlotCheck = "2D Position Plot Checkbox"
twoDPosAniCheck = "2D Position Animation Checkbox"
twoDVelPlotCheck = "2D Velocity Plot Checkbox"
twoDVelAniCheck = "2D Velocity Animation Checkbox"
twoDCalculateBtn = "2D Calculate Button"
twoDClearBtn = "2D Clear Button"

class TwoDForceWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Title of Window
        self.setWindowTitle("2D Force Simulation")
        # Height and Width of Window
        self.resize(800,500)
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        # Layouts
        mainLayout = QVBoxLayout()
        parametersLayout = QHBoxLayout()
        commonParametersLayout = QVBoxLayout()
        customParametersLayout = QVBoxLayout()
        plotSelectionHeaderLayout = QHBoxLayout()
        plotSelectionLayout = QHBoxLayout()
        buttonHeaderLayout = QHBoxLayout()
        buttonLayout = QHBoxLayout()
        # Center Column Header
        centerColumnHeader = QLabel("Parameters")
        centerColumnHeaderFont = centerColumnHeader.font()
        centerColumnHeaderFont.setPointSize(30)
        centerColumnHeader.setFont(centerColumnHeaderFont)
        centerColumnHeader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        mainLayout.addWidget(centerColumnHeader, Qt.AlignmentFlag.AlignHCenter)
        # Common Parameters
        ## Header
        commonParametersHeader = QLabel("Common Parameters")
        commonParametersHeaderFont = commonParametersHeader.font()
        commonParametersHeaderFont.setPointSize(20)
        commonParametersHeader.setFont(commonParametersHeaderFont)
        commonParametersHeader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        commonParametersLayout.addWidget(commonParametersHeader)
        ## Common Masses Dropdown
        commonMassesDropdown = QComboBox()
        commonMassesDropdown.setFixedWidth(200)
        commonMassesDropdown.addItems([
            "Select Common Mass",
            "Sun",
            "Mercury",
            "Venus",
            "Earth",
            "Moon",
            "Mars",
            "Jupiter",
            "Saturn",
            "Uranus",
            "Neptune",
            "Pluto"
        ])
        commonMassesDropdown.setObjectName(twoDCommonObjectDropDownBtnName)
        commonParametersLayout.addWidget(commonMassesDropdown, 0, Qt.AlignmentFlag.AlignHCenter)
        ## Projectile Motion Initial Position
        projectileInitialPosition1 = QLineEdit()
        projectileInitialPosition1.setFixedWidth(200)
        projectileInitialPosition1.setPlaceholderText("Enter Initial Position In (m)")
        projectileInitialPosition1.setObjectName(twoDCommonObjInitPos)
        commonParametersLayout.addWidget(projectileInitialPosition1, 0, Qt.AlignmentFlag.AlignHCenter)
        ## Projectile Motion Initial Velocity
        projectileInitialVelocity1 = QLineEdit()
        projectileInitialVelocity1.setFixedWidth(200)
        projectileInitialVelocity1.setPlaceholderText("Enter Initial Velocity In (m/s)")
        projectileInitialVelocity1.setObjectName(twoDCommonObjInitVel)
        commonParametersLayout.addWidget(projectileInitialVelocity1, 0, Qt.AlignmentFlag.AlignHCenter)
        ## Initial Time Of Model
        initialTime1 = QLineEdit()
        initialTime1.setFixedWidth(200)
        initialTime1.setPlaceholderText("Enter Initial Time Of Model In (s)")
        initialTime1.setObjectName(twoDCommonObjInitTime)
        commonParametersLayout.addWidget(initialTime1, 0, Qt.AlignmentFlag.AlignHCenter)
        ## Final Time Of Model
        finalTime1 = QLineEdit()
        finalTime1.setFixedWidth(200)
        finalTime1.setPlaceholderText("Enter Final Time Of Model In (s)")
        finalTime1.setObjectName(twoDCommonObjFinalTime)
        commonParametersLayout.addWidget(finalTime1, 0, Qt.AlignmentFlag.AlignHCenter)
        # Custom Parameters
        ## Header
        customParametersHeader = QLabel("Custom Parameters")
        customParametersHeaderFont = customParametersHeader.font()
        customParametersHeaderFont.setPointSize(20)
        customParametersHeader.setFont(customParametersHeaderFont)
        customParametersHeader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        customParametersLayout.addWidget(customParametersHeader)
        ## Mass
        customMass = QLineEdit()
        customMass.setFixedWidth(200)
        customMass.setPlaceholderText("Enter Mass Of Object In (Kg)")
        customMass.setObjectName(twoDCustomObjMass)
        customParametersLayout.addWidget(customMass, 0, Qt.AlignmentFlag.AlignHCenter)
        ## Radius Of Mass
        customRadius = QLineEdit()
        customRadius.setFixedWidth(200)
        customRadius.setPlaceholderText("Enter Radius Of Mass In (m)")
        customRadius.setObjectName(twoDCustomObjRadius)
        customParametersLayout.addWidget(customRadius, 0, Qt.AlignmentFlag.AlignHCenter)
        ## Projectile Motion Initial Position
        projectileInitialPosition2 = QLineEdit()
        projectileInitialPosition2.setFixedWidth(200)
        projectileInitialPosition2.setPlaceholderText("Enter Initial Position In (m)")
        projectileInitialPosition2.setObjectName(twoDCustomObjInitPos)
        customParametersLayout.addWidget(projectileInitialPosition2, 0, Qt.AlignmentFlag.AlignHCenter)
        ## Projectile Motion Initial Velocity
        projectileInitialVelocity2 = QLineEdit()
        projectileInitialVelocity2.setFixedWidth(200)
        projectileInitialVelocity2.setPlaceholderText("Enter Initial Velocity In (m/s)")
        projectileInitialVelocity2.setObjectName(twoDCustomObjInitVel)
        customParametersLayout.addWidget(projectileInitialVelocity2, 0, Qt.AlignmentFlag.AlignHCenter)
        ## Initial Time Of Model
        initialTime2 = QLineEdit()
        initialTime2.setFixedWidth(200)
        initialTime2.setPlaceholderText("Enter Initial Time Of Model In (s)")
        initialTime2.setObjectName(twoDCustomObjInitTime)
        customParametersLayout.addWidget(initialTime2, 0, Qt.AlignmentFlag.AlignHCenter)
        ## Final Time Of Model
        finalTime2 = QLineEdit()
        finalTime2.setFixedWidth(200)
        finalTime2.setPlaceholderText("Enter Final Time Of Model In (s)")
        finalTime2.setObjectName(twoDCustomObjFinalTime)
        customParametersLayout.addWidget(finalTime2, 0, Qt.AlignmentFlag.AlignHCenter)
        # Parameters layouts layout addition
        parametersLayout.addLayout(commonParametersLayout)
        parametersLayout.addLayout(customParametersLayout)
        # Plot Selection
        plotSelectionHeader = QLabel("Choose Plot(s)")
        plotSelectionHeaderFont = plotSelectionHeader.font()
        plotSelectionHeaderFont.setPointSize(20)
        plotSelectionHeader.setFont(plotSelectionHeaderFont)
        plotSelectionHeader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        plotSelectionHeaderLayout.addWidget(plotSelectionHeader)
        ## 2D Position Plot
        twoDPosPlot = QCheckBox("2D Position Plot")
        twoDPosPlot.setObjectName(twoDPosPlotCheck)
        plotSelectionLayout.addWidget(twoDPosPlot, 0, Qt.AlignmentFlag.AlignLeft)
        ## 2D Position Animation
        twoDPosAni = QCheckBox("2D Position Animation")
        twoDPosAni.setObjectName(twoDPosAniCheck)
        plotSelectionLayout.addWidget(twoDPosAni, 0, Qt.AlignmentFlag.AlignLeft)
        ## 2D Velocity Plot
        twoDVelPlot = QCheckBox("2D Velocity Plot")
        twoDVelPlot.setObjectName(twoDVelPlotCheck)
        plotSelectionLayout.addWidget(twoDVelPlot, 0, Qt.AlignmentFlag.AlignLeft)
        ## 2D Velocity Animation
        twoDVelAni = QCheckBox("2D Velocity Animation")
        twoDVelAni.setObjectName(twoDVelAniCheck)
        plotSelectionLayout.addWidget(twoDVelAni, 0, Qt.AlignmentFlag.AlignLeft)
        # Buttons
        buttonsHeader = QLabel("Calculate / Clear Selection")
        buttonsHeaderFont = buttonsHeader.font()
        buttonsHeaderFont.setPointSize(20)
        buttonsHeader.setFont(buttonsHeaderFont)
        buttonsHeader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        buttonHeaderLayout.addWidget(buttonsHeader)
        ## Calculate Button
        calculateButton = QPushButton("Calculate")
        calculateButton.setFixedSize(300, 50)
        calculateButton.setObjectName(twoDCalculateBtn)
        calculateButton.clicked.connect(self.OpenPlot)
        buttonLayout.addWidget(calculateButton)
        ## Clear Button
        clearButton = QPushButton("Clear")
        clearButton.setFixedSize(300, 50)
        clearButton.setObjectName(twoDClearBtn)
        clearButton.clicked.connect(self.ClearInputs)
        buttonLayout.addWidget(clearButton)
        # Main layout widget addition
        mainLayout.addLayout(parametersLayout)
        mainLayout.addLayout(plotSelectionHeaderLayout)
        mainLayout.addLayout(plotSelectionLayout)
        mainLayout.addLayout(buttonHeaderLayout)
        mainLayout.addLayout(buttonLayout)
        # Add layouts
        self.setLayout(mainLayout)

    def OpenPlot(self):
        calc = self.Calculate()
        posPlotCheck = self.findChild(QCheckBox, twoDPosPlotCheck)
        posAniCheck = self.findChild(QCheckBox, twoDPosAniCheck)
        velPlotCheck = self.findChild(QCheckBox, twoDVelPlotCheck)
        velAniCheck = self.findChild(QCheckBox, twoDVelAniCheck)
        # Position Plot
        if (posPlotCheck.isChecked() == True):
            self.posPlot = ProjectileMotionWindow(0, calc[0], calc[1], calc[2], calc[3], calc[4], "Projectile", "Projectile Motion Plot: Position Vs. Time")
            self.posPlot.show()
        # Position Animation
        if (posAniCheck.isChecked() == True):
            self.posAni = ProjectileMotionWindow(1, calc[0], calc[1], calc[2], calc[3], calc[4], "Projectile", "Projectile Motion Animation: Position Vs. Time")
            self.posAni.show()
        # Velocity Plot
        if (velPlotCheck.isChecked() == True):
            self.velPlot = ProjectileMotionWindow(2, calc[0], calc[1], calc[2], calc[3], calc[4], "Projectile", "Projectile Motion Plot: Velocity Vs. Time")
            self.velPlot.show()
        # Velocity Animation
        if (velAniCheck.isChecked() == True):
            self.velAni = ProjectileMotionWindow(3, calc[0], calc[1], calc[2], calc[3], calc[4], "Projectile", "Projectile Motion Animation: Velocity Vs. Time")
            self.velAni.show()

    def ClearInputs(self):
        # Grab children from input fields
        commonObjDD = self.findChild(QComboBox, twoDCommonObjectDropDownBtnName)
        commonObjInitPos = self.findChild(QLineEdit, twoDCommonObjInitPos)
        commonObjInitVel = self.findChild(QLineEdit, twoDCommonObjInitVel)
        commonObjInitTime = self.findChild(QLineEdit, twoDCommonObjInitTime)
        commonObjFinalTime = self.findChild(QLineEdit, twoDCommonObjFinalTime)
        customObjMass = self.findChild(QLineEdit, twoDCustomObjMass)
        customObjRadius = self.findChild(QLineEdit, twoDCustomObjRadius)
        customObjInitPos = self.findChild(QLineEdit, twoDCustomObjInitPos)
        customObjInitVel = self.findChild(QLineEdit, twoDCustomObjInitVel)
        customObjInitTime = self.findChild(QLineEdit, twoDCustomObjInitTime)
        customObjFinalTime = self.findChild(QLineEdit, twoDCustomObjFinalTime)
        posPlotCheck = self.findChild(QCheckBox, twoDPosPlotCheck)
        posAniCheck = self.findChild(QCheckBox, twoDPosAniCheck)
        velPlotCheck = self.findChild(QCheckBox, twoDVelPlotCheck)
        velAniCheck = self.findChild(QCheckBox, twoDVelAniCheck)
        calcBtn = self.findChild(QPushButton, twoDCalculateBtn)
        clearBtn = self.findChild(QPushButton, twoDClearBtn)
        # Reset values in fields
        commonObjDD.setCurrentIndex(0)
        commonObjInitPos.clear()
        commonObjInitVel.clear()
        commonObjInitTime.clear()
        commonObjFinalTime.clear()
        customObjMass.clear()
        customObjRadius.clear()
        customObjInitPos.clear()
        customObjInitVel.clear()
        customObjInitTime.clear()
        customObjFinalTime.clear()
        posPlotCheck.setChecked(False)
        posAniCheck.setChecked(False)
        velPlotCheck.setChecked(False)
        velAniCheck.setChecked(False)

    def Calculate(self):
        # Grab children from input fields
        commonObjDD = self.findChild(QComboBox, twoDCommonObjectDropDownBtnName)
        commonObjInitPos = self.findChild(QLineEdit, twoDCommonObjInitPos)
        commonObjInitVel = self.findChild(QLineEdit, twoDCommonObjInitVel)
        commonObjInitTime = self.findChild(QLineEdit, twoDCommonObjInitTime)
        commonObjFinalTime = self.findChild(QLineEdit, twoDCommonObjFinalTime)
        customObjMass = self.findChild(QLineEdit, twoDCustomObjMass)
        customObjRadius = self.findChild(QLineEdit, twoDCustomObjRadius)
        customObjInitPos = self.findChild(QLineEdit, twoDCustomObjInitPos)
        customObjInitVel = self.findChild(QLineEdit, twoDCustomObjInitVel)
        customObjInitTime = self.findChild(QLineEdit, twoDCustomObjInitTime)
        customObjFinalTime = self.findChild(QLineEdit, twoDCustomObjFinalTime)
        calcBtn = self.findChild(QPushButton, twoDCalculateBtn)
        clearBtn = self.findChild(QPushButton, twoDClearBtn)
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
            and (commonObjDD.currentText() != "Select Common Mass" and commonObjInitPos.text() != "" and commonObjInitVel.text() != "" and commonObjInitTime.text() != "" and commonObjFinalTime.text())):
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
                obj.append(RJUPITER)
                obj.append(MJUPITER)
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
            initPos = initialPos
            initVel = initialVel
            ic.append(initPos)
            ic.append(initVel)
            initTime = initialTime
            finTime = finalTime
        # Custom field entered, common not
        elif ((customObjMass.text() != "" and customObjRadius.text() != "" and customObjInitPos.text() != "" and customObjInitVel.text() != "" and customObjInitTime.text() != "" and customObjFinalTime.text() != "") 
            and (commonObjInitPos.text() == "" and commonObjInitVel.text() == "" and commonObjInitTime.text() == "" and commonObjFinalTime.text() == "")):
            objectMass = float(customObjMass.text())
            objectRadius = float(customObjRadius.text())
            initialPos = float(customObjInitPos.text())
            initialVel = float(customObjInitVel.text())
            initialTime = float(customObjInitTime.text())
            finalTime = float(customObjFinalTime.text())
            obj.append(objectMass)
            obj.append(objectRadius)
            objName = objectSelection
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

def RunProgram():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
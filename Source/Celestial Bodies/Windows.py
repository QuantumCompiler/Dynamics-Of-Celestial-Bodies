from ModelFunctions import *

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
        commonParametersLayout.addWidget(commonMassesDropdown, 0, Qt.AlignmentFlag.AlignHCenter)
        ## Projectile Motion Initial Position
        projectileInitialPosition1 = QLineEdit()
        projectileInitialPosition1.setFixedWidth(200)
        projectileInitialPosition1.setPlaceholderText("Enter Initial Position In (m)")
        commonParametersLayout.addWidget(projectileInitialPosition1, 0, Qt.AlignmentFlag.AlignHCenter)
        ## Projectile Motion Initial Velocity
        projectileInitialVelocity1 = QLineEdit()
        projectileInitialVelocity1.setFixedWidth(200)
        projectileInitialVelocity1.setPlaceholderText("Enter Initial Velocity In (m/s)")
        commonParametersLayout.addWidget(projectileInitialVelocity1, 0, Qt.AlignmentFlag.AlignHCenter)
        ## Initial Time Of Model
        initialTime1 = QLineEdit()
        initialTime1.setFixedWidth(200)
        initialTime1.setPlaceholderText("Enter Initial Time Of Model In (s)")
        commonParametersLayout.addWidget(initialTime1, 0, Qt.AlignmentFlag.AlignHCenter)
        ## Final Time Of Model
        finalTime1 = QLineEdit()
        finalTime1.setFixedWidth(200)
        finalTime1.setPlaceholderText("Enter Final Time Of Model In (s)")
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
        customParametersLayout.addWidget(customMass, 0, Qt.AlignmentFlag.AlignHCenter)
        ## Radius Of Mass
        customRadius = QLineEdit()
        customRadius.setFixedWidth(200)
        customRadius.setPlaceholderText("Enter Radius Of Mass In (m)")
        customParametersLayout.addWidget(customRadius, 0, Qt.AlignmentFlag.AlignHCenter)
        ## Projectile Motion Initial Position
        projectileInitialPosition2 = QLineEdit()
        projectileInitialPosition2.setFixedWidth(200)
        projectileInitialPosition2.setPlaceholderText("Enter Initial Position In (m)")
        customParametersLayout.addWidget(projectileInitialPosition2, 0, Qt.AlignmentFlag.AlignHCenter)
        ## Projectile Motion Initial Velocity
        projectileInitialVelocity2 = QLineEdit()
        projectileInitialVelocity2.setFixedWidth(200)
        projectileInitialVelocity2.setPlaceholderText("Enter Initial Velocity In (m/s)")
        customParametersLayout.addWidget(projectileInitialVelocity2, 0, Qt.AlignmentFlag.AlignHCenter)
        ## Initial Time Of Model
        initialTime2 = QLineEdit()
        initialTime2.setFixedWidth(200)
        initialTime2.setPlaceholderText("Enter Initial Time Of Model In (s)")
        customParametersLayout.addWidget(initialTime2, 0, Qt.AlignmentFlag.AlignHCenter)
        ## Final Time Of Model
        finalTime2 = QLineEdit()
        finalTime2.setFixedWidth(200)
        finalTime2.setPlaceholderText("Enter Final Time Of Model In (s)")
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
        plotSelectionLayout.addWidget(twoDPosPlot, 0, Qt.AlignmentFlag.AlignLeft)
        ## 2D Position Animation
        twoDPosAni = QCheckBox("2D Position Animation")
        plotSelectionLayout.addWidget(twoDPosAni, 0, Qt.AlignmentFlag.AlignLeft)
        ## 2D Velocity Plot
        twoDVelPlot = QCheckBox("2D Velocity Plot")
        plotSelectionLayout.addWidget(twoDVelPlot, 0, Qt.AlignmentFlag.AlignLeft)
        ## 2D Velocity Animation
        twoDVelAni = QCheckBox("2D Velocity Animation")
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
        buttonLayout.addWidget(calculateButton)
        ## Clear Button
        clearButton = QPushButton("Clear")
        clearButton.setFixedSize(300, 50)
        buttonLayout.addWidget(clearButton)
        # Main layout widget addition
        mainLayout.addLayout(parametersLayout)
        mainLayout.addLayout(plotSelectionHeaderLayout)
        mainLayout.addLayout(plotSelectionLayout)
        mainLayout.addLayout(buttonHeaderLayout)
        mainLayout.addLayout(buttonLayout)
        # Add layouts
        self.setLayout(mainLayout)

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
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
        # Center Column Header
        centerColumnHeader = QLabel("Parameters")
        centerColumnHeaderFont = centerColumnHeader.font()
        centerColumnHeaderFont.setPointSize(30)
        centerColumnHeader.setFont(centerColumnHeaderFont)
        centerColumnHeader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        mainLayout.addWidget(centerColumnHeader, Qt.AlignmentFlag.AlignHCenter)
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
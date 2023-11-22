# Imports
from ModelFunctions import *

# Object Names
TwoDForceObjName = "2D Force Button"
TwoBodyObjName = "2 Body Button"
ThreeBodyObjName = "3 Body Button"

# Button Parameters
maxButtonHeight = 40
maxButtonWidth = 400

class MainWindow(QMainWindow):
    # Constructor
    def __init__(self):
        super().__init__()
        # Title of Window
        self.setWindowTitle("Celestial Bodies")
        # Height and Width of Window
        self.resize(850,500)
        self.setMinimumWidth(850)
        self.setMinimumHeight(400)
        # Layouts
        mainLayout = QVBoxLayout()
        # Layout spacing / margins
        # Main window header
        mainWindowHeader = QLabel("Celestial Bodies")
        mainWindowHeaderFont = mainWindowHeader.font()
        mainWindowHeaderFont.setPointSize(40)
        mainWindowHeader.setFont(mainWindowHeaderFont)
        # 2D Force Button
        TwoDForceBtn = QPushButton("2D Force Simulator")
        TwoDForceBtn.setMaximumHeight(maxButtonHeight)
        TwoDForceBtn.setMaximumWidth(maxButtonWidth)
        TwoDForceBtn.setObjectName(TwoDForceObjName)
        # 2 Body Button
        TwoBodyBtn = QPushButton("2 Body Simulator")
        TwoBodyBtn.setMaximumHeight(maxButtonHeight)
        TwoBodyBtn.setMaximumWidth(maxButtonWidth)
        TwoBodyBtn.setObjectName(TwoBodyObjName)
        # 3 Body Button
        ThreeBodyBtn = QPushButton("3 Body Simulator")
        ThreeBodyBtn.setMaximumHeight(maxButtonHeight)
        ThreeBodyBtn.setMaximumWidth(maxButtonWidth)
        ThreeBodyBtn.setObjectName(ThreeBodyObjName)
        # Add widgets to mainLayout
        mainLayout.addWidget(mainWindowHeader, 0, Qt.AlignmentFlag.AlignHCenter)
        mainLayout.addWidget(TwoDForceBtn, 0, Qt.AlignmentFlag.AlignHCenter)
        mainLayout.addWidget(TwoBodyBtn, 0, Qt.AlignmentFlag.AlignHCenter)
        mainLayout.addWidget(ThreeBodyBtn, 0, Qt.AlignmentFlag.AlignHCenter)
        # Widgets
        mainWidget = QWidget()
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
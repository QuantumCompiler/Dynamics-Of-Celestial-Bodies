from ProjectileMotion import *
from TwoBodies import *

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### Main Window
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

""" MainWindow - Main window for application
    Member Functions:
        Constructor - Creates window with widgets and layouts
"""
class MainWindow(QMainWindow):
    """ Constructor - Creates window with widgets and layouts
        Input:
            This function does not have any unique input parameters
        Algorithm:
        Output:
            This function does not return a value
    """
    def __init__(self):
        # Object Names
        pmButtonName = "Projectile Motion Button"
        twoButtonName = "Two Body Button"
        # Height / Width Of Widgets
        minBtnWidth = 400
        minBtnHeight = 50
        super().__init__()
        # Title of window
        self.setWindowTitle("Celestial Bodies")
        # Height and width of window
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        self.secondWindow = None
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        # Layouts
        ## Main layout
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(25,25,25,25)
        mainLayout.setSpacing(25)
        ## Header
        header = QLabel("Choose A Simulation")
        mainLayout.addWidget(header, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Buttons
        ## Projectile motion button
        pmBtn = QPushButton("Projectile Motion")
        pmBtn.setObjectName(pmButtonName)
        pmBtn.setMinimumWidth(minBtnWidth)
        pmBtn.setMinimumHeight(minBtnHeight)
        pmBtn.clicked.connect(self.OpenProjectileMotionWindow)
        mainLayout.addWidget(pmBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Two body button
        twoBtn = QPushButton("Two Body")
        twoBtn.setObjectName(twoButtonName)
        twoBtn.setMinimumWidth(minBtnWidth)
        twoBtn.setMinimumHeight(minBtnHeight)
        twoBtn.clicked.connect(self.OpenTwoBodyWindow)
        mainLayout.addWidget(twoBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Spacer after the button
        spacer = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        mainLayout.addSpacerItem(spacer)
        ## Set layout
        centralWidget.setLayout(mainLayout)

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
        self.secondWindow.mainWindowPMSignal.connect(self.show)
        self.secondWindow.show()
        self.hide()

    def OpenTwoBodyWindow(self):
        if not self.secondWindow:
            self.secondWindow = TwoBodyWindow()
        # self.secondWindow.mainWindowSignal.connect(self.show)
        self.secondWindow.show()
        self.hide()

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
from ProjectileMotion import *

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
    # def OpenTwoBodyWindow(self):
    #     if not self.secondWindow:
    #         self.secondWindow = TwoBodyWindow()
    #     self.secondWindow.show()
    #     self.hide()

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
    # def OpenThreeBodyWindow(self):
    #     if not self.secondWindow:
    #         self.secondWindow = ThreeBodyWindow()
    #     self.secondWindow.show()
    #     self.hide()

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
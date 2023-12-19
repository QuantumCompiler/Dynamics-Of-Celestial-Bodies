from ModelFunctions import *

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### Canvas / Plot Window
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### Simulation Window
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

# Object names
homeBtnName = "Home"

class TwoBodyWindow(QWidget):
    # Main window signal
    mainWindowSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        # Widget sizes
        headerSize = 20
        comboBoxMinWidth = 200
        comboBoxMinHeight = 25
        lineEditMinWidth = 200
        lineEditMinHeight = 25
        buttonMinWidth = 200
        buttonMinHeight = 35
        # Title of window
        self.setWindowTitle("Two Body Simulation")
        # Height and width of window
        self.resize(800, 500)
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        ###################################
        ##### Layouts
        ###################################
        # Main layout
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(25,25,25,25)
        mainLayout.setSpacing(20)
        # Main button layout
        mainButtonsLayout = QVBoxLayout()
        mainButtonsLayout.setContentsMargins(0,0,0,0)
        mainButtonsLayout.setSpacing(5)
        # Main buttons layout
        mainBtnLayout = QVBoxLayout()
        mainBtnLayout.setContentsMargins(0,0,0,0)
        mainBtnLayout.setSpacing(5)
        ###################################
        ##### Main Buttons
        ###################################
        # Main buttons header
        mainButtonsHeader = QLabel("Calculate / Clear All / Randomize All / Return Home")
        mainButtonsLayout.addWidget(mainButtonsHeader, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Main buttons home button
        homeBtn = QPushButton("Return Home")
        homeBtn.setObjectName(homeBtnName)
        homeBtn.setMinimumWidth(buttonMinWidth - 50)
        homeBtn.setMinimumHeight(buttonMinHeight)
        homeBtn.clicked.connect(self.ReturnHome)
        mainBtnLayout.addWidget(homeBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Add buttons to parent
        mainButtonsLayout.addLayout(mainBtnLayout)
        ###################################
        ##### Spacers / Set Layout
        ###################################
        # Add layouts
        mainLayout.addLayout(mainButtonsLayout)
        # Spacers
        spacer = QSpacerItem(0, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        mainLayout.addSpacerItem(spacer)
        # Set layout
        self.setLayout(mainLayout)

    def ReturnHome(self):
        # Emit signal
        self.mainWindowSignal.emit()
        # Close current window
        self.close()
from ModelFunctions import *

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### Canvas / Plot Window
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### Simulation Window
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

""" TwoBodyWindow - Class for two body simulation windows
    Member Functions:
        
"""

# Object names
mass1CBName = "Mass 1 Combo Box"
mass1MassLEName = "Mass 1 Mass Line Edit"
mass1MassNameLEName = "Mass 1 Name Line Edit"
mass1InitPosXLEName = "Mass 1 Initial Position In x Line Edit"
mass1InitPosYLEName = "Mass 1 Initial Position In y Line Edit"
mass1InitPosZLEName = "Mass 1 Initial Position In z Line Edit"
mass1InitVelXLEName = "Mass 1 Initial Velocity In x Line Edit"
mass1InitVelYLEName = "Mass 1 Initial Velocity In y Line Edit"
mass1InitVelZLEName = "Mass 1 Initial Velocity In z Line Edit"
mass1ClearBtnName = "Clear Mass 1 Parameters Button"
mass1RandBtnName = "Randomize Mass 1 Parameters Button"
timeValLEName = "Time Value Line Edit"
timeValClearBtnName = "Clear Time Values Button"
timeValRandBtnName = "Randomize Time Values Button"
mass2CBName = "Mass 2 Combo Box"
mass2MassLEName = "Mass 2 Mass Line Edit"
mass2MassNameLEName = "Mass 2 Name Line Edit"
mass2InitPosXLEName = "Mass 2 Initial Position In x Line Edit"
mass2InitPosYLEName = "Mass 2 Initial Position In y Line Edit"
mass2InitPosZLEName = "Mass 2 Initial Position In z Line Edit"
mass2InitVelXLEName = "Mass 2 Initial Velocity In x Line Edit"
mass2InitVelYLEName = "Mass 2 Initial Velocity In y Line Edit"
mass2InitVelZLEName = "Mass 2 Initial Velocity In z Line Edit"
mass2ClearBtnName = "Clear Mass 2 Parameters Button"
mass2RandBtnName = "Randomize Mass 2 Parameters Button"
pos2DPlotCBName = "2D Position Plot Check Box"
pos2DAniCBName = "2D Position Animation Check Box"
vel2DPlotCBName = "2D Velocity Plot Check Box"
vel2DAniCBName = "2D Velocity Animation Check Box"
pos3DPlotCBName = "3D Position Plot Check Box"
pos3DAniCBName = "3D Position Animation Check Box"
vel3DPlotCBName = "3D Velocity Plot Check Box"
vel3DAniCBName = "3D Velocity Animation Check Box"
plotSelAllBtnName = "Select All Check Boxes Button"
plotSelRandBtnName = "Randomize Check Boxes Button"
plotSelUnsBtnName = "Unselect All Check Boxes Button"
calculateBtnName = "Calculate"
clearBtnName = "Clear All"
randomBtnName = "Randomize All"
homeBtnName = "Home"

# Widget sizes
headerSize = 20
comboBoxMinWidth = 200
comboBoxMinHeight = 25
lineEditMinWidth = 200
lineEditMinHeight = 25
buttonMinWidth = 225
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

class TwoBodyWindow(QWidget):
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

    """ ClearMass1Params - Clears the mass 1 parameters children
        Input:
            This function does not have any unique input parameters
        Algorithm:

        Output:
            This function does not return a value
    """
    def ClearMass1Params(self):
        # Grab children
        children = self.GrabChildren()
        # Clear children
        for widget in children[0][1:9]:
            widget.setText("")

    """ DefaultState - Default state for widgets
        Input:
            field - Field that is to be set to default
        Algorithm:
            * Grab children from window
            * Define disable mass 1 function
            * Define disable time function
            * Define disable mass 2 function
            * Define disable checkboxes function
            * Define disable calculate function
            * Define disable all function
            * Set the field(s) to default based upon the input parameter
        Output:
            This function does not return a value
    """
    def DefaultState(self, field):
        # Enable children
        children = self.GrabChildren()
        # Disable mass 1 parameters children function
        def DefaultMass1():
            for widget in children[0][2:10]:
                widget.setDisabled(True)
        # Disable time values children function
        def DefaultTime():
            for widget in children[2][0:2]:
                widget.setDisabled(True)
        # Disable mass 2 parameters children function
        def DefaultMass2():
            for widget in children[1][2:10]:
                widget.setDisabled(True)
        # Disable checkboxes children function
        def DefaultCB():
            for widget in children[3]:
                widget.setDisabled(True)
        # Disable calculate button function
        def DefaultCalcBtn():
            children[4][0].setDisabled(True)
        # Disable all function
        def DefaultAll():
            DefaultMass1()
            DefaultTime()
            DefaultMass2()
            DefaultCB()
            DefaultCalcBtn()
        # Set fields to default state
        if (field == 0):
            DefaultMass1()
        elif (field == 1):
            DefaultTime()
        elif (field == 2):
            DefaultMass2()
        elif (field == 3):
            DefaultCB()
        elif (field == 4):
            DefaultCalcBtn()
        elif (field == 5):
            DefaultAll()

    """ DisableFields - Disables fields based upon input parameter
        Input:
            Field - Integer value that determines what field is to be disabled
                0 - Disable mass 1 parameters
                1 - Disable time values
                2 - Disable mass 2 parameters
                3 - Disable checkbox parameters
                4 - Disable main buttons
                5 - Disable 0-4
        Algorithm:
            * Grab the children from the window
            * Define mass 1 parameters function
            * Define time values function
            * Define mass 2 parameters function
            * Define checkbox parameters function
            * Define main buttons function
            * Define all functions function
            * Disable field based off input parameter value
        Output:
            This function does not return a value
    """
    def DisableFields(self, field):
        # Grab children
        children = self.GrabChildren()
        # Disable mass 1 parameters function
        def DisableMass1Params():
            for widget in children[0]:
                widget.setDisabled(True)
        # Disable time values function
        def DisableTimeVals():
            for widget in children[2]:
                widget.setDisabled(True)
        # Disable mass 2 parameters function
        def DisableMass2Params():
            for widget in children[1]:
                widget.setDisabled(True)
        # Disable checkboxes parameters function
        def DisableCB():
            for widget in children[3]:
                widget.setDisabled(True)
        # Disable calculate button function
        def DisableMainButtons():
            for widget in children[4]:
                widget.setDisabled(True)
        # Disable all function
        def DisableAll():
            DisableMass1Params()
            DisableTimeVals()
            DisableMass2Params()
            DisableCB()
            DisableMainButtons()
        # Disable field from input
        if (field == 0):
            DisableMass1Params()
        elif (field == 1):
            DisableTimeVals()
        elif (field == 2):
            DisableMass2Params()
        elif (field == 3):
            DisableCB()
        elif (field == 4):
            DisableMainButtons()
        elif (field == 5):
            DisableAll()

    """ EnableFields - Enables fields based upon input parameter
        Input:
            Field - Integer value that determines what field is to be enabled
                0 - Enable mass 1 parameters
                1 - Enable time values
                2 - Enable mass 2 parameters
                3 - Enable checkbox parameters
                4 - Enable calculate button
                5 - Enable 0-4
        Algorithm:
            * Grab the children from the window
            * Define mass 1 parameters function
            * Define time values function
            * Define mass 2 parameters function
            * Define checkbox parameters function
            * Define calculate button function
            * Define all functions function
            * Enable field based off input parameter value
        Output:
            This function does not return a value
    """
    def EnableFields(self, field):
        # Grab children
        children = self.GrabChildren()
        # Enable mass 1 parameters function
        def EnableMass1Params():
            for widget in children[0]:
                widget.setEnabled(True)
        # Enable time values function
        def EnableTimeVals():
            for widget in children[1]:
                widget.setEnabled(True)
        # Enable mass 1 parameters function
        def EnableMass2Params():
            for widget in children[2]:
                widget.setEnabled(True)
        # Enable checkboxes function
        def EnableCB():
            for widget in children[3]:
                widget.setEnabled(True)
        # Enable main buttons function
        def EnableMainButtons():
            for widget in children[4]:
                widget.setEnabled(True)
        # Disable all function
        def EnableAll():
            EnableMass1Params()
            EnableTimeVals()
            EnableMass2Params()
            EnableCB()
            EnableMainButtons()
        # Enable field from input
        if (field == 0):
            EnableMass1Params()
        elif (field == 1):
            EnableTimeVals()
        elif (field == 2):
            EnableMass2Params()
        elif (field == 3):
            EnableCB()
        elif (field == 4):
            EnableMainButtons()
        elif (field == 5):
            EnableAll()

    """ GrabChildren - Grabs all the children from the fields
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab the children from the mass 1 parameters field, add them to their own array
            * Grab the children from the mass 2 parameters field, add them to their own array
            * Grab the children from the time values field, add them to their own array
            * Grab the children from the checkbox parameters field, add them to their own array
            * Grab the children from the main buttons field, add them to their own array
        Output:
            mass1Arr - Array of mass 1 children
                mass1Arr[0] - Mass 1 checkbox
                mass1Arr[1] - Mass 1 name line edit
                mass1Arr[2] - Mass 1 mass line edit
                mass1Arr[3] - Mass 1 initial x position line edit
                mass1Arr[4] - Mass 1 initial y position line edit
                mass1Arr[5] - Mass 1 initial z position line edit
                mass1Arr[6] - Mass 1 initial x velocity line edit
                mass1Arr[7] - Mass 1 initial y velocity line edit
                mass1Arr[8] - Mass 1 initial z velocity line edit
                mass1Arr[9] - Mass 1 clear parameters button
                mass1Arr[10] - Mass 1 random parameters button
            mass2Arr - Array of mass 2 children
                mass2Arr[0] - Mass 2 checkbox
                mass2Arr[1] - Mass 2 name line edit
                mass2Arr[2] - Mass 2 mass line edit
                mass2Arr[3] - Mass 2 initial x position line edit
                mass2Arr[4] - Mass 2 initial y position line edit
                mass2Arr[5] - Mass 2 initial z position line edit
                mass2Arr[6] - Mass 2 initial x velocity line edit
                mass2Arr[7] - Mass 2 initial y velocity line edit
                mass2Arr[8] - Mass 2 initial z velocity line edit
                mass2Arr[9] - Mass 2 clear parameters button
                mass2Arr[10] - Mass 2 random parameters button
            timeValArr - Array of time values children
                timeValArr[0] - Time span line edit
                timeValArr[1] - Time span clear button
                timeValArr[2] - Time span random button
            mainBtnsArr - Array of main buttons children
                mainBtnsArr[0] - Calculate button
                mainBtnsArr[1] - Clear button
                mainBtnsArr[2] - Random button
                mainBtnsArr[3] - Home button
    """
    def GrabChildren(self):
        # Mass 1 parameters
        mass1CB = self.findChild(QComboBox, mass1CBName)
        mass1MassNameLE = self.findChild(QLineEdit, mass1MassNameLEName)
        mass1MassLE = self.findChild(QLineEdit, mass1MassLEName)
        mass1InitPosXLE = self.findChild(QLineEdit, mass1InitPosXLEName)
        mass1InitPosYLE = self.findChild(QLineEdit, mass1InitPosYLEName)
        mass1InitPosZLE = self.findChild(QLineEdit, mass1InitPosZLEName)
        mass1InitVelXLE = self.findChild(QLineEdit, mass1InitVelXLEName)
        mass1InitVelYLE = self.findChild(QLineEdit, mass1InitVelYLEName)
        mass1InitVelZLE = self.findChild(QLineEdit, mass1InitVelZLEName)
        mass1ClearBtn = self.findChild(QPushButton, mass1ClearBtnName)
        mass1RandBtn = self.findChild(QPushButton, mass1RandBtnName)
        mass1Arr = [mass1CB, mass1MassNameLE, mass1MassLE, mass1InitPosXLE, mass1InitPosYLE, mass1InitPosZLE, mass1InitVelXLE, mass1InitVelYLE, mass1InitVelZLE, mass1ClearBtn, mass1RandBtn]
        # Mass 2 parameters
        mass2CB = self.findChild(QComboBox, mass2CBName)
        mass2MassNameLE = self.findChild(QLineEdit, mass2MassNameLEName)
        mass2MassLE = self.findChild(QLineEdit, mass2MassLEName)
        mass2InitPosXLE = self.findChild(QLineEdit, mass2InitPosXLEName)
        mass2InitPosYLE = self.findChild(QLineEdit, mass2InitPosYLEName)
        mass2InitPosZLE = self.findChild(QLineEdit, mass2InitPosZLEName)
        mass2InitVelXLE = self.findChild(QLineEdit, mass2InitVelXLEName)
        mass2InitVelYLE = self.findChild(QLineEdit, mass2InitVelYLEName)
        mass2InitVelZLE = self.findChild(QLineEdit, mass2InitVelZLEName)
        mass2ClearBtn = self.findChild(QPushButton, mass2ClearBtnName)
        mass2RandBtn = self.findChild(QPushButton, mass2RandBtnName)
        mass2Arr = [mass2CB, mass2MassNameLE, mass2MassLE, mass2InitPosXLE, mass2InitPosYLE, mass2InitPosZLE, mass2InitVelXLE, mass2InitVelYLE, mass2InitVelZLE, mass2ClearBtn, mass2RandBtn]
        # Time span parameters
        timeValLE = self.findChild(QLineEdit, timeValLEName)
        timeValClearBtn = self.findChild(QPushButton, timeValClearBtnName)
        timeValRandBtn = self.findChild(QPushButton, timeValRandBtnName)
        timeValArr = [timeValLE, timeValClearBtn, timeValRandBtn]
        # Check boxes parameters
        pos2DPlotCB = self.findChild(QCheckBox, pos2DPlotCBName)
        pos2DAniCB = self.findChild(QCheckBox, pos2DAniCBName)
        vel2DPlotCB = self.findChild(QCheckBox, vel2DPlotCBName)
        vel2DAniCB = self.findChild(QCheckBox, vel2DAniCBName)
        pos3DPlotCB = self.findChild(QCheckBox, pos3DPlotCBName)
        pos3DAniCB = self.findChild(QCheckBox, pos3DAniCBName)
        vel3DPlotCB = self.findChild(QCheckBox, vel3DPlotCBName)
        vel3DAniCB = self.findChild(QCheckBox, vel3DAniCBName)
        plotSelAllBtn = self.findChild(QPushButton, plotSelAllBtnName)
        plotSelRandBtn = self.findChild(QPushButton, plotSelRandBtnName)
        plotSelUnsBtn = self.findChild(QPushButton, plotSelUnsBtnName)
        plotSelArr = [pos2DPlotCB, pos2DAniCB, vel2DPlotCB, vel2DAniCB, pos3DPlotCB, pos3DAniCB, vel3DPlotCB, vel3DAniCB, plotSelAllBtn, plotSelRandBtn, plotSelUnsBtn]
        # Main buttons parameters
        calculateBtn = self.findChild(QPushButton, calculateBtnName)
        clearBtn = self.findChild(QPushButton, clearBtnName)
        randomBtn = self.findChild(QPushButton, randomBtnName)
        homeBtn = self.findChild(QPushButton, homeBtnName)
        mainBtnsArr = [calculateBtn, clearBtn, randomBtn, homeBtn]
        # Return arrays
        return mass1Arr, mass2Arr, timeValArr, plotSelArr, mainBtnsArr

    """ InitUI - Initializes the user interface for the window
    
    """
    def InitUI(self):
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
        mainLayout.setSpacing(5)
        # Parameters layout
        paramLayout = QHBoxLayout()
        paramLayout.setContentsMargins(0,0,0,0)
        paramLayout.setSpacing(5)
        # Mass 1 parameters layout
        mass1ParamLayout = QVBoxLayout()
        mass1ParamLayout.setContentsMargins(0,0,0,0)
        mass1ParamLayout.setSpacing(5)
        ## Mass 1 x vals sub layout
        mass1XValsLayout = QHBoxLayout()
        mass1XValsLayout.setContentsMargins(0,0,0,0)
        mass1XValsLayout.setSpacing(5)
        ## Mass 1 y vals sub layout
        mass1YValsLayout = QHBoxLayout()
        mass1YValsLayout.setContentsMargins(0,0,0,0)
        mass1YValsLayout.setSpacing(5)
        ## Mass 1 z vals sub layout
        mass1ZValsLayout = QHBoxLayout()
        mass1ZValsLayout.setContentsMargins(0,0,0,0)
        mass1ZValsLayout.setSpacing(5)
        # Time values layout
        timeValLayout = QVBoxLayout()
        timeValLayout.setContentsMargins(0,0,0,0)
        timeValLayout.setSpacing(5)
        # Mass 2 parameters layout
        mass2ParamLayout = QVBoxLayout()
        mass2ParamLayout.setContentsMargins(0,0,0,0)
        mass2ParamLayout.setSpacing(5)
        ## Mass 2 x vals sub layout
        mass2XValsLayout = QHBoxLayout()
        mass2XValsLayout.setContentsMargins(0,0,0,0)
        mass2XValsLayout.setSpacing(5)
        ## Mass 2 y vals sub layout
        mass2YValsLayout = QHBoxLayout()
        mass2YValsLayout.setContentsMargins(0,0,0,0)
        mass2YValsLayout.setSpacing(5)
        ## Mass 2 z vals sub layout
        mass2ZValsLayout = QHBoxLayout()
        mass2ZValsLayout.setContentsMargins(0,0,0,0)
        mass2ZValsLayout.setSpacing(5)
        # Plot selection layout
        plotSelLayout = QVBoxLayout()
        plotSelLayout.setContentsMargins(0,0,0,0)
        plotSelLayout.setSpacing(5)
        ## 2D Plot selection checkboxes layout
        plotSel2DCBLayout = QHBoxLayout()
        plotSel2DCBLayout.setContentsMargins(0,0,0,0)
        plotSel2DCBLayout.setSpacing(5)
        ## 3D Plot selection checkboxes layout
        plotSel3DCBLayout = QHBoxLayout()
        plotSel3DCBLayout.setContentsMargins(0,0,0,0)
        plotSel3DCBLayout.setSpacing(5)
        ## Plot selection buttons layout
        plotSelBtnLayout = QHBoxLayout()
        plotSelBtnLayout.setContentsMargins(0,0,0,0)
        plotSelBtnLayout.setSpacing(5)
        # Main button layout
        mainButtonsLayout = QVBoxLayout()
        mainButtonsLayout.setContentsMargins(0,0,0,0)
        mainButtonsLayout.setSpacing(5)
        ## Main buttons layout
        mainBtnLayout = QHBoxLayout()
        mainBtnLayout.setContentsMargins(0,0,0,0)
        mainBtnLayout.setSpacing(5)
        ###################################
        ##### Mass 1 Parameters
        ###################################
        # Mass 1 parameters header
        mass1Header = QLabel("Mass 1 Parameters")
        mass1ParamLayout.addWidget(mass1Header, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Mass 1 combo box
        mass1ComboBox = QComboBox()
        mass1ComboBox.setObjectName(mass1CBName)
        mass1ComboBox.setMinimumWidth(comboBoxMinWidth)
        mass1ComboBox.setMinimumHeight(comboBoxMinHeight)
        mass1ComboBox.addItems(cbItems)
        mass1ComboBox.currentIndexChanged.connect(self.OnMass1CBChange)
        mass1ParamLayout.addWidget(mass1ComboBox, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Mass 1 name line edit
        mass1NameLE = QLineEdit()
        mass1NameLE.setObjectName(mass1MassNameLEName)
        mass1NameLE.setMinimumWidth(lineEditMinWidth)
        mass1NameLE.setMinimumHeight(lineEditMinHeight)
        mass1NameLE.setPlaceholderText("Mass 1 Name")
        # mass1NameLE.textChanged.connect(self.OnMass1Change)
        mass1ParamLayout.addWidget(mass1NameLE)
        # Mass 1 mass line edit
        mass1MassLE = QLineEdit()
        mass1MassLE.setObjectName(mass1MassLEName)
        mass1MassLE.setMinimumWidth(lineEditMinWidth)
        mass1MassLE.setMinimumHeight(lineEditMinHeight)
        mass1MassLE.setPlaceholderText("Mass 1 In (Kg)")
        # mass1MassLE.textChanged.connect(self.OnMass1Change)
        mass1ParamLayout.addWidget(mass1MassLE)
        ## Mass 1 initial x position line edit
        mass1XPosLE = QLineEdit()
        mass1XPosLE.setObjectName(mass1InitPosXLEName)
        mass1XPosLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass1XPosLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass1XPosLE.setPlaceholderText("Initial X Position In (m)")
        # mass1XPosLE.textChanged.connect(self.OnMass1Change)
        mass1XValsLayout.addWidget(mass1XPosLE)
        ## Mass 1 initial x velocity line edit
        mass1XVelLE = QLineEdit()
        mass1XVelLE.setObjectName(mass1InitVelXLEName)
        mass1XVelLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass1XVelLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass1XVelLE.setPlaceholderText("Initial X Velocity In (m/s)")
        # mass1XVelLE.textChanged.connect(self.OnMass1Change)
        mass1XValsLayout.addWidget(mass1XVelLE)
        ## Mass 1 initial y position line edit
        mass1YPosLE = QLineEdit()
        mass1YPosLE.setObjectName(mass1InitPosYLEName)
        mass1YPosLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass1YPosLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass1YPosLE.setPlaceholderText("Initial Y Position In (m)")
        # mass1YPosLE.textChanged.connect(self.OnMass1Change)
        mass1YValsLayout.addWidget(mass1YPosLE)
        ## Mass 1 initial y velocity line edit
        mass1YVelLE = QLineEdit()
        mass1YVelLE.setObjectName(mass1InitVelYLEName)
        mass1YVelLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass1YVelLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass1YVelLE.setPlaceholderText("Initial Y Velocity In (m/s)")
        # mass1YVelLE.textChanged.connect(self.OnMass1Change)
        mass1YValsLayout.addWidget(mass1YVelLE)
        ## Mass 1 initial z position line edit
        mass1ZPosLE = QLineEdit()
        mass1ZPosLE.setObjectName(mass1InitPosZLEName)
        mass1ZPosLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass1ZPosLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass1ZPosLE.setPlaceholderText("Initial Z Position In (m)")
        # mass1ZPosLE.textChanged.connect(self.OnMass1Change)
        mass1ZValsLayout.addWidget(mass1ZPosLE)
        ## Mass 1 initial z velocity line edit
        mass1ZVelLE = QLineEdit()
        mass1ZVelLE.setObjectName(mass1InitVelZLEName)
        mass1ZVelLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass1ZVelLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass1ZVelLE.setPlaceholderText("Initial Z Velocity In (m/s)")
        # mass1ZVelLE.textChanged.connect(self.OnMass1Change)
        mass1ZValsLayout.addWidget(mass1ZVelLE)
        ## Add layouts to parent
        mass1ParamLayout.addLayout(mass1XValsLayout)
        mass1ParamLayout.addLayout(mass1YValsLayout)
        mass1ParamLayout.addLayout(mass1ZValsLayout)
        # Clear mass 1 parameters button
        mass1ClearBtn = QPushButton("Clear Mass 1 Parameters")
        mass1ClearBtn.setObjectName(mass1ClearBtnName)
        mass1ClearBtn.setMinimumWidth(buttonMinWidth)
        mass1ClearBtn.setMinimumHeight(buttonMinHeight)
        mass1ClearBtn.clicked.connect(self.ClearMass1Params)
        mass1ParamLayout.addWidget(mass1ClearBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Randomize mass 1 parameters button
        mass1RandBtn = QPushButton("Random Mass 1 Parameters")
        mass1RandBtn.setObjectName(mass1RandBtnName)
        mass1RandBtn.setMinimumWidth(buttonMinWidth)
        mass1RandBtn.setMinimumHeight(buttonMinHeight)
        mass1RandBtn.clicked.connect(self.RandomMass1)
        mass1ParamLayout.addWidget(mass1RandBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Mass 1 parameters spacer
        mass1Spacer = QSpacerItem(0, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        mass1ParamLayout.addSpacerItem(mass1Spacer)
        ###################################
        ##### Time Values 
        ###################################
        # Time values header
        timeValHeader = QLabel("Time Values")
        timeValLayout.addWidget(timeValHeader, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Time span line edit
        timeSpanLE = QLineEdit()
        timeSpanLE.setObjectName(timeValLEName)
        timeSpanLE.setMinimumWidth(lineEditMinWidth)
        timeSpanLE.setMinimumHeight(lineEditMinHeight)
        timeSpanLE.setPlaceholderText("Time Span In Earth Years")
        timeValLayout.addWidget(timeSpanLE)
        # Clear time span buttons
        timeSpanClearBtn = QPushButton("Clear Time Span")
        timeSpanClearBtn.setObjectName(timeValClearBtnName)
        timeSpanClearBtn.setMinimumWidth(buttonMinWidth)
        timeSpanClearBtn.setMinimumHeight(buttonMinHeight)
        timeValLayout.addWidget(timeSpanClearBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Randomize time span buttons
        timeSpanRandBtn = QPushButton("Random Time Span")
        timeSpanRandBtn.setObjectName(timeValRandBtnName)
        timeSpanRandBtn.setMinimumWidth(buttonMinWidth)
        timeSpanRandBtn.setMinimumHeight(buttonMinHeight)
        timeValLayout.addWidget(timeSpanRandBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Time values spacer
        timeSpacer = QSpacerItem(0, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        timeValLayout.addSpacerItem(timeSpacer)
        ###################################
        ##### Mass 2 Parameters
        ###################################
        # Mass 2 parameters header
        mass2ParamHeader = QLabel("Mass 2 Parameters")
        mass2ParamLayout.addWidget(mass2ParamHeader, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Mass 2 combo box
        mass2ComboBox = QComboBox()
        mass2ComboBox.setObjectName(mass2CBName)
        mass2ComboBox.setMinimumWidth(comboBoxMinWidth)
        mass2ComboBox.setMinimumHeight(comboBoxMinHeight)
        mass2ComboBox.addItems(cbItems)
        mass2ParamLayout.addWidget(mass2ComboBox, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Mass 2 name line edit
        mass2NameLE = QLineEdit()
        mass2NameLE.setObjectName(mass2MassNameLEName)
        mass2NameLE.setMinimumWidth(lineEditMinWidth)
        mass2NameLE.setMinimumHeight(lineEditMinHeight)
        mass2NameLE.setPlaceholderText("Mass 2 Name")
        mass2ParamLayout.addWidget(mass2NameLE)
        # Mass 2 mass line edit
        mass2MassLE = QLineEdit()
        mass2MassLE.setObjectName(mass2MassLEName)
        mass2MassLE.setMinimumWidth(lineEditMinWidth)
        mass2MassLE.setMinimumHeight(lineEditMinHeight)
        mass2MassLE.setPlaceholderText("Mass 2 In (Kg)")
        mass2ParamLayout.addWidget(mass2MassLE)
        ## Mass 2 initial x position line edit
        mass2XPosLE = QLineEdit()
        mass2XPosLE.setObjectName(mass2InitPosXLEName)
        mass2XPosLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass2XPosLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass2XPosLE.setPlaceholderText("Initial X Position In (m)")
        mass2XValsLayout.addWidget(mass2XPosLE)
        ## Mass 2 initial x velocity line edit
        mass2XVelLE = QLineEdit()
        mass2XVelLE.setObjectName(mass2InitVelXLEName)
        mass2XVelLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass2XVelLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass2XVelLE.setPlaceholderText("Initial X Velocity In (m/s)")
        mass2XValsLayout.addWidget(mass2XVelLE)
        ## Mass 2 initial y position line edit
        mass2YPosLE = QLineEdit()
        mass2YPosLE.setObjectName(mass2InitPosYLEName)
        mass2YPosLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass2YPosLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass2YPosLE.setPlaceholderText("Initial Y Position In (m)")
        mass2YValsLayout.addWidget(mass2YPosLE)
        ## Mass 2 initial y velocity line edit
        mass2YVelLE = QLineEdit()
        mass2YVelLE.setObjectName(mass2InitVelYLEName)
        mass2YVelLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass2YVelLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass2YVelLE.setPlaceholderText("Initial Y Velocity In (m/s)")
        mass2YValsLayout.addWidget(mass2YVelLE)
        ## Mass 2 initial z position line edit
        mass2ZPosLE = QLineEdit()
        mass2ZPosLE.setObjectName(mass2InitPosZLEName)
        mass2ZPosLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass2ZPosLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass2ZPosLE.setPlaceholderText("Initial Z Position In (m)")
        mass2ZValsLayout.addWidget(mass2ZPosLE)
        ## Mass 2 initial z velocity line edit
        mass2ZVelLE = QLineEdit()
        mass2ZVelLE.setObjectName(mass2InitVelZLEName)
        mass2ZVelLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass2ZVelLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass2ZVelLE.setPlaceholderText("Initial Z Velocity In (m/s)")
        mass2ZValsLayout.addWidget(mass2ZVelLE)
        ## Add layouts to parent
        mass2ParamLayout.addLayout(mass2XValsLayout)
        mass2ParamLayout.addLayout(mass2YValsLayout)
        mass2ParamLayout.addLayout(mass2ZValsLayout)
        # Clear Mass 2 parameters button
        mass2ClearBtn = QPushButton("Clear Mass 2 Parameters")
        mass2ClearBtn.setObjectName(mass2ClearBtnName)
        mass2ClearBtn.setMinimumWidth(buttonMinWidth)
        mass2ClearBtn.setMinimumHeight(buttonMinHeight)
        mass2ParamLayout.addWidget(mass2ClearBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Randomize Mass 2 parameters button
        mass2RandBtn = QPushButton("Random Mass 2 Parameters")
        mass2RandBtn.setObjectName(mass2RandBtnName)
        mass2RandBtn.setMinimumWidth(buttonMinWidth)
        mass2RandBtn.setMinimumHeight(buttonMinHeight)
        mass2ParamLayout.addWidget(mass2RandBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Mass 2 parameters spacer
        mass2Spacer = QSpacerItem(0, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        mass2ParamLayout.addSpacerItem(mass2Spacer)
        # Add layouts to parent
        paramLayout.addLayout(mass1ParamLayout)
        paramLayout.addLayout(timeValLayout)
        paramLayout.addLayout(mass2ParamLayout)
        ###################################
        ##### Plot Selection
        ###################################
        # Plot selection header
        plotSelHeader = QLabel("Select Plot(s)")
        plotSelLayout.addWidget(plotSelHeader, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## 2D Position plot checkbox
        plotSelPosPlot2DCB = QCheckBox("2D Position Plot")
        plotSelPosPlot2DCB.setObjectName(pos2DPlotCBName)
        plotSel2DCBLayout.addWidget(plotSelPosPlot2DCB, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## 2D Position animation checkbox
        plotSelPosAni2DCB = QCheckBox("2D Position Animation")
        plotSelPosAni2DCB.setObjectName(pos2DAniCBName)
        plotSel2DCBLayout.addWidget(plotSelPosAni2DCB, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## 2D Velocity plot checkbox
        plotSelPosVel2DCB = QCheckBox("2D Velocity Plot")
        plotSelPosVel2DCB.setObjectName(vel2DPlotCBName)
        plotSel2DCBLayout.addWidget(plotSelPosVel2DCB, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## 2D Velocity animation checkbox
        plotSelVelAni2DCB = QCheckBox("2D Velocity Animation")
        plotSelVelAni2DCB.setObjectName(vel2DAniCBName)
        plotSel2DCBLayout.addWidget(plotSelVelAni2DCB, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## 3D Position plot checkbox
        plotSelPosPlot3DCB = QCheckBox("3D Position Plot")
        plotSelPosPlot3DCB.setObjectName(pos3DPlotCBName)
        plotSel3DCBLayout.addWidget(plotSelPosPlot3DCB, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## 3D Position animation checkbox
        plotSelPosAni3DCB = QCheckBox("3D Position Animation")
        plotSelPosAni3DCB.setObjectName(pos3DAniCBName)
        plotSel3DCBLayout.addWidget(plotSelPosAni3DCB, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## 3D Velocity plot checkbox
        plotSelPosVel3DCB = QCheckBox("3D Velocity Plot")
        plotSelPosVel3DCB.setObjectName(vel3DPlotCBName)
        plotSel3DCBLayout.addWidget(plotSelPosVel3DCB, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## 3D Velocity animation checkbox
        plotSelVelAni3DCB = QCheckBox("3D Velocity Animation")
        plotSelVelAni3DCB.setObjectName(vel3DAniCBName)
        plotSel3DCBLayout.addWidget(plotSelVelAni3DCB, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Select all checkboxes button
        plotSelAllBtn = QPushButton("Select All Plots")
        plotSelAllBtn.setObjectName(plotSelAllBtnName)
        plotSelAllBtn.setMinimumWidth(buttonMinWidth)
        plotSelAllBtn.setMinimumHeight(buttonMinHeight)
        plotSelBtnLayout.addWidget(plotSelAllBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Random all checkboxes button
        plotSelRandBtn = QPushButton("Random Plots")
        plotSelRandBtn.setObjectName(plotSelRandBtnName)
        plotSelRandBtn.setMinimumWidth(buttonMinWidth)
        plotSelRandBtn.setMinimumHeight(buttonMinHeight)
        plotSelBtnLayout.addWidget(plotSelRandBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Unselect all checkboxes button
        plotSelUnsBtn = QPushButton("Unselect All Plots")
        plotSelUnsBtn.setObjectName(plotSelUnsBtnName)
        plotSelUnsBtn.setMinimumWidth(buttonMinWidth)
        plotSelUnsBtn.setMinimumHeight(buttonMinHeight)
        plotSelBtnLayout.addWidget(plotSelUnsBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Add layouts to parent
        plotSelLayout.addLayout(plotSel2DCBLayout)
        plotSelLayout.addLayout(plotSel3DCBLayout)
        plotSelLayout.addLayout(plotSelBtnLayout)
        # Plot selection spacer
        plotSelectionSpacer = QSpacerItem(0, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        plotSelLayout.addSpacerItem(plotSelectionSpacer)
        ###################################
        ##### Main Buttons
        ###################################
        # Main buttons header
        mainButtonsHeader = QLabel("Calculate / Clear All / Randomize All / Return Home")
        mainButtonsLayout.addWidget(mainButtonsHeader, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Calculate button
        calcBtn = QPushButton("Calculate")
        calcBtn.setObjectName(calculateBtnName)
        calcBtn.setMinimumWidth(buttonMinWidth - 50)
        calcBtn.setMinimumHeight(buttonMinHeight)
        mainBtnLayout.addWidget(calcBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Clear button
        clearBtn = QPushButton("Clear All")
        clearBtn.setObjectName(clearBtnName)
        clearBtn.setMinimumWidth(buttonMinWidth - 50)
        clearBtn.setMinimumHeight(buttonMinHeight)
        mainBtnLayout.addWidget(clearBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Random button
        randomBtn = QPushButton("Random All")
        randomBtn.setObjectName(randomBtnName)
        randomBtn.setMinimumWidth(buttonMinWidth - 50)
        randomBtn.setMinimumHeight(buttonMinHeight)
        mainBtnLayout.addWidget(randomBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Home button
        homeBtn = QPushButton("Return Home")
        homeBtn.setObjectName(homeBtnName)
        homeBtn.setMinimumWidth(buttonMinWidth - 50)
        homeBtn.setMinimumHeight(buttonMinHeight)
        homeBtn.clicked.connect(self.ReturnHome)
        mainBtnLayout.addWidget(homeBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Add layouts to parent
        mainButtonsLayout.addLayout(mainBtnLayout)
        # Main buttons spacer
        mainButtonsSpacer = QSpacerItem(0, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        mainButtonsLayout.addSpacerItem(mainButtonsSpacer)
        ###################################
        ##### Main Spacers / Set Layout
        ###################################
        # Add layouts
        mainLayout.addLayout(paramLayout)
        mainLayout.addLayout(plotSelLayout)
        mainLayout.addLayout(mainButtonsLayout)
        # Spacers
        mainSpacer = QSpacerItem(0, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        mainLayout.addSpacerItem(mainSpacer)
        # Set layout
        self.setLayout(mainLayout)
        # Default state
        self.DefaultState(5)

    """ OnMass1CBChange - Event handler for when mass 1's checkbox is changed
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab the children from the window
            * Grab the current index of the combo box
            * If the combo box is set to 0
                * Clear the parameters
                * Return the field to its default state
            * Otherwise
                * If the combo box is set to anything but 1
                    * Populate the fields with parameters for that object
                * Otherwise
                    * Clear the line edits of the field
        Output:
            This function does not return a value
    """
    def OnMass1CBChange(self):
        # Grab children
        children = self.GrabChildren()
        # Current index
        currentIndex = children[0][0].currentIndex()
        # Combo box set to 0
        if (currentIndex == 0):
            self.ClearMass1Params()
            self.DefaultState(0)
        # Otherwise 
        else:
            self.EnableFields(0)
            children[0][1].setText(str(cbItems[currentIndex]))
            if (currentIndex != 1):
                children[0][2].setText(str(MASSESARR[currentIndex - 2]))
                children[0][3].setText(str(POSMATRIX[currentIndex - 2][0]))
                children[0][4].setText(str(POSMATRIX[currentIndex - 2][1]))
                children[0][5].setText(str(POSMATRIX[currentIndex - 2][2]))
                children[0][6].setText(str(VELMATRIX[currentIndex - 2][0]))
                children[0][7].setText(str(VELMATRIX[currentIndex - 2][1]))
                children[0][8].setText(str(VELMATRIX[currentIndex - 2][2]))
            else:
                for widget in children[0][1:9]:
                    widget.setText("")

    """ RandomMass1 - Randomizes the mass 1 parameters
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab children from the window
            * Generate a random index for the combo box
            * If the object is not the arbitrary object
                * Set the combo box to the random index
            * Otherwise
                * Randomize values for arbitrary object
        Output:

    """
    def RandomMass1(self):
        # Grab children
        children = self.GrabChildren()
        # Generate random number
        randIndex = random.randint(1,12)
        # Not arbitrary object
        if (randIndex != 1):
            children[0][0].setCurrentIndex(randIndex)
        # Arbitrary object
        else:
            children[0][0].setCurrentIndex(randIndex)
            randomMass = round(random.uniform(0.01 * MPLUTO, random.uniform(1, 1e10) * random.choice(MASSESARR)),2)
            randomXPos = round(random.uniform(0, random.choice([-1,1]) * random.randint(1,20) * random.choice(POSMATRIX[1:][1])),2)
            randomYPos = round(random.uniform(0, random.choice([-1,1]) * random.randint(1,20) * random.choice(POSMATRIX[1:][1])),2)
            randomZPos = round(random.uniform(0, random.choice([-1,1]) * random.randint(1,20) * random.choice(POSMATRIX[1:][1])),2)
            randomXVel = round(random.uniform(0, random.choice([-1,1]) * random.randint(1,20) * random.choice(VELMATRIX[1:][1])),2)
            randomYVel = round(random.uniform(0, random.choice([-1,1]) * random.randint(1,20) * random.choice(VELMATRIX[1:][1])),2)
            randomZVel = round(random.uniform(0, random.choice([-1,1]) * random.randint(1,20) * random.choice(VELMATRIX[1:][1])),2)
            randomArr = [randomMass, randomXPos, randomYPos, randomZPos, randomXVel, randomYVel, randomZVel]
            for i in range(len(randomArr)):
                children[0][i + 2].setText(str(randomArr[i]))

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
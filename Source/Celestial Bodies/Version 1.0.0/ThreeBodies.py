from ModelFunctions import *

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### Simulation Window
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

""" ThreeBodyWindow - Class for two body simulation windows
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
xAxisXCBName = "X Axis X Direction CB"
xAxisYCBName = "X Axis Y Direction CB"
xAxisZCBName = "X Axis Z Direction CB"
xAxisTCBName = "X Axis Time CB"
yAxisXCBName = "Y Axis X Direction CB"
yAxisYCBName = "Y Axis Y Direction CB"
yAxisZCBName = "Y Axis Z Direction CB"
yAxisTCBName = "Y Axis Time CB"
zAxisXCBName = "Z Axis X Direction CB"
zAxisYCBName = "Z Axis Y Direction CB"
zAxisZCBName = "Z Axis Z Direction CB"
zAxisTCBName = "Z Axis Time CB"
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

class ThreeBodyWindow(QWidget):
    """ Constructor - Constructs window with widgets and layouts of widgets
        Input:
            mainWindow - The main window of the application
        Algorithm:
            * Set the main window variable
            * Call the init ui function
        Output:
            This function does not return a value
    """
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.InitUI()

    """ InitUI - Initializes the user interface for the window
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Create layouts for the widgets
            * Add widgets to layouts
            * Add layouts to main layout
            * Set main layout
        Output:
            This function does not return a value
    """
    def InitUI(self):
        # Title of window
        self.setWindowTitle("Three Body Simulation")
        # Height and width of window
        self.resize(800, 500)
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        ###################################
        ##### Layouts
        ###################################
        # Main layout
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(10,10,10,10)
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
        ## Plot selection axis layout
        plotSelAxiiCBLayout = QHBoxLayout()
        plotSelAxiiCBLayout.setContentsMargins(0,0,0,0)
        plotSelAxiiCBLayout.setSpacing(5)
        ## Plot selection x axis layout
        plotSelXAxisLayout = QVBoxLayout()
        plotSelXAxisLayout.setContentsMargins(0,0,0,0)
        plotSelXAxisLayout.setSpacing(5)
        ## Plot selection x axis CB layout
        plotSelXAxisCBLayout = QHBoxLayout()
        plotSelXAxisCBLayout.setContentsMargins(0,0,0,0)
        plotSelXAxisCBLayout.setSpacing(5)
        ## Plot selection y axis layout
        plotSelYAxisLayout = QVBoxLayout()
        plotSelYAxisLayout.setContentsMargins(0,0,0,0)
        plotSelYAxisLayout.setSpacing(5)
        ## Plot selection y axis CB layout
        plotSelYAxisCBLayout = QHBoxLayout()
        plotSelYAxisCBLayout.setContentsMargins(0,0,0,0)
        plotSelYAxisCBLayout.setSpacing(5)
        ## Plot selection z axis layout
        plotSelZAxisLayout = QVBoxLayout()
        plotSelZAxisLayout.setContentsMargins(0,0,0,0)
        plotSelZAxisLayout.setSpacing(5)
        ## Plot selection z axis CB layout
        plotSelZAxisCBLayout = QHBoxLayout()
        plotSelZAxisCBLayout.setContentsMargins(0,0,0,0)
        plotSelZAxisCBLayout.setSpacing(5)
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
        mass1ParamLayout.addWidget(mass1ComboBox, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Mass 1 name line edit
        mass1NameLE = QLineEdit()
        mass1NameLE.setObjectName(mass1MassNameLEName)
        mass1NameLE.setMinimumWidth(lineEditMinWidth)
        mass1NameLE.setMinimumHeight(lineEditMinHeight)
        mass1NameLE.setPlaceholderText("Mass 1 Name")
        mass1ParamLayout.addWidget(mass1NameLE)
        # Mass 1 mass line edit
        mass1MassLE = QLineEdit()
        mass1MassLE.setObjectName(mass1MassLEName)
        mass1MassLE.setMinimumWidth(lineEditMinWidth)
        mass1MassLE.setMinimumHeight(lineEditMinHeight)
        mass1MassLE.setPlaceholderText("Mass 1 In (Kg)")
        mass1ParamLayout.addWidget(mass1MassLE)
        ## Mass 1 initial x position line edit
        mass1XPosLE = QLineEdit()
        mass1XPosLE.setObjectName(mass1InitPosXLEName)
        mass1XPosLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass1XPosLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass1XPosLE.setPlaceholderText("Initial X Position In (m)")
        mass1XValsLayout.addWidget(mass1XPosLE)
        ## Mass 1 initial x velocity line edit
        mass1XVelLE = QLineEdit()
        mass1XVelLE.setObjectName(mass1InitVelXLEName)
        mass1XVelLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass1XVelLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass1XVelLE.setPlaceholderText("Initial X Velocity In (m/s)")
        mass1XValsLayout.addWidget(mass1XVelLE)
        ## Mass 1 initial y position line edit
        mass1YPosLE = QLineEdit()
        mass1YPosLE.setObjectName(mass1InitPosYLEName)
        mass1YPosLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass1YPosLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass1YPosLE.setPlaceholderText("Initial Y Position In (m)")
        mass1YValsLayout.addWidget(mass1YPosLE)
        ## Mass 1 initial y velocity line edit
        mass1YVelLE = QLineEdit()
        mass1YVelLE.setObjectName(mass1InitVelYLEName)
        mass1YVelLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass1YVelLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass1YVelLE.setPlaceholderText("Initial Y Velocity In (m/s)")
        mass1YValsLayout.addWidget(mass1YVelLE)
        ## Mass 1 initial z position line edit
        mass1ZPosLE = QLineEdit()
        mass1ZPosLE.setObjectName(mass1InitPosZLEName)
        mass1ZPosLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass1ZPosLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass1ZPosLE.setPlaceholderText("Initial Z Position In (m)")
        mass1ZValsLayout.addWidget(mass1ZPosLE)
        ## Mass 1 initial z velocity line edit
        mass1ZVelLE = QLineEdit()
        mass1ZVelLE.setObjectName(mass1InitVelZLEName)
        mass1ZVelLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass1ZVelLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass1ZVelLE.setPlaceholderText("Initial Z Velocity In (m/s)")
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
        mass1ParamLayout.addWidget(mass1ClearBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Randomize mass 1 parameters button
        mass1RandBtn = QPushButton("Random Mass 1 Parameters")
        mass1RandBtn.setObjectName(mass1RandBtnName)
        mass1RandBtn.setMinimumWidth(buttonMinWidth)
        mass1RandBtn.setMinimumHeight(buttonMinHeight)
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
        ###################################
        ##### Plot selection axis
        ###################################
        # X axis header
        plotSelXAxisHeader = QLabel("X Axis Direction")
        plotSelXAxisLayout.addWidget(plotSelXAxisHeader, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## X axis x direction
        plotSelXAxisXCB = QCheckBox("X")
        plotSelXAxisXCB.setObjectName(xAxisXCBName)
        plotSelXAxisCBLayout.addWidget(plotSelXAxisXCB, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## X axis y direction
        plotSelXAxisYCB = QCheckBox("Y")
        plotSelXAxisYCB.setObjectName(xAxisYCBName)
        plotSelXAxisCBLayout.addWidget(plotSelXAxisYCB, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## X axis z direction
        plotSelXAxisZCB = QCheckBox("Z")
        plotSelXAxisZCB.setObjectName(xAxisZCBName)
        plotSelXAxisCBLayout.addWidget(plotSelXAxisZCB, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## X axis time
        plotSelXAxisTCB = QCheckBox("Time")
        plotSelXAxisTCB.setObjectName(xAxisTCBName)
        plotSelXAxisCBLayout.addWidget(plotSelXAxisTCB, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Add x axis children to parent
        plotSelXAxisLayout.addLayout(plotSelXAxisCBLayout)
        # Y axis header
        plotSelYAxisHeader = QLabel("Y Axis Direction")
        plotSelYAxisLayout.addWidget(plotSelYAxisHeader, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Y axis x direction
        plotSelYAxisXCB = QCheckBox("X")
        plotSelYAxisXCB.setObjectName(yAxisXCBName)
        plotSelYAxisCBLayout.addWidget(plotSelYAxisXCB, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Y axis y direction
        plotSelYAxisYCB = QCheckBox("Y")
        plotSelYAxisYCB.setObjectName(yAxisYCBName)
        plotSelYAxisCBLayout.addWidget(plotSelYAxisYCB, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Y axis z direction
        plotSelYAxisZCB = QCheckBox("Z")
        plotSelYAxisZCB.setObjectName(yAxisZCBName)
        plotSelYAxisCBLayout.addWidget(plotSelYAxisZCB, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Y axis time
        plotSelYAxisTCB = QCheckBox("Time")
        plotSelYAxisTCB.setObjectName(yAxisTCBName)
        plotSelYAxisCBLayout.addWidget(plotSelYAxisTCB, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Add y axis children to parent
        plotSelYAxisLayout.addLayout(plotSelYAxisCBLayout)
        # Z axis header
        plotSelZAxisHeader = QLabel("Z Axis Direction")
        plotSelZAxisLayout.addWidget(plotSelZAxisHeader, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Z axis x direction
        plotSelZAxisXCB = QCheckBox("X")
        plotSelZAxisXCB.setObjectName(zAxisXCBName)
        plotSelZAxisCBLayout.addWidget(plotSelZAxisXCB, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Z axis y direction
        plotSelZAxisYCB = QCheckBox("Y")
        plotSelZAxisYCB.setObjectName(zAxisYCBName)
        plotSelZAxisCBLayout.addWidget(plotSelZAxisYCB, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Z axis z direction
        plotSelZAxisZCB = QCheckBox("Z")
        plotSelZAxisZCB.setObjectName(zAxisZCBName)
        plotSelZAxisCBLayout.addWidget(plotSelZAxisZCB, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Z axis time
        plotSelZAxisTCB = QCheckBox("Time")
        plotSelZAxisTCB.setObjectName(zAxisTCBName)
        plotSelZAxisCBLayout.addWidget(plotSelZAxisTCB, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Add z axis children to parent
        plotSelZAxisLayout.addLayout(plotSelZAxisCBLayout)
        ## Add plot selection children to parent
        plotSelAxiiCBLayout.addLayout(plotSelXAxisLayout)
        plotSelAxiiCBLayout.addLayout(plotSelYAxisLayout)
        plotSelAxiiCBLayout.addLayout(plotSelZAxisLayout)
        ###################################
        ##### Plot selection buttons
        ###################################
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
        plotSelLayout.addLayout(plotSelAxiiCBLayout)
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
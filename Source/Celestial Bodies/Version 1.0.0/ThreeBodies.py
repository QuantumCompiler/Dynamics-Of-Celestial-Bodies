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
mass2RandBtnName = "Randomize Mass 3 Parameters Button"
mass3CBName = "Mass 3 Combo Box"
mass3MassLEName = "Mass 3 Mass Line Edit"
mass3MassNameLEName = "Mass 3 Name Line Edit"
mass3InitPosXLEName = "Mass 3 Initial Position In x Line Edit"
mass3InitPosYLEName = "Mass 3 Initial Position In y Line Edit"
mass3InitPosZLEName = "Mass 3 Initial Position In z Line Edit"
mass3InitVelXLEName = "Mass 3 Initial Velocity In x Line Edit"
mass3InitVelYLEName = "Mass 3 Initial Velocity In y Line Edit"
mass3InitVelZLEName = "Mass 3 Initial Velocity In z Line Edit"
mass3ClearBtnName = "Clear Mass 3 Parameters Button"
mass3RandBtnName = "Randomize Mass 3 Parameters Button"
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

    """ ClearMass1Params - Clears the mass 1 parameters children
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab the children from the window
            * Clear all the line edits in the field
        Output:
            This function does not return a value
    """
    def ClearMass1Params(self):
        # Grab children
        children = self.GrabChildren()
        # Clear children
        for widget in children[0][1:9]:
            widget.setText("")
    
    """ ClearMass2Params - Clears the mass 2 parameters children
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab the children from the window
            * Clear all the line edits in the field
        Output:
            This function does not return a value
    """
    def ClearMass2Params(self):
        # Grab children
        children = self.GrabChildren()
        # Clear children
        for widget in children[1][1:9]:
            widget.setText("")

    """ ClearMass3Params - Clears the mass 3 parameters children
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab the children from the window
            * Clear all the line edits in the field
        Output:
            This function does not return a value
    """
    def ClearMass3Params(self):
        # Grab children
        children = self.GrabChildren()
        # Clear children
        for widget in children[2][1:9]:
            widget.setText("")

    """ ClearTime - Clears the time value line edit
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab children from window
            * Clear the line edit
        Output:
            This function does not return a value
    """
    def ClearTime(self):
        # Grab children
        children = self.GrabChildren()
        # Clear field
        children[3][0].setText("")

    """ ConnectSignals - Connects the signals member functions to applicable widgets
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab children from window
            * Connect widgets to the signals member function
        Output:
            This function does not return a value
    """
    def ConnectSignals(self):
        # Grab children
        children = self.GrabChildren()
        # Connect widgets
        for widgets in children:
            for widget in widgets:
                if isinstance(widget, QComboBox):
                    widget.currentIndexChanged.connect(self.Signals)
                if isinstance(widget, QLineEdit):
                    widget.textChanged.connect(self.Signals)
                if isinstance(widget, QCheckBox):
                    widget.stateChanged.connect(self.Signals)

    """ DefaultState - Default state for widgets
        Input:
            field - Field that is to be set to default
                0 - Default mass 1 parameters
                1 - Default mass 2 parameters
                2 - Default mass 3 parameters
                3 - Default time values
                4 - Default plot selection checkbox parameters
                5 - Default x axis selection checkbox parameters
                6 - Default y axis selection checkbox parameters
                7 - Default z axis selection checkbox parameters
                8 - Default main buttons
                9 - Default 0-8
        Algorithm:
            * Grab children from window
            * Define disable mass 1 function
            * Define disable mass 2 function
            * Define disable mass 3 function
            * Define disable time function
            * Define disable plot selection checkboxes function
            * Define axis selection checkboxes function
            * Define disable calculate function
            * Define disable all function
            * Set the field(s) to default based upon the input parameter
        Output:
            This function does not return a value
    """
    def DefaultState(self, field):
        # Grab children
        children = self.GrabChildren()
        # Default mass 1 parameters children function
        def DefaultMass1():
            for widget in children[0][2:10]:
                widget.setDisabled(True)
        # Default mass 2 parameters children function
        def DefaultMass2():
            for widget in children[1][2:10]:
                widget.setDisabled(True)
        # Default mass 3 parameters children function
        def DefaultMass3():
            for widget in children[2][2:10]:
                widget.setDisabled(True)
        # Default time values children function
        def DefaultTime():
            for widget in children[3]:
                widget.setDisabled(True)
        # Default plot selection checkboxes children function
        def DefaultPlotSelCB():
            for widget in children[4]:
                widget.setDisabled(True)
        # Default x axis selection checkboxes children function
        def DefaultXAxisCB():
            for widget in children[5][0:4]:
                widget.setChecked(False)
                widget.setDisabled(True)
        # Default y axis selection checkboxes children function
        def DefaultYAxisCB():
            for widget in children[5][4:8]:
                widget.setChecked(False)
                widget.setDisabled(True)
        # Default z axis selection checkboxes children function
        def DefaultZAxisCB():
            for widget in children[5][8:12]:
                widget.setChecked(False)
                widget.setDisabled(True)
        # Default calculate button function
        def DefaultCalcBtn():
            children[6][0].setDisabled(True)
        # Default all function
        def DefaultAll():
            DefaultMass1()
            DefaultMass2()
            DefaultMass3()
            DefaultTime()
            DefaultPlotSelCB()
            DefaultXAxisCB()
            DefaultYAxisCB()
            DefaultZAxisCB()
            DefaultCalcBtn()
        # Set fields to default state
        if (field == 0):
            DefaultMass1()
        elif (field == 1):
            DefaultMass2()
        elif (field == 2):
            DefaultMass3()
        elif (field == 3):
            DefaultTime()
        elif (field == 4):
            DefaultPlotSelCB()
        elif (field == 5):
            DefaultXAxisCB()
        elif (field == 6):
            DefaultYAxisCB()
        elif (field == 7):
            DefaultZAxisCB()
        elif (field == 8):
            DefaultCalcBtn()
        elif (field == 9):
            DefaultAll()

    """ DisableFields - Disables fields based upon input parameter
        Input:
            Field - Integer value that determines what field is to be disabled
                0 - Disable mass 1 parameters
                1 - Disable mass 2 parameters
                2 - Disable mass 3 parameters
                3 - Disable time values
                4 - Disable plot selection checkbox parameters
                5 - Disable x axis selection checkbox parameters
                6 - Disable y axis selection checkbox parameters
                7 - Disable z axis selection checkbox parameters
                8 - Disable main buttons
                9 - Disable 0-8
        Algorithm:
            * Grab the children from the window
            * Define mass 1 parameters function
            * Define mass 2 parameters function
            * Define mass 3 parameters function
            * Define time values function
            * Define plot selection checkbox parameters function
            * Define axis selection checkbox parameters function
            * Define main buttons function
            * Define all functions function
            * Disable field based off input parameter value
        Output:
            This function does not return a value
    """
    def DisableFields(self, field):
        # Grab children
        children = self.GrabChildren()
        # Disable mass 1 parameters children function
        def DisableMass1():
            for widget in children[0][2:10]:
                widget.setDisabled(True)
        # Disable mass 2 parameters children function
        def DisableMass2():
            for widget in children[1][2:10]:
                widget.setDisabled(True)
        # Disable mass 3 parameters children function
        def DisableMass3():
            for widget in children[2][2:10]:
                widget.setDisabled(True)
        # Disable time values children function
        def DisableTime():
            for widget in children[3]:
                widget.setDisabled(True)
        # Disable plot selection checkboxes children function
        def DisablePlotSelCB():
            for widget in children[4]:
                widget.setDisabled(True)
        # Disable x axis selection checkboxes children function
        def DisableXAxisCB():
            for widget in children[5][0:4]:
                widget.setDisabled(True)
        # Disable y axis selection checkboxes children function
        def DisableYAxisCB():
            for widget in children[5][4:8]:
                widget.setDisabled(True)
        # Disable z axis selection checkboxes children function
        def DisableZAxisCB():
            for widget in children[5][8:12]:
                widget.setDisabled(True)
        # Disable calculate button function
        def DisableCalcBtn():
            children[6][0].setDisabled(True)
        # Disable all function
        def DisableAll():
            DisableMass1()
            DisableMass2()
            DisableMass3()
            DisableTime()
            DisablePlotSelCB()
            DisableXAxisCB()
            DisableYAxisCB()
            DisableZAxisCB()
            DisableCalcBtn()
        # Set fields to default state
        if (field == 0):
            DisableMass1()
        elif (field == 1):
            DisableMass2()
        elif (field == 2):
            DisableMass3()
        elif (field == 3):
            DisableTime()
        elif (field == 4):
            DisablePlotSelCB()
        elif (field == 5):
            DisableXAxisCB()
        elif (field == 6):
            DisableYAxisCB()
        elif (field == 7):
            DisableZAxisCB()
        elif (field == 8):
            DisableCalcBtn()
        elif (field == 9):
            DisableAll()

    """ EnableFields - Enables fields based upon input parameter
        Input:
            Field - Integer value that determines what field is to be enabled
                0 - Enable mass 1 parameters
                1 - Enable mass 2 parameters
                2 - Enable mass 3 parameters
                3 - Enable time values
                4 - Enable plot selection checkbox parameters
                5 - Enable x axis selection checkbox parameters
                6 - Enable y axis selection checkbox parameters
                7 - Enable z axis selection checkbox parameters
                8 - Enable main buttons
                9 - Enable 0-8
        Algorithm:
            * Grab the children from the window
            * Define mass 1 parameters function
            * Define mass 2 parameters function
            * Define mass 3 parameters function
            * Define time values function
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
        # Enable mass 1 parameters children function
        def EnableMass1():
            for widget in children[0][2:10]:
                widget.setEnabled(True)
        # Enable mass 2 parameters children function
        def EnableMass2():
            for widget in children[1][2:10]:
                widget.setEnabled(True)
        # Enable mass 3 parameters children function
        def EnableMass3():
            for widget in children[2][2:10]:
                widget.setEnabled(True)
        # Enable time values children function
        def EnableTime():
            for widget in children[3]:
                widget.setEnabled(True)
        # Enable plot selection checkboxes children function
        def EnablePlotSelCB():
            for widget in children[4]:
                widget.setEnabled(True)
        # Enable x axis selection checkboxes children function
        def EnableXAxisCB():
            for widget in children[5][0:4]:
                widget.setEnabled(True)
        # Enable y axis selection checkboxes children function
        def EnableYAxisCB():
            for widget in children[5][4:8]:
                widget.setEnabled(True)
        # Enable z axis selection checkboxes children function
        def EnableZAxisCB():
            for widget in children[5][8:12]:
                widget.setEnabled(True)
        # Enable calculate button function
        def EnableCalcBtn():
            children[6][0].setEnabled(True)
        # Enable all function
        def EnableAll():
            EnableMass1()
            EnableMass2()
            EnableMass3()
            EnableTime()
            EnablePlotSelCB()
            EnableXAxisCB()
            EnableYAxisCB()
            EnableZAxisCB()
            EnableCalcBtn()
        # Set fields to default state
        if (field == 0):
            EnableMass1()
        elif (field == 1):
            EnableMass2()
        elif (field == 2):
            EnableMass3()
        elif (field == 3):
            EnableTime()
        elif (field == 4):
            EnablePlotSelCB()
        elif (field == 5):
            EnableXAxisCB()
        elif (field == 6):
            EnableYAxisCB()
        elif (field == 7):
            EnableZAxisCB()
        elif (field == 8):
            EnableCalcBtn()
        elif (field == 9):
            EnableAll()

    """ GrabChildren - Grabs all the children from the fields
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab the children from the mass 1 parameters field, add them to their own array
            * Grab the children from the mass 2 parameters field, add them to their own array
            * Grab the children from the time values field, add them to their own array
            * Grab the children from the plot selection checkbox parameters field, add them to their own array
            * Grab the children from the axis selection checkbox parameters field, add them to their own array
            * Grab the children from the main buttons field, add them to their own array
        Output:
            mass1Arr - Array of mass 1 children
                mass1Arr[0] - Mass 1 combo box
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
                mass2Arr[0] - Mass 2 combo box
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
            mass3Arr - Array of mass 3 children
                mass3Arr[0] - Mass 3 combo box
                mass3Arr[1] - Mass 3 name line edit
                mass3Arr[2] - Mass 3 mass line edit
                mass3Arr[3] - Mass 3 initial x position line edit
                mass3Arr[4] - Mass 3 initial y position line edit
                mass3Arr[5] - Mass 3 initial z position line edit
                mass3Arr[6] - Mass 3 initial x velocity line edit
                mass3Arr[7] - Mass 3 initial y velocity line edit
                mass3Arr[8] - Mass 3 initial z velocity line edit
                mass3Arr[9] - Mass 3 clear parameters button
                mass3Arr[10] - Mass 3 random parameters button
            timeValArr - Array of time values children
                timeValArr[0] - Time span line edit
                timeValArr[1] - Time span clear button
                timeValArr[2] - Time span random button
            plotSelArr - Array of plot selection value children
                plotSelArr[0] - 2D position plot check box
                plotSelArr[1] - 2D position animation check box
                plotSelArr[2] - 2D velocity plot check box
                plotSelArr[3] - 2D velocity animation check box
                plotSelArr[4] - 3D position plot check box
                plotSelArr[5] - 3D position animation check box
                plotSelArr[6] - 3D velocity plot check box
                plotSelArr[7] - 3D velocity animation check box
                plotSelArr[8] - Select all plots button
                plotSelArr[9] - Random plots button
                plotSelArr[10] - Unselect all plots button
            axisSelArr - Array of axis selection value children
                axisSelArr[0] - X axis x direction check box
                axisSelArr[1] - X axis y direction check box
                axisSelArr[2] - X axis z direction check box
                axisSelArr[3] - X axis time check box
                axisSelArr[4] - Y axis x direction check box
                axisSelArr[5] - Y axis y direction check box
                axisSelArr[6] - Y axis z direction check box
                axisSelArr[7] - Y axis time check box
                axisSelArr[8] - Z axis x direction check box
                axisSelArr[9] - Z axis y direction check box
                axisSelArr[10] - Z axis z direction check box
                axisSelArr[11] - Z axis time check box
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
        # Mass 3 parameters
        mass3CB = self.findChild(QComboBox, mass3CBName)
        mass3MassNameLE = self.findChild(QLineEdit, mass3MassNameLEName)
        mass3MassLE = self.findChild(QLineEdit, mass3MassLEName)
        mass3InitPosXLE = self.findChild(QLineEdit, mass3InitPosXLEName)
        mass3InitPosYLE = self.findChild(QLineEdit, mass3InitPosYLEName)
        mass3InitPosZLE = self.findChild(QLineEdit, mass3InitPosZLEName)
        mass3InitVelXLE = self.findChild(QLineEdit, mass3InitVelXLEName)
        mass3InitVelYLE = self.findChild(QLineEdit, mass3InitVelYLEName)
        mass3InitVelZLE = self.findChild(QLineEdit, mass3InitVelZLEName)
        mass3ClearBtn = self.findChild(QPushButton, mass3ClearBtnName)
        mass3RandBtn = self.findChild(QPushButton, mass3RandBtnName)
        mass3Arr = [mass3CB, mass3MassNameLE, mass3MassLE, mass3InitPosXLE, mass3InitPosYLE, mass3InitPosZLE, mass3InitVelXLE, mass3InitVelYLE, mass3InitVelZLE, mass3ClearBtn, mass3RandBtn]
        # Time span parameters
        timeValLE = self.findChild(QLineEdit, timeValLEName)
        timeValClearBtn = self.findChild(QPushButton, timeValClearBtnName)
        timeValRandBtn = self.findChild(QPushButton, timeValRandBtnName)
        timeValArr = [timeValLE, timeValClearBtn, timeValRandBtn]
        # Plot check box parameters
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
        # Axis check box parameters
        xAxisXCB = self.findChild(QCheckBox, xAxisXCBName)
        xAxisYCB = self.findChild(QCheckBox, xAxisYCBName)
        xAxisZCB = self.findChild(QCheckBox, xAxisZCBName)
        xAxisTCB = self.findChild(QCheckBox, xAxisTCBName)
        yAxisXCB = self.findChild(QCheckBox, yAxisXCBName)
        yAxisYCB = self.findChild(QCheckBox, yAxisYCBName)
        yAxisZCB = self.findChild(QCheckBox, yAxisZCBName)
        yAxisTCB = self.findChild(QCheckBox, yAxisTCBName)
        zAxisXCB = self.findChild(QCheckBox, zAxisXCBName)
        zAxisYCB = self.findChild(QCheckBox, zAxisYCBName)
        zAxisZCB = self.findChild(QCheckBox, zAxisZCBName)
        zAxisTCB = self.findChild(QCheckBox, zAxisTCBName)
        axisSelArr = [xAxisXCB, xAxisYCB, xAxisZCB, xAxisTCB, yAxisXCB, yAxisYCB, yAxisZCB, yAxisTCB, zAxisXCB, zAxisYCB, zAxisZCB, zAxisTCB]
        # Main buttons parameters
        calculateBtn = self.findChild(QPushButton, calculateBtnName)
        clearBtn = self.findChild(QPushButton, clearBtnName)
        randomBtn = self.findChild(QPushButton, randomBtnName)
        homeBtn = self.findChild(QPushButton, homeBtnName)
        mainBtnsArr = [calculateBtn, clearBtn, randomBtn, homeBtn]
        # Return arrays
        return mass1Arr, mass2Arr, mass3Arr, timeValArr, plotSelArr, axisSelArr, mainBtnsArr

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
        self.resize(900, 600)
        self.setMinimumWidth(900)
        self.setMinimumHeight(600)
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
        # Mass 3 parameters layout
        mass3ParamLayout = QVBoxLayout()
        mass3ParamLayout.setContentsMargins(0,0,0,0)
        mass3ParamLayout.setSpacing(5)
        ## Mass 3 x vals sub layout
        mass3XValsLayout = QHBoxLayout()
        mass3XValsLayout.setContentsMargins(0,0,0,0)
        mass3XValsLayout.setSpacing(5)
        ## Mass 3 y vals sub layout
        mass3YValsLayout = QHBoxLayout()
        mass3YValsLayout.setContentsMargins(0,0,0,0)
        mass3YValsLayout.setSpacing(5)
        ## Mass 3 z vals sub layout
        mass3ZValsLayout = QHBoxLayout()
        mass3ZValsLayout.setContentsMargins(0,0,0,0)
        mass3ZValsLayout.setSpacing(5)
        # Time values layout
        timeValLayout = QVBoxLayout()
        timeValLayout.setContentsMargins(0,0,0,0)
        timeValLayout.setSpacing(5)
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
        mass1ComboBox.currentIndexChanged.connect(self.OnMass1CBChange)
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
        mass2ComboBox.currentIndexChanged.connect(self.OnMass2CBChange)
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
        mass2ClearBtn.clicked.connect(self.ClearMass2Params)
        mass2ParamLayout.addWidget(mass2ClearBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Randomize Mass 2 parameters button
        mass2RandBtn = QPushButton("Random Mass 2 Parameters")
        mass2RandBtn.setObjectName(mass2RandBtnName)
        mass2RandBtn.setMinimumWidth(buttonMinWidth)
        mass2RandBtn.setMinimumHeight(buttonMinHeight)
        mass2RandBtn.clicked.connect(self.RandomMass2)
        mass2ParamLayout.addWidget(mass2RandBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Mass 2 parameters spacer
        mass2Spacer = QSpacerItem(0, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        mass2ParamLayout.addSpacerItem(mass2Spacer)
        ###################################
        ##### Mass 3 Parameters
        ###################################
        # Mass 3 parameters header
        mass3ParamHeader = QLabel("Mass 3 Parameters")
        mass3ParamLayout.addWidget(mass3ParamHeader, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Mass 3 combo box
        mass3ComboBox = QComboBox()
        mass3ComboBox.setObjectName(mass3CBName)
        mass3ComboBox.setMinimumWidth(comboBoxMinWidth)
        mass3ComboBox.setMinimumHeight(comboBoxMinHeight)
        mass3ComboBox.addItems(cbItems)
        mass3ComboBox.currentIndexChanged.connect(self.OnMass3CBChange)
        mass3ParamLayout.addWidget(mass3ComboBox, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Mass 3 name line edit
        mass3NameLE = QLineEdit()
        mass3NameLE.setObjectName(mass3MassNameLEName)
        mass3NameLE.setMinimumWidth(lineEditMinWidth)
        mass3NameLE.setMinimumHeight(lineEditMinHeight)
        mass3NameLE.setPlaceholderText("Mass 3 Name")
        mass3ParamLayout.addWidget(mass3NameLE)
        # Mass 3 mass line edit
        mass3MassLE = QLineEdit()
        mass3MassLE.setObjectName(mass3MassLEName)
        mass3MassLE.setMinimumWidth(lineEditMinWidth)
        mass3MassLE.setMinimumHeight(lineEditMinHeight)
        mass3MassLE.setPlaceholderText("Mass 3 In (Kg)")
        mass3ParamLayout.addWidget(mass3MassLE)
        ## Mass 3 initial x position line edit
        mass3XPosLE = QLineEdit()
        mass3XPosLE.setObjectName(mass3InitPosXLEName)
        mass3XPosLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass3XPosLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass3XPosLE.setPlaceholderText("Initial X Position In (m)")
        mass3XValsLayout.addWidget(mass3XPosLE)
        ## Mass 3 initial x velocity line edit
        mass3XVelLE = QLineEdit()
        mass3XVelLE.setObjectName(mass3InitVelXLEName)
        mass3XVelLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass3XVelLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass3XVelLE.setPlaceholderText("Initial X Velocity In (m/s)")
        mass3XValsLayout.addWidget(mass3XVelLE)
        ## Mass 3 initial y position line edit
        mass3YPosLE = QLineEdit()
        mass3YPosLE.setObjectName(mass3InitPosYLEName)
        mass3YPosLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass3YPosLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass3YPosLE.setPlaceholderText("Initial Y Position In (m)")
        mass3YValsLayout.addWidget(mass3YPosLE)
        ## Mass 3 initial y velocity line edit
        mass3YVelLE = QLineEdit()
        mass3YVelLE.setObjectName(mass3InitVelYLEName)
        mass3YVelLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass3YVelLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass3YVelLE.setPlaceholderText("Initial Y Velocity In (m/s)")
        mass3YValsLayout.addWidget(mass3YVelLE)
        ## Mass 3 initial z position line edit
        mass3ZPosLE = QLineEdit()
        mass3ZPosLE.setObjectName(mass3InitPosZLEName)
        mass3ZPosLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass3ZPosLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass3ZPosLE.setPlaceholderText("Initial Z Position In (m)")
        mass3ZValsLayout.addWidget(mass3ZPosLE)
        ## Mass 3 initial z velocity line edit
        mass3ZVelLE = QLineEdit()
        mass3ZVelLE.setObjectName(mass3InitVelZLEName)
        mass3ZVelLE.setMinimumWidth(int(lineEditMinWidth / 2))
        mass3ZVelLE.setMinimumHeight(int(lineEditMinHeight / 2))
        mass3ZVelLE.setPlaceholderText("Initial Z Velocity In (m/s)")
        mass3ZValsLayout.addWidget(mass3ZVelLE)
        ## Add layouts to parent
        mass3ParamLayout.addLayout(mass3XValsLayout)
        mass3ParamLayout.addLayout(mass3YValsLayout)
        mass3ParamLayout.addLayout(mass3ZValsLayout)
        # Clear Mass 3 parameters button
        mass3ClearBtn = QPushButton("Clear Mass 3 Parameters")
        mass3ClearBtn.setObjectName(mass3ClearBtnName)
        mass3ClearBtn.setMinimumWidth(buttonMinWidth)
        mass3ClearBtn.setMinimumHeight(buttonMinHeight)
        mass3ClearBtn.clicked.connect(self.ClearMass3Params)
        mass3ParamLayout.addWidget(mass3ClearBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Randomize Mass 3 parameters button
        mass3RandBtn = QPushButton("Random Mass 3 Parameters")
        mass3RandBtn.setObjectName(mass3RandBtnName)
        mass3RandBtn.setMinimumWidth(buttonMinWidth)
        mass3RandBtn.setMinimumHeight(buttonMinHeight)
        mass3RandBtn.clicked.connect(self.RandomMass3)
        mass3ParamLayout.addWidget(mass3RandBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Mass 3 parameters spacer
        mass3Spacer = QSpacerItem(0, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        mass3ParamLayout.addSpacerItem(mass3Spacer)
        # Add layouts to parent
        paramLayout.addLayout(mass1ParamLayout)
        paramLayout.addLayout(mass2ParamLayout)
        paramLayout.addLayout(mass3ParamLayout)
        ###################################
        ##### Time Values 
        ###################################
        # Time values header
        timeValHeader = QLabel("Time Values")
        timeValLayout.addWidget(timeValHeader, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Time span line edit
        timeSpanLE = QLineEdit()
        timeSpanLE.setObjectName(timeValLEName)
        timeSpanLE.setMaximumWidth(lineEditMinWidth)
        timeSpanLE.setMinimumWidth(lineEditMinWidth)
        timeSpanLE.setMaximumHeight(lineEditMinHeight)
        timeSpanLE.setMinimumHeight(lineEditMinHeight)
        timeSpanLE.setPlaceholderText("Time Span In Earth Years")
        timeValLayout.addWidget(timeSpanLE, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Clear time span buttons
        timeSpanClearBtn = QPushButton("Clear Time Span")
        timeSpanClearBtn.setObjectName(timeValClearBtnName)
        timeSpanClearBtn.setMinimumWidth(buttonMinWidth)
        timeSpanClearBtn.setMinimumHeight(buttonMinHeight)
        timeSpanClearBtn.clicked.connect(self.ClearTime)
        timeValLayout.addWidget(timeSpanClearBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Randomize time span buttons
        timeSpanRandBtn = QPushButton("Random Time Span")
        timeSpanRandBtn.setObjectName(timeValRandBtnName)
        timeSpanRandBtn.setMinimumWidth(buttonMinWidth)
        timeSpanRandBtn.setMinimumHeight(buttonMinHeight)
        timeSpanRandBtn.clicked.connect(self.RandomTime)
        timeValLayout.addWidget(timeSpanRandBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        # Time values spacer
        timeSpacer = QSpacerItem(0, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        timeValLayout.addSpacerItem(timeSpacer)
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
        plotSelAllBtn.clicked.connect(self.SelectAllPlots)
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
        plotSelUnsBtn.clicked.connect(self.UnselectAllPlots)
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
        mainLayout.addLayout(timeValLayout)
        mainLayout.addLayout(plotSelLayout)
        mainLayout.addLayout(mainButtonsLayout)
        # Spacers
        mainSpacer = QSpacerItem(0, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        mainLayout.addSpacerItem(mainSpacer)
        # Set layout
        self.setLayout(mainLayout)
        # Set default state
        self.DefaultState(9)
        # Connect to signals
        self.ConnectSignals()

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
                for widget in children[0][2:9]:
                    widget.setText("")
    
    """ OnMass2CBChange - Event handler for when mass 2's checkbox is changed
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
    def OnMass2CBChange(self):
        # Grab children
        children = self.GrabChildren()
        # Current index
        currentIndex = children[1][0].currentIndex()
        # Combo box set to 0
        if (currentIndex == 0):
            self.ClearMass2Params()
            self.DefaultState(1)
        # Otherwise 
        else:
            self.EnableFields(1)
            children[1][1].setText(str(cbItems[currentIndex]))
            if (currentIndex != 1):
                children[1][2].setText(str(MASSESARR[currentIndex - 2]))
                children[1][3].setText(str(POSMATRIX[currentIndex - 2][0]))
                children[1][4].setText(str(POSMATRIX[currentIndex - 2][1]))
                children[1][5].setText(str(POSMATRIX[currentIndex - 2][2]))
                children[1][6].setText(str(VELMATRIX[currentIndex - 2][0]))
                children[1][7].setText(str(VELMATRIX[currentIndex - 2][1]))
                children[1][8].setText(str(VELMATRIX[currentIndex - 2][2]))
            else:
                for widget in children[1][2:9]:
                    widget.setText("")

    """ OnMass3CBChange - Event handler for when mass 3's checkbox is changed
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
    def OnMass3CBChange(self):
        # Grab children
        children = self.GrabChildren()
        # Current index
        currentIndex = children[2][0].currentIndex()
        # Combo box set to 0
        if (currentIndex == 0):
            self.ClearMass3Params()
            self.DefaultState(2)
        # Otherwise 
        else:
            self.EnableFields(2)
            children[2][1].setText(str(cbItems[currentIndex]))
            if (currentIndex != 1):
                children[2][2].setText(str(MASSESARR[currentIndex - 2]))
                children[2][3].setText(str(POSMATRIX[currentIndex - 2][0]))
                children[2][4].setText(str(POSMATRIX[currentIndex - 2][1]))
                children[2][5].setText(str(POSMATRIX[currentIndex - 2][2]))
                children[2][6].setText(str(VELMATRIX[currentIndex - 2][0]))
                children[2][7].setText(str(VELMATRIX[currentIndex - 2][1]))
                children[2][8].setText(str(VELMATRIX[currentIndex - 2][2]))
            else:
                for widget in children[2][2:9]:
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
            This function does not return a value
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
        elif (randIndex == 1):
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
    
    """ RandomMass2 - Randomizes the mass 2 parameters
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
            This function does not return a value
    """
    def RandomMass2(self):
        # Grab children
        children = self.GrabChildren()
        # Generate random number
        randIndex = random.randint(1,12)
        # Not arbitrary object
        if (randIndex != 1):
            children[1][0].setCurrentIndex(randIndex)
        # Arbitrary object
        elif (randIndex == 1):
            children[1][0].setCurrentIndex(randIndex)
            randomMass = round(random.uniform(0.01 * MPLUTO, random.uniform(1, 1e10) * random.choice(MASSESARR)),2)
            randomXPos = round(random.uniform(0, random.choice([-1,1]) * random.randint(1,20) * random.choice(POSMATRIX[1:][1])),2)
            randomYPos = round(random.uniform(0, random.choice([-1,1]) * random.randint(1,20) * random.choice(POSMATRIX[1:][1])),2)
            randomZPos = round(random.uniform(0, random.choice([-1,1]) * random.randint(1,20) * random.choice(POSMATRIX[1:][1])),2)
            randomXVel = round(random.uniform(0, random.choice([-1,1]) * random.randint(1,20) * random.choice(VELMATRIX[1:][1])),2)
            randomYVel = round(random.uniform(0, random.choice([-1,1]) * random.randint(1,20) * random.choice(VELMATRIX[1:][1])),2)
            randomZVel = round(random.uniform(0, random.choice([-1,1]) * random.randint(1,20) * random.choice(VELMATRIX[1:][1])),2)
            randomArr = [randomMass, randomXPos, randomYPos, randomZPos, randomXVel, randomYVel, randomZVel]
            for i in range(len(randomArr)):
                children[1][i + 2].setText(str(randomArr[i]))

    """ RandomMass3 - Randomizes the mass 3 parameters
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
            This function does not return a value
    """
    def RandomMass3(self):
        # Grab children
        children = self.GrabChildren()
        # Generate random number
        randIndex = random.randint(1,12)
        # Not arbitrary object
        if (randIndex != 1):
            children[2][0].setCurrentIndex(randIndex)
        # Arbitrary object
        elif (randIndex == 1):
            children[2][0].setCurrentIndex(randIndex)
            randomMass = round(random.uniform(0.01 * MPLUTO, random.uniform(1, 1e10) * random.choice(MASSESARR)),2)
            randomXPos = round(random.uniform(0, random.choice([-1,1]) * random.randint(1,20) * random.choice(POSMATRIX[1:][1])),2)
            randomYPos = round(random.uniform(0, random.choice([-1,1]) * random.randint(1,20) * random.choice(POSMATRIX[1:][1])),2)
            randomZPos = round(random.uniform(0, random.choice([-1,1]) * random.randint(1,20) * random.choice(POSMATRIX[1:][1])),2)
            randomXVel = round(random.uniform(0, random.choice([-1,1]) * random.randint(1,20) * random.choice(VELMATRIX[1:][1])),2)
            randomYVel = round(random.uniform(0, random.choice([-1,1]) * random.randint(1,20) * random.choice(VELMATRIX[1:][1])),2)
            randomZVel = round(random.uniform(0, random.choice([-1,1]) * random.randint(1,20) * random.choice(VELMATRIX[1:][1])),2)
            randomArr = [randomMass, randomXPos, randomYPos, randomZPos, randomXVel, randomYVel, randomZVel]
            for i in range(len(randomArr)):
                children[2][i + 2].setText(str(randomArr[i]))

    """ RandomTime - Randomizes the time span
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab children
        Output:
            This function does not return a value
    """
    def RandomTime(self):
        # Grab children
        children = self.GrabChildren()
        # Generate random value
        randTime = round(random.uniform(0, 1000), 2)
        # Set random time
        children[3][0].setText(str(randTime))

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

    """ SelectAllPlots - Selects all plot checkboxes
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab children from window
            * Set all checkboxes to checked
        Output:
            This function does not return a value
    """
    def SelectAllPlots(self):
        # Grab children
        children = self.GrabChildren()
        # Select all plots
        for widget in children[4][0:8]:
            widget.setChecked(True)

    """ Signals - Checks for specific conditions of line edits and combo boxes
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab the children from the window
            * Grab boolean values from fields
            * Enable time value field on specific conditions
            * Enable checkboxes on specific conditions
            * Enable calculate button on specific conditions
        Output:
            This function does not return a value
    """
    def Signals(self):
        # Grab children
        children = self.GrabChildren()
        # Check for combo boxes
        mass1ComboBox = children[0][0].currentIndex() != 0
        mass2ComboBox = children[1][0].currentIndex() != 0
        mass3ComboBox = children[2][0].currentIndex() != 0
        mass1Params = all(isinstance(widget, QLineEdit) and widget.text() != "" for widget in children[0][1:9])
        mass2Params = all(isinstance(widget, QLineEdit) and widget.text() != "" for widget in children[1][1:9])
        mass3Params = all(isinstance(widget, QLineEdit) and widget.text() != "" for widget in children[2][1:9])
        timeVals = children[3][0].text() != ""
        plotSelectionCB = any(isinstance(widget, QCheckBox) and widget.isChecked() == True for widget in children[4][0:8])
        no3DCB = all(isinstance(widget, QCheckBox) and widget.isChecked() == False for widget in children[4][4:8])
        xAxisCB = any(isinstance(widget, QCheckBox) and widget.isChecked() == True for widget in children[5][0:4])
        yAxisCB = any(isinstance(widget, QCheckBox) and widget.isChecked() == True for widget in children[5][4:8])
        zAxisCB = any(isinstance(widget, QCheckBox) and widget.isChecked() == True for widget in children[5][8:12])

    """ UnselectAllPlots - Unselects all plot checkboxes
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab children from window
            * Clear all checkboxes
        Output:
            This function does not return a value
    """
    def UnselectAllPlots(self):
        # Grab children
        children = self.GrabChildren()
        # Unselect all plots
        for widget in children[4][0:8]:
            widget.setChecked(False)
        # Unselect all axis
        for widget in children[5]:
            widget.setChecked(False)
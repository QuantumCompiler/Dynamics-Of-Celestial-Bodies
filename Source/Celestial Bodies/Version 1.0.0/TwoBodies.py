from ModelFunctions import *

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### Canvas / Plot Window
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

""" TwoBodyCanvas - Class for two body plots
    Member Functions:
        Constructor - Constructor for canvas with specific input parameters
"""
class TwoBodyCanvas(FigureCanvasQTAgg):
    """ Constructor - Constructor for canvas with specific input parameters
        Input:
            parent - Parent class
            width - Width of canvas
            height - Height of canvas
            dpi - DPI of canvas
        Algorithm:
            * Create a figure with the width, height, and dpi from the input parameters
            * Create an axis and add it to the figure
            * Call the constructor for FigureCanvasQTAgg with the figure previously created
        Output:
            This function does not return a value
    """
    def __init__(self, parent=None, width=3, height=2, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvasQTAgg.__init__(self, fig)

    """ Plot - Plots the results from a two body scenario
        Input:
            plotType - Type of plot that is to be generated
            masses - Array of masses in system
            ic - Matrix of initial conditions for each mass
                ic[0][0] - Mass 1 initial x position
                ic[0][1] - Mass 1 initial y position
                ic[0][2] - Mass 1 initial z position
                ic[1][0] - Mass 2 initial x position
                ic[1][1] - Mass 2 initial y position
                ic[1][2] - Mass 2 initial z position
                ic[2][0] - Mass 1 initial velocity in x
                ic[2][1] - Mass 1 initial velocity in y
                ic[2][2] - Mass 1 initial velocity in z
                ic[3][0] - Mass 2 initial velocity in x
                ic[3][1] - Mass 2 initial velocity in y
                ic[3][2] - Mass 2 initial velocity in z
            t0 - Initial time in seconds of model
            tn - Final time in seconds of model
            i, j, k - Data types that are to be plotted for each axis
                i - X axis
                j - Y axis
                k - Z axis
                    0 - X value
                    1 - Y value
                    2 - Z value
                    3 - Time
            mass1Name - Name of mass 1
            mass2Name - Name of mass 2
        Algorithm:
            * Call the RK4 two body solver
            
        Output:
            This function does not return a value
    """
    def Plot(self, plotType, masses, ic, t0, tn, i, j, k, mass1Name, mass2Name):
        # Call solver
        mass1Pos, mass2Pos, mass1Vel, mass2Vel, timeVals = RK4TwoBody(TwoCoupledBodiesModel, masses, ic, t0, tn)
        # 2D Axis pos
        def Axis2DPos(self, mass1Pos, mass2Pos, timeVals, i, j):
            # Max pos
            maxDistX, maxDistY, maxDistZ, maxTime = MaxVals(mass1Pos, mass2Pos, timeVals)
            # Direction place holder
            iDirection = ''
            jDirection = ''
            if (i == 0):
                iDirection = "$x$"
                self.axes.set_xlim(-maxDistX, maxDistX)
            elif (i == 1):
                iDirection = "$y$"
                self.axes.set_xlim(-maxDistY, maxDistY)
            elif (i == 2):
                iDirection = "$z$"
                self.axes.set_xlim(-maxDistZ, maxDistZ)
            elif (i == 3):
                iDirection = "Time"
                self.axes.set_xlim(0, maxTime)
            if (j == 0):
                jDirection = "$x$"
                self.axes.set_ylim(-maxDistX, maxDistX)
            elif (j == 1):
                jDirection = "$y$"
                self.axes.set_ylim(-maxDistY, maxDistY)
            elif (j == 2):
                jDirection = "$z$"
                self.axes.set_ylim(-maxDistZ, maxDistZ)
            elif (j == 3):
                jDirection = "Time"
                self.axes.set_ylim(0, maxTime)
            # Mass values
            mass1Vals = [mass1Pos[0], mass1Pos[1], mass1Pos[2], timeVals]
            mass2Vals = [mass2Pos[0], mass2Pos[1], mass2Pos[2], timeVals]
            return iDirection, jDirection, mass1Vals, mass2Vals
        # 3D Axis pos
        def Axis3DPos(self, mass1Pos, mass2Pos, timeVals, i, j, k):
            # Max pos
            maxDistX, maxDistY, maxDistZ, maxTime = MaxVals(mass1Pos, mass2Pos, timeVals)
            # Direction place holder
            iDirection = ''
            jDirection = ''
            kDirection = ''
            if (i == 0):
                iDirection = "$x$"
                self.axes.set_xlim(-maxDistX, maxDistX)
            elif (i == 1):
                iDirection = "$y$"
                self.axes.set_xlim(-maxDistY, maxDistY)
            elif (i == 2):
                iDirection = "$z$"
                self.axes.set_xlim(-maxDistZ, maxDistZ)
            elif (i == 3):
                iDirection = "Time"
                self.axes.set_xlim(0, maxTime)
            if (j == 0):
                jDirection = "$x$"
                self.axes.set_ylim(-maxDistX, maxDistX)
            elif (j == 1):
                jDirection = "$y$"
                self.axes.set_ylim(-maxDistY, maxDistY)
            elif (j == 2):
                jDirection = "$z$"
                self.axes.set_ylim(-maxDistZ, maxDistZ)
            elif (j == 3):
                jDirection = "Time"
                self.axes.set_ylim(0, maxTime)
            if (k == 0):
                kDirection = "$x$"
                self.axes.set_zlim(-maxDistX, maxDistX)
            elif (k == 1):
                kDirection = "$y$"
                self.axes.set_zlim(-maxDistY, maxDistY)
            elif (k == 2):
                kDirection = "$z$"
                self.axes.set_zlim(-maxDistZ, maxDistZ)
            elif (k == 3):
                kDirection = "Time"
                self.axes.set_zlim(0, maxTime)
            # Mass values
            mass1Vals = [mass1Pos[0], mass1Pos[1], mass1Pos[2], timeVals]
            mass2Vals = [mass1Pos[0], mass2Pos[1], mass2Pos[2], timeVals]
            return iDirection, jDirection, kDirection, mass1Vals, mass2Vals
        # 2D Axis vel
        def Axis2DVel(self, mass1Vel, mass2Vel, timeVals, i, j):
            # Max vel 
            maxVelX, maxVelY, maxVelZ, maxTime = MaxVals(mass1Vel, mass2Vel, timeVals)
            # Direction place holder
            iDirection = ''
            jDirection = ''
            if (i == 0):
                iDirection = "$v_{x}$"
                self.axes.set_xlim(-maxVelX, maxVelX)
            elif (i == 1):
                iDirection = "$v_{y}$"
                self.axes.set_xlim(-maxVelY, maxVelY)
            elif (i == 2):
                iDirection = "$v_{z}$"
                self.axes.set_xlim(-maxVelZ, maxVelZ)
            elif (i == 3):
                iDirection = "Time"
                self.axes.set_xlim(0, maxTime)
            if (j == 0):
                jDirection = "$v_{x}$"
                self.axes.set_ylim(-maxVelX, maxVelX)
            elif (j == 1):
                jDirection = "$v_{y}$"
                self.axes.set_ylim(-maxVelY, maxVelY)
            elif (j == 2):
                jDirection = "$v_{z}$"
                self.axes.set_ylim(-maxVelZ, maxVelZ)
            elif (j == 3):
                jDirection = "Time"
                self.axes.set_ylim(0, maxTime)
            # Mass values
            mass1Vals = [mass1Vel[0], mass1Vel[1], mass1Vel[2], timeVals]
            mass2Vals = [mass2Vel[0], mass2Vel[1], mass2Vel[2], timeVals]
            return iDirection, jDirection, mass1Vals, mass2Vals
        # Max value
        def MaxVals(param1, param2, param3):
            maxParamX = max(max([val[0] for val in param1]), max([val[0] for val in param2])) * 1.1
            maxParamY = max(max([val[1] for val in param1]), max([val[1] for val in param2])) * 1.1
            maxParamZ = max(max([val[2] for val in param1]), max([val[2] for val in param2])) * 1.1
            max3 = max(param3)
            return maxParamX, maxParamY, maxParamZ, max3
        # Figure notes
        def Notes(self, masses, ic, mass1Name, mass2Name):
            self.figure.subplots_adjust(bottom=0.30)
            mass1Mass = f"{mass1Name}: {masses[0]:.2e} $(Kg)$ "
            mass1InitXPos, mass1InitYPos, mass1InitZPos = f"$x_{0}$ = {ic[0][0]:.2e} $(m)$, ", f"$y_{0}$ = {ic[0][1]:.2e} $(m)$, ", f"$z_{0}$ = {ic[0][2]:.2e} $(m)$, "
            mass1InitXVel, mass1InitYVel, mass1InitZVel = f"$v_{{x_{0}}}$ = {ic[2][0]:.2e} $(m/s)$, ", f"$v_{{y_{0}}}$ = {ic[2][1]:.2e} $(m/s)$, ", f"$v_{{z_{0}}}$ = {ic[2][2]:.2e} $(m/s)$"
            mass1Notes = mass1Mass + mass1InitXPos + mass1InitXVel + mass1InitYPos + mass1InitYVel + mass1InitZPos + mass1InitZVel
            mass2Mass = f"{mass2Name}: {masses[1]:.2e} $(Kg)$ "
            mass2InitXPos, mass2InitYPos, mass2InitZPos = f"$x_{0}$ = {ic[1][0]:.2e} $(m)$, ", f"$y_{0}$ = {ic[1][1]:.2e} $(m)$, ", f"$z_{0}$ = {ic[1][2]:.2e} $(m)$, "
            mass2InitXVel, mass2InitYVel, mass2InitZVel = f"$v_{{x_{0}}}$ = {ic[3][0]:.2e} $(m/s)$, ", f"$v_{{y_{0}}}$ = {ic[3][1]:.2e} $(m/s)$, ", f"$v_{{z_{0}}}$ = {ic[3][2]:.2e} $(m/s)$"
            mass2Notes = mass2Mass + mass2InitXPos + mass2InitXVel + mass2InitYPos + mass2InitYVel + mass2InitZPos + mass2InitZVel
            timeSpanNotes = f"Time Span: {round(float(tn / (365.25 * DS)), 2)} Earth Years"
            self.figure.text(0.1, 0.05, mass1Notes + "\n" + mass2Notes + "\n" + timeSpanNotes, ha='left', va='bottom', fontsize=TWODNOTES)
        # 2D Position labels
        def Pos2DLabels(self, axisParam, i, j, q):
            plotType = ""
            if (q == 0):
                plotType = "Plot"
            else:
                plotType = "Animation"
            self.axes.set_title(f"2D Position {plotType} Of Two Coupled Bodies: {axisParam[1]} vs. {axisParam[0]}", fontsize = TWODPLOTTITLE)
            if (i == 3):
                self.axes.set_xlabel(f"{axisParam[0]} In Seconds", fontsize = TWODPLOTABELS)
            else:
                self.axes.set_xlabel(f"{axisParam[0]} Position In $(m)$", fontsize = TWODPLOTABELS)
            if (j == 3):
                self.axes.set_ylabel(f"{axisParam[1]} In Seconds", fontsize = TWODPLOTABELS)
            else:
                self.axes.set_ylabel(f"{axisParam[1]} Position In $(m)$", fontsize = TWODPLOTABELS)
            self.axes.legend()
        # 3D Position labels
        def Pos3DLabels(self, axisParam, i, j, k, q):
            plotType = ""
            if (q == 0):
                plotType = "Plot"
            else:
                plotType = "Animation"
            self.axes.set_tile(f"3D Position {plotType} Of Two Coupled Bodies: {axisParam[2]} vs. {axisParam[1]} vs. {axisParam[0]}", fontsize = THREEDPLOTTILE)
            if (i == 3):
                self.axes.set_xlabel(f"{axisParam[0]} In Seconds", fontsize = THREEDPLOTLABELS)
            else:
                self.axes.set_xlabel(f"{axisParam[0]} Position In $(m)$", fontsize = THREEDPLOTLABELS)
            if (j == 3):
                self.axes.set_ylabel(f"{axisParam[1]} In Seconds", fontsize = THREEDPLOTLABELS)
            else:
                self.axes.set_ylabel(f"{axisParam[1]} Position In $(m)$", fontsize = THREEDPLOTLABELS)
            self.axes.legend()
            if (k == 3):
                self.axes.set_zlabel(f"{axisParam[2]} In Seconds", fontsize = THREEDPLOTLABELS)
            else:
                self.axes.set_zlabel(f"{axisParam[2]} Position In $(m)$", fontsize = THREEDPLOTLABELS)
        # 2D Velocity labels
        def Vel2DLabels(self, axisParam, i, j, q):
            plotType = ""
            if (q == 0):
                plotType = "Plot"
            else:
                plotType = "Animation"
            self.axes.set_title(f"2D Velocity {plotType} Of Two Coupled Bodies: {axisParam[1]} vs. {axisParam[0]}", fontsize = TWODPLOTTITLE)
            if (i == 3):
                self.axes.set_xlabel(f"{axisParam[0]} In Seconds", fontsize = TWODPLOTABELS)
            else:
                self.axes.set_xlabel(f"{axisParam[0]} Velocity In $(m/s)$", fontsize = TWODPLOTABELS)
            if (j == 3):
                self.axes.set_ylabel(f"{axisParam[1]} In Seconds", fontsize = TWODPLOTABELS)
            else:
                self.axes.set_ylabel(f"{axisParam[1]} Velocity In $(m/s)$", fontsize = TWODPLOTABELS)
            self.axes.legend()
        # Swap masses if applicable
        m1 = masses[0]
        m1Name = mass1Name
        m1Pos = mass1Pos
        m1Vel = mass1Vel
        m2 = masses[1]
        m2Name = mass2Name
        m2Pos = mass2Pos
        m2Vel = mass2Vel
        icCopy = ic
        if (m2 > m1):
            masses[0] = m2
            mass1Pos = m2Pos
            mass1Vel = m2Vel
            mass1Name = m2Name
            masses[1] = m1
            mass2Pos = m1Pos
            mass2Vel = m1Vel
            mass2Name = m1Name
            ic = [icCopy[1],icCopy[0],icCopy[3],icCopy[2]]
        # 2D Position plot
        if (plotType == 0):
            # Clear axes
            self.axes.clear()
            # Max pos function
            axisPos = Axis2DPos(self, mass1Pos, mass2Pos, timeVals, i, j)
            # Plot
            self.axes.plot(axisPos[2][i], axisPos[2][j], 'o', color = "green", markersize = 2, label = mass1Name)
            self.axes.plot(axisPos[3][i], axisPos[3][j], 'o', color = "blue", markersize = 1, label = mass2Name)
            # Title and labels
            Pos2DLabels(self, axisPos, i, j, 0)
            # Notes
            Notes(self, masses, ic, mass1Name, mass2Name)
            # Draw plot on canvas
            self.draw()
        # 2D Position animation
        elif (plotType == 1):
            # Clear axes
            self.axes.clear()
            # Max pos function
            axisPos = Axis2DPos(self, mass1Pos, mass2Pos, timeVals, i, j)
            # Animation parameters
            mass1, = self.axes.plot([], [], 'o', color = 'green', markersize = 2, label = mass1Name)
            mass2, = self.axes.plot([], [], 'o', color = 'blue', markersize = 1, label = mass2Name)
            mass1Trail, = self.axes.plot([], [], '-', color = 'green', linewidth = 1, alpha = 0.5)
            mass2Trail, = self.axes.plot([], [], '-', color = 'blue', linewidth = 1, alpha = 0.5)
            # Init function
            def init():
                mass1.set_data([], [])
                mass2.set_data([], [])
                mass1Trail.set_data([], [])
                mass2Trail.set_data([], [])
                return mass1, mass2, mass1Trail, mass2Trail
            # Animate function
            def animate(q):
                mass1.set_data([axisPos[2][i][q]], [axisPos[2][j][q]])
                mass2.set_data([axisPos[3][i][q]], [axisPos[3][j][q]])
                mass1Trail.set_data(axisPos[2][i][:q+1], axisPos[2][j][:q+1])
                mass2Trail.set_data(axisPos[3][i][:q+1], axisPos[3][j][:q+1])
                return mass1, mass2, mass1Trail, mass2Trail
            # Animation
            self.ani = FuncAnimation(self.figure, animate, init_func = init, frames = len(axisPos[2][3]), interval = 1e-5, blit = True, repeat = True)
            # Title and labels
            Pos2DLabels(self, axisPos, i, j, 1)
            # Notes
            Notes(self, masses, ic, mass1Name, mass2Name)
            # Draw
            self.draw()
        # 2D Velocity plot
        elif (plotType == 2):
            # Clear axes
            self.axes.clear()
            # Max vel function
            axisVel = Axis2DVel(self, mass1Vel, mass2Vel, timeVals, i, j)
            # Plot
            self.axes.plot(axisVel[2][i], axisVel[2][j], 'o', color = "green", markersize = 2, label = mass1Name)
            self.axes.plot(axisVel[3][i], axisVel[3][j], 'o', color = "blue", markersize = 1, label = mass2Name)
            # Title and labels
            Vel2DLabels(self, axisVel, i, j, 0)
            # Notes
            Notes(self, masses, ic, mass1Name, mass2Name)
            # Draw
            self.draw()
        # 2D Velocity animation
        elif (plotType == 3):
            # Clear axes
            self.axes.clear()
            # Max vel function
            axisVel = Axis2DVel(self, mass1Vel, mass2Vel, timeVals, i, j)
            # Animation parameters
            mass1, = self.axes.plot([], [], 'o', color = 'green', markersize = 2, label = mass1Name)
            mass2, = self.axes.plot([], [], 'o', color = 'blue', markersize = 1, label = mass2Name)
            mass1Trail, = self.axes.plot([], [], '-', color = 'green', linewidth = 1, alpha = 0.5)
            mass2Trail, = self.axes.plot([], [], '-', color = 'blue', linewidth = 1, alpha = 0.5)
            # Init function
            def init():
                mass1.set_data([], [])
                mass2.set_data([], [])
                mass1Trail.set_data([], [])
                mass2Trail.set_data([], [])
                return mass1, mass2, mass1Trail, mass2Trail
            # Animate function
            def animate(q):
                mass1.set_data([axisVel[2][i][q]], [axisVel[2][j][q]])
                mass2.set_data([axisVel[3][i][q]], [axisVel[3][j][q]])
                mass1Trail.set_data(axisVel[2][i][:q+1], axisVel[2][j][:q+1])
                mass2Trail.set_data(axisVel[3][i][:q+1], axisVel[3][j][:q+1])
                return mass1, mass2, mass1Trail, mass2Trail
            # Animation
            self.ani = FuncAnimation(self.figure, animate, init_func = init, frames = len(axisVel[2][3]), interval = 1e-5, blit = True, repeat = True)
            # Title and labels
            Vel2DLabels(self, axisVel, i, j, 1)
            # Notes
            Notes(self, masses, ic, mass1Name, mass2Name)
            # Draw
            self.draw()
        # 3D position plot
        elif (plotType == 4):
            # Clear axes
            self.axes.clear()
            # Max pos function
            axisPos = Axis3DPos(self, mass1Pos, mass2Pos, timeVals, i, j, k)
            # Plot
            self.axes.plot(axisPos[3][i], axisPos[3][j], axisPos[3][k], 'o', color = "green", markersize = 2, label = mass1Name)
            self.axes.plot(axisPos[4][i], axisPos[4][j], axisPos[4][k], 'o', color = "blue", markersize = 1, label = mass2Name)
            # Title and labels
            Pos3DLabels(self, axisPos, i, j, k, 0)
            # Draw
            self.draw()

""" TwoBodyPlotWindow - Class for two body motion plot windows
    Member Functions:
        Constructor - Creates windows with specific input parameters
        closeEvent - Deletes plot canvas when window is closed
"""
class TwoBodyPlotWindow(QWidget):
    """ Constructor - Creates windows with specific input parameters
        Input:
            
        Algorithm:
            * Set the window title
            * Set the size of the window
            * Create the layout
            * Create the canvas for the plot
            * Create the tool bar for the canvas
            * Add the widgets to the layouts
            * Set the layout
        Output:
            This function does not return any values
    """
    def __init__(self, plotType, masses, ic, t0, tn, i, j, k, mass1Name, mass2Name, windowTitle):
        super().__init__()
        # Window title
        self.setWindowTitle(windowTitle)
        # Window sizes
        self.resize(800,500)
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        # Layout
        self.layout = QVBoxLayout()
        # Canvas for plot
        self.plotCanvas = TwoBodyCanvas(self, width=3, height=2, dpi=100)
        self.plotCanvas.Plot(plotType, masses, ic, t0, tn, i, j, k, mass1Name, mass2Name)
        # Tool bar
        self.toolBar = NavigationToolbar(self.plotCanvas, self)
        # Widget layout addition
        self.layout.addWidget(self.plotCanvas)
        self.layout.addWidget(self.toolBar)
        # Set layout
        self.setLayout(self.layout)

    """ closeEvent - Deletes plot canvas when window is closed
        Input:
            event - Object for the close event
        Algorithm:
            * Check if the window has the attributes "plotCanvas" and "ani"
            * Stop the animation if the window has an animation in it
            * Call the close event method
        Output:
            This function does not return a value
    """
    def closeEvent(self, event):
        if hasattr(self, 'plotCanvas') and hasattr(self.plotCanvas, 'ani'):
            self.plotCanvas.ani.event_source.stop()
        super().closeEvent(event)

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

    """ Calculate - Generates the plot(s) for specific conditions
    
    """
    def Calculate(self):
        # Grab children
        children = self.GrabChildren()
        # Values from fields
        masses = []
        ic = []
        # Axis indices
        def AxisIndices(children):
            xAxisIndex = None
            yAxisIndex = None
            zAxisIndex = None
            for index, widget in enumerate(children[4][0:4]):
                if (widget.isChecked() == True):
                    xAxisIndex = index
                    break
            for index, widget in enumerate(children[4][4:8]):
                if (widget.isChecked() == True):
                    yAxisIndex = index
                    break
            for index, widget in enumerate(children[4][8:12]):
                if (widget.isChecked() == True):
                    zAxisIndex = index
                    break
            return xAxisIndex, yAxisIndex, zAxisIndex
        # Dialog box
        def Dialog(self, message):
            dialogBox = QDialog(self)
            dialogBox.setWindowTitle("Invalid Input")
            dialogBox.setFixedSize(400, 75)
            warningLabel = QLabel(message, dialogBox)
            warningFont = warningLabel.font()
            warningFont.setPointSize(13)
            warningLabel.setFont(warningFont)
            warningLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            layout = QVBoxLayout()
            layout.addWidget(warningLabel)
            dialogBox.setLayout(layout)
            dialogBox.exec()
        # Grab values
        def GrabValues(children):
            mass1 = float(children[0][2].text())
            mass1Name = str(children[0][1].text())
            mass1InitPos = [float(str(children[0][3].text())), float(str(children[0][4].text())), float(str(children[0][5].text()))]
            mass1InitVel = [float(str(children[0][6].text())), float(str(children[0][7].text())), float(str(children[0][8].text()))]
            mass2 = float(children[1][2].text())
            mass2Name = str(children[1][1].text())
            mass2InitPos = [float(str(children[1][3].text())), float(str(children[1][4].text())), float(str(children[1][5].text()))]
            mass2InitVel = [float(str(children[1][6].text())), float(str(children[1][7].text())), float(str(children[1][8].text()))]
            timeSpan = float(float(children[2][0].text()) * 365.25 * DS)
            masses = [mass1, mass2]
            ic = [mass1InitPos, mass2InitPos, mass1InitVel, mass2InitVel]
            return masses, ic, timeSpan, mass1Name, mass2Name
        # Input fields entered check
        mass1IsNum = all(isinstance(widget, QLineEdit) and self.IsNum(str(widget.text())) == True for widget in children[0][2:9])
        mass1IsPos = self.IsPositive(float(str(children[0][2].text()))) == True
        mass2IsNum = all(isinstance(widget, QLineEdit) and self.IsNum(str(widget.text())) == True for widget in children[1][2:9])
        mass2IsPos = self.IsPositive(float(str(children[1][2].text()))) == True
        timeIsNum = self.IsNum(str(children[2][0].text())) == True
        timeIsPos = self.IsPositive(float(str(children[2][0].text()))) == True
        if (mass1IsNum == True and mass2IsNum == True and timeIsNum):
            if (mass1IsPos == True and mass2IsPos == True and timeIsPos == True):
                values = GrabValues(children)
                axis = AxisIndices(children)
                # 2D Position Plot
                if (children[3][0].isChecked() == True):
                    self.TwoDPosPlot = TwoBodyPlotWindow(0, values[0], values[1], 0, values[2], axis[0], axis[1], axis[2], values[3], values[4], "2D Two Body Position Plot")
                    self.TwoDPosPlot.show()
                # 2D Position Animation
                if (children[3][1].isChecked() == True):
                    self.TwoDPosAni = TwoBodyPlotWindow(1, values[0], values[1], 0, values[2], axis[0], axis[1], axis[2], values[3], values[4], "2D Two Body Position Animation")
                    self.TwoDPosAni.show()
                # 2D Velocity Plot
                if (children[3][2].isChecked() == True):
                    self.TwoDVelPlot = TwoBodyPlotWindow(2, values[0], values[1], 0, values[2], axis[0], axis[1], axis[2], values[3], values[4], "2D Two Body Velocity Plot")
                    self.TwoDVelPlot.show()
                # 2D Velocity Animation
                if (children[3][3].isChecked() == True):
                    self.TwoDVelAni = TwoBodyPlotWindow(3, values[0], values[1], 0, values[2], axis[0], axis[1], axis[2], values[3], values[4], "2D Two Body Velocity Animation")
                    self.TwoDVelAni.show()
                # 3D Position Plot
                if (children[3][4].isChecked() == True):
                    self.ThreeDPosPlot = TwoBodyPlotWindow(4, values[0], values[1], 0, values[2], axis[0], axis[1], axis[2], values[3], values[4], "3D Two Body Position Plot")
                    self.ThreeDPosPlot.show()
            else:
                if (mass1IsPos != True):
                    Dialog(self, "Please enter a positive value for Mass 1.")
                if (timeIsPos != True):
                    Dialog(self, "Please enter a positive value for the time span.")
                if (mass2IsPos != True):
                    Dialog(self, "Please enter a positive value for Mass 2.")
        else:
            if (mass1IsNum != True):
                Dialog(self, "Please enter numerical values for the parameters of Mass 1.")
            if (timeIsNum != True):
                Dialog(self, "Please enter numerical values for the time span.")
            if (mass2IsNum != True):
                Dialog(self, "Please enter numerical values for the parameters of Mass 2.")

    """ ClearAll - Clears all input fields
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab children
            * Call member functions
            * Set checkboxes to default value
        Output:
            This function does not return a value
    """
    def ClearAll(self):
        # Grab children
        children = self.GrabChildren()
        # Member functions
        self.UnselectAllPlots()
        self.ClearTime()
        self.ClearMass2Params()
        self.ClearMass1Params()
        # Reset checkboxes
        children[0][0].setCurrentIndex(0)
        children[1][0].setCurrentIndex(0)

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
        children[2][0].setText("")

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
                1 - Default time values
                2 - Default mass 2 parameters
                3 - Default plot selection checkbox parameters
                4 - Default x axis selection checkbox parameters
                5 - Default y axis selection checkbox parameters
                6 - Default z axis selection checkbox parameters
                7 - Default main buttons
                8 - Default 0-7
        Algorithm:
            * Grab children from window
            * Define disable mass 1 function
            * Define disable time function
            * Define disable mass 2 function
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
        # Default time values children function
        def DefaultTime():
            for widget in children[2]:
                widget.setDisabled(True)
        # Default mass 2 parameters children function
        def DefaultMass2():
            for widget in children[1][2:10]:
                widget.setDisabled(True)
        # Default plot selection checkboxes children function
        def DefaultPlotSelCB():
            for widget in children[3]:
                widget.setDisabled(True)
        # Default x axis selection checkboxes children function
        def DefaultXAxisCB():
            for widget in children[4][0:4]:
                widget.setChecked(False)
                widget.setDisabled(True)
        # Default y axis selection checkboxes children function
        def DefaultYAxisCB():
            for widget in children[4][4:8]:
                widget.setChecked(False)
                widget.setDisabled(True)
        # Default z axis selection checkboxes children function
        def DefaultZAxisCB():
            for widget in children[4][8:12]:
                widget.setChecked(False)
                widget.setDisabled(True)
        # Default calculate button function
        def DefaultCalcBtn():
            children[5][0].setDisabled(True)
        # Default all function
        def DefaultAll():
            DefaultMass1()
            DefaultTime()
            DefaultMass2()
            DefaultPlotSelCB()
            DefaultXAxisCB()
            DefaultYAxisCB()
            DefaultZAxisCB()
            DefaultCalcBtn()
        # Set fields to default state
        if (field == 0):
            DefaultMass1()
        elif (field == 1):
            DefaultTime()
        elif (field == 2):
            DefaultMass2()
        elif (field == 3):
            DefaultPlotSelCB()
        elif (field == 4):
            DefaultXAxisCB()
        elif (field == 5):
            DefaultYAxisCB()
        elif (field == 6):
            DefaultZAxisCB()
        elif (field == 7):
            DefaultCalcBtn()
        elif (field == 8):
            DefaultAll()

    """ DisableFields - Disables fields based upon input parameter
        Input:
            Field - Integer value that determines what field is to be disabled
                0 - Disable mass 1 parameters
                1 - Disable time values
                2 - Disable mass 2 parameters
                3 - Disable plot selection checkbox parameters
                4 - Disable x axis selection checkbox parameters
                5 - Disable y axis selection checkbox parameters
                6 - Disable z axis selection checkbox parameters
                7 - Disable main buttons
                8 - Disable 0-7
        Algorithm:
            * Grab the children from the window
            * Define mass 1 parameters function
            * Define time values function
            * Define mass 2 parameters function
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
        # Disable time values children function
        def DisableTime():
            for widget in children[2]:
                widget.setDisabled(True)
        # Disable mass 2 parameters children function
        def DisableMass2():
            for widget in children[1][2:10]:
                widget.setDisabled(True)
        # Disable plot selection checkboxes children function
        def DisablePlotSelCB():
            for widget in children[3]:
                widget.setDisabled(True)
        # Disable x axis selection checkboxes children function
        def DisableXAxisCB():
            for widget in children[4][0:4]:
                widget.setDisabled(True)
        # Disable y axis selection checkboxes children function
        def DisableYAxisCB():
            for widget in children[4][4:8]:
                widget.setDisabled(True)
        # Disable z axis selection checkboxes children function
        def DisableZAxisCB():
            for widget in children[4][8:12]:
                widget.setDisabled(True)
        # Disable calculate button function
        def DisableCalcBtn():
            children[5][0].setDisabled(True)
        # Disable all function
        def DisableAll():
            DisableMass1()
            DisableTime()
            DisableMass2()
            DisablePlotSelCB()
            DisableXAxisCB()
            DisableYAxisCB()
            DisableZAxisCB()
            DisableCalcBtn()
        # Set fields to default state
        if (field == 0):
            DisableMass1()
        elif (field == 1):
            DisableTime()
        elif (field == 2):
            DisableMass2()
        elif (field == 3):
            DisablePlotSelCB()
        elif (field == 4):
            DisableXAxisCB()
        elif (field == 5):
            DisableYAxisCB()
        elif (field == 6):
            DisableZAxisCB()
        elif (field == 7):
            DisableCalcBtn()
        elif (field == 8):
            DisableAll()

    """ EnableFields - Enables fields based upon input parameter
        Input:
            Field - Integer value that determines what field is to be enabled
                0 - Enable mass 1 parameters
                1 - Enable time values
                2 - Enable mass 2 parameters
                3 - Enable plot selection checkbox parameters
                4 - Enable x axis selection checkbox parameters
                5 - Enable y axis selection checkbox parameters
                6 - Enable z axis selection checkbox parameters
                7 - Enable main buttons
                8 - Enable 0-7
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
        # Enable mass 1 parameters children function
        def EnableMass1():
            for widget in children[0][2:10]:
                widget.setEnabled(True)
        # Enable time values children function
        def EnableTime():
            for widget in children[2]:
                widget.setEnabled(True)
        # Enable mass 2 parameters children function
        def EnableMass2():
            for widget in children[1][2:10]:
                widget.setEnabled(True)
        # Enable plot selection checkboxes children function
        def EnablePlotSelCB():
            for widget in children[3]:
                widget.setEnabled(True)
        # Enable x axis selection checkboxes children function
        def EnableXAxisCB():
            for widget in children[4][0:4]:
                widget.setEnabled(True)
        # Enable y axis selection checkboxes children function
        def EnableYAxisCB():
            for widget in children[4][4:8]:
                widget.setEnabled(True)
        # Enable z axis selection checkboxes children function
        def EnableZAxisCB():
            for widget in children[4][8:12]:
                widget.setEnabled(True)
        # Enable calculate button function
        def EnableCalcBtn():
            children[5][0].setEnabled(True)
        # Enable all function
        def EnableAll():
            EnableMass1()
            EnableTime()
            EnableMass2()
            EnablePlotSelCB()
            EnableXAxisCB()
            EnableYAxisCB()
            EnableZAxisCB()
            EnableCalcBtn()
        # Set fields to default state
        if (field == 0):
            EnableMass1()
        elif (field == 1):
            EnableTime()
        elif (field == 2):
            EnableMass2()
        elif (field == 3):
            EnablePlotSelCB()
        elif (field == 4):
            EnableXAxisCB()
        elif (field == 5):
            EnableYAxisCB()
        elif (field == 6):
            EnableZAxisCB()
        elif (field == 7):
            EnableCalcBtn()
        elif (field == 8):
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
        return mass1Arr, mass2Arr, timeValArr, plotSelArr, axisSelArr, mainBtnsArr

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
        plotSelAllBtn.clicked.connect(self.SelectAllPlots)
        plotSelBtnLayout.addWidget(plotSelAllBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Random all checkboxes button
        plotSelRandBtn = QPushButton("Random Plots")
        plotSelRandBtn.setObjectName(plotSelRandBtnName)
        plotSelRandBtn.setMinimumWidth(buttonMinWidth)
        plotSelRandBtn.setMinimumHeight(buttonMinHeight)
        plotSelRandBtn.clicked.connect(self.RandomPlots)
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
        calcBtn.clicked.connect(self.Calculate)
        mainBtnLayout.addWidget(calcBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Clear button
        clearBtn = QPushButton("Clear All")
        clearBtn.setObjectName(clearBtnName)
        clearBtn.setMinimumWidth(buttonMinWidth - 50)
        clearBtn.setMinimumHeight(buttonMinHeight)
        clearBtn.clicked.connect(self.ClearAll)
        mainBtnLayout.addWidget(clearBtn, alignment = Qt.AlignmentFlag.AlignHCenter)
        ## Random button
        randomBtn = QPushButton("Random All")
        randomBtn.setObjectName(randomBtnName)
        randomBtn.setMinimumWidth(buttonMinWidth - 50)
        randomBtn.setMinimumHeight(buttonMinHeight)
        randomBtn.clicked.connect(self.RandomAll)
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
        self.DefaultState(8)
        # Connect signals function
        self.ConnectSignals()

    """ IsNum - Checks to see if an input is able to be converted to a number
        Input:
            string - String value that is trying to be converted to a float
        Algorithm:
            * Try the conversion, if it succeeds, return true
            * Otherwise, return false
        Output:
            This function returns a boolean value for if a value has been successfully converted
    """
    def IsNum(self, string):
        # Attempt conversion
        try:
            float(string)
            return True
        except ValueError:
            return False

    """ IsPositive - Checks if a number is positive
        Input:
            value - Value that is being checked
        Algorithm:
            * If the value is non zero and positive, return True
            * Otherwise, return False
        Output:
            This function returns a boolean value for if a number is positive
    """
    def IsPositive(self, value):
        # Greater than zero
        if (value > 0):
            return True
        # Less than or equal to zero
        else:
            return False

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
            self.DefaultState(2)
        # Otherwise 
        else:
            self.EnableFields(2)
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

    """ RandomAll - Randomizes all input fields
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Call member functions
        Output:
            This function does not return a value
    """
    def RandomAll(self):
        # Member functions
        self.RandomMass1()
        self.RandomMass2()
        self.RandomTime()
        self.RandomPlots()

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

    """ RandomPlots - Randomizes the checkboxes that get selected
        Input:
            This function does not have any unique input parameters
        Algorithm:
            * Grab children from window
            * Generate random integers and append them to an array
            * Check boxes based upon the modulo of a given random integer being zero
            * Check if no boxes where checked
                * If no boxes were checked, set a random checkbox to be checked
        Output:
            This function does not return a value
    """
    def RandomPlots(self):
        # Grab children
        children = self.GrabChildren()
        # Random integers
        randInts = []
        for i in range(2,10):
            randInts.append(random.randint(1,1000))
        # Check boxes
        self.UnselectAllPlots()
        index = 0
        boolArr = []
        for widget in children[3][0:8]:
            if (randInts[index] % (index + 2) == 0):
                widget.setChecked(True)
                boolArr.append(True)
            else:
                boolArr.append(False)
            index += 1
        # Check if all are false
        allFalse = all(vals == False for vals in boolArr)
        if (allFalse == True):
            randIndex = random.randint(0,8)
            children[3][randIndex].setChecked(True)
        # Axis selection
        no3DCB = all(isinstance(widget, QCheckBox) and widget.isChecked() == False for widget in children[3][4:8])
        possibleIndices = [0,1,2,3]
        randXIndex = random.choice(possibleIndices)
        children[4][0 + randXIndex].setChecked(True)
        possibleIndices.remove(randXIndex)
        randYIndex = random.choice(possibleIndices)
        possibleIndices.remove(randYIndex)
        children[4][4 + randYIndex].setChecked(True)
        if (no3DCB == False):
            randZIndex = random.choice(possibleIndices)
            possibleIndices.remove(randZIndex)
            children[4][8 + randZIndex].setChecked(True)

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
        children[2][0].setText(str(randTime))

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
        mass1Params = all(isinstance(widget, QLineEdit) and widget.text() != "" for widget in children[0][1:9])
        mass2Params = all(isinstance(widget, QLineEdit) and widget.text() != "" for widget in children[1][1:9])
        timeVals = children[2][0].text() != ""
        plotSelectionCB = any(isinstance(widget, QCheckBox) and widget.isChecked() == True for widget in children[3][0:8])
        no3DCB = all(isinstance(widget, QCheckBox) and widget.isChecked() == False for widget in children[3][4:8])
        xAxisCB = any(isinstance(widget, QCheckBox) and widget.isChecked() == True for widget in children[4][0:4])
        yAxisCB = any(isinstance(widget, QCheckBox) and widget.isChecked() == True for widget in children[4][4:8])
        zAxisCB = any(isinstance(widget, QCheckBox) and widget.isChecked() == True for widget in children[4][8:12])
        # Enable time values
        if (mass1ComboBox == True or mass2ComboBox == True):
            self.EnableFields(1)
        else:
            self.ClearTime()
            self.DefaultState(1)
        # Enable plot selection checkboxes
        if (mass1Params == True and mass2Params == True and timeVals == True):
            self.EnableFields(3)
        else:
            self.UnselectAllPlots()
            self.DefaultState(3)
            self.DefaultState(4)
            self.DefaultState(5)
            self.DefaultState(6)
        # Enable axis selection
        if (plotSelectionCB == True):
            self.EnableFields(4)
            if (xAxisCB == True):
                self.EnableFields(5)
                xAxisIndex = None
                for index, widget in enumerate(children[4][0:4]):
                    if (widget.isChecked() == True):
                        xAxisIndex = index
                        break
                for index, widget in enumerate(children[4][0:4]):
                    widget.setEnabled(index == xAxisIndex)
                    widget.setDisabled(index != xAxisIndex)
                for index, widget in enumerate(children[4][4:8]):
                    widget.setDisabled(index == xAxisIndex)
                if (yAxisCB == True):
                    yAxisIndex = None
                    for index, widget in enumerate(children[4][4:8]):
                        if (widget.isChecked() == True):
                            yAxisIndex = index
                            break
                    for index, widget in enumerate(children[4][4:8]):
                        widget.setEnabled(index == yAxisIndex)
                        widget.setDisabled(index != yAxisIndex)
                    if (no3DCB == False):
                        for index, widget in enumerate(children[4][8:12]):
                            widget.setEnabled(index != xAxisIndex or index != yAxisIndex)
                            widget.setDisabled(index == xAxisIndex or index == yAxisIndex)
                        if (zAxisCB == True):
                            zAxisIndex = None
                            for index, widget in enumerate(children[4][8:12]):
                                if (widget.isChecked() == True):
                                    zAxisIndex = index
                                    break
                            for index, widget in enumerate(children[4][8:12]):
                                widget.setEnabled(index == zAxisIndex)
                                widget.setDisabled(index != zAxisIndex)
                    else:
                        self.DefaultState(6)
                else:
                    self.DefaultState(6)
            else:
                self.DefaultState(5)
                self.DefaultState(6)
        else:
            self.DefaultState(4)
            self.DefaultState(5)
            self.DefaultState(6)
        # Enable calculate button
        if (mass1Params == True and mass2Params == True and timeVals == True and plotSelectionCB == True):
            if (no3DCB == True):
                if (xAxisCB == True and yAxisCB == True):
                    self.EnableFields(7)
                else:
                    self.DefaultState(7)
            else:
                if (xAxisCB == True and yAxisCB == True and zAxisCB == True):
                    self.EnableFields(7)
                else:
                    self.DefaultState(7)
        else:
            self.DefaultState(7)

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
        for widget in children[3][0:8]:
            widget.setChecked(True)

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
        for widget in children[3][0:8]:
            widget.setChecked(False)
        # Unselect all axis
        for widget in children[4]:
            widget.setChecked(False)
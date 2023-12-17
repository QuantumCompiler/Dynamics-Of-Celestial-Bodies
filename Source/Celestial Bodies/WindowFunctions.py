from ModelFunctions import *

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### Projectile Motion Classes
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

""" ProjectileMotionCanvas - Class for projectile motion plots
    Member Functions:
        Constructor - Constructor for canvas with specific input parameters
        Plot - Plots the results from a projectile motion scenario
"""
class ProjectileMotionCanvas(FigureCanvasQTAgg):
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

    """ Plot - Plots the results from a projectile motion scenario
        Input:
            plotType - Integer that indicates the type of plot to be created
                0 - Position versus time 2D plot
                1 - Position versus time animation
                2 - Velocity versus time 2D plot
                3 - Velocity versus time animation
            obj - Array of values for a given object
                obj[0] - Mass of object in Kg
                obj[1] - Radius of object in m
            ic - Array of initial conditions for a projectile
                ic[0] - Initial vertical position in meters
                ic[1] - Initial vertical velocity in meters / second
            t0 - Initial time of model in seconds
            tn - Final time of model in seconds
            objName - Name of object
            projectileName - Name of projectile
        Algorithm:
            * Call the solver function for projectile motion
            * If the plotType is 0, plot the Position versus time 2D plot
                * Create the plot
                * Set the title, labels, and legend
                * Add the notes to the bottom of the plot
                * Draw the plot on the canvas
            * If the plotType is 1, plot the Position versus time animation
                * Create an array for the point and trail of the plot
                * Set the minimum and maximum for the axes in the plot
                * Create the initialize inner function
                * Create the animate inner function
                * Call the animation for the canvas
                * Set the title, labels, and legend
                * Add the notes to the bottom of the plot
                * Draw the animation on the canvas
            * If the plotType is 2, plot the Velocity versus time 2D plot
                * Create the plot
                * Set the title, labels, and legend
                * Add the notes to the bottom of the plot
                * Draw the plot on the canvas
            * If the plotType is 3, plot the Velocity versus time animation
                * Create an array for the point and trail of the plot
                * Set the minimum and maximum for the axes in the plot
                * Create the initialize inner function
                * Create the animate inner function
                * Call the animation for the canvas
                * Set the title, labels, and legend
                * Add the notes to the bottom of the plot
                * Draw the animation on the canvas
        Output:
            This function does not return a value
    """
    def Plot(self, plotType, obj, ic, t0, tn, objName, projectileName):
        # Call solver
        position, velocity, time = ProjectileMotionSolver(obj, ic, t0, tn)
        # Position Plot
        if (plotType == 0):
            # Clear axes
            self.axes.clear()
            # Plot
            self.axes.plot(time, position, '-', color = 'green', linewidth = 1, label = projectileName)
            # Title, labels, legend
            self.axes.set_title(f"Projectile Motion Plot Of Position Under The Influence Of {objName}", fontsize = TWODPLOTTITLE)
            self.axes.set_xlabel(f"Time In Seconds (s)", fontsize = TWODPLOTABELS)
            self.axes.set_ylabel(f"Vertical Position In (m)", fontsize = TWODPLOTABELS)
            self.axes.legend()
            # Notes
            self.figure.subplots_adjust(bottom=0.35)
            objNotes = f"Object: {objName}, Mass = {obj[0]} $(Kg)$, Radius = {obj[1]} $(m)$"
            initNotes = f"Initial Conditions: {projectileName}, Initial Vertical Position = {ic[0]} $(m)$, Initial Vertical Velocity = {ic[1]} $(m/s)$"
            finalNotes = f"Final Conditions: {projectileName}, Final Vertical Position = {round(position[-1],2)} $(m)$, Final Vertical Velocity = {round(velocity[-1],2)} $(m/s)$"
            timeNotes = f"Simulation From {t0} $(s)$ to {tn} $(s)$"
            self.figure.text(0.1, 0.05, objNotes + "\n" + initNotes + "\n" + finalNotes + "\n" + timeNotes, ha='left', va='bottom', fontsize=TWODNOTES)
            # Draw plot on canvas
            self.draw()
        # Position animation
        if (plotType == 1):
            # Clear axes
            self.axes.clear()
            # Arrays for point and trail
            projectile, = self.axes.plot([], [], 'o', color='green', markersize=2, label=projectileName)
            projectileTrail, = self.axes.plot([], [], '-', color='green', linewidth=1, alpha=0.5)
            # Max and min of axes
            self.axes.set_xlim(min(time) - 0.05 * max(time), 1.05 * max(time))
            self.axes.set_ylim(min(position) - 0.05 * max(position), 1.05 * max(position))
            # Initialize function
            def init():
                projectile.set_data([], [])
                projectileTrail.set_data([], [])
                return projectile, projectileTrail
            # Animation function
            def animate(k):
                projectile.set_data([time[k], position[k]])
                projectileTrail.set_data(time[:k+1], position[:k+1])
                return projectile, projectileTrail
            # Animation
            self.ani = FuncAnimation(self.figure, animate, init_func=init, frames=len(time), interval=1e-5, blit=True, repeat=True)
            # Title, labels, legend
            self.axes.set_title(f"Projectile Motion Animation Of Position Under The Influence Of {objName}", fontsize = TWODANIMTITLE)
            self.axes.set_xlabel(f"Time In Seconds (s)", fontsize = TWODANIMLABELS)
            self.axes.set_ylabel(f"Vertical Position In (m)", fontsize = TWODANIMLABELS)
            self.axes.legend()
            # Notes
            self.figure.subplots_adjust(bottom=0.35)
            objNotes = f"Object: {objName}, Mass = {obj[0]} $(Kg)$, Radius = {obj[1]} $(m)$"
            initNotes = f"Initial Conditions: {projectileName}, Initial Vertical Position = {ic[0]} $(m)$, Initial Vertical Velocity = {ic[1]} $(m/s)$"
            finalNotes = f"Final Conditions: {projectileName}, Final Vertical Position = {round(position[-1],2)} $(m)$, Final Vertical Velocity = {round(velocity[-1],2)} $(m/s)$"
            timeNotes = f"Simulation From {t0} $(s)$ to {tn} $(s)$"
            self.figure.text(0.1, 0.05, objNotes + "\n" + initNotes + "\n" + finalNotes + "\n" + timeNotes, ha='left', va='bottom', fontsize=TWODNOTES)
            # Draw animation on canvas
            self.draw()
        # Velocity plot
        if (plotType == 2):
            # Clear axes
            self.axes.clear()
            # Plot
            self.axes.plot(time, velocity, '-', color = 'green', linewidth = 1, label = projectileName)
            # Title, labels, legend
            self.axes.set_title(f"Projectile Motion Plot Of Velocity Under The Influence Of {objName}", fontsize = TWODPLOTTITLE)
            self.axes.set_xlabel(f"Time In Seconds (s)", fontsize = TWODPLOTABELS)
            self.axes.set_ylabel(f"Vertical Velocity In $(\\frac{{m}}{{s}})$", fontsize = TWODPLOTABELS)
            self.axes.legend()
            # Notes
            self.figure.subplots_adjust(bottom=0.35)
            objNotes = f"Object: {objName}, Mass = {obj[0]} $(Kg)$, Radius = {obj[1]} $(m)$"
            initNotes = f"Initial Conditions: {projectileName}, Initial Vertical Position = {ic[0]} $(m)$, Initial Vertical Velocity = {ic[1]} $(m/s)$"
            finalNotes = f"Final Conditions: {projectileName}, Final Vertical Position = {round(position[-1],2)} $(m)$, Final Vertical Velocity = {round(velocity[-1],2)} $(m/s)$"
            timeNotes = f"Simulation From {t0} $(s)$ to {tn} $(s)$"
            self.figure.text(0.1, 0.05, objNotes + "\n" + initNotes + "\n" + finalNotes + "\n" + timeNotes, ha='left', va='bottom', fontsize=TWODNOTES)
            # Draw plot on canvas
            self.draw()
        # Velocity animation
        if (plotType == 3):
            # Clear axes
            self.axes.clear()
            # Arrays for point and trail
            projectile, = self.axes.plot([], [], 'o', color='green', markersize=2, label=projectileName)
            projectileTrail, = self.axes.plot([], [], '-', color='green', linewidth=1, alpha=0.5)
            # Max and min of axes
            self.axes.set_xlim(min(time) - 0.05 * max(time), 1.05 * max(time))
            if (max(velocity) <= 0):
                self.axes.set_ylim(min(velocity) - 0.05 * max(velocity), 0.05 * abs(min(velocity)))
            else:
                self.axes.set_ylim(min(velocity) - 0.05 * max(velocity), 1.05 * max(velocity))
            # Initialize function
            def init():
                projectile.set_data([], [])
                projectileTrail.set_data([], [])
                return projectile, projectileTrail
            # Animation function
            def animate(k):
                projectile.set_data([time[k], velocity[k]])
                projectileTrail.set_data(time[:k+1], velocity[:k+1])
                return projectile, projectileTrail
            # Animation
            self.ani = FuncAnimation(self.figure, animate, init_func=init, frames=len(time), interval=1e-5, blit=True, repeat=True)
            # Title, labels, legend
            self.axes.set_title(f"Projectile Motion Animation Of Velocity Under The Influence Of {objName}", fontsize = TWODANIMTITLE)
            self.axes.set_xlabel(f"Time In Seconds (s)", fontsize = TWODANIMLABELS)
            self.axes.set_ylabel(f"Vertical Velocity In $(\\frac{{m}}{{s}})$", fontsize = TWODPLOTABELS)
            self.axes.legend()
            # Notes
            self.figure.subplots_adjust(bottom=0.35)
            objNotes = f"Object: {objName}, Mass = {obj[0]} $(Kg)$, Radius = {obj[1]} $(m)$"
            initNotes = f"Initial Conditions: {projectileName}, Initial Vertical Position = {ic[0]} $(m)$, Initial Vertical Velocity = {ic[1]} $(m/s)$"
            finalNotes = f"Final Conditions: {projectileName}, Final Vertical Position = {round(position[-1],2)} $(m)$, Final Vertical Velocity = {round(velocity[-1],2)} $(m/s)$"
            timeNotes = f"Simulation From {t0} $(s)$ to {tn} $(s)$"
            self.figure.text(0.1, 0.05, objNotes + "\n" + initNotes + "\n" + finalNotes + "\n" + timeNotes, ha='left', va='bottom', fontsize=TWODNOTES)
            # Draw animation on canvas
            self.draw()

""" ProjectileMotionWindow - Class for projectile motion windows
    Member Functions:
        Constructor - Creates windows with specific input parameters
        closeEvent - Deletes plot canvas when window is closed
"""
class ProjectileMotionPlotWindow(QWidget):
    """ Constructor - Creates windows with specific input parameters
        Input:
            plotType - Integer that indicates the type of plot to be created
                0 - Position versus time 2D plot
                1 - Position versus time animation
                2 - Velocity versus time 2D plot
                3 - Velocity versus time animation
            obj - Array of values for a given object
                obj[0] - Mass of object in Kg
                obj[1] - Radius of object in m
            ic - Array of initial conditions for a projectile
                ic[0] - Initial vertical position in meters
                ic[1] - Initial vertical velocity in meters / second
            t0 - Initial time of model in seconds
            tn - Final time of model in seconds
            objName - Name of object
            projectileName - Name of projectile
            windowTitle - Title for window
        Algorithm:
            * Set the title of the window
            * Set the sizes of the window
            * Create the layout for the window
            * Create the canvas for the plot for the specific plot type
            * Generate the toolbar for the canvas
            * Add the widgets to the layout
            * Set the layout
        Output:
            This function does not return a value
    """
    def __init__(self, plotType, obj, ic, t0, tn, objName, projectileName, windowTitle):
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
        self.plotCanvas = ProjectileMotionCanvas(self, width=3, height=2, dpi=100)
        self.plotCanvas.Plot(plotType, obj, ic, t0, tn, objName, projectileName)
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
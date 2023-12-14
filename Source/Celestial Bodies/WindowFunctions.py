from ModelFunctions import *



# Projectile Motion Classes

class ProjectileMotionCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=3, height=2, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvasQTAgg.__init__(self, fig)

    def Plot(self, plotType, obj, ic, t0, tn, objName, projectileName):
        # Call function
        position, velocity, time = ProjectileMotionSolver(obj, ic, t0, tn)
        if (plotType == 0):
            self.axes.plot(time, position, '-', color = 'green', linewidth = 1, label = projectileName)
            self.axes.set_title(f"Projectile Motion Plot Of Position Under The Influence Of {objName}", fontsize = TWODPLOTTITLE)
            self.axes.set_xlabel(f"Time In Seconds (s)", fontsize = TWODPLOTABELS)
            self.axes.set_ylabel(f"Vertical Position In (m)", fontsize = TWODPLOTABELS)
            self.axes.legend()
            self.draw()
        if (plotType == 1):
            projectile, = self.axes.plot([], [], 'o', color='green', markersize=2, label=projectileName)
            projectileTrail, = self.axes.plot([], [], '-', color='green', linewidth=1, alpha=0.5)
            self.axes.set_xlim(min(time) - 0.05 * max(time), 1.05 * max(time))
            self.axes.set_ylim(min(position) - 0.05 * max(position), 1.05 * max(position))
            def init():
                projectile.set_data([], [])
                projectileTrail.set_data([], [])
                return projectile, projectileTrail
            def animate(k):
                projectile.set_data([time[k], position[k]])
                projectileTrail.set_data(time[:k+1], position[:k+1])
                return projectile, projectileTrail
            self.ani = FuncAnimation(self.figure, animate, init_func=init, frames=len(time), interval=1e-5, blit=True, repeat=True)
            self.axes.set_title(f"Projectile Motion Animation Of Position Under The Influence Of {objName}", fontsize = TWODANIMTITLE)
            self.axes.set_xlabel(f"Time In Seconds (s)", fontsize = TWODANIMLABELS)
            self.axes.set_ylabel(f"Vertical Position In (m)", fontsize = TWODANIMLABELS)
            self.axes.legend()
            self.draw()
        if (plotType == 2):
            self.axes.plot(time, velocity, '-', color = 'green', linewidth = 1, label = projectileName)
            self.axes.set_title(f"Projectile Motion Plot Of Velocity Under The Influence Of {objName}", fontsize = TWODPLOTTITLE)
            self.axes.set_xlabel(f"Time In Seconds (s)", fontsize = TWODPLOTABELS)
            self.axes.set_ylabel(f"Vertical Velocity In $(\\frac{{m}}{{s}})$", fontsize = TWODPLOTABELS)
            self.axes.legend()
            self.draw()
        if (plotType == 3):
            projectile, = self.axes.plot([], [], 'o', color='green', markersize=2, label=projectileName)
            projectileTrail, = self.axes.plot([], [], '-', color='green', linewidth=1, alpha=0.5)
            self.axes.set_xlim(min(time) - 0.05 * max(time), 1.05 * max(time))
            if (max(velocity) <= 0):
                self.axes.set_ylim(min(velocity) - 0.05 * max(velocity), 0.05 * abs(min(velocity)))
            else:
                self.axes.set_ylim(min(velocity) - 0.05 * max(velocity), 1.05 * max(velocity))
            def init():
                projectile.set_data([], [])
                projectileTrail.set_data([], [])
                return projectile, projectileTrail
            def animate(k):
                projectile.set_data([time[k], velocity[k]])
                projectileTrail.set_data(time[:k+1], velocity[:k+1])
                return projectile, projectileTrail
            self.ani = FuncAnimation(self.figure, animate, init_func=init, frames=len(time), interval=1e-5, blit=True, repeat=True)
            self.axes.set_title(f"Projectile Motion Animation Of Velocity Under The Influence Of {objName}", fontsize = TWODANIMTITLE)
            self.axes.set_xlabel(f"Time In Seconds (s)", fontsize = TWODANIMLABELS)
            self.axes.set_ylabel(f"Vertical Velocity In $(\\frac{{m}}{{s}})$", fontsize = TWODPLOTABELS)
            self.axes.legend()
            self.draw()

class ProjectileMotionWindow(QWidget):
    def __init__(self, plotType, obj, ic, t0, tn, objName, projectileName, windowTitle):
        super().__init__()
        self.setWindowTitle(windowTitle)
        self.resize(800,500)
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        self.layout = QVBoxLayout()
        self.plotCanvas = ProjectileMotionCanvas(self, width=3, height=2, dpi=100)
        self.plotCanvas.Plot(plotType, obj, ic, t0, tn, objName, projectileName)
        self.layout.addWidget(self.plotCanvas)
        self.toolBar = NavigationToolbar(self.plotCanvas, self)
        self.layout.addWidget(self.toolBar)
        self.setLayout(self.layout)

    def closeEvent(self, event):
        if hasattr(self, 'plotCanvas') and hasattr(self.plotCanvas, 'ani'):
            self.plotCanvas.ani.event_source.stop()
        super().closeEvent(event)
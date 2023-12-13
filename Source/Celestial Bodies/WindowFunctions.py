from ModelFunctions import *



# Projectile Motion Classes

class ProjectileMotionCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=3, height=2, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvasQTAgg.__init__(self, fig)

    def Plot(self, yaxis, obj, ic, t0, tn, objName, projectileName):
        # Call function
        position, velocity, time = ProjectileMotionSolver(obj, ic, t0, tn)
        if (yaxis == 0):
            self.axes.plot(position, time, '-', color = 'green', linewidth = 1, label = projectileName)
            self.axes.set_title(f"Projectile Motion Plot Of Position Under The Influence Of {objName}", fontsize = TWODPLOTTITLE)
            self.axes.set_xlabel(f"Time In Seconds (s)", fontsize = TWODPLOTABELS)
            self.axes.set_ylabel(f"Vertical Position In (m)", fontsize = TWODPLOTABELS)
            self.axes.legend()
            self.draw()

class ProjectileMotionWindow(QWidget):
    def __init__(self, plotType, obj, ic, t0, tn, objName, projectileName):
        super().__init__()
        self.setWindowTitle("Plot Integration with Toolbar")
        self.setGeometry(100, 100, 800, 600)
        layout = QVBoxLayout()
        if (plotType == 0):
            plotCanvas = ProjectileMotionCanvas(self, width=3, height=2, dpi=100)
            plotCanvas.Plot(0, obj, ic, t0, tn, objName, projectileName)
        layout.addWidget(plotCanvas)
        toolBar = NavigationToolbar(plotCanvas, self)
        layout.addWidget(toolBar)
        self.setLayout(layout)
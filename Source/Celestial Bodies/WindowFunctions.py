from ModelFunctions import *

# class PlotCanvas2D(FigureCanvasQTAgg):
#     def __init__(self, parent=None, width=3, height=2, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = fig.add_subplot(111)
#         FigureCanvasQTAgg.__init__(self, fig)

#     def plot(self, inputData, plotTitle):
#         self.axes.plot(inputData, 'r-')
#         self.axes.set_title(plotTitle)
#         self.draw()

# class PlotWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Plot Integration with Toolbar")
#         self.setGeometry(100, 100, 800, 600)
#         centralWidget = QWidget(self)
#         self.setCentralWidget(centralWidget)
#         layout = QVBoxLayout(centralWidget)
#         plotCanvas = PlotCanvas2D(self, width=3, height=2)
#         layout.addWidget(plotCanvas)
#         toolBar = NavigationToolbar(plotCanvas, self)
#         layout.addWidget(toolBar)


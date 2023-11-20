# Imports
from ModelFunctions import *

# masses = [MSUN, MEARTH]
# ic = [SUNPOS, EARTHPOS, SUNVEL, EARTHVEL]

# Masses = [2e30, 5.972e24]
# Ic = [
#     [0,0,0],
#     [AU,0,0],
#     [0,0,0],
#     [0,2.97848e4,0]
# ]

# CoupledTwoBody2DPlotPos(masses, ic, 0, EARTHPERIOD, 0, 1, "Sun", "Earth")

# CoupledTwoBody2DAnimPos(masses, ic, 0, EARTHPERIOD, 0, 1, "Sun", "Earth")

# CoupledTwoBody2DPlotVel(masses, ic, 0, EARTHPERIOD, 0, "Sun", "Earth")

# CoupledTwoBody2DAnimVel(masses, ic, 0, EARTHPERIOD, 0, "Sun", "Earth")

# class MainWindow(QMainWindow):
#     # Constructor
#     def __init__(self):
#         super().__init__()
#         # Title of Window
#         self.setWindowTitle("Celestial Bodies")
#         # Height and Width of Window
#         self.resize(850,500)
#         self.setMinimumWidth(850)
#         self.setMinimumHeight(400)

# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# sys.exit(app.exec())
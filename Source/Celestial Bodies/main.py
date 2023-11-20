# Imports
from ModelFunctions import *

threeMasses = [MSUN, MEARTH, MMOON]

threeIC = [SUNPOS, EARTHPOS, MOONPOS, SUNVEL, EARTHVEL, MOONVEL]

CoupledThreeBody2DPlotPos(threeMasses, threeIC, 0, EARTHPERIOD, 0, 1, "Sun", "Earth", "Moon")

CoupledThreeBody2DAnimPos(threeMasses, threeIC, 0, EARTHPERIOD, 0, 1, "Sun", "Earth", "Moon")

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
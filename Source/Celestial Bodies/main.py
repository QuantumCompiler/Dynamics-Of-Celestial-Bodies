# Imports
from ModelFunctions import *

# Widget Names 
HeaderLabel = "Choose A Simulation"
TwoDForceLabel = "2D Force"
TwoBodyLabel = "2 Body Simulation"
ThreeBodyLabel = "3 Body Simulation"

# Object Names
TwoDForceObjName = "2D Force Button"
TwoBodyObjName = "2 Body Button"
ThreeBodyObjName = "3 Body Button"

class MainWindow(QMainWindow):
    # Constructor
    def __init__(self):
        super().__init__()
        # Title of Window
        self.setWindowTitle("Celestial Bodies")
        # Height and Width of Window
        self.resize(800,500)
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        # Header label
        self.headerLabel = QLabel(HeaderLabel, self)
        self.centerWidgetHoriz(self.headerLabel)
        headerFont = self.headerLabel.font()
        headerFont.setPointSize(50)
        self.headerLabel.setFont(headerFont)
        self.headerLabel.adjustSize()
        self.headerLabel.move((self.size().width() - self.headerLabel.size().width()) // 2, int(0.05 * self.size().height()))
        # 2 Body Button
        self.TwoDForceBtn = QPushButton(TwoDForceLabel, self)
        self.TwoDForceBtn.setFixedSize(400, 50)
        self.TwoDForceBtn.setObjectName(TwoDForceObjName)
        self.centerWidgetHoriz(self.TwoDForceBtn)
        self.TwoDForceBtn.move(self.TwoDForceBtn.pos().x(), 6 * self.headerLabel.pos().y())
        # 2 Body Button
        self.TwoBodyBtn = QPushButton(TwoBodyLabel, self)
        self.TwoBodyBtn.setFixedSize(400, 50)
        self.TwoBodyBtn.setObjectName(TwoBodyObjName)
        self.centerWidgetHoriz(self.TwoBodyBtn)
        self.TwoBodyBtn.move(self.TwoBodyBtn.pos().x(), self.TwoDForceBtn.pos().y() + 50)
        # 3 Body Button
        self.ThreeBodyBtn = QPushButton(ThreeBodyLabel, self)
        self.ThreeBodyBtn.setFixedSize(400, 50)
        self.ThreeBodyBtn.setObjectName(ThreeBodyObjName)
        self.centerWidgetHoriz(self.ThreeBodyBtn)
        self.ThreeBodyBtn.move(self.ThreeBodyBtn.pos().x(), self.TwoBodyBtn.pos().y() + 50)
        
    def centerWidgetHoriz(self, widget):
        windowWidth = self.size().width()
        widgetWidth = widget.size().width()
        widgetYPos = widget.pos().y()
        horizCenter = (windowWidth - widgetWidth) // 2
        widget.move(horizCenter, widgetYPos)

    def resizeEvent(self, event):
        self.centerWidgetHoriz(self.headerLabel)
        self.centerWidgetHoriz(self.TwoDForceBtn)
        self.centerWidgetHoriz(self.TwoBodyBtn)
        self.centerWidgetHoriz(self.ThreeBodyBtn)
        super().resizeEvent(event)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

# # First button
# self.button1 = QPushButton("Button 1", self)
# self.button1.move(50, 50)  # Position the first button

# # Calculate position for the second button
# # 10 pixels to the right of the first button
# button2_x = self.button1.x() + self.button1.width() + 100
# button2_y = self.button1.y() + 100

# # Second button
# self.button2 = QPushButton("Button 2", self)
# self.button2.move(button2_x, button2_y)  # Position the second button
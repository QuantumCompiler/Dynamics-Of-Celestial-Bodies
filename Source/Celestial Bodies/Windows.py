from ModelFunctions import *

class TwoDForceWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Title of Window
        self.setWindowTitle("2D Force Simulation")
        # Height and Width of Window
        self.resize(800,500)
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        # Layouts
        mainLayout = QHBoxLayout()
        leftColumn = QVBoxLayout()
        rightColumn = QVBoxLayout()
        # Left column
        leftColumnHeader = QLabel("Parameters")
        leftHeaderFont = leftColumnHeader.font()
        leftHeaderFont.setPointSize(30)
        leftColumnHeader.setFont(leftHeaderFont)
        leftColumnHeader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        leftColumn.addWidget(leftColumnHeader, Qt.AlignmentFlag.AlignHCenter)
        # Right column
        rightColumnHeader = QLabel("Output")
        rightHeaderFont = rightColumnHeader.font()
        rightHeaderFont.setPointSize(30)
        rightColumnHeader.setFont(rightHeaderFont)
        rightColumnHeader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        rightColumn.addWidget(rightColumnHeader, Qt.AlignmentFlag.AlignHCenter)
        # Add layouts
        mainLayout.addLayout(leftColumn)
        mainLayout.addLayout(rightColumn)
        self.setLayout(mainLayout)

class TwoBodyWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Title of Window
        self.setWindowTitle("2 Body Simulation")
        # Height and Width of Window
        self.resize(800,500)
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        # Layouts
        mainLayout = QHBoxLayout()
        leftColumn = QVBoxLayout()
        rightColumn = QVBoxLayout()
        # Left column
        leftColumnHeader = QLabel("Parameters")
        leftHeaderFont = leftColumnHeader.font()
        leftHeaderFont.setPointSize(30)
        leftColumnHeader.setFont(leftHeaderFont)
        leftColumnHeader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        leftColumn.addWidget(leftColumnHeader, Qt.AlignmentFlag.AlignHCenter)
        # Right column
        rightColumnHeader = QLabel("Output")
        rightHeaderFont = rightColumnHeader.font()
        rightHeaderFont.setPointSize(30)
        rightColumnHeader.setFont(rightHeaderFont)
        rightColumnHeader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        rightColumn.addWidget(rightColumnHeader, Qt.AlignmentFlag.AlignHCenter)
        # Add layouts
        mainLayout.addLayout(leftColumn)
        mainLayout.addLayout(rightColumn)
        self.setLayout(mainLayout)

class ThreeBodyWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Title of Window
        self.setWindowTitle("3 Body Simulation")
        # Height and Width of Window
        self.resize(800,500)
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        # Layouts
        mainLayout = QHBoxLayout()
        leftColumn = QVBoxLayout()
        rightColumn = QVBoxLayout()
        # Left column
        leftColumnHeader = QLabel("Parameters")
        leftHeaderFont = leftColumnHeader.font()
        leftHeaderFont.setPointSize(30)
        leftColumnHeader.setFont(leftHeaderFont)
        leftColumnHeader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        leftColumn.addWidget(leftColumnHeader, Qt.AlignmentFlag.AlignHCenter)
        # Right column
        rightColumnHeader = QLabel("Output")
        rightHeaderFont = rightColumnHeader.font()
        rightHeaderFont.setPointSize(30)
        rightColumnHeader.setFont(rightHeaderFont)
        rightColumnHeader.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        rightColumn.addWidget(rightColumnHeader, Qt.AlignmentFlag.AlignHCenter)
        # Add layouts
        mainLayout.addLayout(leftColumn)
        mainLayout.addLayout(rightColumn)
        self.setLayout(mainLayout)
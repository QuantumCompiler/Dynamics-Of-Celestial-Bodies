QT       += core gui qml quick          
CONFIG   += c++17                       
TEMPLATE  = app
TARGET    = main                       

SOURCES += src/C/main.cpp src/C/SimulationController.cpp
HEADERS += src/C/SimulationController.h
RESOURCES += QML.qrc

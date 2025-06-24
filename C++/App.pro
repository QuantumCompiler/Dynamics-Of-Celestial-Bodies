QT       += core gui qml quick          
CONFIG   += c++17                       
TEMPLATE  = app
TARGET    = main                       

SOURCES += src/C/main.cpp src/C/CPPSimulationController.cpp
HEADERS += src/C/CPPSimulationController.h
RESOURCES += QML.qrc

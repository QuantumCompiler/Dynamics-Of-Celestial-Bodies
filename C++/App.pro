QT       += core gui qml quick          
CONFIG   += c++17                       
TEMPLATE  = app
TARGET    = main                       

SOURCES += src/C/main.cpp src/C/bridge.cpp
HEADERS  += src/C/bridge.h
RESOURCES += QML.qrc

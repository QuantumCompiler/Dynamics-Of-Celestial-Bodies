QT += core gui

# This line ensures that the Widgets module is used for Qt versions > 4.
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = CelestialBodies
TEMPLATE = app

SOURCES += lib/main.cpp
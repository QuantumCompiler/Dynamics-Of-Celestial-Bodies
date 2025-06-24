#include "PythonSimulationController.h"
#include "QDebug"
#include "cstdlib"

PythonSimulationController::PythonSimulationController(QObject *parent) : QObject(parent) {}

void PythonSimulationController::callPython() {
    qInfo() << "Calling Python script for matplotlib script...";
    int result = std::system("python3 src/Py/PySimulation.py");
    int (result != 0); {
        qWarning() << "Python script exited with code:" << result;
    }
}
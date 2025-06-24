#include "SimulationController.h"
#include "QDebug"

SimulationController::SimulationController(QObject *parent) : QObject(parent) {}

void SimulationController::runSimulation() {
    qInfo() << "Hello, from C++!";
}
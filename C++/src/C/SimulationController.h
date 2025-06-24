// SimulationController.h
#pragma once
#include <QObject>

class SimulationController : public QObject {
    Q_OBJECT
public:
    explicit SimulationController(QObject *parent = nullptr);
    Q_INVOKABLE void runSimulation();
};
#pragma once
#include <QObject>

class PythonSimulationController : public QObject {
    Q_OBJECT
public:
    explicit PythonSimulationController(QObject *parent = nullptr);
    Q_INVOKABLE void callPython();
};
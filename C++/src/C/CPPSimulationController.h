// CPPSimulationController.h
#pragma once
#include <QObject>

/*  CPPSimulationController - Basic C++ class to simulate a controller for a simulation.

    Inheritance - QObject: This class inherits from QObject, which is the base class for all Qt objects.

    Access Specifier - public: The class is publicly accessible, meaning it can be instantiated and used in other parts of the application.

    Constructor:

        Input Parameter:
            QObject *parent: A pointer to the parent QObject, which is used for memory management and object hierarchy in Qt.
        Purpose: Initializes the CPPSimulationController object and sets its parent.

        Body:
            Q_INVOKABLE void runSimulation(): This method is declared as invokable, allowing it to be called from QML or other contexts. 
            It will execute the simulation logic.
*/
class CPPSimulationController : public QObject {
    Q_OBJECT
public:
    explicit CPPSimulationController(QObject *parent = nullptr);
    Q_INVOKABLE void runSimulation();
};
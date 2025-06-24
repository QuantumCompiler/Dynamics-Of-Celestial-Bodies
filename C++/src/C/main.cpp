#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlContext>

#include "CPPSimulationController.h"
#include "PythonSimulationController.h"

int main(int argc, char *argv[]) {
    QGuiApplication app(argc, argv);
    QQmlApplicationEngine engine;

    CPPSimulationController cppSimController;
    PythonSimulationController pySimController;
    engine.rootContext()->setContextProperty("simController", &cppSimController);
    engine.rootContext()->setContextProperty("pySimController", &pySimController);

    engine.load(QUrl(QStringLiteral("qrc:src/QML/main.qml")));
    if (engine.rootObjects().isEmpty())
        return -1;

    return app.exec();
}

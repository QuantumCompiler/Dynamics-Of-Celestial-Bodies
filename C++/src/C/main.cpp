#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlContext>

#include "SimulationController.h"

int main(int argc, char *argv[]) {
    QGuiApplication app(argc, argv);
    QQmlApplicationEngine engine;

    SimulationController simController;
    engine.rootContext()->setContextProperty("simController", &simController);

    engine.load(QUrl(QStringLiteral("qrc:src/QML/main.qml")));
    if (engine.rootObjects().isEmpty())
        return -1;

    return app.exec();
}

#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlContext>

#include "CPPSimulationController.h"

int main(int argc, char *argv[]) {
    QGuiApplication app(argc, argv);
    QQmlApplicationEngine engine;

    CPPSimulationController cppSimController;
    engine.rootContext()->setContextProperty("simController", &cppSimController);

    engine.load(QUrl(QStringLiteral("qrc:src/QML/main.qml")));
    if (engine.rootObjects().isEmpty())
        return -1;

    return app.exec();
}

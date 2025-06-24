#include "bridge.h"
#include <QProcess>
#include <QString>

BackendBridge::BackendBridge(QObject *parent) : QObject(parent) {}

QString BackendBridge::callPython()
{
    QProcess process;
    process.start("python3", QStringList() << "../backend.py");
    process.waitForFinished();
    QString output = process.readAllStandardOutput();
    return output.trimmed();
}

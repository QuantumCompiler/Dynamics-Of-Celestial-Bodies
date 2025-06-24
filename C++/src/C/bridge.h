#ifndef BRIDGE_H
#define BRIDGE_H

#include <QObject>

class BackendBridge : public QObject
{
    Q_OBJECT
public:
    explicit BackendBridge(QObject *parent = nullptr);

    Q_INVOKABLE QString callPython();
};

#endif // BRIDGE_H

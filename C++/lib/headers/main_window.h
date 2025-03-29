#ifndef MAIN_WINDOW_H
#define MAIN_WINDOW_H
#include <QMainWindow>
#include <QWidget>

class MainWindow : public QMainWindow
{
    Q_OBJECT
public:
    explicit MainWindow(QWidget *parent = nullptr);
};

#endif
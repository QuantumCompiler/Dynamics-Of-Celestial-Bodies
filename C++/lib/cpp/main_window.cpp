#include "../headers/main_window.h"

MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent)
{
    this->setWindowTitle("Celestial Bodies");
    this->resize(800, 500);
    this->setMinimumSize(400, 300);
}
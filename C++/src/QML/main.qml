import QtQuick 2.15
import QtQuick.Controls 2.15
import "../JS/helpers.js" as Helpers

ApplicationWindow {
    id: homeWindow
    visible: true
    width: 800
    height: 500
    minimumWidth: 300
    minimumHeight: 200
    title: "Celestial Bodies"

    property color windowColor: "black"
    property color windowHeaderColor: "white"
    property color pythonButtonBGColor: "white"
    property color pythonButtonTextColor: "green"

    background: Rectangle {
        color: homeWindow.windowColor
    }

    // Main column
    Column {
        anchors.centerIn: parent
        spacing: 15

        // C++ Implementation
        Button {
            text: "C++ Simulation"
            onClicked: simController.runSimulation();
        }
    }
}
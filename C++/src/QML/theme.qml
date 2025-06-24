import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    id: themeWindow
    visible: false
    width: 600
    height: 400
    minimumWidth: 600
    minimumHeight: 400
    title: "Theme Window"

    property color windowColor: "black"
    property color windowHeaderColor: "white"
    property color buttonColor: "white"
    property color buttonTextColor: "black"
    property bool themeDefault: true

    background: Rectangle {
        color: themeWindow.windowColor
    }

    // Main Column
    Column {
        anchors.centerIn: parent
        spacing: 15

        // Header text
        Text {
            id: headerText
            text: "Here is another window for you :)"
            color: themeWindow.windowHeaderColor
        }

        // Change Theme Button
        Row {
            anchors.horizontalCenter: parent.horizontalCenter
            Button {
                id: themeButton
                text: "Change Theme"
                background: Rectangle {
                    radius: 15
                    color: themeWindow.buttonColor
                }

                contentItem: Text {
                    text: parent.text
                    color: themeWindow.buttonTextColor
                    font.pixelSize: 16
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.fill: parent
                }

                onClicked: {
                    if (themeWindow.themeDefault == true) {
                        themeWindow.windowColor = "white"
                        themeWindow.windowHeaderColor = "black"
                        themeWindow.buttonColor = "black"
                        themeWindow.buttonTextColor = "white"
                        themeWindow.themeDefault = false
                    } else {
                        themeWindow.windowColor = "black"
                        themeWindow.windowHeaderColor = "white"
                        themeWindow.buttonColor = "white"
                        themeWindow.buttonTextColor = "black"
                        themeWindow.themeDefault = true
                    }
                }
            }
        }
    }
}
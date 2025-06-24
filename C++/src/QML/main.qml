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
    title: "QML + JS + C++ + Python"

    property color windowColor: "black"
    property color windowHeaderColor: "white"
    property color pythonButtonBGColor: "white"
    property color pythonButtonTextColor: "green"

    background: Rectangle {
        color: homeWindow.windowColor
    }

    // Load external files
    Loader {
        source: "theme.qml";
    }
    Loader {
        source: "navigation.qml";
    }

    // Main column
    Column {
        anchors.centerIn: parent
        spacing: 15

        Text {
            id: resultText
            text: "Click Me :)"
            color: homeWindow.windowHeaderColor
            anchors.horizontalCenter: parent.horizontalCenter
        }

        // JavaScript button
        Row {
            spacing: 10
            anchors.horizontalCenter: parent.horizontalCenter

            Button {
                id: jsButton
                text: "Hello World, From JavaScript"
                background: Rectangle {
                    radius: 10
                    color: "white"
                }

                // Customize Content of button
                contentItem: Text {
                    text: parent.text
                    color: "orange"
                    font.pixelSize: 16
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.fill: parent
                }

                // Change Text With JS
                onClicked: {
                    resultText.text = Helpers.message("Hello from JavaScript!")
                    resultText.color = "orange"
                    firstEle.text = "You"
                    firstEle.color = "white"
                    secEle.text = "Just Used"
                    secEle.color = "white"
                    thirdEle.text = "JavaScript!"
                    thirdEle.color = "orange"
                }
            }
        }

        // Row text
        Row {
            spacing: 10
            anchors.horizontalCenter: parent.horizontalCenter
            
            Text {
                id: firstEle
                text: "This Is"
                color: "red"
            }
            
            Text {
                id: secEle
                text: "A"
                color: "white"
            }

            Text {
                id: thirdEle
                text: "Row Test"
                color: "blue"
            }
        }

        // Button row
        Row {
            spacing: 10
            anchors.horizontalCenter: parent.horizontalCenter

            // Reset Button
            Button {
                id: resetBut
                text: "Reset"
                background: Rectangle {
                    radius: 10
                    color: "white"
                }

                // Customize content of button
                contentItem: Text{
                    text: parent.text
                    color: "black"
                    font.pixelSize: 16
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.fill: parent
                }

                onClicked: {
                    resultText.text = "Click Me :)"
                    resultText.color = "white"
                    firstEle.text = "This Is"
                    firstEle.color = "red"
                    secEle.text = "A"
                    secEle.color = "white"
                    thirdEle.text = "Row Test"
                    thirdEle.color = "blue"
                }
            }

            // Theme Changer Button
            Button {
                id: themeBut
                text: "Theme Changer"
                background: Rectangle {
                    radius: 10
                    color: "white"
                }

                // Customize content of button
                contentItem: Text{
                    text: parent.text
                    color: "black"
                    font.pixelSize: 16
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.fill: parent
                }

                onClicked: {
                    var component = Qt.createComponent("theme.qml")
                    var window = component.createObject()
                    window.show()
                }
            }

            // Navigation Demo Button
            Button {
                id: navBut
                text: "Navigation Demo"
                background: Rectangle {
                    radius: 10
                    color: "white"
                }

                // Customize content of buttons
                contentItem: Text{
                    text: parent.text
                    color: "black"
                    font.pixelSize: 16
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.fill: parent
                }

                onClicked: {
                    var component = Qt.createComponent("navigation.qml")
                    var window = component.createObject()
                    window.show()
                }
            }
        }
    }
}
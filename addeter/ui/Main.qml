import QtQuick 2.14
import QtQuick.Layouts 1.14
import QtQuick.Controls 2.14
import QtQuick.Window 2.14
import QtQuick.Controls.Universal 2.14

ApplicationWindow {
    id: page
    width: 650
    height: 300
    visible: true

    Rectangle {
        id: rect1
        x: 0
        color: "#2196F3"
        anchors.left: parent.left
        anchors.right: parent.right
        height: 50

        Text {
            id: leftlabel
            Layout.alignment: Qt.AlignHCenter
            color: "white"
            font.pointSize: 25
            font.bold: true
            text: "Addeter"
            Layout.preferredHeight: 100
            topPadding: 0
            leftPadding: 25
        }
    }
    StackView {
        id: stackView
        initialItem: home
        anchors.fill: parent
        anchors.topMargin: 50

        Component {
            id: addHost
            AddHost {}
        }

        Component {
            id: home
            Home {}
        }
    }
}

import QtQuick 2.14
import QtQuick.Layouts 1.14
import QtQuick.Controls 2.14
import QtQuick.Window 2.14
import QtQuick.Controls.Universal 2.14

ColumnLayout {
    id: addHostColumn
    spacing: 0
    Layout.alignment: Qt.AlignTop
    Layout.topMargin: 25
    property StackView view

    ColumnLayout {
        spacing: 0
        Layout.minimumWidth: 300
        Layout.alignment: Qt.AlignHCenter | Qt.AlignTop
        Layout.topMargin: 25

        TextField {
            id: newHostLabel
            placeholderText: qsTr("Label")
            Layout.alignment: Qt.AlignHCenter
            Layout.minimumWidth: 300
            Layout.bottomMargin: 10
        }

        TextField {
            id: newHostURL
            placeholderText: qsTr("URL")
            Layout.alignment: Qt.AlignHCenter
            Layout.minimumWidth: 300
        }

        CheckBox {
            id: newHostEnabled
            Layout.alignment: Qt.AlignHCenter
            Layout.minimumWidth: 300
            checked: true
            text: "enabled"
        }

        GridLayout {
            Layout.minimumWidth: 300
            Layout.alignment: Qt.AlignHCenter
            id: addHostGrid
            columns: 2

            Button {
                text: "Save"
                Layout.alignment: Qt.AlignHCenter
                Layout.minimumWidth: 150
                onClicked: {
                    con.add_host(newHostLabel.text, newHostURL.text,
                                 newHostEnabled.checked)
                    stackView.pop()
                }
            }
            Button {
                text: "Cancel"
                Layout.alignment: Qt.AlignHCenter
                Layout.minimumWidth: 150
                onClicked: stackView.pop()
            }
        }
    }
}

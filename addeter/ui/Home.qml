import QtQuick 2.14
import QtQuick.Layouts 1.14
import QtQuick.Controls 2.14
import QtQuick.Window 2.14
import QtQuick.Controls.Universal 2.14

GridLayout {
    id: mainGrid
    columns: 3
    flow: width > height ? GridLayout.LeftToRight : GridLayout.TopToBottom
    property StackView view

    ColumnLayout {
        spacing: 0
        Layout.minimumWidth: 300
        Layout.alignment: Qt.AlignTop
        Layout.topMargin: 25

        Button {
            id: update_button
            text: "Update hosts file"
            Layout.alignment: Qt.AlignHCenter
            Layout.minimumWidth: 250
            Layout.bottomMargin: 10
            onClicked: password_dialog_update.visible = true
        }
        Button {
            id: reset_button
            text: "Reset hosts file"
            Layout.alignment: Qt.AlignHCenter
            Layout.minimumWidth: 250
            Layout.bottomMargin: 10
            onClicked: password_dialog_reset.visible = true
        }
        Button {
            text: "Add Host"
            Layout.alignment: Qt.AlignHCenter
            Layout.minimumWidth: 250
            onClicked: stackView.push(addHost)
        }
        Dialog {
            id: password_dialog_update
            visible: false
            title: "Password"
            modal: true
            anchors.centerIn: Overlay.overlay

            contentItem: ColumnLayout {
                Layout.minimumWidth: 300
                Layout.alignment: Qt.AlignHCenter

                Text {
                    text: "To edit the hosts file on your system, your password is needed to acquire sudo rights."
                    Layout.maximumWidth: 300
                    Layout.minimumHeight: 80
                    wrapMode: Text.WordWrap
                }

                TextField {
                    id: password_dialog_update_text
                    placeholderText: qsTr("Password")
                    Layout.alignment: Qt.AlignHCenter
                    Layout.minimumWidth: 300
                    echoMode: TextInput.Password
                }

                GridLayout {
                    Layout.minimumWidth: 300
                    Layout.alignment: Qt.AlignHCenter
                    columns: 2

                    Button {
                        id: password_dialog_update_start
                        text: "Start update"
                        Layout.alignment: Qt.AlignHCenter
                        Layout.minimumWidth: 150
                        onClicked: {
                            con.update_hosts(password_dialog_update_text.text)
                            password_dialog_update.visible = false
                        }
                        BusyIndicator {
                            height: 48
                            running: password_dialog_update_start.pressed
                        }
                    }
                    Button {
                        text: "Cancel"
                        Layout.alignment: Qt.AlignHCenter
                        Layout.minimumWidth: 150
                        onClicked: password_dialog_update.visible = false
                    }
                }
            }
        }

        Dialog {
            id: password_dialog_reset
            visible: false
            title: "Password"
            modal: true
            anchors.centerIn: Overlay.overlay

            contentItem: ColumnLayout {
                Layout.minimumWidth: 300
                Layout.alignment: Qt.AlignHCenter

                Text {
                    text: "To edit the hosts file on your system, your password is needed to acquire sudo rights."
                    Layout.maximumWidth: 300
                    Layout.minimumHeight: 80
                    wrapMode: Text.WordWrap
                }

                TextField {
                    id: password_dialog_reset_text
                    placeholderText: qsTr("Password")
                    Layout.alignment: Qt.AlignHCenter
                    Layout.minimumWidth: 300
                    echoMode: TextInput.Password
                }

                GridLayout {
                    Layout.minimumWidth: 300
                    Layout.alignment: Qt.AlignHCenter
                    columns: 2

                    Button {
                        id: password_dialog_reset_start
                        text: "Start reset"
                        Layout.alignment: Qt.AlignHCenter
                        Layout.minimumWidth: 150
                        onClicked: {
                            con.reset_hosts(password_dialog_reset_text.text)
                            password_dialog_reset.visible = false
                        }
                        BusyIndicator {
                            height: 48
                            running: password_dialog_reset_start.pressed
                        }
                    }
                    Button {
                        text: "Cancel"
                        Layout.alignment: Qt.AlignHCenter
                        Layout.minimumWidth: 150
                        onClicked: password_dialog_reset.visible = false
                    }
                }
            }
        }
    }

    ColumnLayout {
        id: rightcolumn
        spacing: 2
        Layout.columnSpan: 1
        Layout.minimumWidth: 300
        Layout.fillWidth: true
        Layout.alignment: Qt.AlignTop
        Layout.topMargin: 25

        ListView {
            id: listView
            Layout.alignment: Qt.AlignLeft
            clip: true
            Layout.minimumWidth: 300
            Layout.fillHeight: true
            Layout.leftMargin: 20
            flickableDirection: Flickable.VerticalFlick
            boundsBehavior: Flickable.StopAtBounds

            model: con.model
            delegate: RowLayout {

                Switch {
                    text: hostLabel
                    checked: hostEnabled
                    onToggled: con.toggle_host(hostURL, checked)
                }

                Button {
                    icon.name: "delete"
                    icon.source: "resources/icons/trash-alt.svg"
                    Layout.maximumWidth: 40
                    onClicked: con.remove_host(hostURL)
                }
            }

            ScrollBar.vertical: ScrollBar {}
        }
    }
}

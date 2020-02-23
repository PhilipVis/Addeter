import os
import sys

from PySide2.QtCore import QUrl
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine

from bridge import Bridge
from ui.style_rc import *

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Instance of the Python object
    bridge = Bridge()

    # Expose the Python object to QML
    context = engine.rootContext()
    context.setContextProperty("con", bridge)

    application_path = (
        sys._MEIPASS
        if getattr(sys, "frozen", False)
        else os.path.dirname(os.path.abspath(__file__))
    )

    file = os.path.join(application_path, "ui/Main.qml")
    engine.load(QUrl.fromLocalFile(file))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())

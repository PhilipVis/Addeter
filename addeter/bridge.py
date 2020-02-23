import subprocess

from PySide2.QtCore import QObject, Signal, Property, Slot, QAbstractListModel, Qt, QModelIndex

import hosts
from config.config import Config


class Bridge(QObject):
    modelChanged = Signal()

    def __init__(self, parent=None):
        super(Bridge, self).__init__(parent)
        self._model = HostsListModel()
        self.config = Config()
        self.add_hosts_to_model()

    # Expose model as a property of our backend
    @Property(QObject, constant=False, notify=modelChanged)
    def model(self):
        return self._model

    def add_hosts_to_model(self):
        self.config.get_host_urls()
        for url in self.config.get_host_urls():
            self._model.append_row(url, self.config.get_label_for_host(url), self.config.is_host_enabled(url))

    @Slot(str, str, bool)
    def add_host(self, url, label, enabled):
        self.config.add_host(url, label)
        self.config.enable_host(url)
        self._model.append_row(url, label, enabled)

    @Slot(str, bool)
    def toggle_host(self, url, enabled):
        if enabled:
            self.config.enable_host(url)
        else:
            self.config.disable_host(url)

    @Slot(str)
    def remove_host(self, url):
        self._model.remove_row(url)
        self.config.remove_host(url)

    @Slot(str)
    def update_hosts(self, password):
        cmd1 = subprocess.Popen(['echo', password], stdout=subprocess.PIPE)
        # task = subprocess.Popen(['sudo','-S'] + command, shell=True, stdin=cmd1.stdout,  stdout=subprocess.PIPE)
        # subprocess.run(['sudo','-S', 'python', os.path.dirname(os.path.realpath(__file__)) + '/hosts/hosts.py', 'test'], stdin=cmd1.stdout)
        hosts.update_hosts_file(self.config.get_host_urls(), password)

    @Slot(str)
    def reset_hosts(self, password):
        hosts.reset_hosts_file(password)


class HostsListModel(QAbstractListModel):
    label_role = Qt.UserRole + 1000
    checked_role = Qt.UserRole + 1001
    url_role = Qt.UserRole + 1002

    def __init__(self, parent=None):
        super(HostsListModel, self).__init__(parent)
        self._assets = []

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return 0
        return len(self._assets)

    def data(self, index, role=Qt.DisplayRole):

        if 0 <= index.row() < self.rowCount() and index.isValid():
            item = self._assets[index.row()]

            if role == HostsListModel.label_role:
                return item['hostLabel']

            elif role == HostsListModel.checked_role:
                return item['hostEnabled']

            elif role == HostsListModel.url_role:
                return item['hostURL']

    def roleNames(self):
        roles = dict()
        roles[HostsListModel.label_role] = b'hostLabel'
        roles[HostsListModel.checked_role] = b'hostEnabled'
        roles[HostsListModel.url_role] = b'hostURL'
        return roles

    def append_row(self, url, name, ischecked):
        self.beginInsertRows(QModelIndex(), self.rowCount(),
                             self.rowCount())
        self._assets.append({'hostURL': url, 'hostLabel': name, 'hostEnabled': ischecked})
        self.endInsertRows()

    def remove_row(self, url):
        for row in range(0, len(self._assets)):
            if self._assets[row]['hostURL'] == url:
                self.beginRemoveRows(QModelIndex(), row, row)
                self._assets.pop(row)
                self.endRemoveRows()
                break

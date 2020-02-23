from distutils import util
import os
import configparser
from pathlib import Path

from appdirs import AppDirs


class Config():
    CONFIG_DIR_NAME = "Addeter"
    CONFIG_FILE_NAME = "hosts.ini"
    LABEL_KEY = "label"
    ENABLED_KEY = "enabled"

    def __init__(self):
        self.hosts_config_file = os.path.join(AppDirs(self.CONFIG_DIR_NAME).user_config_dir, self.CONFIG_FILE_NAME)
        self.config = configparser.ConfigParser()

        if not os.path.isfile(self.hosts_config_file):
            self.create_hosts_config()
        else:
            self.hosts = self.load_hosts_from_config()

    def create_hosts_config(self):
        if not os.path.isdir(os.path.dirname(self.hosts_config_file)):
            Path(os.path.dirname(self.hosts_config_file)).mkdir(parents=True, exist_ok=True)
        self.config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), self.CONFIG_FILE_NAME))
        self.save_hosts_to_config()

    def load_hosts_from_config(self):
        self.config.read(self.hosts_config_file)

    def save_hosts_to_config(self):
        config_file = open(self.hosts_config_file, "w+")
        self.config.write(config_file)

    def get_host_urls(self):
        return self.config.sections()

    def get_enabled_host_urls(self):
        enabled_hosts = list()

        for host_url in self.config.sections():
            if (self.is_host_enabled(host_url)):
                enabled_hosts.append(host_url)

        return enabled_hosts

    def get_label_for_host(self, url):
        return self.config.get(url, self.LABEL_KEY)

    def is_host_enabled(self, url):
        return bool(util.strtobool(self.config.get(url, self.ENABLED_KEY)))

    def add_host(self, url, label):
        self.config.add_section(url)
        self.config.set(url, self.LABEL_KEY, label)
        self.enable_host(url)
        self.save_hosts_to_config()

    def remove_host(self, url):
        self.config.remove_section(url)
        self.save_hosts_to_config()

    def disable_host(self, url):
        self.config.set(url, self.ENABLED_KEY, "false")
        self.save_hosts_to_config()

    def enable_host(self, url):
        self.config.set(url, self.ENABLED_KEY, "true")
        self.save_hosts_to_config()

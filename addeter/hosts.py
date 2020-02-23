import io
import subprocess
import tempfile

import requests
from orderedset._orderedset import OrderedSet

ADDETER_START = "##### ADDETER START #####"
ADDETER_END = "##### ADDETER END #####"
HOSTS_PATH = "/etc/hosts"


def update_hosts_file(hosts_urls, password):
    update_hosts_set = OrderedSet()

    reset_hosts_file(password)
    hosts_file_text = read_hosts_file(password)
    for line in hosts_file_text.splitlines():
        update_hosts_set.add(line + "\n")

    update_hosts_set.add(ADDETER_START + "\n")
    update_hosts_set.update(load_remote_hosts(hosts_urls))
    update_hosts_set.add(ADDETER_END + "\n")

    write_hosts_file(password, update_hosts_set)


def load_remote_hosts(hosts_urls):
    hosts_set = set()

    for host_url in hosts_urls:
        hosts_set.update(load_remote_host_file(host_url))

    return hosts_set


def load_remote_host_file(host_url):
    hosts_set = set()

    request = requests.get(host_url)
    for line in io.StringIO(request.text):
        hosts_set.add(line)

    return hosts_set


def reset_hosts_file(password):
    reset_hosts_set = OrderedSet()
    reading_addeter_lines = False

    hosts_file_text = read_hosts_file(password)

    if (ADDETER_START in hosts_file_text):

        for line in hosts_file_text.splitlines():
            if (reading_addeter_lines):
                if (line == ADDETER_END):
                    reading_addeter_lines = False
            elif (line == ADDETER_START):
                reading_addeter_lines = True
            else:
                reset_hosts_set.add(line + "\n")

        write_hosts_file(password, reset_hosts_set)


def read_hosts_file(password):
    cmd1 = subprocess.Popen(['echo', password], stdout=subprocess.PIPE, universal_newlines=True)
    p = subprocess.Popen(['sudo', '-S', 'cat', HOSTS_PATH], stdin=cmd1.stdout, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, universal_newlines=True)

    output, errors = p.communicate()

    return output


def write_hosts_file(password, hosts_set):
    temp_file = tempfile.NamedTemporaryFile()

    with open(temp_file.name, "w") as temp_file_write:
        for line in hosts_set:
            temp_file_write.write(line)

    cmd1 = subprocess.Popen(['echo', password], stdout=subprocess.PIPE, universal_newlines=True)
    subprocess.run(['sudo', '-S', 'cp', temp_file.name, HOSTS_PATH], stdin=cmd1.stdout)

    temp_file.close()

# Addeter
Addeter is Gui application that helps you use the hosts file to block ads and trackers.

Use Addeter to manage a list of host file URL's like [Dan Pollock's hosts](http://someonewhocares.org/hosts/) and 
[Steven Blacks unified hosts](https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts), and to 
easily update the hosts file on your system with these hosts files. 

# Why use the system's hosts file 

Most are more familiar with using a browser extension to block unwanted ads and trackers. 
Here is a short overview of the advantages and drawbacks of using the system's host file to block ads and trackers 
compared with browser extensions.

## Advantages of the systems host file

- It blocks ads and tracker for the whole operating system, not just the browser.
- Least resource heavy method to block ads and trackers, negligible impact on the system's performance.

## Drawbacks of the systems host file

- It is bypassed when using DNS over HTTPS or when connections are made directly to an IP address.
- Blocked ads might still be seen visually in the browser as empty content blocks, while browser extensions will 
usually be able to hide these. (This does help make you more aware of ads being blocked though)

# Installation/Usage

Addeter is provided as a single executable binary file for Linux. Download the latest release 
[here](https://github.com/PhilipVis/Addeter/releases) and execute it to start the application. 

# Tech used

Addeter is written in [Python 3](https://docs.python.org/3/). It uses 
[PySide2 and QtQuick/QML](https://doc.qt.io/qtforpython/contents.html) for the graphical user interface.


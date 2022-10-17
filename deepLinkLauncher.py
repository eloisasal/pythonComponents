#!/usr/bin/python

"""
How to install with Anaconda (windows):
    conda config --append channels conda-forge
    pip install pyqt6
How to install pip:
    sudo apt install python3-pip
Upgrading pip:
    python3 -m pip install --upgrade pip
How to install the missing libraries with pip:
    pip3 install PyQt6
How to run the beta program:
    python3 ./iOSDeepLinkLauncher.py
Author: Eloi Sasal Renom
"""

import sys, os
from PyQt6.QtWidgets import (QComboBox, QWidget, QMessageBox, QApplication, QGridLayout,
    QPushButton, QApplication)
from functools import partial

class Launcher(QWidget):
    debuggingSession = True
    isAutoSizeEnabled = False
    defaultiOS = True
    deeplinks = []
    deepLinkPrefix = ''
    positions = [(i, j) for i in range(6) for j in range(4)]

    def setDeeplinks(self, deepLinks):
        self.deeplinks = deepLinks

    def setDeepLinkPrefix(self, deepLinkPrefix):
        self.deepLinkPrefix = deepLinkPrefix

    def setAutoSize(self, enableAutoSize):
        self.isAutoSizeEnabled = enableAutoSize
        print("Hi")

    def setDefaultOS(self, defaultiOS):
        self.defaultiOS = defaultiOS

    def __init__(self, deepLinkPrefix='', deeplinks=[]):
        super().__init__()
        self.deepLinkPrefix = deepLinkPrefix
        self.deeplinks = deeplinks
        #self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        for position, name in zip(self.positions, self.deeplinks):

            if name == '':
                continue

            button = QPushButton(name)
            button.clicked.connect(partial(self.deeplinkGrid, name))
            grid.addWidget(button, *position)

        comboBox = QComboBox(self)
        comboBox.addItem("Windows")
        comboBox.addItem("mac")
        comboBox.addItem("featureX")
        comboBox.move(750, 750)
        grid.addWidget(comboBox, *(750,750))

        #comboBox.activated[str].connect(self.style_choice)

        self.setWindowTitle('DeepLink Launcher')
        self.show()

    """
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                    "Are you sure to quit?", QMessageBox.StandardButton.Yes |
                    QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
    """

    def deeplinkGrid(self, deeplink):
        print(deeplink)
        if deeplink is not None:
            if self.defaultiOS :
                #ios execute
                deeplinkSelected = 'xcrun simctl openurl booted "'+self.deepLinkPrefix+deeplink+'"'
                print("iOS: "+deeplinkSelected)
                if not self.debuggingSession:
                    os.system(deeplinkSelected)
            else:
                #Android execute
                deeplinkSelected = 'adb shell am start -a android.intent.action.VIEW -d "'+self.deepLinkPrefix+deeplink+'"'
                print("Android: "+deeplinkSelected)
                if not self.debuggingSession:
                    os.system(deeplinkSelected)
"""
#Running example, the deeplinks are in a matrix of 4x6 for now (in future upgrades will be dinamically)
def main():
    app = QApplication(sys.argv)
    ex = Launcher('', [ '', '', '', '',
                    '', '', '', '',
                    '', '', '', '',
                    '', '', '', '',
                    '', '', '', '',
                    '', '', '', ''])
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
"""
#Running example, the deeplinks are in a matrix of 4x6 for now (in future upgrades will be dinamically)
def main():
    app = QApplication(sys.argv)
    launcher = Launcher()
    launcher.setDeeplinks([ '.', 'WINDOWS/TESTING', '.', '.',
                    '.', '.', '.', 'WINDOWS/test',
                    '.', '.', '.', '.',
                    '.', '.', '.', '.',
                    '.', '.', '.', '.',
                    '.', '.', '.', '.'])
    launcher.setDeepLinkPrefix("WINDOWS")
    launcher.initUI()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
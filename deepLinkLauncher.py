#!/usr/bin/python

"""
How to install the missing libraries:
    python3 -m pip install --upgrade pip
    pip3 install PyQt6
How to run the beta program:
    python3 ./iOSDeepLinkLauncher.py
Author: Eloi Sasal Renom
"""

import sys, os
from PyQt6.QtWidgets import (QWidget, QMessageBox, QApplication, QGridLayout,
    QPushButton, QApplication)
from functools import partial

class Launcher(QWidget):
    isAutoSizeEnabled = False
    defaultiOS = True
    deeplinks = []
    deepLinkPrefix = ''
    positions = [(i, j) for i in range(6) for j in range(4)]

    def setAutoSize(self, enableAutoSize):
        self.isAutoSizeEnabled = enableAutoSize
    
    def setDeeplinkPrefix(self, deeplinkPrefix):
        self.deepLinkPrefix = deeplinkPrefix
    
    def setDefaultOS(self, defaultiOS):
        self.defaultiOS = defaultiOS
    
    def __init__(self, deepLinkPrefix, deeplinks):
        super().__init__()
        #self.deepLinkPrefix = deepLinkPrefix
        #self.deeplinks = deeplinks
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
        
        self.setWindowTitle('DeepLink Launcher')
        self.show()


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                    "Are you sure to quit?", QMessageBox.StandardButton.Yes |
                    QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def deeplinkGrid(self, deeplink):
        print(deeplink)
        if deeplink is not None:
            #ios execute
            deeplinkSelected = 'xcrun simctl openurl booted "'+deepLinkPrefix+deeplink+'"'
            print("iOS: "+deeplinkSelected)
            os.system(deeplinkSelected)
            #Android execute
            deeplinkSelected = 'adb shell am start -a android.intent.action.VIEW -d "'+deepLinkPrefix+deeplink+'"'
            print("Android: "+deeplinkSelected)
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

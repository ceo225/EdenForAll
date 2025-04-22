#This is a sample code for developing web application using pyqt5  for Eden Operating system(EdenBSD)
#Compilation is done using devel/nuitka(which i have tested and works great)

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        # Add here the URL of the web app you wish to create 
        self.browser.setUrl(QUrl('http://example.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

app = QApplication(sys.argv)
#Here goes the name of the App name
QApplication.setApplicationName('my web app')
window = MainWindow()
app.exec_()

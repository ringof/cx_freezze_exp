from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import QProcess
from PyQt5 import QtGui
import sys

class embeddedTerminal(QMainWindow):
    def __init__(self, MainWindow):
        super().__init__()
        # set the title
        MainWindow.setWindowTitle("V-TOOLS v0.1 ALPHA")
        # setting  the geometry of window
        MainWindow.setGeometry(0, 0, 400, 300)
        self._processes = []
        self.terminal = QWidget(MainWindow)
        layout = QVBoxLayout()
        layout.addWidget(self.terminal)
        self._start_process(
            'xterm',
            ['-into', str(int(self.terminal.winId())),
             '-e', 'tmux', 'new', '-s', 'my_session']
        )
        button = QPushButton('List files')
        layout.addWidget(button)
        self.setCentralWidget(self.terminal)
        button.clicked.connect(self._list_files)
        #self.terminal.show()

    def _start_process(self, prog, args):
        child = QProcess()
        self._processes.append(child)
        child.start(prog, args)

    def _list_files(self):
        self._start_process(
            'tmux', ['send-keys', '-t', 'my_session:0', 'ls', 'Enter'])


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('hat.ico'))
        # set the title
        self.setWindowTitle("V-TOOLS v0.1 ALPHA")
  
        # setting  the geometry of window
        self.setGeometry(0, 0, 400, 300)
  
        introBox = QHBoxLayout()
        introLabel = QLabel("V-Tools:\n ALPHA - Do not use for production")
        introLabel.setStyleSheet("QLabel {background-color: red;}")
        introLabel.setFixedHeight(40)
        introBox.addWidget(introLabel)

        labelBox = QHBoxLayout()
        # creating a label widget
        headerLabel = QLabel("Connect to the ICE CREAM")
        #headerLabel.setStyleSheet("QLabel {background-color: red;}")
        headerLabel.setAlignment(QtCore.Qt.AlignCenter)
        labelBox.addWidget(headerLabel)
        
        buttonBox = QHBoxLayout()
        btn1 = QPushButton("Status Checker")
        btn2 = QPushButton("Stick Checker")
        btn3 = QPushButton("Brickbats Checker")
        buttonBox.addWidget(btn1)
        buttonBox.addWidget(btn2)
        buttonBox.addWidget(btn3)

        #buttonWidget = QWidget()
        #buttonWidget.setLayout(buttonBox)

        coreWidget = QWidget()
        coreBox = QVBoxLayout()
        coreBox.addLayout(introBox)
        coreBox.addLayout(labelBox)
        coreBox.addLayout(buttonBox)
        coreWidget.setLayout(coreBox)
        self.setCentralWidget(coreWidget)

        btn1.clicked.connect(self.btn_runscript)
        btn2.clicked.connect(self.btn_runterminal)
        # show all the widgets
        self.show()

    def btn_runscript(self):
        folderpath = QFileDialog.getExistingDirectory(None, 'Select Folder to Save Files')
        print (folderpath)
        return folderpath

    def btn_runterminal(self):
        self.window = QMainWindow()
        self.ui = embeddedTerminal(self.window)
        self.window.show()

def main():
    app = QApplication(sys.argv)
    window = Window() 
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(425, 459)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.player1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.player1.setFont(font)
        self.player1.setText("")
        self.player1.setAlignment(QtCore.Qt.AlignCenter)
        self.player1.setObjectName("player1")
        self.verticalLayout.addWidget(self.player1)
        self.gameBoard = TictactoeWidget(self.centralwidget)
        self.gameBoard.setEnabled(False)
        self.gameBoard.setObjectName("gameBoard")
        self.verticalLayout.addWidget(self.gameBoard)
        self.player2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.player2.setFont(font)
        self.player2.setText("")
        self.player2.setAlignment(QtCore.Qt.AlignCenter)
        self.player2.setObjectName("player2")
        self.verticalLayout.addWidget(self.player2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 425, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew_Game = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newgame.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Game.setIcon(icon)
        self.actionNew_Game.setObjectName("actionNew_Game")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/application-exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon1)
        self.actionQuit.setObjectName("actionQuit")
        self.menu.addAction(self.actionNew_Game)
        self.menu.addSeparator()
        self.menu.addAction(self.actionQuit)
        self.menubar.addAction(self.menu.menuAction())
        self.toolBar.addAction(self.actionNew_Game)
        self.toolBar.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TicTacToe"))
        self.menu.setTitle(_translate("MainWindow", "&Файл"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew_Game.setText(_translate("MainWindow", "New Game"))
        self.actionNew_Game.setToolTip(_translate("MainWindow", "Начать новую игру"))
        self.actionNew_Game.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setToolTip(_translate("MainWindow", "Выйти из программы"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))

from TicTacToeWidget import TictactoeWidget
import res.resources_rc

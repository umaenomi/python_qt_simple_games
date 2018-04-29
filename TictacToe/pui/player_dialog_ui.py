# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(246, 93)
        Dialog.setMinimumSize(QtCore.QSize(246, 93))
        Dialog.setMaximumSize(QtCore.QSize(246, 93))
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.player1_name = QtWidgets.QLineEdit(Dialog)
        self.player1_name.setObjectName("player1_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.player1_name)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.player2_name = QtWidgets.QLineEdit(Dialog)
        self.player2_name.setObjectName("player2_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.player2_name)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.label.setBuddy(self.player1_name)
        self.label_2.setBuddy(self.player2_name)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.player1_name.textChanged['QString'].connect(Dialog.update_ok_button_state)
        self.player2_name.textChanged['QString'].connect(Dialog.update_ok_button_state)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Имена игроков"))
        self.label.setText(_translate("Dialog", "Имя игрока &1"))
        self.label_2.setText(_translate("Dialog", "Имя игрока &2"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../defaultVars.ui'
#
# Created: Mon Aug 17 16:20:06 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_addDefaultVar(object):
    def setupUi(self, addDefaultVar):
        addDefaultVar.setObjectName("addDefaultVar")
        addDefaultVar.resize(402, 417)
        self.groupBox = QtGui.QGroupBox(addDefaultVar)
        self.groupBox.setGeometry(QtCore.QRect(20, 230, 361, 141))
        self.groupBox.setObjectName("groupBox")
        self.variableTable = QtGui.QTableWidget(self.groupBox)
        self.variableTable.setGeometry(QtCore.QRect(4, 15, 351, 121))
        self.variableTable.setObjectName("variableTable")
        self.variableTable.setColumnCount(1)
        self.variableTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.variableTable.setHorizontalHeaderItem(0, item)
        self.variableTable.horizontalHeader().setVisible(False)
        self.variableTable.horizontalHeader().setCascadingSectionResizes(False)
        self.variableTable.horizontalHeader().setHighlightSections(False)
        self.variableTable.horizontalHeader().setMinimumSectionSize(100)
        self.variableTable.horizontalHeader().setStretchLastSection(True)
        self.variableTable.verticalHeader().setMinimumSectionSize(15)
        self.groupBox_2 = QtGui.QGroupBox(addDefaultVar)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 67, 361, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.otherVariablesTable = QtGui.QTableWidget(self.groupBox_2)
        self.otherVariablesTable.setGeometry(QtCore.QRect(4, 15, 351, 141))
        self.otherVariablesTable.setObjectName("otherVariablesTable")
        self.otherVariablesTable.setColumnCount(1)
        self.otherVariablesTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.otherVariablesTable.setHorizontalHeaderItem(0, item)
        self.otherVariablesTable.horizontalHeader().setVisible(False)
        self.otherVariablesTable.horizontalHeader().setMinimumSectionSize(100)
        self.otherVariablesTable.horizontalHeader().setStretchLastSection(True)
        self.otherVariablesTable.verticalHeader().setMinimumSectionSize(15)
        self.groupBox_3 = QtGui.QGroupBox(addDefaultVar)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 10, 361, 51))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(6, 0, 371, 51))
        self.label.setObjectName("label")
        self.addVariable = QtGui.QLineEdit(addDefaultVar)
        self.addVariable.setGeometry(QtCore.QRect(20, 380, 113, 21))
        self.addVariable.setObjectName("addVariable")
        self.addVariableButton = QtGui.QPushButton(addDefaultVar)
        self.addVariableButton.setGeometry(QtCore.QRect(140, 379, 241, 25))
        self.addVariableButton.setObjectName("addVariableButton")

        self.retranslateUi(addDefaultVar)
        QtCore.QMetaObject.connectSlotsByName(addDefaultVar)

    def retranslateUi(self, addDefaultVar):
        addDefaultVar.setWindowTitle(QtGui.QApplication.translate("addDefaultVar", "Edit default variables", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("addDefaultVar", "Current Default Variable", None, QtGui.QApplication.UnicodeUTF8))
        self.variableTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("addDefaultVar", "Varaibles", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("addDefaultVar", "Other Variables in this model", None, QtGui.QApplication.UnicodeUTF8))
        self.otherVariablesTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("addDefaultVar", "Other Variables", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("addDefaultVar", "Add and remove variables to the default collect list by \n"
" typing in the bottom line. Added variables do not have to \n"
" be in the top box.", None, QtGui.QApplication.UnicodeUTF8))
        self.addVariableButton.setText(QtGui.QApplication.translate("addDefaultVar", "Add Variable", None, QtGui.QApplication.UnicodeUTF8))

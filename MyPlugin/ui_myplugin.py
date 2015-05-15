# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_myplugin.ui'
#
# Created: Fri May 16 11:49:46 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MyPlugin(object):
    def setupUi(self, MyPlugin):
        MyPlugin.setObjectName(_fromUtf8("MyPlugin"))
        MyPlugin.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(MyPlugin)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(MyPlugin)
        self.label.setGeometry(QtCore.QRect(120, 80, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(MyPlugin)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), MyPlugin.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MyPlugin.reject)
        QtCore.QMetaObject.connectSlotsByName(MyPlugin)

    def retranslateUi(self, MyPlugin):
        MyPlugin.setWindowTitle(QtGui.QApplication.translate("MyPlugin", "MyPlugin", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MyPlugin", "Geospatial Python Rocks!", None, QtGui.QApplication.UnicodeUTF8))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myplugin_dialog_base.ui'
#
# Created: Fri May 15 12:14:20 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MyPluginDialogBase(object):
    def setupUi(self, MyPluginDialogBase):
        MyPluginDialogBase.setObjectName(_fromUtf8("MyPluginDialogBase"))
        MyPluginDialogBase.resize(400, 300)
        self.button_box = QtGui.QDialogButtonBox(MyPluginDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.label = QtGui.QLabel(MyPluginDialogBase)
        self.label.setGeometry(QtCore.QRect(120, 80, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(MyPluginDialogBase)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), MyPluginDialogBase.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), MyPluginDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(MyPluginDialogBase)

    def retranslateUi(self, MyPluginDialogBase):
        MyPluginDialogBase.setWindowTitle(_translate("MyPluginDialogBase", "My Plugin", None))
        self.label.setText(_translate("MyPluginDialogBase", "Ziaaaaa!", None))


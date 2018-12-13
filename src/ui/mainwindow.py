# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TCPCounter(object):
    def setupUi(self, TCPCounter):
        TCPCounter.setObjectName("TCPCounter")
        TCPCounter.resize(800, 600)
        TCPCounter.setMinimumSize(QtCore.QSize(800, 600))
        TCPCounter.setMaximumSize(QtCore.QSize(800, 600))
        self.tcplist = QtWidgets.QTableWidget(TCPCounter)
        self.tcplist.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.tcplist.setMinimumSize(QtCore.QSize(800, 500))
        self.tcplist.setMaximumSize(QtCore.QSize(800, 500))
        self.tcplist.setRowCount(0)
        self.tcplist.setColumnCount(6)
        self.tcplist.setObjectName("tcplist")
        item = QtWidgets.QTableWidgetItem()
        self.tcplist.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tcplist.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tcplist.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tcplist.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tcplist.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tcplist.setHorizontalHeaderItem(5, item)
        self.tcplist.horizontalHeader().setDefaultSectionSize(150)
        self.tcplist.horizontalHeader().setMinimumSectionSize(100)

        self.retranslateUi(TCPCounter)
        QtCore.QMetaObject.connectSlotsByName(TCPCounter)

    def retranslateUi(self, TCPCounter):
        _translate = QtCore.QCoreApplication.translate
        TCPCounter.setWindowTitle(_translate("TCPCounter", "Form"))
        item = self.tcplist.horizontalHeaderItem(0)
        item.setText(_translate("TCPCounter", "pid"))
        item = self.tcplist.horizontalHeaderItem(1)
        item.setText(_translate("TCPCounter", "local_address"))
        item = self.tcplist.horizontalHeaderItem(2)
        item.setText(_translate("TCPCounter", "local_port"))
        item = self.tcplist.horizontalHeaderItem(3)
        item.setText(_translate("TCPCounter", "remote_address"))
        item = self.tcplist.horizontalHeaderItem(4)
        item.setText(_translate("TCPCounter", "remote_port"))
        item = self.tcplist.horizontalHeaderItem(5)
        item.setText(_translate("TCPCounter", "status"))


import sys
import psutil
import time
import net.connect_data_decoder as cdd
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtWidgets, QtCore
from ui.mainwindow import Ui_TCPCounter

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TCPCounter()
        self.ui.setupUi(self)
        self.show()

    def startSessoinListen(self):
        connects = psutil.net_connections()
        sessionLen=len(connects)
        self.ui.tcplist.setRowCount(0)
        self.ui.sessionNum.setText(str(sessionLen))
        for row_number, connect in enumerate(connects):
            self.ui.tcplist.insertRow(row_number)
            self.ui.tcplist.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(cdd.get_pid(connect))))
            self.ui.tcplist.setItem(row_number, 1, QtWidgets.QTableWidgetItem(cdd.get_local_address(connect)))
            self.ui.tcplist.setItem(row_number, 2, QtWidgets.QTableWidgetItem(cdd.get_local_port(connect)))
            self.ui.tcplist.setItem(row_number, 3, QtWidgets.QTableWidgetItem(cdd.get_remote_address(connect)))
            self.ui.tcplist.setItem(row_number, 4, QtWidgets.QTableWidgetItem(cdd.get_remote_port(connect)))
            self.ui.tcplist.setItem(row_number, 5, QtWidgets.QTableWidgetItem(cdd.get_status(connect)))

app = QApplication(sys.argv)
w = AppWindow()
timer = QtCore.QTimer(w)
timer.timeout.connect(lambda: w.startSessoinListen())
timer.start(1000)
w.show()
sys.exit(app.exec_())

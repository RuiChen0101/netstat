import sys
import psutil
import time
import net.connect_data_decoder as cdd
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtWidgets
from ui.mainwindow import Ui_TCPCounter

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TCPCounter()
        self.ui.setupUi(self)
        self.show()
        connects = psutil.net_connections()
        for row_number, connect in enumerate(connects):
            self.ui.tcplist.insertRow(row_number)
            self.ui.tcplist.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(cdd.get_pid(connect))))
            self.ui.tcplist.setItem(row_number, 1, QtWidgets.QTableWidgetItem(cdd.get_local_address(connect)))
            self.ui.tcplist.setItem(row_number, 2, QtWidgets.QTableWidgetItem(cdd.get_local_port(connect)))
            self.ui.tcplist.setItem(row_number, 3, QtWidgets.QTableWidgetItem(cdd.get_remote_address(connect)))
            self.ui.tcplist.setItem(row_number, 4, QtWidgets.QTableWidgetItem(cdd.get_remote_port(connect)))
            self.ui.tcplist.setItem(row_number, 5, QtWidgets.QTableWidgetItem(cdd.get_status(connect)))

    def start_list(self):
        connects = psutil.net_connections()
        for row_number, connect in enumerate(connects):
            self.ui.tcplist.insertRow(row_number)
            self.ui.tcplist.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(cdd.get_pid(connect))))
            self.ui.tcplist.setItem(row_number, 1, QtWidgets.QTableWidgetItem(cdd.get_local_address(connect)))
            self.ui.tcplist.setItem(row_number, 2, QtWidgets.QTableWidgetItem(cdd.get_local_port(connect)))
            self.ui.tcplist.setItem(row_number, 3, QtWidgets.QTableWidgetItem(cdd.get_remote_address(connect)))
            self.ui.tcplist.setItem(row_number, 4, QtWidgets.QTableWidgetItem(cdd.get_remote_port(connect)))
            self.ui.tcplist.setItem(row_number, 5, QtWidgets.QTableWidgetItem(cdd.get_status(connect)))
        # self.ui.tcplist.clear()

app = QApplication(sys.argv)
w = AppWindow()
w.show()
time.sleep(1)
# w.start_list()
sys.exit(app.exec_())

from PyQt6.QtWidgets import QMessageBox
from retail_project.connectors.employee_connector import EmployeeConnector
from retail_project.uis.LoginMainWindow import Ui_MainWindow


class LoginMainWindowEX(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.process_login)  # Sửa click -> clicked

    def process_login(self):
        email = self.lineEditEmail.text()
        password = self.lineEditPassword.text()

        ec = EmployeeConnector()
        ec.connect()
        em = ec.login(email, password)

        msg = QMessageBox()
        if em is None:
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Login Failed, please try again")
            msg.setWindowTitle("Login Failed")
        else:
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("Login Success!")
            msg.setWindowTitle("Login Successful")

        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

        ec.disconnect()  # Nếu connector có hàm này

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
from admin_panel import AdminPanel
from delivery_panel import DeliveryPanel
from user_panel import UserPanel

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("KFC Uzbekistan")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        admin_button = QPushButton("Официант / Администратор", self)
        admin_button.clicked.connect(self.open_admin_panel)
        layout.addWidget(admin_button)

        delivery_button = QPushButton("Курьер", self)
        delivery_button.clicked.connect(self.open_delivery_panel)
        layout.addWidget(delivery_button)

        user_button = QPushButton("Пользователь", self)
        user_button.clicked.connect(self.open_user_panel)
        layout.addWidget(user_button)

    def open_admin_panel(self):
        self.admin_panel = AdminPanel()
        self.admin_panel.show()

    def open_delivery_panel(self):
        self.delivery_panel = DeliveryPanel()
        self.delivery_panel.show()

    def open_user_panel(self):
        self.user_panel = UserPanel()
        self.user_panel.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())

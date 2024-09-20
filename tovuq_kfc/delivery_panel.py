from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QMessageBox
import data  


class DeliveryPanel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Курьер")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.orders_label = QLabel("Назначенные заказы:")
        layout.addWidget(self.orders_label)

        update_button = QPushButton("Обновить заказы", self)
        update_button.clicked.connect(self.update_orders)
        layout.addWidget(update_button)

        complete_button = QPushButton("Отметить доставку заказа", self)
        complete_button.clicked.connect(self.complete_order)
        layout.addWidget(complete_button)

    def update_orders(self):
        orders = data.get_orders() 
        orders_text = "\n".join([f"Заказ {order[0]}: {order[1]}, сумма: {order[3]} UZS, адрес: {order[4]}" for order in orders])
        self.orders_label.setText(orders_text)

    def complete_order(self):
        QMessageBox.information(self, "Заказ доставлен", "Заказ был успешно доставлен.")


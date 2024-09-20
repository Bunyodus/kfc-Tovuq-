from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QSpinBox, QLineEdit, QMessageBox
import data  

class UserPanel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пользователь")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.total_price = 0

        self.address_input = QLineEdit(self)
        self.address_input.setPlaceholderText("Введите адрес доставки")
        layout.addWidget(self.address_input)

        self.promo_input = QLineEdit(self)
        self.promo_input.setPlaceholderText("Введите промокод")
        layout.addWidget(self.promo_input)

        self.menu_label = QLabel("Меню:")
        layout.addWidget(self.menu_label)

        self.dishes = [
            {"name": "Баскет Дуэт", "price": 25000},
            {"name": "Чизбургер", "price": 18000},
            {"name": "Криспи Стрипсы", "price": 15000},
            {"name": "Куриные крылышки", "price": 20000},
        ]

        self.quantity_inputs = []
        for dish in self.dishes:
            dish_name = QLabel(dish["name"], self)
            dish_price = QLabel(f'{dish["price"]} UZS', self)

            quantity = QSpinBox(self)
            quantity.setRange(0, 10)
            quantity.setValue(0)

            self.quantity_inputs.append(quantity)

            layout.addWidget(dish_name)
            layout.addWidget(dish_price)
            layout.addWidget(quantity)

        self.calculate_button = QPushButton("Рассчитать стоимость", self)
        self.calculate_button.clicked.connect(self.calculate_total)
        layout.addWidget(self.calculate_button)

        self.total_label = QLabel("Общая стоимость: 0 UZS", self)
        layout.addWidget(self.total_label)

        self.order_button = QPushButton("Оформить заказ", self)
        self.order_button.clicked.connect(self.place_order)
        layout.addWidget(self.order_button)

    def calculate_total(self):
        self.total_price = 0
        for i, dish in enumerate(self.dishes):
            quantity = self.quantity_inputs[i].value()
            self.total_price += dish["price"] * quantity

        promo_code = self.promo_input.text()
        if promo_code == "KFC2024":
            self.total_price *= 0.9 

        self.total_label.setText(f"Общая стоимость: {self.total_price} UZS")

    def place_order(self):
        address = self.address_input.text()
        if not address:
            QMessageBox.warning(self, "Ошибка", "Введите ваш адрес для доставки!")
            return

        for i, dish in enumerate(self.dishes):
            quantity = self.quantity_inputs[i].value()
            if quantity > 0:
                data.add_order(dish["name"], quantity, dish["price"] * quantity, address)

        QMessageBox.information(self, "Заказ оформлен", f"Ваш заказ на сумму {self.total_price} UZS отправлен!")

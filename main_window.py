from PySide6.QtWidgets import QVBoxLayout, QWidget, QApplication, QLineEdit, QFormLayout, QPushButton, QTableWidget, QTableWidgetItem
import PySide6.QtCore
from data_accessor import DataAccessor
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Товары и категории магазина")
        self.setGeometry(150, 150, 800, 400)
        layout = QVBoxLayout()

        form_layout = QFormLayout()
        self.name_product = QLineEdit()
        self.price_product = QLineEdit()
        self.category_id_product = QLineEdit()
        self.product_id = QLineEdit()

        form_layout.addRow("Название товара: ", self.name_product)
        form_layout.addRow("Цена продукта: ", self.price_product)
        form_layout.addRow("Id Категории: ", self.category_id_product)
        form_layout.addRow("ID товара для удаления:", self.product_id)

        self.add_product = QPushButton("Добавить товар")
        self.add_product.clicked.connect(self.add_new_product)
        self.delete_product = QPushButton("Удалить товар")
        self.delete_product.clicked.connect(self.delete_new_product)

        self.product_table = QTableWidget(0, 4)
        self.product_table.setHorizontalHeaderLabels(["Id Товара", "Название товара", "Цена", "Id Категории"])

        layout.addLayout(form_layout)

        layout.addWidget(self.product_table)
        layout.addWidget(self.add_product)
        layout.addWidget(self.delete_product)

        self.setLayout(layout)

    def add_new_product(self):
        name = self.name_product.text()
        price = float(self.price_product.text())
        category_id = int(self.category_id_product.text())

        data_accessor = DataAccessor()
        data_accessor.insert_product(name, price, category_id)

        self.load_products()

    def delete_new_product(self):
        product_id = int(self.product_id.text())
        data_accessor = DataAccessor()
        data_accessor.delete_product(product_id)

        self.load_products()

    def load_products(self):
        data_accessor = DataAccessor()
        products = data_accessor.get_all_products()

        self.product_table.setRowCount(0)
        for row_index, row_data in enumerate(products):
            self.product_table.insertRow(row_index)
            for col_index, value in enumerate(row_data):
                self.product_table.setItem(row_index, col_index, QTableWidgetItem(str(value)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
        
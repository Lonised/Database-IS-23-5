import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QComboBox
from data_accessor import DataAccessor

class CafeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.db = DataAccessor()
        self.init_ui()

    def init_ui(self):
    	layout = QVBoxLayout()
        
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Стол", "Блюдо", "Кол-во", "Время"])
        layout.addWidget(self.table)

  
        self.load_data()

        self.table_input = QLineEdit(self)
        self.item_select = QComboBox(self)
        self.quantity_input = QLineEdit(self)
        self.time_input = QLineEdit(self)

        layout.addWidget(QLabel("Номер стола:"))
        layout.addWidget(self.table_input)
        layout.addWidget(QLabel("Блюдо:"))
        layout.addWidget(self.item_select)
        layout.addWidget(QLabel("Количество:"))
        layout.addWidget(self.quantity_input)
        layout.addWidget(QLabel("Время заказа:"))
        layout.addWidget(self.time_input)
        
        self.load_menu()

        add_button = QPushButton("Добавить заказ")
        add_button.clicked.connect(self.add_order)
        layout.addWidget(add_button)

        del_button = QPushButton("Удалить заказ")
        del_button.clicked.connect(self.delete_order)
        layout.addWidget(del_button)

        self.setLayout(layout)
        self.setWindowTitle("Учёт заказов в кафе")
        self.resize(500, 400)

    def load_menu(self):
        self.item_select.clear()
        menu = self.db.get_menu_items()
        for item in menu:
            self.item_select.addItem(item[1], item[0]) 

    def delete_order(self):
        selected = self.table.currentRow()
        if selected >= 0:
            order_id = int(self.table.item(selected, 0).text())
            self.db.delete_order(order_id)
            self.load_data()

    def closeEvent(self, event):
        self.db.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CafeApp()
    window.show()
    sys.exit(app.exec())

 


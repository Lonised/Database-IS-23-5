import sys
import psycopg2
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QListView, QFormLayout,
    QLabel, QMessageBox
)
from PySide6.QtCore import QStringListModel


DB_PARAMS = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "2680",
    "host": "localhost",
    "port": "5432"
}


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Список заказов")
        self.resize(600, 400)

        layout = QVBoxLayout(self)
        self.list_view = QListView()
        self.model = QStringListModel()
        self.list_view.setModel(self.model)

        self.details_layout = QFormLayout()
        self.table_label = QLabel()
        self.time_label = QLabel()
        self.price_label = QLabel()
        self.details_layout.addRow("Номер стола:", self.table_label)
        self.details_layout.addRow("Время заказа:", self.time_label)
        self.details_layout.addRow("Сумма заказа:", self.price_label)

        layout.addWidget(self.list_view)
        layout.addLayout(self.details_layout)

        self.load_data()
        self.list_view.clicked.connect(self.show_details)

    def load_data(self):
        try:
            conn = psycopg2.connect(**DB_PARAMS)
            cur = conn.cursor()
            cur.execute("""
                SELECT 
                    tables.table_number,
                    orders.order_time,
                    orders.total_price
                FROM tables
                JOIN orders ON orders.table_id = tables.id
            """)
            self.data = cur.fetchall()
            display_list = [
                f"Стол {row[0]} — {row[1]} | {row[2]} тг" for row in self.data
            ]
            self.model.setStringList(display_list)
            cur.close()
            conn.close()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка подключения", str(e))
            self.data = []

    def show_details(self, index):
        row = self.data[index.row()]
        self.table_label.setText(str(row[0]))
        self.time_label.setText(str(row[1]))
        self.price_label.setText(str(row[2]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())





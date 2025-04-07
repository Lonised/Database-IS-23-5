import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from db import get_connection

class CarApp(QWidget):
    def _init_(self):
        super()._init_()

        self.setWindowTitle("Поля выбора студентов")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        form_layout = QFormLayout()
        self.name_input = QLineEdit()
        self.subject = QLineEdit()
        form_layout.addRow("Имя студента:", self.name_input)
        form_layout.addRow("Название предмета:", self.subject_input)

        self.add_student_btn = QPushButton("Добавить студента")
        self.add_student_btn.clicked.connect(self.add_student)

        self.student_table = QTableWidget(0, 4)
        self.student_table.setHorizontalHeaderLabels(["ID", "Имя_студента", "Группа"])

        # Кнопки
        self.load_grades_btn = QPushButton("Обновить оценки студентов")
        self.load_grades_btn.clicked.connect(self.load_cars)

        layout.addLayout(form_layout)
        layout.addWidget(self.add_student_btn)
        layout.addWidget(self.grades_table)
        layout.addWidget(self.load_grades_btn)

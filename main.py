import sys
import os
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QMessageBox, QVBoxLayout, QStackedLayout, QLabel, QHBoxLayout, QTextEdit, QDialog, QSizePolicy # type: ignore
from PyQt6.QtGui import QFont, QPixmap, QIcon # type: ignore
from PyQt6.QtCore import Qt, QTimer # type: ignore


class Minesweeper(QMainWindow):
    def __init__(self, rows=10, cols=10, mines=10):
        super().__init__()
        self.setWindowTitle("САПЕР")
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.buttons = {}
        self.mine_field = [[0 for _ in range(cols)] for _ in range(rows)]
        self.game_over = False
        self.safe_cells_opened = 0
        self.time_elapsed = 0

        self.initUI()
        self.place_mines()

        # Настройка таймера
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # Обновление каждую секунду

        self.setWindowIcon(QIcon(r"C:\Users\silis\OneDrive\Desktop\prog\mines\149.jpg"))
        self.setFixedSize(self.sizeHint())

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Основной макет
        self.layout = QVBoxLayout(central_widget)

        # Информационная панель
        self.info_panel = QHBoxLayout()

        # Метка времени
        self.timer_label = QLabel("Время: 0 s")
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info_panel.addWidget(self.timer_label)

        # Метка очков
        self.score_label = QLabel("Очки: 0")
        self.score_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info_panel.addWidget(self.score_label)

        # Добавляем информационную панель в основной макет
        self.layout.addLayout(self.info_panel)

        # Сетка для кнопок
        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)

        # Добавление кнопок в сетку
        for row in range(self.rows):
            for col in range(self.cols):
                button = QPushButton("")
                button.setFixedSize(40, 40)
                button.clicked.connect(lambda checked, r=row, c=col: self.on_button_click(r, c))
            
            # Добавляем обработчик правого клика
                button.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
                button.customContextMenuRequested.connect(lambda event, r=row, c=col: self.on_right_click(event, r, c))

                self.buttons[(row, col)] = button
                self.grid_layout.addWidget(button, row, col)

    def update_timer(self):
        if not self.game_over:
            self.time_elapsed += 1
            self.timer_label.setText(f"Время: {self.time_elapsed} s")

    def update_score(self):
        score = self.safe_cells_opened
        self.score_label.setText(f"Очки: {score}")

    def place_mines(self):
        mine_positions = random.sample(range(self.rows * self.cols), self.mines)
        for pos in mine_positions:
            row, col = divmod(pos, self.cols)
            self.mine_field[row][col] = -1
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if 0 <= r < self.rows and 0 <= c < self.cols and self.mine_field[r][c] != -1:
                        self.mine_field[r][c] += 1

    def on_button_click(self, row, col):
        if self.game_over:
            return
        if self.mine_field[row][col] == -1:
            self.end_game(False)
        else:
            self.reveal_cells(row, col)
            if self.check_win():
                self.end_game(True)
                   
                
    def on_right_click(self, event, row, col):
        if self.game_over:
            return
        button = self.buttons[(row, col)]
        if button.text() == "":
            button.setText("🚩")
        elif button.text() == "🚩":
            button.setText("")

    def reveal_cells(self, row, col):
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return
        button = self.buttons[(row, col)]
        if button.isEnabled() and self.mine_field[row][col] >= 0:
            cell_value = self.mine_field[row][col]
            button.setText(str(cell_value) if cell_value > 0 else "")
            button.setStyleSheet(self.get_cell_color(cell_value))
            button.setEnabled(False)
            self.safe_cells_opened += 1
            self.update_score()
            if cell_value == 0:
                for r in range(row - 1, row + 2):
                    for c in range(col - 1, col + 2):
                        self.reveal_cells(r, c)

    def get_cell_color(self, value):
        colors = {
            1: "color: blue;",
            2: "color: green;",
            3: "color: red;",
            4: "color: purple;",
            5: "color: orange;",
        }
        return colors.get(value, "")

    def check_win(self):
        return self.safe_cells_opened == self.rows * self.cols - self.mines

    def end_game(self, won):
        self.game_over = True
        self.timer.stop()
        for row in range(self.rows):
            for col in range(self.cols):
                if self.mine_field[row][col] == -1:
                    self.buttons[(row, col)].setText("💣")
        score_message = f"Очки: {self.safe_cells_opened}"
        
        if won:
            self.show_message("Вы выиграли!", f"Вы нашли все безопасные клетки!")
        else:
            self.show_message("Игра окончена", f"Вы наткнулись на мину!")

    def show_message(self, title, message):
        from PyQt6.QtWidgets import QMessageBox
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()

    
    class Minesweeper(QMainWindow):
     def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Minesweeper")
        self.showFullScreen()  # Set the window to fullscreen

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.grid_layout = QGridLayout(self.central_widget)
        self.create_board(10, 10)  # Example: 10x10 grid

    def create_board(self, rows, cols):
        self.buttons = {}
        for row in range(rows):
            for col in range(cols):
                button = QPushButton('')
                button.setStyleSheet("""
                    QPushButton {
                        font-size: 14px;
                        border: 2px solid #CCCCCC;
                        border-radius: 5px;
                        background-color: #F0F0F0;
                        padding: 5px;
                    }
                    QPushButton:pressed {
                        background-color: #D0D0D0;
                    }
                """)
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                button.clicked.connect(lambda checked, r=row, c=col: self.on_cell_clicked(r, c))
                self.grid_layout.addWidget(button, row, col)
                self.buttons[(row, col)] = button

    def show_message(self, title, text):
        final_text = f"{text}\n\nОчки: {self.safe_cells_opened}\nВремя: {self.time_elapsed} секунд"
        
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setIcon(QMessageBox.Icon.NoIcon)
        msg.setWindowTitle(title)
        msg.setText(final_text)
        msg.setStyleSheet("font-size: 14px;")

        replay_button = msg.addButton("Играть снова", QMessageBox.ButtonRole.ActionRole)
        replay_button.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                font-weight: bold;
                color: #FFFFFF;
                background-color: #4CAF50;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #45A049;
            }
            QPushButton:pressed {
                background-color: #388E3C;
            }
""")

        menu_button = msg.addButton("Главное меню", QMessageBox.ButtonRole.RejectRole)
        menu_button.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                font-weight: bold;
                color: #FFFFFF;
                background-color: #F44336;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #E53935;
            }
            QPushButton:pressed {
                background-color: #D32F2F;
            }
""")

        msg.exec()

        if msg.clickedButton() == replay_button:
            self.restart_game()
        elif msg.clickedButton() == menu_button:
            self.return_to_main_menu()

    def return_to_main_menu(self):
        self.main_menu = MainMenu()
        self.main_menu.show()
        self.close()

    def restart_game(self):
        self.safe_cells_opened = 0
        self.game_over = False
        self.mine_field = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.place_mines()
        
        
        for row in range(self.rows):
            for col in range(self.cols):
                button = self.buttons[(row, col)]
                button.setText("")
                button.setEnabled(True)
        
    
    # Сбрасываем количество безопасных открытых клеток и статус игры
        self.safe_cells_opened = 0
        self.game_over = False

    # Сбрасываем таймер
        self.time_elapsed = 0
        self.timer_label.setText(f"Время: {self.time_elapsed} s")  # Обновляем отображение времени

    # Перезапускаем поле с минами
        self.mine_field = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.place_mines()

    # Обновляем кнопки (очищаем их и включаем)
        for row in range(self.rows):
            for col in range(self.cols):
                button = self.buttons[(row, col)]
                button.setText("")
                button.setEnabled(True)

    # Перезапускаем таймер
                self.timer.start(1000)  # Запускаем таймер снова

class DifficultyMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Выбор уровня сложности")
        self.setFixedSize(300, 250)  # Slightly taller for better spacing
        
        self.setWindowIcon(QIcon(r"C:\Users\silis\OneDrive\Desktop\prog\mines\149.jpg"))
        
        # Main layout
        layout = QVBoxLayout()
        
        # Title label
        label = QLabel("Выберите уровень сложности:")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the text
        label.setStyleSheet("font-size: 16px; font-weight: bold; color: #4CAF50;")
        layout.addWidget(label)
        
        # Easy button
        easy_button = QPushButton("Лёгкий уровень (5x5)")
        easy_button.setStyleSheet(self.button_style())
        easy_button.clicked.connect(lambda: self.start_game(5, 5, 5))
        layout.addWidget(easy_button)
        
        # Medium button
        medium_button = QPushButton("Средний уровень (9x9)")
        medium_button.setStyleSheet(self.button_style())
        medium_button.clicked.connect(lambda: self.start_game(9, 9, 10))
        layout.addWidget(medium_button)
        
        # Hard button
        hard_button = QPushButton("Тяжёлый уровень (12x12)")
        hard_button.setStyleSheet(self.button_style())
        hard_button.clicked.connect(lambda: self.start_game(12, 12, 20))
        layout.addWidget(hard_button)
        
        # Central widget and layout setup
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def button_style(self):
        return """
        QPushButton {
            background-color: #4CAF50;
            color: white;
            font-size: 14px;
            font-weight: bold;
            border: 2px solid #4CAF50;
            border-radius: 5px;
            padding: 10px;
            margin: 10px;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        QPushButton:pressed {
            background-color: #388e3c;
        }
        """
    
    def start_game(self, rows, cols, mines):
        self.game_window = Minesweeper(rows, cols, mines)
        self.game_window.show()
        self.close()


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Сапер")
        self.setGeometry(100, 100, 800, 600)  # Начальный размер окна
        self.setWindowIcon(QIcon(r"C:\Users\silis\OneDrive\Desktop\prog\mines\149.jpg"))

        # Установка фона
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        pixmap = QPixmap(r"C:\Users\silis\OneDrive\Desktop\prog\mines\151.jpg")  # Ваше изображение
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)  # Масштабируем по размеру окна

        self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowMaximizeButtonHint)
        
        # Опционально: устанавливаем фиксированный размер окна
        self.setFixedSize(400, 400)  # Установите размер окна по вашему усмотрению

        # Создание центрального виджета
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.main_layout = QStackedLayout(self.central_widget)

        # Инициализация главного меню
        self.init_main_menu()

    def init_main_menu(self):
        # Виджет главного меню
        main_menu_widget = QWidget()
        outer_layout = QVBoxLayout(main_menu_widget)
        outer_layout.addStretch(1)

        # Макет для кнопок
        button_layout = QVBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Заголовок
        title_label = QLabel("САПЕР")
        title_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("""
            color: #D4D4D4;  /* Тёмно-зелёный цвет */
""")
        button_layout.addWidget(title_label)

        # Кнопка "Играть"
        play_button = QPushButton("Играть")
        play_button.setFixedSize(220, 50)
        play_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #43A047, stop: 1 #66BB6A
            );
            color: white;
            border: 2px solid #388E3C;
            border-radius: 8px;
            font-size: 18px;
            font-weight: bold;
            padding: 5px;
        }
        QPushButton:hover {
            background: qlineargradient(
                x1: 0, y1: 0, x2: 0, y2: 1,
                stop: 0 #66BB6A, stop: 1 #81C784
            );
        }
        QPushButton:pressed {
            background-color: #388E3C;
        }
""")
        play_button.clicked.connect(self.open_difficulty_menu)
        button_layout.addWidget(play_button)

        # Другие кнопки
        rules_button = QPushButton("Правила игры")
        rules_button.setFixedSize(220, 50)
        rules_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #4CAF50, stop: 1 #81C784
                );
                color: white;
                border: 2px solid #388E3C;
                border-radius: 8px;
                font-size: 18px;
                font-weight: bold;
                padding: 5px;
            }
            QPushButton:hover {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #81C784, stop: 1 #A5D6A7
                );
            }
            QPushButton:pressed {
                background-color: #388E3C;
            }
""")
        rules_button.clicked.connect(self.show_rules)
        button_layout.addWidget(rules_button)

        exit_button = QPushButton("Выйти из игры")
        exit_button.setFixedSize(220, 50)
        exit_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #E53935, stop: 1 #F44336
                );
                color: white;
                border: 2px solid #C62828;
                border-radius: 8px;
                font-size: 18px;
                font-weight: bold;
                padding: 5px;
            }
            QPushButton:hover {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 0, y2: 1,
                    stop: 0 #F44336, stop: 1 #E57373
                );
            }
            QPushButton:pressed {
                background-color: #C62828;
            }
""")
        exit_button.clicked.connect(self.close)
        button_layout.addWidget(exit_button)

        # Добавление кнопок в макет
        outer_layout.addLayout(button_layout)
        outer_layout.addStretch(1)
        self.main_layout.addWidget(main_menu_widget)
        self.main_layout.setCurrentWidget(main_menu_widget)

    def resizeEvent(self, event):
        """Обновление размера фонового изображения при изменении размера окна."""
        pixmap = QPixmap(r"C:\Users\silis\OneDrive\Desktop\prog\mines\151.jpg")  # Загрузка фонового изображения
        if not pixmap.isNull():
            self.background_label.setGeometry(0, 0, self.width(), self.height())
            scaled_pixmap = pixmap.scaled(
                self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation
            )
            self.background_label.setPixmap(scaled_pixmap)
        super().resizeEvent(event)
        

    def show_rules(self):
        # Создание виджета с правилами игры
        rules_widget = QWidget()
        layout = QVBoxLayout(rules_widget)
        layout.setContentsMargins(15, 15, 15, 15)

        # Кнопка "Назад"
        back_button = QPushButton("Назад")
        back_button.setFixedSize(100, 30)
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 5px;
                border: 1px solid #388E3C;
            }
            QPushButton:hover {
                background-color: #388E3C;
            }
        """)
        back_button.clicked.connect(self.return_to_main_menu)
        layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignLeft)

        # Заголовок "Правила игры"
        title_label = QLabel("Правила игры")
        title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: #4CAF50;") 
        layout.addWidget(title_label)

        # Оформленный текст правил
        rules_text = """
        <p><b>Игра "Сапер" — это классическая логическая игра, целью которой является очистить минное поле, не подрываясь на минах.</b></p>
        <p><b>Игровое поле:</b> Игровое поле представляет собой сетку клеток, под некоторыми из которых находятся мины. Мины скрыты, и задача игрока — найти их, открывая клетки.</p>
        <p><b>Начало игры:</b> В начале игры вы можете кликнуть по любой клетке. Если это мина, игра окончена. Если это пустая клетка, на ней появится число, указывающее, сколько мин находится в соседних клетках. Клетки с числами дают подсказки, которые помогают вычислить расположение мин.</p>
        <p><b>Числа и их значение:</b> Число на открытой клетке показывает количество мин, находящихся в восьми соседних клетках (по горизонтали, вертикали и диагонали). Например, если на клетке число "3", это значит, что вокруг этой клетки (в соседних 8 клетках) расположены три мины.</p>
        <p><b>Флаги:</b> Если вы думаете, что под какой-то клеткой находится мина, вы можете пометить её флажком, правым щелчком мыши. Это помогает не забыть, где потенциально находятся мины. Однако будьте осторожны — если флажок поставлен на пустой клетке, это может быть ошибкой.</p>
        <p><b>Стратегия:</b> Важно использовать логику и стратегию, чтобы минимизировать риск открытия клеток наугад. Обратите внимание на числа и размещайте флаги, чтобы постепенно раскрывать поле. Стратегия также включает в себя использование так называемого "метода исключения": если вы уверены, что в определенной области мины не могут быть, вы можете безопасно открывать такие клетки. На некоторых уровнях игры можно столкнуться с ситуациями, когда без логических выкладок нельзя обойтись, и вам придется принять рискованные решения.</p>
        <p><b>Советы для новичков:</b> Не торопитесь при открытии клеток. Начинайте с углов и краев поля — они обычно содержат меньшее количество соседних клеток, что снижает риск ошибки. Со временем вы будете лучше предсказывать расположение мин, улучшая свою стратегию.</p>

        <p><i>Удачи!</i></p>
"""

        text_widget = QTextEdit()
        text_widget.setHtml(rules_text)
        text_widget.setReadOnly(True)
        text_widget.setStyleSheet("""
            QTextEdit {
                background-color: #f4f4f9;
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 15px;
                font-family: Arial;
                font-size: 12pt;
                line-height: 1.6;
                color: #333;
            }
        """)
        
        layout.addWidget(text_widget)

        self.main_layout.addWidget(rules_widget)
        self.main_layout.setCurrentWidget(rules_widget)

    def return_to_main_menu(self):
        # Возвращаемся к главному меню
        self.init_main_menu()

    def open_difficulty_menu(self):
        self.difficulty_menu = DifficultyMenu()
        self.difficulty_menu.show()
        self.close()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_menu = MainMenu()
    main_menu.show()
    sys.exit(app.exec())

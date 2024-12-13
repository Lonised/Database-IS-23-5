import tkinter as tk
import random

# Создаем основное окно
root = tk.Tk()
root.title("Поле 9 мини-полей с крестиками-ноликами")

# Параметры для поля
line_thickness = 1  # Толщина линий между клетками
cell_size = 50      # Размер одной клетки
player = "X"        # Текущий игрок ("X" или "O")
grid = [[["" for _ in range(3)] for _ in range(3)] for _ in range(9)]  # Игровое поле 9 мини-полей
active_field = -1   # Текущее активное мини-поле (начальное -1)
winners = [-1] * 9  # Список победителей для мини-полей (-1 - нет победителя, 0 - "X", 1 - "O")
big_grid = [["" for _ in range(3)] for _ in range(3)]  # Основное игровое поле (где ставятся большие крестики и нолики)
big_winners = [-1] * 9  # Победители для основного поля

# Создаем начальное окно
root = tk.Tk()
root.title("Выбор режима игры")

# Заголовок
title_label = tk.Label(root, text="Добро пожаловать в игру!", font=("Arial", 24))
title_label.pack(pady=20)

# Кнопка для начала игры PvP (игрок против игрока)
pvp_button = tk.Button(root, text="Игрок против Игрока", font=("Arial", 14), width=20, command=start_pvp)
pvp_button.pack(pady=10)

# Кнопка для начала игры PvE (игрок против компьютера)
pve_button = tk.Button(root, text="Игрок против Компьютера", font=("Arial", 14), width=20, command=start_pve)
pve_button.pack(pady=10)

# Кнопка для выхода
exit_button = tk.Button(root, text="Выход", font=("Arial", 14), width=20, command=root.quit)
exit_button.pack(pady=20)

# Запускаем главное окно
root.mainloop()

def on_click_pvp(event):
    global player, active_field  # Заявляем о глобальности player и active_field

    col = event.x // (cell_size * 3)
    row = event.y // (cell_size * 3)

    mini_field = col + row * 3
    cell_x = (event.x % (cell_size * 3)) // cell_size
    cell_y = (event.y % (cell_size * 3)) // cell_size

    if grid[mini_field][cell_y][cell_x] == "" and (active_field == -1 or active_field == mini_field) and winners[mini_field] == -1:
        grid[mini_field][cell_y][cell_x] = player  # Игрок ставит X или O
# Создаем холст (Canvas) для рисования
canvas = tk.Canvas(root, width=cell_size * 9, height=cell_size * 9)
canvas.pack()

# Функция для рисования крестика (X)
def draw_x(x1, y1, x2, y2):
    # Рисуем крестик "X" в клетке
    canvas.create_line(x1, y1, x2, y2, fill="blue", width=5)
    canvas.create_line(x1, y2, x2, y1, fill="blue", width=5)

# Функция для рисования нолика (O)
def draw_o(x1, y1, x2, y2):
    # Рисуем окружность (O) в клетке
    canvas.create_oval(x1, y1, x2, y2, outline="green", width=5)

# Функция для проверки победителя в мини-поле
def check_winner(mini_field):
    for row in range(3):
        if grid[mini_field][row][0] == grid[mini_field][row][1] == grid[mini_field][row][2] != "":
            return grid[mini_field][row][0]
    
    for col in range(3):
        if grid[mini_field][0][col] == grid[mini_field][1][col] == grid[mini_field][2][col] != "":
            return grid[mini_field][0][col]
    
    if grid[mini_field][0][0] == grid[mini_field][1][1] == grid[mini_field][2][2] != "":
        return grid[mini_field][0][0]
    
    if grid[mini_field][0][2] == grid[mini_field][1][1] == grid[mini_field][2][0] != "":
        return grid[mini_field][0][2]
    
    return None  # Нет победителя

# Функция для рисования сетки
def draw_grid():
    # Рисуем основную сетку
    for i in range(10):  # 10 линий для 9 клеток
        line_color = '#1F8D95' if i == 0 or i == 9 else '#8E44AD'  # Розовые и голубые линии
        canvas.create_line(0, i * cell_size, cell_size * 9, i * cell_size, width=line_thickness, fill=line_color)
        canvas.create_line(i * cell_size, 0, i * cell_size, cell_size * 9, width=line_thickness, fill=line_color)

    # Рисуем мини-поля с красивыми рамками
    for row in range(3):
        for col in range(3):
            x1 = col * 3 * cell_size
            y1 = row * 3 * cell_size
            x2 = x1 + 3 * cell_size
            y2 = y1 + 3 * cell_size
            canvas.create_rectangle(x1, y1, x2, y2, outline='#F39C12', width=5)  # Золотые рамки для мини-полей

    # Подсвечиваем активное мини-поле
    if active_field != -1:
        row = active_field // 3
        col = active_field % 3
        x1 = col * 3 * cell_size
        y1 = row * 3 * cell_size
        x2 = x1 + 3 * cell_size
        y2 = y1 + 3 * cell_size
        canvas.create_rectangle(x1, y1, x2, y2, outline='#E74C3C', width=8)  # Красная подсветка для активного поля

    # Рисуем крестики и нолики
    for i in range(9):
        for row in range(3):
            for col in range(3):
                mark = grid[i][row][col]
                if mark != "":
                    x1 = (i % 3) * 3 * cell_size + col * cell_size
                    y1 = (i // 3) * 3 * cell_size + row * cell_size
                    x2 = x1 + cell_size
                    y2 = y1 + cell_size
                    if mark == "X":
                        draw_x(x1, y1, x2, y2)  # Рисуем крестик
                    elif mark == "O":
                        draw_o(x1, y1, x2, y2)  # Рисуем нолик

    # Отображаем победный знак в центре мини-поля
    for i in range(9):
        if winners[i] != -1:
            row = i // 3
            col = i % 3
            x1 = col * 3 * cell_size + cell_size
            y1 = row * 3 * cell_size + cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            # Рисуем победный знак по центру
            if winners[i] == 0:  # Победил "X"
                canvas.create_line(x1 - 15, y1 - 15, x2 + 15, y2 + 15, fill="blue", width=5)
                canvas.create_line(x1 - 15, y2 + 15, x2 + 15, y1 - 15, fill="blue", width=5)
            elif winners[i] == 1:  # Победил "O"
                canvas.create_oval(x1 - 15, y1 - 15, x2 + 15, y2 + 15, outline="green", width=5)

# Функция для хода компьютера с случайным выбором клетки в активном поле
def computer_move():
    global active_field  # Заявляем о глобальности active_field

    # Проверка, если активное поле заблокировано (в нем уже есть победитель)
    if winners[active_field] != -1:
        # Находим доступное мини-поле, чтобы бот мог сделать ход
        available_fields = [i for i in range(9) if winners[i] == -1]  # Доступные поля (где нет победителя)
        if available_fields:
            active_field = random.choice(available_fields)  # Выбираем случайное доступное поле

    # Получаем все пустые клетки в активном мини-поле
    empty_cells = []
    row_start = (active_field // 3) * 3
    col_start = (active_field % 3) * 3
    for row in range(3):
        for col in range(3):
            mini_field = active_field
            if grid[mini_field][row][col] == "":
                empty_cells.append((row, col))

    # Если есть пустые клетки, бот делает ход
    if empty_cells:
        row, col = random.choice(empty_cells)
        grid[active_field][row][col] = "O"  # Бот ставит "O"

        # Проверка на победителя в мини-поле
        winner = check_winner(active_field)
        if winner:
            winners[active_field] = 0 if winner == "X" else 1  # Обновляем победителя

        # Переключаем игрока
        global player
        player = "X"

        # Обновляем активное мини-поле
        active_field = col + row * 3

    draw_grid()  # Перерисовываем сетку

    # После хода бота, ждем 2 секунды перед тем, как дать игроку сделать ход
    root.after(2000, enable_player_turn)

# Функция для сброса игры
def new_game():
    global grid, active_field, winners, player
    grid = [[["" for _ in range(3)] for _ in range(3)] for _ in range(9)]  # Сбрасываем игровое поле
    active_field = -1  # Сбрасываем активное поле
    winners = [-1] * 9  # Сбрасываем победителей для мини-полей
    player = "X"  # Устанавливаем игрока "X" первым
    canvas.delete("all")  # Очищаем холст
    draw_grid()  # Перерисовываем начальную сетку

# Функция для обработки кликов
def on_click(event):
    global player, active_field  # Заявляем о глобальности player и active_field

    # Игрок может делать ход только в пустую клетку активного мини-поля
    col = event.x // (cell_size * 3)
    row = event.y // (cell_size * 3)

    mini_field = col + row * 3
    cell_x = (event.x % (cell_size * 3)) // cell_size
    cell_y = (event.y % (cell_size * 3)) // cell_size

    if grid[mini_field][cell_y][cell_x] == "" and (active_field == -1 or active_field == mini_field) and winners[mini_field] == -1:
        grid[mini_field][cell_y][cell_x] = "X"  # Игрок ставит "X"

        # Проверка на победителя в мини-поле
        winner = check_winner(mini_field)
        if winner:
            winners[mini_field] = 0 if winner == "X" else 1  # Обновляем победителя

        # Переключаем игрока
        player = "O"

        # Обновляем активное мини-поле
        active_field = cell_x + cell_y * 3

    draw_grid()  # Перерисовываем сетку

    # После хода игрока, ждем 2 секунды, чтобы дать ход боту
    root.after(1000, computer_move)

# Функция для включения хода игрока после того, как бот сделал свой ход
def enable_player_turn():
    global player
    player = "X"  # Даем игроку возможность сделать ход

# Обновляем функцию для хода компьютера, чтобы она проверяла победителя на уровне большого поля
def computer_move():
    global active_field  # Заявляем о глобальности active_field

    # Проверка, если активное поле заблокировано (в нем уже есть победитель)
    if winners[active_field] != -1:
        # Находим доступное мини-поле, чтобы бот мог сделать ход
        available_fields = [i for i in range(9) if winners[i] == -1]  # Доступные поля (где нет победителя)
        if available_fields:
            active_field = random.choice(available_fields)  # Выбираем случайное доступное поле

    # Получаем все пустые клетки в активном мини-поле
    empty_cells = []
    row_start = (active_field // 3) * 3
    col_start = (active_field % 3) * 3
    for row in range(3):
        for col in range(3):
            mini_field = active_field
            if grid[mini_field][row][col] == "":
                empty_cells.append((row, col))

    # Если есть пустые клетки, бот делает ход
    if empty_cells:
        row, col = random.choice(empty_cells)
        grid[active_field][row][col] = "O"  # Бот ставит "O"

        # Проверка на победителя в мини-поле
        winner = check_winner(active_field)
        if winner:
            winners[active_field] = 0 if winner == "X" else 1  # Обновляем победителя

        # Переключаем игрока
        global player
        player = "X"

        # Обновляем активное мини-поле
        active_field = col + row * 3

    draw_grid()  # Перерисовываем сетку
# Функция для проверки победителя на основном поле
def check_big_winner():
    for row in range(3):
        if big_grid[row][0] == big_grid[row][1] == big_grid[row][2] != "":
            announce_winner(big_grid[row][0])

    for col in range(3):
        if big_grid[0][col] == big_grid[1][col] == big_grid[2][col] != "":
            announce_winner(big_grid[0][col])

    if big_grid[0][0] == big_grid[1][1] == big_grid[2][2] != "":
        announce_winner(big_grid[0][0])

    if big_grid[0][2] == big_grid[1][1] == big_grid[2][0] != "":
        announce_winner(big_grid[0][2])

# Функция для проверки победителя на основном поле
def check_big_winner():
    for row in range(3):
        if big_grid[row][0] == big_grid[row][1] == big_grid[row][2] != "":
            announce_winner(big_grid[row][0])

    for col in range(3):
        if big_grid[0][col] == big_grid[1][col] == big_grid[2][col] != "":
            announce_winner(big_grid[0][col])

    if big_grid[0][0] == big_grid[1][1] == big_grid[2][2] != "":
        announce_winner(big_grid[0][0])

    if big_grid[0][2] == big_grid[1][1] == big_grid[2][0] != "":
        announce_winner(big_grid[0][2])

# Функция для объявления победителя на большом поле
def announce_winner(winner):
    print(f"Победитель! Игрок {winner} выиграл.")
    canvas.create_text(cell_size * 4.5, cell_size * 4.5, text=f"Победитель! {winner} победил.", font=("Arial", 30), fill="red")
    canvas.unbind("<Button-1>")  # Отключаем клики после победы

    # После хода бота, ждем 2 секунды перед тем, как дать игроку сделать ход
    root.after(2000, enable_player_turn)

# Создание кнопки "Новая игра"
new_game_button = tk.Button(root, text="Новая игра", font=("Arial", 14), command=new_game)
new_game_button.pack(side=tk.BOTTOM, pady=10)

# Рисуем начальную сетку
draw_grid()

# Устанавливаем обработчик кликов
canvas.bind("<Button-1>", on_click)

# Запуск главного цикла
root.mainloop()

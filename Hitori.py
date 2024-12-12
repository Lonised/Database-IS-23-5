import pygame
import random
import sys
import time

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 5  # Начальный размер сетки
CELL_SIZE = 100

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (220, 220, 220)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Константы для кнопок
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50
BUTTON_COLOR = GREEN
BUTTON_TEXT_COLOR = BLACK
BUTTON_SPACING = 20  # Расстояние между кнопками


class Hitori:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Hitori')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 50)
        self.small_font = pygame.font.Font(None, 30)

        # Смещение сетки на экране
        self.offset_x = (SCREEN_WIDTH - GRID_SIZE * CELL_SIZE) // 2
        self.offset_y = (SCREEN_HEIGHT - GRID_SIZE * CELL_SIZE) // 3

        # Параметры кнопок
        total_width = 3 * BUTTON_WIDTH + 2 * BUTTON_SPACING
        start_x = (SCREEN_WIDTH - total_width) // 2
        button_y = self.offset_y + GRID_SIZE * CELL_SIZE + 20

        self.check_button = pygame.Rect(start_x, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.restart_button = pygame.Rect(
            start_x + BUTTON_WIDTH + BUTTON_SPACING, button_y, BUTTON_WIDTH, BUTTON_HEIGHT
        )
        self.change_size_button = pygame.Rect(
            start_x + 2 * (BUTTON_WIDTH + BUTTON_SPACING), button_y, BUTTON_WIDTH, BUTTON_HEIGHT
        )

        # Логика игры
        self.grid = self.generate_grid()
        self.blocked_cells = set()
        self.circled_cells = set()
        self.message = ""  # Сообщение об ошибке или успехе
        self.message_time = None  # Время, когда было выведено сообщение

    def generate_grid(self):
        """Генерация случайной сетки с уникальными числами."""
        grid = []
        for _ in range(GRID_SIZE):
            row = []
            row_numbers = set()
            for _ in range(GRID_SIZE):
                num = random.randint(1, GRID_SIZE)
                while num in row_numbers:
                    num = random.randint(1, GRID_SIZE)
                row.append(num)
                row_numbers.add(num)
            grid.append(row)
        return grid

    def draw_grid(self):
        """Отрисовка сетки на экране."""
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x = col * CELL_SIZE + self.offset_x
                y = row * CELL_SIZE + self.offset_y

                # Цвет клетки
                if (row, col) in self.blocked_cells:
                    pygame.draw.rect(self.screen, GRAY, (x, y, CELL_SIZE, CELL_SIZE))
                else:
                    pygame.draw.rect(self.screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
                
                # Граница клетки
                pygame.draw.rect(self.screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 2)

                # Число в клетке
                text = self.font.render(str(self.grid[row][col]), True, BLACK)
                text_rect = text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                self.screen.blit(text, text_rect)

                # Круг в клетке
                if (row, col) in self.circled_cells:
                    pygame.draw.circle(
                        self.screen,
                        BLUE,
                        (x + CELL_SIZE // 2, y + CELL_SIZE // 2),
                        CELL_SIZE // 3,
                        3
                    )

    def draw_buttons(self):
        """Отрисовка кнопок."""
        pygame.draw.rect(self.screen, BUTTON_COLOR, self.check_button)
        check_text = self.small_font.render('Проверить', True, BUTTON_TEXT_COLOR)
        check_text_rect = check_text.get_rect(center=self.check_button.center)
        self.screen.blit(check_text, check_text_rect)

        pygame.draw.rect(self.screen, BUTTON_COLOR, self.restart_button)
        restart_text = self.small_font.render('Рестарт', True, BUTTON_TEXT_COLOR)
        restart_text_rect = restart_text.get_rect(center=self.restart_button.center)
        self.screen.blit(restart_text, restart_text_rect)

        pygame.draw.rect(self.screen, BUTTON_COLOR, self.change_size_button)
        change_size_text = self.small_font.render('Размер поля', True, BUTTON_TEXT_COLOR)
        change_size_text_rect = change_size_text.get_rect(center=self.change_size_button.center)
        self.screen.blit(change_size_text, change_size_text_rect)

    def draw_message(self):
        """Отрисовка сообщения об ошибке или успешном решении."""
        if self.message:
            # Проверка, прошло ли уже 3 секунды
            if self.message_time and time.time() - self.message_time >= 3:
                self.message = ""  # Очистить сообщение через 3 секунды

            if self.message:  # Если сообщение не пустое, отобразить его
                message_text = self.font.render(self.message, True, RED)
                message_rect = message_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
                self.screen.blit(message_text, message_rect)

    def handle_click(self, pos, button):
        """Обработка кликов мыши на клетках и кнопках."""
        x, y = pos
        row = (y - self.offset_y) // CELL_SIZE
        col = (x - self.offset_x) // CELL_SIZE

        if button == 1:  # Левая кнопка — блокировка клетки
            if (row, col) in self.blocked_cells:
                self.blocked_cells.remove((row, col))
            else:
                self.blocked_cells.add((row, col))

            # Убираем круг с клетки, если он есть
            if (row, col) in self.circled_cells:
                self.circled_cells.remove((row, col))

        elif button == 3:  # Правая кнопка — добавление круга в клетку
            if (row, col) in self.circled_cells:
                self.circled_cells.remove((row, col))
            else:
                self.circled_cells.add((row, col))

    def check_solution(self):
        """Проверка решения (проверка ошибок)."""
        errors = []

        # Проверка уникальности чисел в строках и столбцах
        for i in range(GRID_SIZE):
            row_numbers = set()
            col_numbers = set()
            for j in range(GRID_SIZE):
                if (i, j) not in self.blocked_cells:
                    if self.grid[i][j] in row_numbers:
                        errors.append((i, j))  # Ошибка в строке
                    row_numbers.add(self.grid[i][j])

                if (j, i) not in self.blocked_cells:
                    if self.grid[j][i] in col_numbers:
                        errors.append((j, i))  # Ошибка в столбце
                    col_numbers.add(self.grid[j][i])

        return errors

    def restart_game(self):
        """Перезапуск игры."""
        self.grid = self.generate_grid()
        self.blocked_cells = set()
        self.circled_cells = set()
        self.message = ""  # Очистка сообщения
        self.message_time = None  # Сброс времени

    def change_grid_size(self):
        """Изменение размера поля."""
        global GRID_SIZE, CELL_SIZE

        # Изменяем размер сетки
        if GRID_SIZE == 5:
            GRID_SIZE = 6
            CELL_SIZE = 80
        else:
            GRID_SIZE = 5
            CELL_SIZE = 100

        # Пересоздаем сетку
        self.grid = self.generate_grid()
        self.blocked_cells = set()
        self.circled_cells = set()
        self.message = ""  # Очистка сообщения
        self.message_time = None  # Сброс времени

        # Смещение сетки
        self.offset_x = (SCREEN_WIDTH - GRID_SIZE * CELL_SIZE) // 2
        self.offset_y = (SCREEN_HEIGHT - GRID_SIZE * CELL_SIZE) // 3

    def run(self):
        """Основной цикл игры."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Левая кнопка мыши
                        if self.check_button.collidepoint(event.pos):
                            errors = self.check_solution()
                            if not errors:
                                self.message = "Головоломка решена!"
                                self.message_time = time.time()  # Засекаем время
                            else:
                                self.message = "Ошибка в решении!"
                                self.message_time = time.time()  # Засекаем время

                        elif self.restart_button.collidepoint(event.pos):
                            self.restart_game()

                        elif self.change_size_button.collidepoint(event.pos):
                            self.change_grid_size()

                    if event.button in [1, 3]:  # Левый или правый клик по клетке
                        self.handle_click(event.pos, event.button)

            self.screen.fill(LIGHT_GRAY)
            self.draw_grid()  # Отрисовка сетки
            self.draw_buttons()  # Отрисовка кнопок
            self.draw_message()  # Отрисовка сообщения об ошибке или успехе
            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()
        sys.exit()


# Запуск игры
if __name__ == '__main__':
    game = Hitori()
    game.run()

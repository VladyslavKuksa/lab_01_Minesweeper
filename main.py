import pygame
import random

# Константи
WIDTH = 500
HEIGHT = 500
ROWS = 10
COLS = 10
CELL_SIZE = 50
FPS = 30
MINE_COUNT = 10

# Кольори
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)

# Ініціалізація Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Клас комірки
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = col * CELL_SIZE
        self.y = row * CELL_SIZE
        self.mine = False
        self.flagged = False
        self.revealed = False
        self.adjacent_mines = 0

    def draw(self):
        if self.revealed:
            pygame.draw.rect(screen, GRAY, (self.x, self.y, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLACK, (self.x, self.y, CELL_SIZE, CELL_SIZE), 1)  # Додано рамку
            if self.mine:
                pygame.draw.circle(screen, RED, (self.x + CELL_SIZE // 2, self.y + CELL_SIZE // 2), CELL_SIZE // 4)  # Змінено колір на червоний
            elif self.adjacent_mines > 0:
                font = pygame.font.Font(None, CELL_SIZE // 2)
                if self.adjacent_mines == 1:
                    text = font.render(str(self.adjacent_mines), True, CYAN)
                elif self.adjacent_mines == 2:
                    text = font.render(str(self.adjacent_mines), True, GREEN)
                else:
                    text = font.render(str(self.adjacent_mines), True, BLACK)
                text_rect = text.get_rect(center=(self.x + CELL_SIZE // 2, self.y + CELL_SIZE // 2))
                screen.blit(text, text_rect)
        else:
            pygame.draw.rect(screen, BLUE, (self.x, self.y, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLACK, (self.x, self.y, CELL_SIZE, CELL_SIZE), 1)  # Додано рамку
            if self.flagged:
                font = pygame.font.Font(None, CELL_SIZE // 2)
                text = font.render("F", True, BLACK)
                text_rect = text.get_rect(center=(self.x + CELL_SIZE // 2, self.y + CELL_SIZE // 2))
                screen.blit(text, text_rect)

# Генерація дошки
board = []
for row in range(ROWS):
    board.append([])
    for col in range(COLS):
        board[row].append(Cell(row, col))

# Розміщення мін
mines = random.sample(range(ROWS * COLS), MINE_COUNT)
for mine in mines:
    row = mine // COLS
    col = mine % COLS
    board[row][col].mine = True

# Підрахунок кількості сусідніх мін для кожної комірки
for row in range(ROWS):
    for col in range(COLS):
        if not board[row][col].mine:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= row + i < ROWS and 0 <= col + j < COLS:
                        if board[row + i][col + j].mine:
                            board[row][col].adjacent_mines += 1

# Головний цикл гри
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not game_over:
                # Обробка лівого кліку миші
                pos = pygame.mouse.get_pos()
                col = pos[0] // CELL_SIZE
                row = pos[1] // CELL_SIZE
                if not board[row][col].flagged:
                    board[row][col].revealed = True
                    if board[row][col].mine:
                        # Гравець програв
                        game_over = True
            elif event.button == 3 and not game_over:
                # Обробка правого кліку миші
                pos = pygame.mouse.get_pos()
                col = pos[0] // CELL_SIZE
                row = pos[1] // CELL_SIZE
                if not board[row][col].revealed:
                    board[row][col].flagged = not board[row][col].flagged

    # Перевірка перемоги
    if not game_over:
        mine_count = sum(cell.mine and not cell.flagged for row in board for cell in row)
        unrevealed_count = sum(not cell.revealed for row in board for cell in row)
        if mine_count == 0 and unrevealed_count == MINE_COUNT:
            # Гравець переміг
            game_over = True

    # Оновлення екрану
    screen.fill(BLACK)
    for row in range(ROWS):
        for col in range(COLS):
            board[row][col].draw()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

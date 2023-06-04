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
                pygame.draw.circle(screen, BLACK, (self.x + CELL_SIZE // 2, self.y + CELL_SIZE // 2), CELL_SIZE // 4)
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

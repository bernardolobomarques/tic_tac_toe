import pygame
import time
import sys

COLOR = (50, 100, 250)
WIDTH = 600
LENGTH = WIDTH
FONT = "Courier New"
LINE_ONE = WIDTH / 3
LINE_TWO = LINE_ONE * 2

is_player_cross = True
spaces = [False] * 9

class Screen:
    def __init__(self) -> None:
        self.display = pygame.display.set_mode((WIDTH, LENGTH))
        pygame.display.set_caption("Tic Tac Toe")
        self.font = FONT
        self.display.fill(COLOR)

    def draw(self):
        for i in range(1, 3):
            pygame.draw.line(self.display, "white", (0, i * LINE_ONE), (WIDTH, i * LINE_ONE), 2)
            pygame.draw.line(self.display, "white", (i * LINE_ONE, 0), (i * LINE_ONE, WIDTH), 2)
        pygame.display.update()

    @staticmethod
    def click_tracking(pos):
        x, y = pos
        row = y // 200
        col = x // 200
        box_num = row * 3 + col + 1
        center_x = col * 200 + 100
        center_y = row * 200 + 100
        return box_num, center_x, center_y

    def winner(self, s):
        self.display_message(f"{s} won!")

    def draw_game(self):
        self.display_message("It's a draw!")

    def display_message(self, message):
        winner_screen = pygame.display.set_mode((WIDTH, LENGTH))
        winner_screen.fill("black")
        font = pygame.font.SysFont(FONT, 42)
        text = font.render(message, True, "white")
        text_rect = text.get_rect(center=(WIDTH // 2, LENGTH // 2 - 50))
        winner_screen.blit(text, text_rect)

        button_font = pygame.font.SysFont(FONT, 30)
        button_text = button_font.render("Play Again", True, "black")
        button_rect = pygame.Rect(WIDTH // 2 - 100, LENGTH // 2, 200, 50)
        pygame.draw.rect(winner_screen, "white", button_rect)
        button_text_rect = button_text.get_rect(center=button_rect.center)
        winner_screen.blit(button_text, button_text_rect)

        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if button_rect.collidepoint(event.pos):
                        return

def draw_symbol(box, screen):
    n, x, y = box
    font = pygame.font.SysFont(FONT, 60)
    global is_player_cross

    text = font.render("X" if is_player_cross else "O", True, "white")
    text_rect = text.get_rect(center=(x, y))
    screen.display.blit(text, text_rect)
    spaces[n - 1] = 1 if is_player_cross else 2
    is_player_cross = not is_player_cross

def win(spaces):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)              # Diagonal
    ]
    for a, b, c in win_conditions:
        if spaces[a] == spaces[b] == spaces[c] and spaces[a] != False:
            return spaces[a]
    return False

def loop():
    screen = Screen()
    is_playing = True
    global spaces
    spaces = [False] * 9

    while is_playing:
        screen.draw()
        control = win(spaces)
        if control == False:
            if all(spaces):
                screen.draw_game()
                spaces = [False] * 9
                is_player_cross = True
                screen.display.fill(COLOR)
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        pos = pygame.mouse.get_pos()
                        box = screen.click_tracking(pos)
                        if not spaces[box[0] - 1]:
                            draw_symbol(box, screen)
        else:
            screen.winner("Player X" if control == 1 else "Player O")
            spaces = [False] * 9
            is_player_cross = True
            screen.display.fill(COLOR)
        pygame.time.Clock().tick(60)

def start_game():
    pygame.init()

def end_game():
    pygame.quit()

def main():
    start_game()
    loop()
    end_game()

if __name__ == "__main__":
    main()

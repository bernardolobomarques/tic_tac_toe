import pygame
import time

COLOR = (50,100, 250)
WIDTH = 600
LENGH = WIDTH
FONT = "Courier New"
LINE_ONE = WIDTH / 3
LINE_TWO = LINE_ONE * 2

is_player_cross = True
spaces = []

class Screen():
    def __init__(self) -> None:
        self.display = pygame.display.set_mode((WIDTH, LENGH))
        pygame.display.set_caption("Tic Tac Toe")
        self.fonte = FONT
        self.display.fill(COLOR)

    def draw(self):
        pygame.draw.line(self.display, "white", (0, LINE_ONE), (WIDTH,LINE_ONE), 2) #FIRST HORIZONTAL LINE
        pygame.draw.line(self.display, "white", (0, LINE_TWO), (WIDTH,LINE_TWO), 2) #SECOND HORIZONTAL LINE

        pygame.draw.line(self.display, "white", (LINE_ONE, 0), (LINE_ONE,WIDTH), 2) #FIRST HORIZONTAL LINE
        pygame.draw.line(self.display, "white", (LINE_TWO, 0), (LINE_TWO,WIDTH), 2) #SECOND HORIZONTAL LINE

        pygame.display.update()

    @staticmethod
    def click_tracking(pos):
        x, y = pos

        if x <= 200:
            #Box 1
            if y <= 200:
                return 1, 100, 100
            
            #Box 4
            elif y > 200 and y <= 400:
                return 4, 100, 300
            
            #Box 7
            elif y > 400 and y <= 600:
                return 7, 100, 500

        elif x > 200 and x <= 400:
            #Box 2
            if y <= 200:
                return 2, 300, 100
            
            #Box 5
            elif y  > 200 and y <= 400:
                return 5, 300, 300
            
            #Box 7
            elif y > 400 and y <= 600:
                return 8, 300, 500
            
        elif x > 400 and x <= 600:
            #Box 3
            if y <= 200:
                return 3, 500, 100
            
            #Box 6
            elif y > 200 and y <= 400:
                return 6, 500, 300
            
            #Box 9
            elif y > 400 and y <=600:
                return 9, 500, 500
            
    def winner(self, s):
        self.display.fill("black")
        font = pygame.font.SysFont(FONT, 42)
        text = font.render(f"{s} won!", True, "white")
        text_rect = text.get_rect(center=(WIDTH//2, LENGH//2))
        self.display.blit(text, text_rect)

     
def draw_symbol(box, screen):
    n, x, y = box
    font = pygame.font.SysFont(FONT, 60)
    global is_player_cross
    
    if is_player_cross:
        text = font.render("X", True, "white")
    else:
        text = font.render("O", True, "white")
    text_rect = text.get_rect(center=(x, y))

    if is_player_cross == True:
        is_player_cross = False
    else:
        is_player_cross = True

    screen.display.blit(text, text_rect)

def win(spaces):
    if spaces[0] == spaces[1] == spaces[2] and spaces[0] != False:
        return spaces[0]
    elif spaces[3] == spaces[4] == spaces[5] and spaces[3] != False:
        return spaces[3]
    
    elif spaces[6] == spaces[7] == spaces[8] and spaces[6] != False:
        return spaces[6]
    
    elif spaces[0] == spaces[3] == spaces[6] and spaces[0] != False:
        return spaces[0]
    
    elif spaces[1] == spaces[4] == spaces[7] and spaces[1] != False:
        return spaces[1]
    
    elif spaces[2] == spaces[5] == spaces[8] and spaces[2] != False:
        return spaces[2]
    
    elif spaces[0] == spaces[4] == spaces[8] and spaces[0] != False:
        return spaces[0]
    
    elif spaces[2] == spaces[4] == spaces[6]  and spaces[2] != False:
        return spaces[2]
    else:
        return False

def loop():
    screen = Screen()
    is_playing = True
    global spaces
    spaces = [False, False, False, False, False, False, False, False, False]

    while is_playing:
        screen.draw()
        control = win(spaces)
        if control == False:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
                #Posicionamento do mouse
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    box = screen.click_tracking(pos)
                    
                    if not spaces[box[0]-1]:
                        draw_symbol(box, screen)
                        if is_player_cross:
                            spaces[box[0]-1] = 1
                        else:
                            spaces[box[0]-1] = 2
        else:
            screen.winner(control)
            # time.sleep(5)
            # break

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
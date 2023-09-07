import pygame , sys, time
import numpy as np
pygame.init()

DISABLE_COLOR  = (100,100,100)
CLICKED_COLOR  = (100,100,1)
NORMAL_COLOR   = (255,255,255)
BORDER_COLOR   = (0,0,20)
HOVER_COLOR    = (150,0,150)
TEXT_COLOR     = (0,0,100)
class Mouse:
    def __init__(self):
        self.clicked = False

    def get_pos(self):
        x, y = pygame.mouse.get_pos()
        return [x,y]

    def is_pressed(self):
        if pygame.mouse.get_pressed()[0] and not self.clicked:
            self.clicked = True
            return True
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False
            return False
mouse = Mouse()

class Button:
    def __init__(self, surface, x, y, w, h, command, row, col, font_size=50):
        self.surface = surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.row = row
        self.col = col
        self.disabled = False
        self.command = command
        self.font = pygame.font.SysFont("HELVETICA",font_size)

    def update(self, char):
        x,y = pygame.mouse.get_pos()
        text = self.font.render(char,1,TEXT_COLOR)
        coor = [self.x - text.get_width()//2 + self.w//2, self.y - text.get_height()//2 + self.h//2]
        color = NORMAL_COLOR
        if (x > self.x and x < self.x + self.w) and (y > self.y and y < self.y + self.h):
            color = HOVER_COLOR
            if mouse.is_pressed() and not self.disabled:
                self.command(self)
                color = CLICKED_COLOR
        if self.disabled or char=="x" or char=="o":
            color = DISABLE_COLOR
        pygame.draw.rect(self.surface, color, (self.x, self.y, self.w, self.h))
        pygame.draw.rect(self.surface, BORDER_COLOR, (self.x, self.y, self.w, self.h), 1)
        self.surface.blit(text,coor)


def get_game_state(grid):
    for row in range(3):
        if grid[row][0] == grid[row][1] and grid[row][0] == grid[row][2] and grid[row][0] != "":
            return grid[row][0]
    
    for col in range(3):
        if grid[0][col] == grid[1][col] and grid[0][col] == grid[2][col] and grid[0][col] != "":
            return grid[0][col]
    
    if grid[0][0] == grid[1][1] and grid[0][0]==grid[2][2] and grid[0][0] != "":
        return grid[0][0]
    if grid[0][2] == grid[1][1] and grid[0][2] == grid[2][0] and grid[0][2] != "":
        return grid[0][2]

    return ""

def get_new_bigger_grid(all_grids):
    all_grids = np.array(all_grids)
    output = [["" for _ in range(3)] for _ in range(3)]
    output[0][0] = get_game_state(all_grids[0:3, 0:3])
    output[0][1] = get_game_state(all_grids[0:3, 3:6])
    output[0][2] = get_game_state(all_grids[0:3, 6:9])

    output[1][0] = get_game_state(all_grids[3:6, 0:3])
    output[1][1] = get_game_state(all_grids[3:6, 3:6])
    output[1][2] = get_game_state(all_grids[3:6, 6:9])
    
    output[2][0] = get_game_state(all_grids[6:9, 0:3])
    output[2][1] = get_game_state(all_grids[6:9, 3:6])
    output[2][2] = get_game_state(all_grids[6:9, 6:9])
    return output

if __name__ == "__main__":
    
    grids =[['.', '.', '.', '.', '.', '.', '.', '.', '.'], 
            ['.', 'x', '.', 'x', 'x', 'o', '.', '.', '.'], 
            ['.', 'o', 'o', '.', 'o', 'x', 'x', 'x', '.'], 
            ['.', 'x', 'o', 'x', 'o', '.', 'x', 'o', '.'], 
            ['o', 'x', 'o', 'o', 'o', 'o', 'x', '.', '.'], 
            ['.', '.', '.', 'o', '.', '.', 'x', 'x', '.'], 
            ['.', 'x', 'o', '.', 'o', '.', 'x', '.', '.'], 
            ['.', 'x', '.', 'o', 'x', 'x', 'x', 'o', '.'], 
            ['.', '.', 'o', 'o', '.', '.', '.', '.', '.']]

    for row in range(9):
        for col in range(9):
            print(grids[row][col], end=" ")
        print()

    print(get_new_bigger_grid(grids))
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
    def __init__(self, surface, x, y, w, h, command, row, col):
        self.surface = surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.row = row
        self.col = col
        self.font = pygame.font.SysFont("HELVETICA",50)
        self.disabled = False
        self.command = command

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

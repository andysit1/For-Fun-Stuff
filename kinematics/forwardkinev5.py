import pygame
import math
width, height = 1680, 720
WHITE = pygame.Color("white")

class arm:
    def __init__(self, window, parent):
        self.startpoint = pygame.math.Vector2(round(width/2), round(height/2))
        self.endpoint = pygame.math.Vector2(170, 0)
        self.color = pygame.Color('red')
        self.window = window
        self.angle = 0
        self.length = 100
        self.y = 0
        self.x = 0
        self.parent = parent
        self.func_type = ''
        self.factor = 0
        self.mag = 0

    def getEndPosX(self):
        angle = self.angle
        parent = self.parent
        while(parent):
            angle += parent.angle
            parent = parent.parent
        return self.x + math.cos(angle) * self.length
    
    def getEndPosY(self):
        angle = self.angle
        parent = self.parent #arm1
        while(parent):
            angle += parent.angle
            parent = parent.parent
        return self.y + math.sin(angle) * self.length
    
    def connect(self, point1, point2):
        pygame.draw.line(self.window, self.color, point1, point2, width=4)
    
    def create(self, x, y, len):
        self.x = x
        self.y = y
        pygame.draw.line(self.window, self.color, (x, y), ((x+len),y), width=4)

    def update(self, angle):
        self.angle = math.sin(angle) * self.mag
        self.connect(self.startpoint, (self.getEndPosX(),self.getEndPosY()))


class arm_segments(arm):
    def __init__(self, window, parent):
        arm.__init__(self, window, parent)
        self.color = pygame.Color('black')
    def update(self, angle):
        parent = self.parent
        cords = parent.getEndPosX(), parent.getEndPosY()

        if self.func_type == 'cos':
            self.angle = math.cos(angle * self.factor) * self.mag
        elif self.func_type == 'sin':
            self.angle = math.sin(angle * self.factor) * self.mag
        else:
            print('Error: Input in argument incorrect...')

        self.connect(cords, (self.getEndPosX(),self.getEndPosY()))


def screen(window):
    window.fill(WHITE)    

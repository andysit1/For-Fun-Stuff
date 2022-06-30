from django.forms import NullBooleanField
from numpy import angle
import pygame
import math



width, height = 640, 480
window = pygame.display.set_mode((width, height))
FPSCLOCK = pygame.time.Clock()

WHITE = pygame.Color("white")

class arm:
    def __init__(self, window, parent):
        self.startpoint = pygame.math.Vector2(320, 240)
        self.endpoint = pygame.math.Vector2(170, 0)
        self.color = pygame.Color('red')
        self.window = window
        self.angle = 0
        self.length = 100
        self.y = 0
        self.x = 0
        self.parent = parent
        self.func_type = ' '

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

    def update(self, angle, mag):
        self.angle = math.sin(angle) * mag
        self.connect(self.startpoint, (self.getEndPosX(),self.getEndPosY()))



class arm_segments(arm):
    def __init__(self, window, parent):
        arm.__init__(self, window, parent)

    def update(self, angle, mag, factor, func_type):
        parent = self.parent
        cords = parent.getEndPosX(), parent.getEndPosY()
        
        if func_type == 'cos':
            self.angle = math.cos(angle * factor) * mag
        elif func_type == 'sin':
            self.angle = math.sin(angle * factor) * mag
        else:
            print('Error: Input in argument incorrect...')

        self.connect(cords, (self.getEndPosX(),self.getEndPosY()))


def screen(window):
    window.fill(WHITE)    

arm1 = arm(window, False)
arm2 = arm_segments(window, arm1)
arm3 = arm_segments(window, arm2)

def main():
    angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        arm1.create(round(width/2), round(height/2), arm1.length)
        arm2.create(arm1.getEndPosX(), arm1.getEndPosY(), arm2.length)
        arm3.create(arm2.getEndPosX(), arm2.getEndPosY(), arm3.length)
        screen(window)
        arm1.update(angle, 1.2)
        arm2.update(angle, 0.93, 0.873, 'cos')
        arm3.update(angle, 1.34, 1.57, 'sin')
        angle += 0.05
        pygame.display.flip()
        FPSCLOCK.tick(45)
main()
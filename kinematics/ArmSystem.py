from operator import index
import sys

from matplotlib.pyplot import draw
from forwardkinev5 import arm, arm_segments, screen
import pygame
import math

width, height = 1680, 720
window = pygame.display.set_mode((width, height))
FPSCLOCK = pygame.time.Clock()

class armSystem():
    def __init__(self, window):
        self.window = window
        self.arm_array = []
        self.num_arms_current = 0

    def create_mult(self, num_arms):
        self.num_arms_current = num_arms
        for i in range(num_arms):
            if i == 0:
                self.arm_array.append(arm(self.window, False))
            else:
                self.arm_array.append(arm_segments(self.window, self.arm_array[i-1]))

    def draw_arms(self):
        for i in range(self.num_arms_current):
            if i == 0:
                self.arm_array[i].create(round(width/2), round(height/2), self.arm_array[i].length)
            else:
                self.arm_array[i].create(self.arm_array[i-1].getEndPosX(), self.arm_array[i-1].getEndPosY(), self.arm_array[i].length)

    def store_values(self, index, func_type, mag, factor):
        self.arm_array[index].func_type = func_type
        self.arm_array[index].mag = mag
        self.arm_array[index].factor = factor

    def store(self,index, x, y):
        self.arm_array[index].x, self.arm_array[index].y = x, y

    def update(self, index, angle):
        if index == 0:
            self.store(index, round(width/2), round(height/2))
            self.arm_array[index].update(angle)
        else:   
            self.store(index, self.arm_array[index-1].getEndPosX(), self.arm_array[index-1].getEndPosY())
            self.arm_array[index].update(angle)
            #arm3.update(angle, 1.34, 1.57, 'sin')
system = armSystem(window)
system.create_mult(4)
    #index, func_type, mag, factor
system.store_values(0, 'sin', 1.2, None)
system.store_values(1, 'cos', 0.93, 0.873)
system.store_values(2, 'sin', 1.34, 1.57)
system.store_values(3, 'cos', 1.74, 3.21)

def main():
    angle = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit() 
        screen(window) 
        system.update(0, angle)
        system.update(1, angle)
        system.update(2, angle)
        system.update(3, angle)
        angle += 0.05
        pygame.display.flip()
        FPSCLOCK.tick(45)
main()

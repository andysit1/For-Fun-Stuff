
import pygame
import os
import random
import time


pygame.init()

rain = (152, 68, 158)
background = (215, 181, 216)
width, height = (1920, 1080)

fps = 60
fpsClock = pygame.time.Clock()

window = pygame.display.set_mode((width, height))

dt = fpsClock.tick(fps)/1000
print(dt)
running = True

class drop:
    def __init__(self, window):
        self.x = random.randint(5, 1915)
        self.y = random.randint(-2000, -700)
        self.z = random.randint(0, 50)

        self.zlength = map(self.z, 0, 50, 10, 20)
        self.yspeed = map(self.z, 0, 50, 4, 8)
        self.width = map(self.z, 0, 50, 1, 3)

        self.color = rain
        self.window = window

    def fall(self):
        if self.y > height:
            self.y = random.randint(-10 ,0)
        else:
            self.y += self.yspeed
            self.yspeed = map(self.z, 0, 50, 4, 20)

    def draw_rain(self):
        pygame.draw.rect(self.window,self.color,(self.x, self.y, self.width, self.zlength))


x_count = 0
class drop_left_right:
    def __init__(self, window, x_count):
        self.x = x_count
        self.y = random.randint(-700, -100)

        self.length = random.randint(10, 20)
        self.z = random.randint(0, 20)

        self.zlength = map(self.z, 0, 20, 10, 20)
        self.yspeed = map(self.z, 0, 20, 4, 8)
        self.width = map(self.z, 0, 20, 1, 3)

        self.color = rain
        self.window = window

    def fall(self):
        if self.y > height:
            self.y = random.randint(-10 ,0)
        else:
            self.y += self.yspeed
            self.yspeed = map(self.z, 0, 20, 4, 20)

    def draw_rain(self):
        pygame.draw.rect(self.window,self.color,(self.x, self.y, self.width, self.zlength))

def screen(window):
    window.fill(background)

def map(val, x1, x2, y1, y2):
    min, max = x1, x2 
    V_min, V_max = y1, y2 
    scale = val / max
    return round((y2 - y1) * scale + V_min)

num_drops = 2000
rainfall = []

left_right = []
for i in range(0, width):
    x_count += 1
    left_right.append(drop_left_right(window, x_count))

for i in range(0, num_drops):
    rainfall.append(drop(window))

WholeMap = False
leftToright = False
while running:
    screen(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                leftToright = False
                WholeMap = True
            elif event.key == pygame.K_2:
                WholeMap = False
                leftToright = True
                print(leftToright)
    if WholeMap == True: 
        for i in rainfall:
            i.draw_rain()
            i.fall()
        pygame.display.flip()

    if leftToright == True:
        for i in left_right:
            i.draw_rain()
            i.fall()
        pygame.display.flip()
    screen(window)
    fpsClock.tick(fps)


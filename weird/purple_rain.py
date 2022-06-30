from asyncio.windows_events import _WindowsSelectorEventLoop
import pygame
import random

rain = (152, 68, 158)
background = (215, 181, 216)
screen_size = (700, 700)

class Raindrop:
    def __init__(self, window):
        self.x = random.randint(5, 695) #location of x and y
        self.y = random.randint(-1500, 0)
        self.zaxis = random.randint(0, 30)# distance z
        self.width = random.randint(0, 3) #actual size of rectange
        self.color = rain
        self.window = window
        self.length = map(self.zaxis,0,20,0,30)
        self.yspeed = map(self.zaxis,0,0.05,0,30)
    
    def fall(self): 
        self.y += self.yspeed
        self.yspeed += (0.025*self.zaxis)/30 #closest  = 0.000433 #furthest = 0.025
        if self.y  >= 700:
            self.y = random.randint(-200, -100)
            self.yspeed = random.uniform(2.5,2)
    
    def create(self):
        pygame.draw.rect(self.window,self.color,(self.x,self.y,self.width,self.length))


def screen(window):
    window.fill(background)

def map(x, x1, x2, y1, y2): #30 - 0/ 20 - 0
    return y1 + x * (y2-y2)/(x2-x1)

def main():
    window = pygame.display.set_mode((screen_size))
    rainfall = []
    num_drops = 700

    for i in range(0, num_drops):
        rainfall.append(Raindrop(window))

    while True:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                pygame.quit()
                exit()
        if pygame.key.key_code("space") == pygame.K_SPACE:
            for i in rainfall:
                i.create()
                i.fall()
            pygame.display.flip()
        else:
            None
        screen(window)
        
main()



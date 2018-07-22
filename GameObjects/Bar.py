import pygame

class Bar():
    width = 20
    height = 70

    y_velocity = 0
    
    current_x = 0
    current_y = 0

    
    def __init__(self, start_x, start_y):
        x = start_x
        y = start_y
    
    def drawBar(self, screen, x, y, color):
        pygame.draw.rect(screen, color, (x, y, self.width, self.height), 0)
        pygame.draw.circle(screen, (255,0,0), (int(x), int(y)), 5)
        pygame.draw.circle(screen, (255,0,0), (int(x), int(y)+self.height), 5)
                           

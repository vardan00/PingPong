import pygame

class Ball():
    radius = 10
    def drawCircle(self, screen, x, y, color):
        pygame.draw.circle(screen, color, (x,y), self.radius)
        

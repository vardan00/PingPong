import pygame, random
from GameObjects.Ball import Ball
from GameObjects.Bar import Bar


class colors():
    black = (0,0,0)
    white = (255,255,255)
color = colors()

pygame.init()
screen_height, screen_width = 600, 600
gameDisplay = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()



paddle_one = Bar(300, 300)

c = Ball(screen_width, screen_height)


def gameLoop():
    x = screen_height *.5
    y = screen_width *.5

    crashed = False
    close = False
    y_change = 0    
    while not crashed and not close:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                
                elif event.key == pygame.K_DOWN:
                    y_change = 5
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        if y+y_change > 0 and y+y_change < screen_height-70:
            y+=y_change
    
        gameDisplay.fill((0,0,0))
        
        paddle_one.drawBar(gameDisplay, 20, y, (255,255,255))

        c.drawCircle(gameDisplay, 400+c.x_velocity, 300+c.y_velocity, (255,255,255))
        pygame.display.update()
    
        clock.tick(60)
        
gameLoop()
pygame.quit()
quit()
    

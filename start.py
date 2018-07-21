import pygame
from GameObjects.Ball import Ball
from GameObjects.Bar import Bar

class boundaries():
    a = 7
class colors():
    black = (0,0,0)
    white = (255,255,255)

pygame.init()

screen_height, screen_width = 600, 600

color = colors()

gameDisplay = pygame.display.set_mode((screen_height, screen_width))

pygame.display.set_caption("Ping Pong")

clock = pygame.time.Clock()

x = screen_height *.5
y = screen_width *.5

crashed = False
close = False

paddle_one = Bar(300, 300)

c = Ball()
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
    c.drawCircle(gameDisplay, 400, 300, (255,255,255))
    pygame.display.update()
    
    clock.tick(60)

pygame.quit()
quit()

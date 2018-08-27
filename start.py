import pygame, random
from GameObjects.Ball import Ball
from GameObjects.Bar import Bar
from Render import render

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
paddle_two = Bar(300, 300)

c = Ball(screen_width, screen_height)

keyDict = {"up":False, "down":False, "w":False, "s":False}

def gameLoop():
    x = screen_height *.5
    y = screen_width *.5
    y2 = screen_width *.5

    crashed = False
    close = False
    y_change = 0
    y_change2 = 0
    
    while not crashed and not close:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    keyDict["up"] = True
                elif event.key == pygame.K_DOWN:
                    keyDict["down"] = True
                elif event.key == pygame.K_w:
                    keyDict["w"] = True
                elif event.key == pygame.K_s:
                    keyDict["s"] = True
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    keyDict["up"] = False
                elif event.key == pygame.K_DOWN:
                    keyDict["down"] = False
                elif event.key == pygame.K_w:
                    keyDict["w"] = False
                elif event.key == pygame.K_s:
                    keyDict["s"] = False

        if keyDict["up"]:
            print(keyDict["up"])
            y_change = -5
        elif keyDict["down"]:
            y_change = 5
        elif not keyDict["down"] and not keyDict["up"]:
            y_change = 0

        if keyDict["w"]:
            y_change2 = -5
        elif keyDict["s"]:
            print(keyDict['w'])
            y_change2 = 5
        elif not keyDict["s"] and not keyDict["s"]:
            print(keyDict['w'])
            y_change2 = 0

    
        if y+y_change > 0 and y+y_change < screen_height-70:
            y+=y_change
            
        if y2+y_change2 > 0 and y2+y_change2 < screen_height-70:
            y2+=y_change2

        gameDisplay.fill((0,0,0))
        render.drawBar(paddle_one, gameDisplay, 20, y, (255,255,255))
        render.drawBar(paddle_two, gameDisplay, 580, y2, (255,255,255))
        
        if c.x_left_boundary <= paddle_one.x_right_boundary:
            if (paddle_one.y_up_boundary <= c.y_top_boundary and paddle_one.y_bottom_boundary >= c.y_bottom_boundary):
                render.drawCircle(c, gameDisplay, 400+c.x_velocity, 300+c.y_velocity, (255,255,255), True)
            else:
                render.drawCircle(c, gameDisplay, 400+c.x_velocity, 300+c.y_velocity, (255,255,255))
        else:
            render.drawCircle(c, gameDisplay, 400+c.x_velocity, 300+c.y_velocity, (255,255,255))

                
        pygame.display.update()
    
        clock.tick(60)
        
gameLoop()
pygame.quit()
quit()
    

import pygame


def drawCircle(ball, screen, x, y, color, hit=False):
    if hit:
        ball.x_velocity = ball.x_velocity * (-1)
    elif  ball.x_left_boundary <=  0: 
        ball.reset()
    if ball.x_right_boundary  >= ball.screen_x_boundary:
        ball.x_velocity = ball.x_velocity * -1
        
    if ball.y_bottom_boundary  >= ball.screen_y_boundary or ball.y_top_boundary <= 0:
        ball.y_velocity = ball.y_velocity * (-1)

    ball.y_pos += ball.y_velocity
    ball.x_pos += ball.x_velocity
    ball.update()
        
    pygame.draw.circle(screen, color, (ball.x_pos,ball.y_pos), ball.radius)
    pygame.draw.circle(screen, (255,0,0), (ball.x_pos,ball.y_pos), 5)
                                                                                                                                


def drawBar(bar, screen, x, y, color):
    bar.current_x = x
    bar.current_y = y
    bar.update_boundaries()
    pygame.draw.rect(screen, color, (x, y, bar.width, bar.height), 0)
    pygame.draw.circle(screen, (255,0,0), (int(x), int(y)), 5)
    pygame.draw.circle(screen, (255,0,0), (int(x), int(y)+bar.height), 5) 

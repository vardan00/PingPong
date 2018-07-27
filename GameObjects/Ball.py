import pygame, random, math

class Ball():
    radius = 10
    start_angle = 0

    screen_x_boundary = 0
    screen_y_boundary = 0

    x_left_boundary = 0
    x_right_boundary = 0

    y_top_boundary = 0
    y_bottom_boundary = 0
    
    x_velocity = 0
    y_velocity = 0

    x_pos = 0
    y_pos = 0


    def update(self):
        self.x_left_boundary = self.x_pos - self.radius
        self.x_right_boundary = self.x_pos + self.radius
        self.y_top_boundary = self.y_pos - self.radius
        self.y_bottom_boundary = self.y_pos + self.radius
        
    
    def reset(self):
        self.start_angle = random.randint(0, 360)
        self.y_velocity = int(5*math.sin(self.start_angle))
        self.x_velocity = int(5*math.cos(self.start_angle))
        self.x_pos = int(self.screen_x_boundary * .5)
        self.y_pos = int(self.screen_y_boundary * .5)
        self.update()
    

    def __init__(self, screen_width, screen_height):
        self.start_angle = random.randint(0, 360)

        self.screen_x_boundary = screen_width
        self.screen_y_boundary = screen_height
        
        self.x_pos = int(screen_width * .5)
        self.y_pos = int(screen_height * .5)

        self.y_velocity = int(5*math.sin(self.start_angle))
        self.x_velocity = int(5*math.cos(self.start_angle))
        print(self.x_velocity)
        print(self.y_velocity)
        
    def drawCircle(self, screen, x, y, color, hit=False):

        if hit:
            self.x_velocity = self.x_velocity * (-1)        
        elif  self.x_left_boundary <=  0: # or self.x_right_boundary  >= self.screen_x_boundary:
            self.reset()
        if self.x_right_boundary  >= self.screen_x_boundary:
            self.x_velocity = self.x_velocity * -1
            
        if self.y_bottom_boundary  >= self.screen_y_boundary or self.y_top_boundary <= 0:
            self.y_velocity = self.y_velocity * (-1)
            print(self.y_velocity)

        self.y_pos += self.y_velocity
        self.x_pos += self.x_velocity
        self.update()
        
        pygame.draw.circle(screen, color, (self.x_pos,self.y_pos), self.radius)
        pygame.draw.circle(screen, (255,0,0), (self.x_pos,self.y_pos), 5)    

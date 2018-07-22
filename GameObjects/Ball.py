import pygame, random, math

class Ball():
    radius = 10
    start_angle = 0

    x_boundary = 0
    y_boundary = 0
    
    x_velocity = 0
    y_velocity = 0

    x_pos = 0
    y_pos = 0

    def reset(self):
        
        self.start_angle = random.randint(0, 360)
        self.x_pos = int(self.x_boundary * .5)
        self.y_pos = int(self.y_boundary * .5)
        self.y_velocity = int(5*math.sin(self.start_angle))
        self.x_velocity = int(5*math.cos(self.start_angle))
        

    def __init__(self, screen_width, screen_height):
        self.start_angle = random.randint(0, 360)

        self.x_boundary = screen_width
        self.y_boundary = screen_height
        
        self.x_pos = int(screen_width * .5)
        self.y_pos = int(screen_height * .5)

        self.y_velocity = int(5*math.sin(self.start_angle))
        self.x_velocity = int(5*math.cos(self.start_angle))
        print(self.x_velocity)
        print(self.y_velocity)
        
    def drawCircle(self, screen, x, y, color, hit=False):

        if hit:
            self.x_velocity = self.x_velocity * (-1)
        
        elif self.x_pos + self.radius >= self.x_boundary or self.x_pos + self.radius <= self.radius :
            self.reset()
            
        if self.y_pos + self.radius >= self.y_boundary or self.y_pos + self.radius <= self.radius:
            self.y_velocity = self.y_velocity * (-1)
            print(self.y_velocity)

        self.y_pos += self.y_velocity
        self.x_pos += self.x_velocity
        
        pygame.draw.circle(screen, color, (self.x_pos,self.y_pos), self.radius)

    

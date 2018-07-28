import random, math

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
      

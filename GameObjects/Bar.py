import pygame

class Bar():
    width = 20
    height = 70

    y_velocity = 0
    
    current_x = 0
    current_y = 0

    x_right_boundary = 0
    y_up_boundary = 0
    y_bottom_boundary = 0
    
    def __init__(self, start_x, start_y):
        self.current_x = start_x
        self.current_y = start_y
        self.update_boundaries()
        
    def update_boundaries(self):
        self.x_right_boundary = self.current_x + self.width
        self.y_up_boundary = self.current_y
        self.y_bottom_boundary = self.current_y + self.height



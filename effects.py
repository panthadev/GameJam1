import pygame


class Effects():

    def __init__(self):
        pass
    
    def draw(self):
        pass
    def update(self):
        pass


class Ring(Effects):

    def __init__(self, screen, center, max_radius, num_rings, color, width):
        super().__init__()
        self.screen = screen
        self.center = center
        self.max_radius = max_radius
        self.num_rings = num_rings

        self.color = color
        self.width = width
        
        self.rings_list = []

        self.frame = 0
        self.current_radius = 0



    def draw(self):

        if len(self.rings_list) < self.num_rings:

            if self.frame % 2 == 0:
                self.current_radius += 1
            
            inner_ring = pygame.draw.circle(self.screen, self.color, (self.center[0], self.center[1]), 
                                      self.current_radius, self.width)
            outer_ring = pygame.draw.circle(self.screen, self.color, (self.center[0], self.center[1]), 
                                      self.current_radius + 10, self.width)
            temp_list = [inner_ring, outer_ring]
            
            if self.current_radius == self.max_radius:
                self.frame = 0
                self.current_radius = 0
                self.rings_list.append(temp_list)


        pass
    
    
    def update(self):
        self.frame += 1
        self.draw()
        pass


class Particles(Effects):

    def __init__(self):
        super().__init__()
        pass



class Noise(Ring):

    def __init__(self):
        super().__init__()
        pass

   
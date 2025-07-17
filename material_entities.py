import pygame


class MaterialEntity():

    def __init__(self, screen, image, pos, material):
        self.screen = screen
        self.image = image
        self.pos = pos
        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.material = material

    def collisions(self):
        pass

    def update(self):
        pass




class Structure(MaterialEntity):

    def __init__(self, screen, image, pos, material):
        super().__init__(screen, image, pos, material)
    

    def collisions(self):
        # create effects
        pass


    def update(self):

        self.collisions()



class ThrowableItem(MaterialEntity):

    def __init__(self, screen, image, pos, material, velocity_x, velocity_y):
        super().__init__(screen, image, pos, material)

        # for movement 
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.move_vector = pygame.math.Vector2(velocity_x, velocity_y)

        # for anchoring
        self.anchor = None
    
    
    def collisions(self):
        # ricochet
        pass


    def update(self):

        if self.anchor != None:
            self.rect.center = self.anchor.rect.center #if anchored to player, sets player as center
        
        self.collisions()

        self.rect = self.rect.move(self.move_vector) # should be set at (0,0) until thrown by player
        self.screen.blit(self.image, self.rect)

        
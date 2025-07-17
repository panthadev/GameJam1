import pygame


class Player():

    def __init__(self, screen, image, throwables_list):
        
        self.screen = screen
        self.image = image
        self.image.fill("darkgreen")
        self.rect = self.image.get_rect()

        self.throwables_list = throwables_list
        self.held_object = None
        

    def pick_up(self):

        if self.held_object == None:

            for throwable in self.throwables_list: # iterates through all throwables on map
                if self.rect.colliderect(throwable): # if player collides with one

                    self.held_object = throwable # players held object becomes that
                    throwable.anchor = self # the throwable anchors itself and its movement to player
                if self.held_object != None: # once a throwable is picked, stops the loop
                    print("loop broken")
                    break
        pass

    
    def throw(self):
         
        mouse_pos = pygame.mouse.get_pos()
        throw_vec_magnitude = (self.rect.center[0] - mouse_pos[0],  self.rect.center[1] - mouse_pos[1])
        throw_vec = pygame.math.Vector2(throw_vec_magnitude)
        rev_throw_vec = pygame.math.Vector2(-throw_vec[0], -throw_vec[1])
        throw_vec = throw_vec * 0.1

        
        pygame.draw.line(self.screen, (0,0,255), self.rect.center, 
                         (self.rect.center[0]  + throw_vec[0], self.rect.center[1]  + throw_vec[1]), 2)

        pygame.draw.line(self.screen, (255,0,0), self.rect.center, 
                         (self.rect.center[0]  + rev_throw_vec[0], self.rect.center[1]  + rev_throw_vec[1]), 2)

        print(throw_vec)

        keys = pygame.key.get_pressed()
       
        if keys[pygame.K_t]:
            if self.held_object != None:
                self.held_object.move_vector = throw_vec
                self.held_object.anchor = None
                self.held_object = None


    def movement(self):
        keys = pygame.key.get_pressed()
       
        if keys[pygame.K_w]:
            self.rect = self.rect.move(0, -1)
        elif keys[pygame.K_a]:
            self.rect = self.rect.move(-1, 0)
        elif keys[pygame.K_s]:
            self.rect = self.rect.move(0, 1)
        elif keys[pygame.K_d]:
            self.rect = self.rect.move(1, 0)
    
        # special controls
        elif keys[pygame.K_SPACE]:
            self.pick_up()




    def update(self):
        self.throw()
        self.movement()
        self.screen.blit(self.image, self.rect)
        pass
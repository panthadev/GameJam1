import pygame
import numpy
import random

pygame.init()
screen_width = 1075
screen_height = 540
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    

    # RENDER YOUR GAME HERE

    screen.fill("white")

   

    

    




    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
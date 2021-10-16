# importing all needed modules
import pygame
from walker import Walker

# initializing pygame
pygame.init()

# Permanent variables: Scale, each block size, width, height, dimensions
WIDTH = 800
HEIGHT = 600
DIMENSIONS = (WIDTH, HEIGHT)

BLACK = (0, 0, 0)

# Setting up pygame
screen = pygame.display.set_mode(DIMENSIONS)
pygame.display.set_caption('Natural Random Walker')

FRAMES = int(1000/60)

# BEGINNING
walkers = []

def create_random_walker(pos):
    walkers.append(Walker([pos[0], pos[1]]))

# Game loop
while True:
    pygame.time.delay(FRAMES)
    screen.fill(BLACK)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONUP:
            create_random_walker(pygame.mouse.get_pos())

    for walker in walkers:
        walker.render(pygame, screen)
        walker.update(screen)


    pygame.display.update()





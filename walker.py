import random
from steerer import Steerer

GREEN = (0, 255, 0)
RADIUS = 5

class Walker:
    def __init__(self, pos):
        self.pos = pos
        self.steerer = Steerer(pos)
        self.trail_col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.positions = [(pos[0], pos[1])]

    def render(self, pygame, screen):
        for position in self.positions:
            pygame.draw.circle(screen, self.trail_col, position, 1)

        pygame.draw.circle(screen, GREEN, self.pos, RADIUS)
        self.steerer.render(pygame, screen, self.pos)

    def update(self, screen):
        c = 30
        x_vel = (self.steerer.focus_pos[0] - self.pos[0]) / c
        y_vel = (self.steerer.focus_pos[1] - self.pos[1]) / c

        self.pos[0] += x_vel
        self.pos[1] += y_vel

        self.add_position()

        if self.pos[0] > screen.get_width():
            self.pos[0] = 0
        elif self.pos[0] < 0:
            self.pos[0] = screen.get_width()

        if self.pos[1] > screen.get_height():
            self.pos[1] = 0
        elif self.pos[1] < 0:
            self.pos[1] = screen.get_height()

        self.steerer.update(self.pos)

    def add_position(self):
        if len(self.positions) > 200:
            self.positions.pop(0)
        
        self.positions.append((self.pos[0], self.pos[1]))


        


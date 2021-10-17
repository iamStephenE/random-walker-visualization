import random
import math

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (30, 144, 255)

# random radius: 20 : 50
# random angle: 0 : 360 
# random distance: radius + 10 : radius + 20

class Steerer:
    def __init__(self, w_pos):
        self.radius = random.randint(20, 50)
        self.angle = random.randint(0, 360) * (math.pi / 180)
        self.distance = random.randint(self.radius + 10, self.radius + 20)
        self.thickness = int(self.radius / 10)

        self.step = 0.1

        self.steerer_pos = [w_pos[0] + self.distance * math.cos(self.angle), w_pos[1] + self.distance * math.sin(self.angle)]
        
        self.focus_angle = random.randint(0, 360) * (math.pi / 180)
        self.focus_pos = self.calculate_focus_pos()

    def calculate_focus_pos(self):
        x = self.steerer_pos[0] + (self.radius-self.thickness/2) * math.cos(self.focus_angle)
        y = self.steerer_pos[1] + (self.radius-self.thickness/2) * math.sin(self.focus_angle)
        return [x, y]
    
    def render(self, pygame, screen, w_pos):
        pygame.draw.circle(screen, WHITE, self.steerer_pos, self.radius, width=self.thickness)
        pygame.draw.circle(screen, RED, self.focus_pos, self.thickness)
        
        x_disp = self.focus_pos[0] - w_pos[0]
        y_disp = self.focus_pos[1] - w_pos[1]
        extension_pos = (w_pos[0] + 2 * x_disp, w_pos[1] + 2 * y_disp)

        pygame.draw.line(screen, WHITE, w_pos, extension_pos, width=1)
        pygame.draw.line(screen, BLUE, w_pos, self.focus_pos, width=2)

    def update(self, w_pos):
        # change its position due to its direction of motion and rotate by an angle
        # cross product
        cp = self.cross_product(w_pos)

        # to have less spirals, make it so that the turning rate of the entire steerer system
        # is greater than the rate at which the focus (red point) turns
        self.angle += cp / 45000
        self.focus_angle += cp / 50000

        self.steerer_pos = [w_pos[0] + self.distance * math.cos(self.angle), w_pos[1] + self.distance * math.sin(self.angle)]
        self.update_focus_pos()

    def cross_product(self, w_pos):
        v1 = (self.steerer_pos[0] - self.focus_pos[0],self.steerer_pos[1] - self.focus_pos[1])
        v2 = (self.steerer_pos[0] - w_pos[0], self.steerer_pos[1] - w_pos[1])
        return v1[0] * v2[1] - v1[1] * v2[0]

    # update by moving it a random degree
    def update_focus_pos(self):
        inc = self.step if random.randint(1, 2) == 1 else -self.step
        self.focus_angle += inc
        self.focus_pos = self.calculate_focus_pos()
            




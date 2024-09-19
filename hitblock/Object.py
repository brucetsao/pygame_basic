import pygame


class Ball(object):
    def __init__(self, canvas, pos, radius):
        self.pygame = pygame
        self.canvas = canvas
        self.pos = pos
        self.radius = radius
        self.color = (100, 200, 200)
        self.visible = True
        self.rect = self.pygame.draw.circle(self.canvas, self.color, self.pos, self.radius)

    def update(self):
        if (self.visible):
            self.rect = self.pygame.draw.circle(self.canvas, self.color, self.pos, self.radius)


class Paddle(object):
    def __init__(self, canvas, rect):
        self.pygame = pygame
        self.canvas = canvas
        self.rect = rect
        self.color = (255, 255, 255)
        self.visible = True

    def update(self):
        if (self.visible):
            self.pygame.draw.rect(self.canvas, self.color, self.rect)
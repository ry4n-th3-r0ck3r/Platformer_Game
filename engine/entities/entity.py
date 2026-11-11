import pygame


class Entity:

    def __init__(self, x, y, width, height, color, solid=False):
        self.x = float(x)
        self.y = float(y)

        self.width = width
        self.height = height

        self.color = color

        self.solid = solid

    @property
    def hitbox(self):
        return pygame.Rect(
            round(self.x),
            round(self.y),
            self.width,
            self.height
        )
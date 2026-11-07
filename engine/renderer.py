import pygame


class Renderer:

    def __init__(self, screen):
        self.screen = screen

    def draw_entity(self, entity):

        rectangle = pygame.Rect(
            entity.x,
            entity.y,
            entity.width,
            entity.height
        )

        pygame.draw.rect(
            self.screen,
            entity.color,
            rectangle
        )
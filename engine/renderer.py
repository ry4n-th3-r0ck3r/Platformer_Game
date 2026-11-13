import pygame


class Renderer:

    def __init__(self, screen):
        self.screen = screen

    def draw_entity(self, entity, camera):
        # Convert world position to screen position
        screen_x, screen_y = camera.apply(entity)

        rectangle = pygame.Rect(
            round(screen_x),
            round(screen_y),
            entity.width,
            entity.height
        )

        pygame.draw.rect(
            self.screen,
            entity.color,
            rectangle
        )
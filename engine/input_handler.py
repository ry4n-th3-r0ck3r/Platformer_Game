import pygame


class InputHandler:

    def get_horizontal_input(self):

        keys = pygame.key.get_pressed()

        direction = 0

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            direction -= 1

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            direction += 1

        return direction

    def get_jump_input(self, event):

        return (
                event.type == pygame.KEYDOWN
                and event.key in (pygame.K_SPACE, pygame.K_w, pygame.K_UP)
        )
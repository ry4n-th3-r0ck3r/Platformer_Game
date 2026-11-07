import pygame
from engine.entities.entity import Entity
from engine.renderer import Renderer


class Game:

    def __init__(self):
        pygame.init()

        # Window configuration
        self.width = 800
        self.height = 600
        self.fps = 60

        # Initialize display
        self.screen = pygame.display.set_mode(
            (self.width, self.height)
        )

        pygame.display.set_caption("Platformer")

        # Game clock
        self.clock = pygame.time.Clock()

        # Initialize renderer
        self.renderer = Renderer(self.screen)

        # Store game entities
        self.entities = []

            #placeholder
        self.entities.append(
            Entity(100, 400, 32, 48, (0, 100, 255))
        )

        # Ground
        self.entities.append(
            Entity(0, 550, 800, 50, (0, 180, 0))
        )

        # Floating platforms
        self.entities.append(
            Entity(250, 450, 150, 20, (0, 180, 0))
        )

        self.entities.append(
            Entity(500, 350, 150, 20, (0, 180, 0))
        )

        # Running state
        self.running = True

    def run(self):
        while self.running:

            self.handle_events()

            self.update()

            self.render()

            self.clock.tick(self.fps)

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def render(self):

        # Clear screen
        self.screen.fill((30, 30, 30))

        # Draw entities
        for entity in self.entities:
            self.renderer.draw_entity(entity)

        # Update display
        pygame.display.flip()

        pygame.display.flip()
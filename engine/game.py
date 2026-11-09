import pygame

from engine.entities.entity import Entity
from engine.entities.player import Player
from engine.renderer import Renderer
from engine.input_handler import InputHandler


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

        # Initialize renderer
        self.renderer = Renderer(self.screen)

        # Initialize input handler
        self.input_handler = InputHandler()

        # Create player
        self.player = Player(
            100, 400, 32, 48, (0, 100, 255)
        )

        # Create entity list
        self.entities = [
            self.player,

            # Ground
            Entity(0, 550, 800, 50, (0, 180, 0)),

            # Platforms
            Entity(250, 450, 150, 20, (0, 180, 0)),
            Entity(500, 350, 150, 20, (0, 180, 0))
        ]

        # Temporary floor boundary
        self.floor_y = 550

        # Running state
        self.running = True

    def run(self):
        while self.running:
            # Limit delta time to prevent large physics jumps during frame drops
            dt = min(self.clock.tick(self.fps) / 1000.0, 0.05)

            self.handle_events()

            self.update(dt)

            self.render()

        pygame.quit()

    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif self.input_handler.get_jump_input(event):
                self.player.jump()

    def update(self, dt):

        # Horizontal input
        direction = self.input_handler.get_horizontal_input()

        self.player.velocity_x = direction * self.player.speed

        # Update player physics
        self.player.update(dt)

        # Temporary floor collision
        if self.player.y + self.player.height >= self.floor_y:
            self.player.y = self.floor_y - self.player.height

            self.player.velocity_y = 0

            self.player.grounded = True

    def render(self):

        # Clear screen
        self.screen.fill((30, 30, 30))

        # Draw entities
        for entity in self.entities:
            self.renderer.draw_entity(entity)

        # Update display
        pygame.display.flip()

        pygame.display.flip()
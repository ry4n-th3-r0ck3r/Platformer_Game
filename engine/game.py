import pygame

from engine.entities.entity import Entity
from engine.entities.player import Player
from engine.renderer import Renderer
from engine.input_handler import InputHandler
from engine.physics.collision import CollisionSystem
from engine.camera import Camera


class Game:

    def __init__(self):
        pygame.init()

        # Window configuration
        self.width = 800
        self.height = 600
        self.fps = 30

        # Initialize display
        self.screen = pygame.display.set_mode(
            (self.width, self.height)
        )
        #Initialize camera
        self.world_width = 3000
        self.world_height = 600

        self.camera = Camera(
            self.width,
            self.height,
            self.world_width,
            self.world_height
        )

        pygame.display.set_caption("Platformer")

        # Game clock
        self.clock = pygame.time.Clock()

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
            Entity(0, 550, 3000, 50, (0, 180, 0), solid=True),

            # Platforms
            Entity(250, 450, 150, 20, (0, 180, 0), solid=True),
            Entity(500, 350, 150, 20, (0, 180, 0), solid=True),

            Entity(900, 450, 150, 20, (0, 180, 0), solid=True),
            Entity(1200, 400, 150, 20, (0, 180, 0), solid=True),
            Entity(1500, 350, 150, 20, (0, 180, 0), solid=True),
            Entity(1900, 450, 150, 20, (0, 180, 0), solid=True),
            Entity(2200, 400, 150, 20, (0, 180, 0), solid=True),
            Entity(2500, 400, 150, 20, (0, 180, 0), solid=True)

        ]

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

        direction = self.input_handler.get_horizontal_input()

        self.player.velocity_x = direction * self.player.speed

        solids = [
            entity for entity in self.entities
            if entity.solid
        ]

        CollisionSystem.move(self.player, solids, dt)

        # Follow the player after updating their position
        self.camera.follow(self.player)

    def render(self):

        self.screen.fill((30, 30, 30))

        for entity in self.entities:
            self.renderer.draw_entity(entity, self.camera)

        # Update display
        pygame.display.flip()
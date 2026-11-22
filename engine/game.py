import pygame

from engine.entities.player import Player
from engine.renderer import Renderer
from engine.input_handler import InputHandler
from engine.physics.collision import CollisionSystem
from engine.camera import Camera
from pathlib import Path
from engine.levels.level_loader import LevelLoader
from engine.levels.level_manager import LevelManager


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

        pygame.display.set_caption("Platformer")

        # Game clock
        self.clock = pygame.time.Clock()

        # Initialize renderer
        self.renderer = Renderer(self.screen)

        # Initialize input handler
        self.input_handler = InputHandler()

        # Locate our level directory
        project_root = Path(__file__).resolve().parent.parent

        level_directory = project_root / "assets" / "levels"

        # Initialize level management
        self.level_manager = LevelManager(level_directory)

        # Register available levels
        self.level_manager.register_level("level_01.json")
        self.level_manager.register_level("level_02.json")

        # Load the first level
        self.level = self.level_manager.load_level(0)

        # Create the player at the level's spawn position
        self.player = Player(
            self.level.spawn_x,
            self.level.spawn_y,
            32,
            48,
            (0, 100, 255)
        )

        #Sets camera
        self.camera = Camera(
            self.width,
            self.height,
            self.level.width,
            self.level.height
        )

        # Combine the player with the level's entities
        self.entities = [self.player] + self.level.entities

        # Running state
        self.running = True

    def next_level(self):

        # Load the next level
        self.level = self.level_manager.next_level()

        # Reset player position
        self.player.x = float(self.level.spawn_x)
        self.player.y = float(self.level.spawn_y)

        # Reset movement and physics state
        self.player.velocity_x = 0
        self.player.velocity_y = 0
        self.player.grounded = False

        # Replace old level entities
        self.entities = [self.player] + self.level.entities

        # Update camera world dimensions
        self.camera.world_width = self.level.width
        self.camera.world_height = self.level.height

        # Immediately reposition camera
        self.camera.follow(self.player)

        print(
            f"Loaded level {self.level_manager.current_index + 1}"
        )

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

            # Switch to the next level when N is pressed
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                self.next_level()

            # Handle jumping
            elif self.input_handler.get_jump_input(event):
                self.player.jump()

    def update(self, dt):

        # Process horizontal input
        direction = self.input_handler.get_horizontal_input()

        self.player.velocity_x = direction * self.player.speed

        # Retrieve solid objects from the current level
        solids = self.level.get_solids()

        # Update player physics and resolve collisions
        CollisionSystem.move(self.player, solids, dt)

        # Update camera position
        self.camera.follow(self.player)

        CollisionSystem.move(self.player, solids, dt)

        # Follow the player after updating their position
        self.camera.follow(self.player)

    def render(self):

        self.screen.fill((30, 30, 30))

        for entity in self.entities:
            self.renderer.draw_entity(entity, self.camera)

        # Update display
        pygame.display.flip()
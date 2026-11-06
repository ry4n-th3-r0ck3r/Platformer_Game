import pygame


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

        pygame.display.set_caption("Platformer Game")

        # Game clock
        self.clock = pygame.time.Clock()

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
        self.screen.fill((30, 30, 30))

        pygame.display.flip()
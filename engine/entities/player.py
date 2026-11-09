from engine.entities.entity import Entity


class Player(Entity):

    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)

        # Horizontal movement
        self.speed = 250
        self.velocity_x = 0

        # Vertical movement
        self.velocity_y = 0
        self.gravity = 1200
        self.jump_strength = -500

        # Player state
        self.grounded = False

    def jump(self):
        if self.grounded:
            self.velocity_y = self.jump_strength
            self.grounded = False

    def update(self, dt):

        # Horizontal movement
        self.x += self.velocity_x * dt

        # Apply gravity
        self.velocity_y += self.gravity * dt

        # Vertical movement
        self.y += self.velocity_y * dt
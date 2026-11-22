from engine.entities.entity import Entity


class Player(Entity):

    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)

        # Horizontal movement
        self.speed = 200
        self.velocity_x = 0

        # Vertical movement
        self.velocity_y = 0
        self.gravity = 1000
        self.jump_strength = -500

        # Player state
        self.grounded = False

    def jump(self):
        if self.grounded:
            self.velocity_y = self.jump_strength
            self.grounded = False

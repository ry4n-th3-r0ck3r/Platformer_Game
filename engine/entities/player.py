from engine.entities.entity import Entity


class Player(Entity):

    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)

        self.speed = 250

        self.velocity_x = 0

    def update(self, dt):
        # Delta time (dt) is the elapsed time between frames in seconds.
        # Multiplying velocity by dt keeps movement consistent regardless of frame rate.
        self.x += self.velocity_x * dt
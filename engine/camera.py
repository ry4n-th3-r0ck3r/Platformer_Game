class Camera:

    def __init__(self, width, height, world_width, world_height):
        self.x = 0
        self.y = 0

        self.width = width
        self.height = height

        self.world_width = world_width
        self.world_height = world_height

    def follow(self, target):

        # Center camera on target
        target_x = target.x + target.width / 2 - self.width / 2
        target_y = target.y + target.height / 2 - self.height / 2

        # Keep camera within world boundaries
        self.x = max(
            0,
            min(target_x, max(0, self.world_width - self.width))
        )

        self.y = max(
            0,
            min(target_y, max(0, self.world_height - self.height))
        )

    def apply(self, entity):
        return entity.x - self.x, entity.y - self.y
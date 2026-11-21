class Level:

    def __init__(self, width, height, entities, spawn_x, spawn_y):

        # World dimensions
        self.width = width
        self.height = height

        # Entities belonging to this level
        self.entities = entities

        # Player starting position
        self.spawn_x = spawn_x
        self.spawn_y = spawn_y

    def get_solids(self):

        # Return entities that participate in solid collisions
        return [
            entity for entity in self.entities
            if entity.solid
        ]
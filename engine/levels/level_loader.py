import json
from pathlib import Path

from engine.entities.entity_factory import EntityFactory
from engine.levels.level import Level


class LevelLoader:

    @staticmethod
    def load(file_path):

        # Convert the supplied path into a Path object
        file_path = Path(file_path)

        # Read the JSON file
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        # Extract level dimensions
        width = data["width"]
        height = data["height"]

        # Extract player spawn coordinates
        spawn_x = data["player_spawn"]["x"]
        spawn_y = data["player_spawn"]["y"]

        # Construct entities through the factory
        entities = [
            EntityFactory.create(entity_data)
            for entity_data in data["entities"]
        ]

        # Return the completed level
        return Level(
            width=width,
            height=height,
            entities=entities,
            spawn_x=spawn_x,
            spawn_y=spawn_y
        )
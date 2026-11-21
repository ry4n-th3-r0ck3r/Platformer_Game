import json
from pathlib import Path

from engine.entities.entity import Entity
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

        # Store the entities created from JSON
        entities = []

        # Convert JSON definitions into Python objects
        for entity_data in data["entities"]:

            entity_type = entity_data["type"]

            if entity_type == "platform":

                entity = Entity(
                    x=entity_data["x"],
                    y=entity_data["y"],
                    width=entity_data["width"],
                    height=entity_data["height"],
                    color=tuple(entity_data["color"]),
                    solid=entity_data["solid"]
                )

                entities.append(entity)

            else:
                raise ValueError(
                    f"Unsupported entity type: {entity_type}"
                )

        # Construct the completed level
        return Level(
            width=width,
            height=height,
            entities=entities,
            spawn_x=spawn_x,
            spawn_y=spawn_y
        )
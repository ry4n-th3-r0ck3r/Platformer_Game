from pathlib import Path

from engine.levels.level_loader import LevelLoader


class LevelManager:

    def __init__(self, level_directory):

        self.level_directory = Path(level_directory)

        # Registered level filenames
        self.levels = []

        # Currently active level
        self.current_level = None

        # Index of the active level
        self.current_index = 0

    def register_level(self, filename):

        level_path = self.level_directory / filename

        if not level_path.is_file():
            raise FileNotFoundError(
                f"Level file not found: {level_path}"
            )

        self.levels.append(filename)

    def load_level(self, index):

        if not 0 <= index < len(self.levels):
            raise IndexError("Invalid level index")

        filename = self.levels[index]

        level_path = self.level_directory / filename

        # Construct the level from its JSON definition
        level = LevelLoader.load(level_path)

        # Update the active level only after loading succeeds
        self.current_level = level
        self.current_index = index

        return level

    def next_level(self):

        if not self.levels:
            raise ValueError("No levels registered")

        # Wrap around to the first level
        next_index = (
            self.current_index + 1
        ) % len(self.levels)

        return self.load_level(next_index)
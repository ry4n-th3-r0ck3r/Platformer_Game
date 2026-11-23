from engine.entities.entity import Entity


class EntityFactory:

    # Registry of supported entity types
    _registry = {}

    @classmethod
    def register(cls, entity_type, constructor):

        # Prevent accidental duplicate registrations
        if entity_type in cls._registry:
            raise ValueError(
                f"Entity type already registered: {entity_type}"
            )

        cls._registry[entity_type] = constructor

    @classmethod
    def create(cls, entity_data):

        entity_type = entity_data["type"]

        # Verify that the entity type is supported
        if entity_type not in cls._registry:
            raise ValueError(
                f"Unsupported entity type: {entity_type}"
            )

        # Retrieve the registered constructor
        constructor = cls._registry[entity_type]

        # Construct and return the entity
        return constructor(entity_data)


# Register our existing platform type
EntityFactory.register(
    "platform",
    lambda data: Entity(
        x=data["x"],
        y=data["y"],
        width=data["width"],
        height=data["height"],
        color=tuple(data["color"]),
        solid=data["solid"]
    )
)
class CollisionSystem:

    @staticmethod
    def move(entity, solids, dt):

        # HORIZONTAL MOVEMENT

        previous_x = entity.x

        # Calculate new horizontal position
        entity.x += entity.velocity_x * dt

        for solid in solids:

            # Check vertical overlap using floating-point coordinates
            vertical_overlap = (
                    entity.y < solid.y + solid.height
                    and entity.y + entity.height > solid.y
            )

            if not vertical_overlap:
                continue

            # Moving right: check if player crossed the platform's left edge
            if (
                    entity.velocity_x > 0
                    and previous_x + entity.width <= solid.x <= entity.x + entity.width
            ):
                entity.x = solid.x - entity.width
                entity.velocity_x = 0

            # Moving left: check if player crossed the platform's right edge
            elif (
                    entity.velocity_x < 0
                    and previous_x >= solid.x + solid.width >= entity.x
            ):
                entity.x = solid.x + solid.width
                entity.velocity_x = 0

        # VERTICAL MOVEMENT

        previous_y = entity.y

        # Calculate displacement using current velocity and gravity
        entity.y += (
                entity.velocity_y * dt
                + 0.5 * entity.gravity * dt * dt
        )

        # Update velocity for the next frame
        entity.velocity_y += entity.gravity * dt

        for solid in solids:

            # Check overlap using floating-point coordinates
            horizontal_overlap = (
                entity.x < solid.x + solid.width
                and entity.x + entity.width > solid.x
            )

            if not horizontal_overlap:
                continue

            # Landing on a platform
            if (
                    entity.velocity_y >= 0
                    and previous_y + entity.height <= solid.y <= entity.y + entity.height
            ):
                entity.y = solid.y - entity.height
                entity.velocity_y = 0
                entity.grounded = True

            # Hitting the underside of a platform
            elif (
                    entity.velocity_y < 0
                    and previous_y >= solid.y + solid.height >= entity.y
            ):
                entity.y = solid.y + solid.height
                entity.velocity_y = 0
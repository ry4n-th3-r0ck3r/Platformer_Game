class CollisionSystem:

    @staticmethod
    def move(entity, solids, dt):

        # HORIZONTAL MOVEMENT

        previous_x = entity.x
        entity.x += entity.velocity_x * dt

        for solid in solids:

            if entity.hitbox.colliderect(solid.hitbox):

                # Collision from the left
                if (
                    entity.velocity_x > 0
                    and previous_x + entity.width <= solid.x
                ):
                    entity.x = solid.x - entity.width
                    entity.velocity_x = 0

                # Collision from the right
                elif (
                    entity.velocity_x < 0
                    and previous_x >= solid.x + solid.width
                ):
                    entity.x = solid.x + solid.width
                    entity.velocity_x = 0

        # VERTICAL MOVEMENT

        entity.velocity_y += entity.gravity * dt

        previous_y = entity.y
        entity.y += entity.velocity_y * dt

        entity.grounded = False

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
                and previous_y + entity.height <= solid.y
                and entity.y + entity.height >= solid.y
            ):
                entity.y = solid.y - entity.height
                entity.velocity_y = 0
                entity.grounded = True

            # Hitting the underside of a platform
            elif (
                entity.velocity_y < 0
                and previous_y >= solid.y + solid.height
                and entity.y <= solid.y + solid.height
            ):
                entity.y = solid.y + solid.height
                entity.velocity_y = 0
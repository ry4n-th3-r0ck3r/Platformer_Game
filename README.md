# 2D Platformer Engine

## Overview

A modular 2D side-scrolling platformer engine developed using Python and Pygame.

The goal of this project is to create a reusable foundation for developing 2D platformer games. The engine will handle core functionality such as rendering, movement, physics, collision detection, and level management while allowing developers to customize graphics, gameplay mechanics, and additional systems.

This project follows an incremental, Agile development approach, with new features introduced and tested individually.

## Technologies

- Python 3.12
- Pygame
- PyCharm
- Git and GitHub

## Planned Sprints


Sprint 1: Core Game Loop

Status: Complete

Initialize Pygame.

Create the application window.

Implement the main game loop.

Handle application events.

Implement frame rate limiting.

Ensure clean application shutdown.

*****************************************

Sprint 2: Basic Rendering System

Status: Complete

Implement a basic Entity class.

Implement a dedicated Renderer class.

Separate entity data from rendering logic.

Support rendering multiple entities.

Display placeholder objects using colored rectangles.

Planned Sprints

*****************************************

Sprint 3: Player Movement

Status: Complete

Implement a Player class.

Introduce keyboard input handling.

Support horizontal player movement.

Separate input processing from movement logic.

Implement frame-independent movement.

*****************************************

Sprint 4: Gravity and Jumping

Status: Current

Introduce vertical velocity.

Implement gravity.

Implement jumping mechanics.

Establish basic physics parameters.

*****************************************

Sprint 5: Collision Detection

Status: Planned

Implement collision detection between entities.

Resolve collisions with solid surfaces.

Prevent movement through walls and platforms.

Implement grounded-state detection.

*****************************************

Sprint 6: Camera System

Status: Planned

Implement a scrolling camera.

Support levels larger than the game window.

Track the player as they move through the world.

Separate world coordinates from screen coordinates.

*****************************************

Sprint 7: Level Management

Status: Planned

Implement a Level class.

Introduce tile-based environments.

Support loading levels from external files.

Separate level data from engine functionality.

*****************************************

Sprint 8: Sprite and Animation Support

Status: Planned

Load external image assets.

Replace placeholder rectangles with sprites.

Implement basic sprite animations.

Maintain separation between rendering and game logic.

*****************************************

Sprint 9: Entity Management

Status: Planned

Expand the entity system.

Support multiple entity types.

Introduce basic enemy entities.

Support entity creation and removal during gameplay.

*****************************************

Sprint 10: Engine Extensibility

Status: Planned

Evaluate the existing architecture.

Establish interfaces for optional gameplay systems.

Support extending entities with additional functionality.

Demonstrate modularity through a simple optional system.

Refactor existing components where necessary.

*****************************************

## Project Goals

- Develop a reusable 2D platformer engine.
- Maintain a modular and extensible architecture.
- Separate game logic from graphics and rendering.
- Support customizable sprites, levels, and gameplay mechanics.
- Allow additional systems, such as inventories and combat mechanics, to be implemented independently.
- Maintain a functioning engine throughout development.

## Installation

Clone the repository and navigate to the project directory.

Install Pygame:

```bash
python -m pip install pygame
```

Run the application:

```bash
python main.py
```

## Development Status

**Current Version:** 0.2.0

**Current Sprint:** Sprint 3 — Basic Rendering System

This project is under active development. Features and architecture may change as development progresses.

## Development Philosophy

The engine is designed around modularity, reusability, and incremental improvement.

Each development sprint focuses on implementing and testing a specific component before introducing additional functionality.
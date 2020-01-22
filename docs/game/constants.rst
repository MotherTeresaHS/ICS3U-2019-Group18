.. _constants:

Constants
==========

Before you start programming, you will need to create a file with constants in it. This file will be unchangeable from your code.py file to avoid inconsistencies in your code. Here are a few of the constants you will need:

- The size of the screen along the X axis
- The size of the screen along the Y axis
- The number of grid spaces along the X axis
- The number of grid spaces along the Y axis
- The size of your sprites
- The movement speed of the spaceship
- Coordinates for off the top of the screen
- Coordinates for off the left of the screen
- Coordinates for off the right of the screen
- Coordinates for off the bottom of the screen
- A cap for the amount of lasers you want
- A cap for the amount of asteroids you have per side of screen
- The X coordinate for sprites being stored off screen
- The Y coordinate for sprites being stored off screen
- The speed of the asteroids
- The speed of the lasers
- Another laser speed to feel consistent with lasers moving upwards during the 360 degree spread shot

Remember when creating your constants that they should all be written in capitals to distinguish them from other variables in your program.

.. code-block:: python
  :linenos:

    SCREEN_X = 160
    SCREEN_Y = 128
    SCREEN_GRID_X = 16
    SCREEN_GRID_Y = 8
    SPRITE_SIZE = 16
    SHIP_MOVEMENT_SPEED = 1
    OFF_TOP_SCREEN = -1 - SPRITE_SIZE
    OFF_LEFT_SCREEN = -1 - SPRITE_SIZE
    OFF_RIGHT_SCREEN = SCREEN_X + SPRITE_SIZE
    OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE
    LASER_CREATION_TOTAL = 8
    ASTEROID_CREATION_TOTAL = 3
    OFF_SCREEN_X = -500
    OFF_SCREEN_Y = -100
    ASTEROID_SPEED = 1
    LASER_SPEED = 2
    EXTRA_LASER_SPEED = 3

You will also want colour palettes for your text. Two will be provided here: one for the MT Studios splash scene, while the other is a more generic score palette.

.. code-block:: python
  :linenos:

    MT_GAME_STUDIO_PALETTE = (b'\xf8\x1f\x00\x00\xcey\x00\xff\xf8\x1f\xff\x19\xfc\xe0\xfd\xe0'
       b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

    SCORE_PALETTE = (b'\xf8\x1f\x00\x00\xcey\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
       b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

The last thing you will want in your constants file should be a list to keep track of the four button states: up (not pressed), just pressed, still pressed, and released.

.. code-block:: python
  :linenos:

    # Using for button state
    button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released",
    }

Once you have your constants file you should be able to start programming your actual game.
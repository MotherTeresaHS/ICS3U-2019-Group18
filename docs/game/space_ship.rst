.. _space_ship:

Space Ship
==========

The next step is to get your spaceship working. You have to start by creating a list that will hold your primary sprites (namely your spaceship). You will then need to create your spaceship sprite and append it to the list in the 0th position. Remember, this is done outside your game loop.

.. code-block:: python
  :linenos:

    # This list contains the primary sprites
    sprites = []

    # Creating spaceship sprite
    ship = stage.Sprite(image_bank_1, 14, 75, 56)
    sprites.insert(0, ship)

You will need to paint your sprite onto the screen. You can do this by adding your sprite list in front of your background. 

.. code-block:: python
  :linenos:

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = sprites + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

The next thing you will need to do to ensure it continues to show up is to have it rendered on screen. You do this at the bottom of the inside of your game loop.

.. code-block:: python
  :linenos:

    game.render_sprites(sprites)
    game.tick()

You will want to make sure your spaceship will be able to move, and keep it from moving off screen. This is all done in the game loop. The first thing you have to do is to set your keys to be watching if a button is being pressed. Next, since your user will be using the D-Pad to move around, you will want to add an if statement to detect if a specific button on the D-Pad. 
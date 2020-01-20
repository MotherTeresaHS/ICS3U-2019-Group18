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

You will need to paint and render any new sprite list you add using the same methods. Finally, you will want to make sure your spaceship will be able to move, and keep it from moving off screen. This is all done in the game loop. The first thing you have to do is to set your keys to be watching if a button is being pressed. Next, since your user will be using the D-Pad to move around, you will want to add an if statement to detect if a specific button on the D-Pad. Depending on which button is pressed, your spaceship will move in a different direction. You will also want to make sure your spaceship can't move off screen. You can do this by putting an if statement inside your previous if statement. If the ship's X or Y coordinates goes off the screen limits indicated in your constants file, it will move the ship back on screen. There is also a variable that is changed each time a button on the D-Pad is pressed. This variable will be used later to determine the directions the lasers fire.

.. code-block:: python
  :linenos:

        # get user input
        keys = ugame.buttons.get_pressed()

        # Move ship right
        if keys & ugame.K_RIGHT:
            state_of_button = 2
            if ship.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
            else:
                ship.move(ship.x + constants.SHIP_MOVEMENT_SPEED, ship.y)
            pass

        # Move ship left
        if keys & ugame.K_LEFT:
            state_of_button = 4
            if ship.x < 0:
                ship.move(0, ship.y)
            else:
                ship.move(ship.x - constants.SHIP_MOVEMENT_SPEED, ship.y)
            pass

        # Move ship up
        if keys & ugame.K_UP:
            state_of_button = 1
            if ship.y < 0:
                ship.move(ship.x, 0)
            else:
                ship.move(ship.x, ship.y - constants.SHIP_MOVEMENT_SPEED)
            pass

        # Move ship down
        if keys & ugame.K_DOWN:
            state_of_button = 3
            if ship.y > constants.SCREEN_Y - constants.SPRITE_SIZE:
                ship.move(ship.x, constants.SCREEN_Y - constants.SPRITE_SIZE)
            else:
                ship.move(ship.x, ship.y + constants.SHIP_MOVEMENT_SPEED)
            pass

Your spaceship should now be able to move properly without going off screen.
.. _background:

Background
==========

The first thing you will want to do is get the background working on your game scene. You must first set the image bank to be the gamesprite image bank. Use a for loop to place the background tile throughout the screen. Be sure this is set under your game scene function.

.. code-block:: python
  :linenos:

    # The image bank for the game
    image_bank_1 = stage.Bank.from_bmp16("gamesprite.bmp")

    # sets the background to image 1 in the bank
    background = stage.Grid(image_bank_1, 10, 8)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_X):
            background.tile(x_location, y_location, 0)

The next thing to do is to make sure the background is rendered on your game. You will need to set your framerate to 60, then set your game layers. You may not have any other layers than your background right now, however when you do add more be sure that the background layer is always the last one referenced. The final thing you need to do is render your game. These few lines of code should be placed just above the game function's game loop.

.. code-block:: python
  :linenos:

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

You should now have a functioning background. Your initial game scene should look something like this:

.. code-block:: python
  :linenos:

    game_scene():
        # This is the game scene for Asteroid Dodger
        
        # The image bank for the game
        image_bank_1 = stage.Bank.from_bmp16("gamesprite.bmp")

        # sets the background to image 1 in the bank
        background = stage.Grid(image_bank_1, 10, 8)
        for x_location in range(constants.SCREEN_GRID_X):
            for y_location in range(constants.SCREEN_GRID_X):
                background.tile(x_location, y_location, 0)
        
        # create a stage for the background to show up on
        #   and set the frame rate to 60fps
        game = stage.Stage(ugame.display, 60)
        # set the layers, items show up in order
        game.layers = [background]
        # render the background and inital location of sprite list
        # most likely you will only render background once per scene
        game.render_block()
        
        # Game loop
        while True:
            # Get user input
            
            # Update game logic
            
            # Redraw sprite list
            pass
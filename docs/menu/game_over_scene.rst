.. _game_over_scene:

Game Over Scene
===============

The game over scene is the scene that the game scene will swap to once the player's spaceship has collided with an asteroid. The first thing you will need to do is set the image bank to be the gamesprites image bank. To set your background, use a for loop to itterate through all the on screen tiles and place a black background.

.. code-block:: python
  :linenos:

    # The image bank for the game
    image_bank_1 = stage.Bank.from_bmp16("gamesprite.bmp")

    # sets the background to image 1 in the bank
    background = stage.Grid(image_bank_1, 10, 8)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_X):
            background.tile(x_location, y_location, 1)

Before I continue explaining how to place more items on screen, we should stop and make sure that we have all the information we need to display. When the game scene swapped to the game over scene, it passed two variables: one with the amount of asteroids the player destroyed and the other being the exact epoch time that the game scene was activated. Epoch time is the exat amount of time in seconds that has passed since January 1st, 1970. We can use this to calculate the amount of time the player survived by subtracting the game start epoch time from the epoch time the game over scene activated, subtracting an additional 4 from the amount of seconds the game scene stopped after the asteroid collided witht the spaceship. Your answer will be how long the player survived in seconds.

.. code-block:: python
  :linenos:

    # Converting epoch time to seconds
    seconds_survived = time.time() - time_start - 4

The next thing to display on screen is the text: the game over text, the number of asteroids destroyed text, and the time survived text. You will need to create a list to hold the text you create. Next create the text with the desired dimensions, palette (mt game studios palette), and coordinates. Append your text to the list. For the amount of asteroids destroyed text, display the asteroids destroyed variable passed into the game over scene function by the game scene function. To display the time the player survived in seconds, display the time survived variable that you performed the caluclations with in the step above.

.. code-block:: python
  :linenos:

    # The list that holds all the text
    text = []

    # The game over text
    text1 = stage.Text(width=37, height=22, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(50, 5)
    text1.text("Game Over")
    text.append(text1)

    # This text displays how many asteroids the user destroyed
    text2 = stage.Text(width=37, height=22, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(5, 40)
    text2.text("Asteroids Shot: {0}".format(asteroids_destroyed))
    text.append(text2)

    # This text displays how many asteroids the user destroyed
    text3 = stage.Text(width=37, height=22, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text3.move(5, 80)
    text3.text("Alive: {0} seconds".format(seconds_survived))
    text.append(text3)

The last thing to do is to be sure that your frame rate is 60, and that your text and background have been properly layered and rendered on screen.

.. code-block:: python
  :linenos:

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

Your game over scene should now be working.
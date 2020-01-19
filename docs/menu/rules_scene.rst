.. _rules_scene:

Rules Scene
===========

In this scene you can see the rules on how to play Asteroid Dodger. The first thing you will need to do is set the image bank to be the gamesprites image bank. To set your background, use a for loop to itterate through all the on screen tiles and place a black background.

.. code-block:: python
  :linenos:

    # The image bank for the game
    image_bank_1 = stage.Bank.from_bmp16("gamesprite.bmp")

    # sets the background to image 1 in the bank
    background = stage.Grid(image_bank_1, 10, 8)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_X):
            background.tile(x_location, y_location, 1)

You will need to display all your rules text and a title for your scene. You will need to create a list to hold the text you create. Next create the text with the desired dimensions, palette (mt game studios palette), and coordinates. Append your text to the list. If you run out of room in a particular line to display it on screen, be sure that the next line is closer to the previous one to make it look like a continuation rather than a new rule.

.. code-block:: python
  :linenos:

    # The list that holds all the text
    text = []

    # The following text displays all the game rules
    text1 = stage.Text(width=37, height=22, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(50, 5)
    text1.text("Rules")
    text.append(text1)

    text2 = stage.Text(width=34, height=19, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(0, 20)
    text2.text("Use D-Pad to move")
    text.append(text2)

    text3 = stage.Text(width=34, height=19, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text3.move(0, 35)
    text3.text("Touch ammo to pickup")
    text.append(text3)

    text4 = stage.Text(width=34, height=19, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text4.move(0, 50)
    text4.text("Release 'A' to shoot")
    text.append(text4)

    text5 = stage.Text(width=34, height=19, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text5.move(0, 65)
    text5.text("Game ends when")
    text.append(text5)

    text6 = stage.Text(width=34, height=19, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text6.move(0, 75)
    text6.text("hit by asteroid")
    text.append(text6)

    text7 = stage.Text(width=34, height=19, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text7.move(15, 105)
    text7.text("'Start' to begin")
    text.append(text7)

The next thing you will need to do is to be sure that your frame rate is 60, and that your text and background have been properly layered and rendered on screen.

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

The last thing you will need to do is to make sure you can get to your game scene. In your game loop, set keys to detect whether or not a button has been pressed. Use an if statement to detect if the start button has been pressed. If the start button has been pressed, swap to the game scene by calling the game scene function.

.. code-block:: python
  :linenos:

        # get user input
        keys = ugame.buttons.get_pressed()

        # update game logic
        if keys & ugame.K_START != 0:  # Start button
            keys = 0
            ugame.K_START = 0
            game_scene()
            pass

If these instructions were followed correctly, your rules scene should now work.
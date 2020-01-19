.. _menu_scene:

Menu Scene
===========

The menu scene is how you get into the main game or look at the rules. Like all scenes previous, the first thing that needs to be done is to set the image bank, which in this case is the gamesprites image bank. You must then use a for loop to itterate through each tile and place a plain blank tile as the background.

.. code-block:: python
  :linenos:

    # The image bank for the game
    image_bank_1 = stage.Bank.from_bmp16("gamesprite.bmp")

    # sets the background to image 1 in the bank
    background = stage.Grid(image_bank_1, 10, 8)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_X):
            background.tile(x_location, y_location, 1)

You will also need to set up button detection for the start and select buttons, as they will be how you swap scenes later on.

.. code-block:: python
  :linenos:

    # Reupdating keys
    keys = 0

    # Buttons to keep state information on
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

There are also three instances of text: the title, and two instructional texts, one reading 'press start to begin' and the other saying 'press select for rules'. Like previous scenes, you must create a list to contain the text. Then create the text with the appropriate dimensions, palette (mt game studios palette), and coordinates. Append each text to the list.

.. code-block:: python
  :linenos:

    # The list that holds all the text
    text = []

    text1 = stage.Text(width=37, height=22, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(20, 20)
    text1.text("Asteroid Dodger")
    text.append(text1)

    text2 = stage.Text(width=37, height=22, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(15, 80)
    text2.text("'Start' to begin")
    text.append(text2)

    text3 = stage.Text(width=37, height=22, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text3.move(8, 100)
    text3.text("'Select' for rules")
    text.append(text3)

You will then need to make a larger model of the game scene spaceship show up on this scene. To do this, create a list to hold your sprites, then append the left and right sides of the spaceship to the list. Line up the coordinates so that the two sprites connect to create a larger scale spaceship.

.. code-block:: python
  :linenos:

    # This list keeps all the sprites
    sprites = []

    # Adding the left and right of the ship to the sprite list
    ship_left = stage.Sprite(image_bank_1, 11, 64, 45)
    sprites.append(ship_left)
    ship_right = stage.Sprite(image_bank_1, 12, 80, 45)
    sprites.append(ship_right)

As it is for every other scene, you must once again set your frame rate to 60, paint the sprite, text and background layers and render the initial scene screen.

.. code-block:: python
  :linenos:

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + sprites + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

Next you must get the start and select buttons working. In your game loop, set keys to detect if either of the two buttons are pressed. Use an if statement to detect whether the start button is pressed or not. If the start button is pressed, swap to the game scene by calling the game scene function.

.. code-block:: python
  :linenos:

        # get user input
        keys = ugame.buttons.get_pressed()

        # update game logic
        if keys & ugame.K_START != 0:  # Start button
            keys = 0
            ugame.K_START = 0
            game_scene()
            break

Now use another if statement to detect if the select button has been pressed. If the select button is pressed, swap to the rules scene by calling the rules scene function.

.. code-block:: python
  :linenos:

        if keys & ugame.K_SELECT != 0:  # Select button
            keys = 0
            ugame.K_SELECT = 0
            rules_scene()
            break

Also insert a render into your game loop to ensure that the sprites on screen stay rendered.

.. code-block:: python
  :linenos:

        # redraw sprite list
        game.render_sprites(sprites)
        game.tick()

You should now have a properly functioning menu scene.
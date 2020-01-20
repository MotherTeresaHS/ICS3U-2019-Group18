.. _snakob_scene:

Snakob Splash Scene
===================

The second company to make Asteroid Dodger is Snakob Studios. They are the main creators of the game, and will be the second splash scene to appear. Like the other splash scene, you must first set an image bank. The image bank this time will be the splash scene image bank. Then set the background of the screen to be the first image in the image bank. In this case, the background will be plain black.

.. code-block:: python
  :linenos:

    # Splash screen image bank
    image_bank_3 = stage.Bank.from_bmp16("splash_scene.bmp")

    # sets the background to image 1 in the bank
    background = stage.Grid(image_bank_3, constants.SCREEN_GRID_X, \
                            constants.SCREEN_GRID_Y)

You must also display the Snakob Studios title text. Similar to the MT splash scene, create a list to hold all your text. Create the text with proper dimensions, palette, and coordinates, then append it to the list.

.. code-block:: python
  :linenos:

    # This list holds the text
    text = []

    # The Snakob Studios text
    text1 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(25, 20)
    text1.text("Snakob Studios")
    text.append(text1)

For the Snakob Studios logo, instead of setting individual background tiles, they will be interlinked sprites to form in an image. Create a list to hold all the sprites. Then append each piece of the Snakob logo to the list. Be sure it is in its proper coordinates to interlock correctly with the other sprites.

.. code-block:: python
  :linenos:

    # This list holds the sprites for snakob
    sprites =[]

    # These sprites connect to create snakob
    bottom_left = stage.Sprite(image_bank_3, 13, 65, 100)
    sprites.append(bottom_left)

    mid_tail = stage.Sprite(image_bank_3, 14, 81, 100)
    sprites.append(mid_tail)

    mid_left_neck = stage.Sprite(image_bank_3, 9, 65, 84)
    sprites.append(mid_left_neck)

    mid_right_neck = stage.Sprite(image_bank_3, 10, 81, 84)
    sprites.append(mid_right_neck)

    mid_left_side_face = stage.Sprite(image_bank_3, 5, 65, 68)
    sprites.append(mid_left_side_face)

    right_eye = stage.Sprite(image_bank_3, 6, 81, 68)
    sprites.append(right_eye)

    left_side_face = stage.Sprite(image_bank_3, 4, 49, 68)
    sprites.append(left_side_face)

    end_of_tongue = stage.Sprite(image_bank_3, 7, 97, 68)
    sprites.append(end_of_tongue)

    top_of_left_eye = stage.Sprite(image_bank_3, 1, 65, 52)
    sprites.append(top_of_left_eye)

    end_of_tail = stage.Sprite(image_bank_3, 3, 97, 52)
    sprites.append(end_of_tail)

    left_eyebrow = stage.Sprite(image_bank_3, 2, 81, 52)
    sprites.append(left_eyebrow)
    
    bulky_part_tail = stage.Sprite(image_bank_3, 8, 49, 84)
    sprites.append(bulky_part_tail)
    
    lower_tail = stage.Sprite(image_bank_3, 12, 49, 100)
    sprites.append(lower_tail)
    
    extra_pixels = stage.Sprite(image_bank_3, 15, 96, 100)
    sprites.append(extra_pixels)

You will also need to get Snakob's hissing sound working. To do this, open the hiss sound file in the snakob splash scene, then define your sound variable. Be sure that your sound is not muted before you play the sound file.

.. code-block:: python
  :linenos:

    # Get sounds ready
    hiss_sound = open("hiss.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(hiss_sound)

The next thing to do is to make sure all your sprites, text, and background tiles are set properly. Similar to what you did in the MT splash scene, paint them on the proper layers, set the frame rate to 60, and render the initial position of the sprites and text.

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

The final thing to do is make a timer to swap out of the Snakob splash scene. You can do this by adding a time.sleep() for three seconds in your game loop, then call the menu scene. You will also need to make sure your sprites remain rendered on screen.

.. code-block:: python
  :linenos:

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic
        time.sleep(3.0)
        menu_scene()

        # redraw sprite list
        game.render_sprites(sprites)
        game.tick()

You should now have a working Snakob Studios splash scene.
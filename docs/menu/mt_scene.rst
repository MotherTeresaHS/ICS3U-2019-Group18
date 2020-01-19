.. _mt_scene:

MT Splash Scene
==============

Asteroid Dodger has two studios to its name: it was made by Snakob Studios, and distributed by MT Game Studios. Each has a splash scene before the actual menu shows up. The MT Game Studios splash scene shows up first. The first thing you must do is establish an image bank for this scene. You must use the mt game studios image bank. Then set the background of the screen to be the first image in the image bank. In this case, the background will be plain white.

.. code-block:: python
  :linenos:

    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)

You must then make sure the MT Game Studios logo displays. You can do this to set individual tiles from your image bank to different spots on the screen. If the pieces are fitted together properly, the image on screen will be the MT Game Studios logo.

.. code-block:: python
  :linenos:

    # used this program to split the image into tile:
    #    https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

You must also display the title of the studio on screen. You must first create a list to store all your text. Then create the text by establishing its font, size, palette (mt game studios palette in your constants file), and its location. Append your text to the text list.

.. code-block:: python
  :linenos:

    text = []

    text1 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

The next thing you will want to do is to get the sound ready. Open the coin sound file in the MT splash scene, then define your sound variable. Be sure that your sound is not muted before you play the sound file.

.. code-block:: python
  :linenos:

    # get sound ready
    # Use this guide to convert your other sounds to something that will work
    #    https://learn.adafruit.com/microcontroller-compatible-audio-file-
    #    conversion
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

For any of your text or background tiles to appear they must be painted on the screen. You can do this by modifying your initial game layer. be sure your text is in front of your background. You will also need to set the frame rate to 60, and render your text and background on screen.

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

In your game loop, have a time.sleep() for three seconds to keep the MT Game Studios scene up for three seconds. After three seconds, call the next splash scene to swap scenes.

.. code-block:: python
  :linenos:

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 3 seconds
        time.sleep(3.0)
        game_splash_screen()

        # redraw sprite list

You should now have a fully functional MT Game Studios splash scene.
.. _background:

Background
==========

The first thing you will want to do is get the background working on your game scene. You must first set the image bank to be the game scene image bank.

.. code-block:: python
  :linenos:

    # The image bank for the game
    image_bank_1 = stage.Bank.from_bmp16("gamesprite.bmp")

    # sets the background to image 1 in the bank
    background = stage.Grid(image_bank_1, 10, 8)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_X):
            background.tile(x_location, y_location, 0)
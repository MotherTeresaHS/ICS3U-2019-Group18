.. _asteroids:

Asteroids
==========

Once you have your spaceship working you can now add functionality for the asteroids. To have asteroids at each side of the screen, you will need four different lists (one for each side). Use a for loop to create asteroids up to the set amount from your constants file, and append the asteroids to their lists. This is to be done outside your gameloop.

.. code-block:: python
  :linenos:

    # Creating asteroids
    # Asteroids staring from the left
    left_asteroids = []
    for left_asteroid_number in range(constants.ASTEROID_CREATION_TOTAL):
        single_left_asteroid = stage.Sprite(image_bank_1, 4,
                                            constants.OFF_SCREEN_X,
                                            constants.OFF_SCREEN_Y)
        left_asteroids.append(single_left_asteroid)

    # Asteroids staring from the top
    top_asteroids = []
    for top_asteroid_number in range(constants.ASTEROID_CREATION_TOTAL):
        single_up_asteroid = stage.Sprite(image_bank_1, 5,
                                          constants.OFF_SCREEN_X,
                                          constants.OFF_SCREEN_Y)
        top_asteroids.append(single_up_asteroid)

    # Asteroids starting from the right
    right_asteroids = []
    for right_asteroid_number in range(constants.ASTEROID_CREATION_TOTAL):
        single_right_asteroid = stage.Sprite(image_bank_1, 6,
                                             constants.OFF_SCREEN_X,
                                             constants.OFF_SCREEN_Y)
        right_asteroids.append(single_right_asteroid)

    # Asteroids staring from the bottom
    bottom_asteroids = []
    for down_asteroid_number in range(constants.ASTEROID_CREATION_TOTAL):
        single_down_asteroid = stage.Sprite(image_bank_1, 7,
                                            constants.OFF_SCREEN_X,
                                            constants.OFF_SCREEN_Y)
        bottom_asteroids.append(single_down_asteroid)

When you have your asteroids ready, you will need to be able to have them move across the screen. Once again, each side of their screen will need a way to scroll lasers. For this, create a for loop in your game loop that itterates through all the asteroids in a list. If the assteroid isn't in purgatory off screen, it will scroll across the screen in the desired direction.
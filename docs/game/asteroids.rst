.. _asteroids:

Asteroids
==========

Once you have your spaceship working you can now add functionality for the asteroids. To have asteroids at each side of the screen, you will need four different lists (one for each side). Use a for loop to create asteroids up to the set amount from your constants file, and append the asteroids to their lists. This is to be done outside your gameloop. Be sure your asteroids have been painted and rendered on screen.

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
    reset_left_asteroid()

    # Asteroids staring from the top
    top_asteroids = []
    for top_asteroid_number in range(constants.ASTEROID_CREATION_TOTAL):
        single_up_asteroid = stage.Sprite(image_bank_1, 5,
                                          constants.OFF_SCREEN_X,
                                          constants.OFF_SCREEN_Y)
        top_asteroids.append(single_up_asteroid)
    reset_top_asteroid()

    # Asteroids starting from the right
    right_asteroids = []
    for right_asteroid_number in range(constants.ASTEROID_CREATION_TOTAL):
        single_right_asteroid = stage.Sprite(image_bank_1, 6,
                                             constants.OFF_SCREEN_X,
                                             constants.OFF_SCREEN_Y)
        right_asteroids.append(single_right_asteroid)
    reset_right_asteroid()

    # Asteroids staring from the bottom
    bottom_asteroids = []
    for down_asteroid_number in range(constants.ASTEROID_CREATION_TOTAL):
        single_down_asteroid = stage.Sprite(image_bank_1, 7,
                                            constants.OFF_SCREEN_X,
                                            constants.OFF_SCREEN_Y)
        bottom_asteroids.append(single_down_asteroid)
    reset_bottom_asteroid()

When you have your asteroids ready, you will need to be able to have them move across the screen. Once again, each side of their screen will need a way to scroll asteroids. For this, create a for loop in your game loop that itterates through all the asteroids in a list. An if statement within will deterimine if the asteroid isn't in purgatory off screen, and will scroll across the screen in the desired direction. Within said if statement should be another if statement determining if the asteroid has reached the other side of the screen. If the asteroid has, it will be moved back into purgatory off screen and wait to be sent out again.

.. code-block:: python
  :linenos:

        # Scroll asteroids from left of screen
        for left_asteroid_number in range(len(left_asteroids)):
            if left_asteroids[left_asteroid_number].x < constants.OFF_RIGHT_SCREEN:
                left_asteroids[left_asteroid_number].move(
                left_asteroids[left_asteroid_number].x + constants.ASTEROID_SPEED,
                left_asteroids[left_asteroid_number].y)
                if left_asteroids[left_asteroid_number].x > constants.SCREEN_X:
                    left_asteroids[left_asteroid_number].move(constants.OFF_SCREEN_X,
                                                              constants.OFF_SCREEN_Y)
                    reset_left_asteroid()

        # Scroll asteroids from top of screen
        for top_asteroid_number in range(len(top_asteroids)):
            if top_asteroids[top_asteroid_number].y < constants.OFF_BOTTOM_SCREEN:
                top_asteroids[top_asteroid_number].move(
                top_asteroids[top_asteroid_number].x,
                top_asteroids[top_asteroid_number].y + constants.ASTEROID_SPEED)
                if top_asteroids[top_asteroid_number].y > constants.SCREEN_Y:
                    top_asteroids[top_asteroid_number].move(constants.OFF_SCREEN_X,
                                                            constants.OFF_SCREEN_Y)
                    reset_top_asteroid()

        # Scroll asteroids from right of screen left
        for right_asteroid_number in range(len(right_asteroids)):
            if right_asteroids[right_asteroid_number].x > constants.OFF_LEFT_SCREEN:
                right_asteroids[right_asteroid_number].move(
                right_asteroids[right_asteroid_number].x - constants.ASTEROID_SPEED,
                right_asteroids[right_asteroid_number].y)
                if right_asteroids[right_asteroid_number].x < 0 - constants.SPRITE_SIZE:
                    right_asteroids[right_asteroid_number].move(constants.OFF_SCREEN_X,
                                                                constants.OFF_SCREEN_Y)
                    reset_right_asteroid()

        # Scroll asteroids from bottom of screen
        for down_asteroid_number in range(len(bottom_asteroids)):
            if bottom_asteroids[down_asteroid_number].y > constants.OFF_TOP_SCREEN:
                bottom_asteroids[down_asteroid_number].move(
                bottom_asteroids[down_asteroid_number].x,
                bottom_asteroids[down_asteroid_number].y - constants.ASTEROID_SPEED)
                if bottom_asteroids[down_asteroid_number].y < 0 - constants.SPRITE_SIZE:
                    bottom_asteroids[down_asteroid_number].move(constants.OFF_SCREEN_X,
                                                                constants.OFF_SCREEN_Y)
                    reset_bottom_asteroid()

The final thing you will need is a way to set and reset the asteroids off screen at a random location and distance so they remain unpredictable to the player. You will need to create four seperate functions outside your game loop, one for each asteroid list. These functions will be called immediately after the creation of your asteroids and when they reach the other side of the screen from where they started (they must be called after all the processes from above). The proper placement of the function calls is displayed in the sample code above. When the function is called, it will have a for loop with an if statement that checks each asteroid of the particular list to see if it is on screen or not. This is similar to what you have done above. If the asteroid is read as in purgatory off screen, it will be moved to a random X and Y coordinate just off the screen and begin its way across the screen. This way, each time the function is called the asteroid will reset itself without interfering with the other asteroids.

.. code-block:: python
  :linenos:

    # These functions set and reset the start coordinates of asteroids
    def reset_left_asteroid():
        # Sets and resets the start coordinates of asteroids starting on the left
        for left_asteroid_number in range(len(left_asteroids)):
            if left_asteroids[left_asteroid_number].x < 0:
                left_asteroids[left_asteroid_number].move(random.randint
                                                          (-100, 0 -
                                                           constants.SPRITE_SIZE),
                                                          random.randint
                                                          (0, constants.SCREEN_Y))
                break

    def reset_top_asteroid():
        # Sets and resets the start coordinates of asteroids starting on the top
        for top_asteroid_number in range(len(top_asteroids)):
            if top_asteroids[top_asteroid_number].y < 0:
                top_asteroids[top_asteroid_number].move(random.randint
                                                        (0, constants.SCREEN_X),
                                                        random.randint
                                                        (-100, 0 -
                                                         constants.SPRITE_SIZE))
                break

    def reset_right_asteroid():
        # Sets and resets the start coordinates of asteroids starting on the right
        for right_asteroid_number in range(len(right_asteroids)):
            if right_asteroids[right_asteroid_number].x < 0:
                right_asteroids[right_asteroid_number].move(random.randint
                                                            (constants.SCREEN_X, 228),
                                                            random.randint
                                                            (0, constants.SCREEN_Y))
                break

    def reset_bottom_asteroid():
        # Sets and resets the start coordinates of asteroids starting on the bottom
        for down_asteroid_number in range(len(bottom_asteroids)):
            if bottom_asteroids[down_asteroid_number].y < 0:
                bottom_asteroids[down_asteroid_number].move(random.randint
                                                        (0, constants.SCREEN_X),
                                                        random.randint
                                                        (160 + constants.SPRITE_SIZE,
                                                         260))
                break

You should now have asteroids that scroll across the screen from all four directions and are able to reset themselves.
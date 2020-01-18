.. _ammo_packs:

Ammo Packs
==========

The space ship is not able to fire lasers immediately. For this, it needs ammo packs. I will cover mechanics on the different lasers you can fire later and how to do so, but for now this will show you how the ammo packs work. The first thing you will need is to create a new list for your ammo pack sprites. There are three different ammo packs you will need to generate and append to the list. Assure that they originate in purgatory off screen. Also be sure that you have added them to be painted and rendered on the screen.

.. code-block:: python
  :linenos:

    # This list contains the ammo packs
    ammo = []

    # Creating ammo pack sprites
    single_shot = stage.Sprite(image_bank_1, 15,
                               constants.OFF_SCREEN_X,
                               constants.OFF_SCREEN_Y)
    ammo.append(single_shot)
    spread_shot = stage.Sprite(image_bank_1, 2,
                               constants.OFF_SCREEN_X,
                               constants.SCREEN_GRID_Y)
    ammo.append(spread_shot)
    around_shot = stage.Sprite(image_bank_1, 3, constants.OFF_SCREEN_X,
                               constants.OFF_SCREEN_Y)
    ammo.append(around_shot)

Next you will need a function that calls on a random ammo pack and places it somewhere random on the screen. The first thing you will need to do for this is set some initial values. These values include a variable for the timer, and a random number generator that determines when the timer stops and resets. Some of these values will be used later when determining what lasers fire and how, but they will be used in the next step.

.. code-block:: python
  :linenos:
  
    # Setting the ammo generation timer and values
    timer = 0
    generation_time = random.randint(500, 1500)
    ammo_type = 0
    firing_type = 0
    state_of_button = 0

You now need to make the function itself. The first three lines in the function should make sure the ammo packs are all in purgatory before a new one is placed. This way, there won't be two ammo packs on screen at once. Next you need a random number generator set between 1 and 100 that will determine what type of ammo pack spawns. When the function is called, an ammo pack will be moved on screen depending on which number was chosen. You should have a 50% chance of getting a singular projectile pack, 30% chance of getting a three projectile spread, and 20% chance of getting an eight projectile all around shot. Also depending on which pack was chosen, a variable has to be updated to indicate what kind of laser to fire when the player decides to use the ammo.

.. code-block:: python
  :linenos:
  
    # This function randomly generates ammo packs
    def spawn_ammo():
        single_shot.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        spread_shot.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        around_shot.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        type_of_ammo = random.randint(1, 100)
        ammo_variant = 0
        if type_of_ammo <= 50:
            ammo_variant = 1
            single_shot.move(random.randint(0 + constants.SPRITE_SIZE,
                                            constants.SCREEN_X -
                                            constants.SPRITE_SIZE),
                             random.randint(0 + constants.SPRITE_SIZE,
                                            constants.SCREEN_Y -
                                            constants.SPRITE_SIZE))
        elif type_of_ammo >= 51 and type_of_ammo <= 80:
            ammo_variant = 2
            spread_shot.move(random.randint(0 + constants.SPRITE_SIZE,
                                            constants.SCREEN_X -
                                            constants.SPRITE_SIZE),
                             random.randint(0 + constants.SPRITE_SIZE,
                                            constants.SCREEN_Y -
                                            constants.SPRITE_SIZE))
        elif type_of_ammo >= 81:
            ammo_variant = 3
            around_shot.move(random.randint(0 + constants.SPRITE_SIZE,
                                            constants.SCREEN_X -
                                            constants.SPRITE_SIZE),
                             random.randint(0 + constants.SPRITE_SIZE,
                                            constants.SCREEN_Y -
                                            constants.SPRITE_SIZE))

Something important you will need is a timer that calls your spawn ammo function after a short period of time. In the game loop, create a for loop that itterates through a small set of numbers. Each time the itteration is complete, add 1 to your pre established timer variable. When your timer equals your generation time variable, your ammo function is called. The timer resets to zero, a new random number is chosen for the generation time, and the process repeats itself.

.. code-block:: python
  :linenos:
  
        # Ammo spawn timer
        for counter in range(1, 61):
            if counter == 60:
                timer = timer + 1
                if timer == generation_time:
                    ammo_type = spawn_ammo()
                    timer = 0
                    generation_time = random.randint(500, 1500)
                else:
                    continue

The last thing you will need is something to detect if the spaceship has collided with (picked up) the ammo pack. To do this you will need a for loop watching if a series of coordinates (hitbox) on each have intersected. If this happens, the ammo pack is removed from the screen. At this point the player should be able to fire a specific laser pattern depending on which ammo pack they picked up.

.. code-block:: python
  :linenos:
  
        # This detects if the ship has hit and collected an ammo pack
        for ammo_number in range(len(ammo)):
            if ammo[ammo_number].x > 0:
                for sprite_number in range(len(sprites)):
                    if sprites[sprite_number].x > 0:
                        if stage.collide(ammo[ammo_number].x + 6,
                                         ammo[ammo_number].y + 3,
                                         ammo[ammo_number].x + 10,
                                         ammo[ammo_number].y + 13,
                                         sprites[sprite_number].x + 1,
                                         sprites[sprite_number].y + 1,
                                         sprites[sprite_number].x + 14,
                                         sprites[sprite_number].y + 14):
                            ammo[ammo_number].move(constants.OFF_SCREEN_X,
                                                   constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(load_sound)

Your ammo packs should now be fully functional.
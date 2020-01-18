.. _lasers:

Lasers
==========

The next thing to get working is actually firing the lasers themselves. Like all the other sprites, they must first be created and added to a list. Make sure the list is both painted and rendered on screen. Similar to the asteroids, the lasers will be created and appended to a list with a for loop and will appear in purgatory off screen. 

.. code-block:: python
  :linenos:

    # This list contains the laser sprites
    lasers = []

    # Generating laser sprites
    for laser_number in range(constants.LASER_CREATION_TOTAL):
        single_laser = stage.Sprite(image_bank_1, 10,
                                            constants.OFF_SCREEN_X,
                                            constants.OFF_SCREEN_Y)
        lasers.append(single_laser)

The first think we will want to do before we program the lasers is to have a way to count the asteroids that have been hit by the lasers. To do this, initialize a variable equal to 0 to keep score outside your game loop. Every time an asteroid is hit with a laser, the score will increase by one.

.. code-block:: python
  :linenos:

    # Score counter for the asteroids
    asteroid_counter = 0

Lasers are fundamentaly the hardest and most tedious part of this program. Before we start working on the lasers, we need a method of firing them. The player must use the A button to fire their lasers after they pick up an ammo pack. We first need to set up a way of detecting the state of the A button as we want the lasers to fire when the button has just been pressed. This should be in the game loop.

.. code-block:: python
  :linenos:

        # A button to fire
        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

Next we need to program multiple ways for the ammo to fire once the A button has been pressed, as well as the different types of ammo. I am going to do this through a large if statement with smaller if statements in between to figure out what direction to fire and how many lasers to fire. I will start with detecting what kind of ammo the user has in the game loop. The variable that determines this is the firing type. If the user hits the A button and they have not picked up an ammo pack, nothing will happen. If the user has picked up a red ammo pack, one laser will be moved to the ship's coordinates. If the user has picked up a yellow ammo pack, three lasers will be moved to the ship's coordinates. If the user has picked up a blue ammo pack, all eight laser will be moved to the ship's coordinates. On the end of each there is four if statements that detect which button was last pressed on the D-Pad. For the singular projectile and three projectile spread, they will always travel in the direction of the last button pressed on the D-Pad. In any instance that lasers are summoned to the ship's coordinates, the laser sound will play indicating the player has fired a laser.

.. code-block:: python
  :linenos:

        # Firing ammo using the a button
        if a_button == constants.button_state["button_just_pressed"]:
            for laser_number in range(len(lasers)):
                # No ammo
                if ammo_type == 0:
                    break
                # Single shot
                elif ammo_type == 1:
                    if lasers[1].x < 0:
                        lasers[1].move(ship.x, ship.y)
                        sound.stop()
                        sound.play(laser_sound)
                        firing_type = 1
                        ammo_type = 0
                        if state_of_button == 1:
                            firing_direction = 1
                        elif state_of_button == 2:
                            firing_direction = 2
                        elif state_of_button == 3:
                            firing_direction = 3
                        elif state_of_button == 4:
                            firing_direction = 4
                        break
                # Spread shot
                elif ammo_type == 2:
                    if lasers[1].x < 0:
                        lasers[1].move(ship.x, ship.y)
                    if lasers[2].x < 0:
                        lasers[2].move(ship.x, ship.y)
                    if lasers[3].x < 0:
                        lasers[3].move(ship.x, ship.y)
                        sound.stop()
                        sound.play(laser_sound)
                        firing_type = 2
                        ammo_type = 0
                        if state_of_button == 1:
                            firing_direction = 1
                        elif state_of_button == 2:
                            firing_direction = 2
                        elif state_of_button == 3:
                            firing_direction = 3
                        elif state_of_button == 4:
                            firing_direction = 4
                        break
                    # Around shot
                elif ammo_type == 3:
                    if lasers[0].x < 0:
                        lasers[0].move(ship.x, ship.y)
                    if lasers[1].x < 0:
                        lasers[1].move(ship.x, ship.y)
                    if lasers[2].x < 0:
                        lasers[2].move(ship.x, ship.y)
                    if lasers[3].x < 0:
                        lasers[3].move(ship.x, ship.y)
                    if lasers[4].x < 0:
                        lasers[4].move(ship.x, ship.y)
                    if lasers[5].x < 0:
                        lasers[5].move(ship.x, ship.y)
                    if lasers[6].x < 0:
                        lasers[6].move(ship.x, ship.y)
                    if lasers[7].x < 0:
                        lasers[7].move(ship.x, ship.y)
                        sound.stop()
                        sound.play(laser_sound)
                        firing_type = 3
                        ammo_type = 0
                        break
                    else:
                        continue

Now we need a way to move the lasers across the screen in the desired direction. To do this we will have a for loop in the game loop that continuosly itterate through all eight lasers.

.. code-block:: python
  :linenos:

        # Firing lasers
        for laser_number in range(len(lasers)):

There are three large chunks inside this for loop. The first is the singular projectile shot. If the laser isn't off screen in purgatory (because the player has pressed the A button), the laser will scroll in a specific direction according to the last button pressed on the D-Pad. Once the laser reaches off screen, it is moved back to purgatory to await its next use. The type of ammo and firing direction is then reupdated to zero as to not cause problems with future ammo packs collected and lasers fired.

.. code-block:: python
  :linenos:

            # Single shot
            if firing_type == 1:
                # Upwards shot
                if lasers[1].x > 0 and firing_direction == 1:
                    lasers[1].move(lasers[1].x, lasers[1].y -
                                   constants.LASER_SPEED)
                    if lasers[1].y < constants.OFF_TOP_SCREEN:
                        lasers[1].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                        firing_type = 0
                        firing_direction = 0
                # Right shot
                elif lasers[1].y > 0 and firing_direction == 2:
                    lasers[1].move(lasers[1].x + constants.LASER_SPEED,
                                   lasers[1].y)
                    if lasers[1].x >= constants.OFF_RIGHT_SCREEN:
                        lasers[1].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                        firing_type = 0
                        firing_direction = 0
                # Downwards shot
                elif lasers[1].x > 0 and firing_direction == 3:
                    lasers[1].move(lasers[1].x, lasers[1].y +
                                   constants.LASER_SPEED)
                    if lasers[1].y >= constants.OFF_BOTTOM_SCREEN:
                        lasers[1].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                        firing_type = 0
                        firing_direction = 0
                # Left shot
                elif lasers[1].y > 0 and firing_direction == 4:
                    lasers[1].move(lasers[1].x - constants.LASER_SPEED,
                                   lasers[1].y)
                    if lasers[1].x < constants.OFF_LEFT_SCREEN:
                        lasers[1].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                        firing_type = 0
                        firing_direction = 0

The second chunk is the three projectile spread shot. It functions similarly to the singular projectile. If the laser is not in purgatory, one of the three lasers travels straight across the screen according to the firing direction. The two other lasers travel diagonally in the same relative direction as the first one on a perpendicular angle from one another. All of them travel at the same speed. All three lasers must leave the screen before they are sent back to their off screen purgatory. This way if a laser is removed early for striking an asteroid the other two don't dissappear for what seems like no reason. After being moved back to purgatory, just like the singular shot, the type of ammo and firing direction is then reupdated to zero as to not cause problems with future ammo packs collected and lasers fired.

.. code-block:: python
  :linenos:

            if firing_type == 2:
                # Up shot
                if lasers[laser_number].y > -17 and firing_direction == 1:
                    lasers[1].move(lasers[1].x, lasers[1].y
                                   - constants.LASER_SPEED)
                    lasers[2].move(lasers[2].x + constants.LASER_SPEED,
                                   lasers[2].y - constants.LASER_SPEED)
                    lasers[3].move(lasers[3].x - constants.LASER_SPEED,
                                   lasers[3].y - constants.LASER_SPEED)
                    if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                        lasers[1].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                    if lasers[2].y < constants.OFF_TOP_SCREEN:
                        lasers[2].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                    if lasers[3].y < constants.OFF_TOP_SCREEN:
                        lasers[3].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                    if lasers[1].x == constants.OFF_SCREEN_X and \
                       lasers[2].x == constants.OFF_SCREEN_X and \
                       lasers[3].x == constants.OFF_SCREEN_X:
                        firing_type = 0
                        firing_direction = 0
                # Right shot
                elif lasers[laser_number].x < 176 and firing_direction == 2:
                    lasers[1].move(lasers[1].x + constants.LASER_SPEED,
                                   lasers[1].y)
                    lasers[2].move(lasers[2].x + constants.LASER_SPEED,
                                   lasers[2].y - constants.LASER_SPEED)
                    lasers[3].move(lasers[3].x + constants.LASER_SPEED,
                                   lasers[3].y + constants.LASER_SPEED)
                    if lasers[1].x >= constants.OFF_RIGHT_SCREEN:
                        lasers[1].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                    if lasers[2].x >= constants.OFF_RIGHT_SCREEN:
                        lasers[2].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                    if lasers[3].x >= constants.OFF_RIGHT_SCREEN:
                        lasers[3].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                    if lasers[1].x == constants.OFF_SCREEN_X and \
                       lasers[2].x == constants.OFF_SCREEN_X and \
                       lasers[3].x == constants.OFF_SCREEN_X:
                        firing_type = 0
                        firing_direction = 0
                # Downwards shot
                elif lasers[laser_number].y > 0 and firing_direction == 3:
                    lasers[1].move(lasers[1].x, lasers[1].y +
                                   constants.LASER_SPEED)
                    lasers[2].move(lasers[2].x - constants.LASER_SPEED,
                                   lasers[2].y + constants.LASER_SPEED)
                    lasers[3].move(lasers[3].x + constants.LASER_SPEED,
                                   lasers[3].y + constants.LASER_SPEED)
                    if lasers[1].y >= constants.OFF_BOTTOM_SCREEN:
                        lasers[1].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                    if lasers[2].y >= constants.OFF_BOTTOM_SCREEN:
                        lasers[2].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                    if lasers[3].y >= constants.OFF_BOTTOM_SCREEN:
                        lasers[3].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                    if lasers[1].x == constants.OFF_SCREEN_X and \
                       lasers[2].x == constants.OFF_SCREEN_X and \
                       lasers[3].x == constants.OFF_SCREEN_X:
                        firing_type = 0
                        firing_direction = 0
                # Left shot
                elif lasers[laser_number].x > -17 and firing_direction == 4:
                    lasers[1].move(lasers[1].x - constants.LASER_SPEED,
                                   lasers[1].y)
                    lasers[2].move(lasers[2].x - constants.LASER_SPEED,
                                   lasers[2].y + constants.LASER_SPEED)
                    lasers[3].move(lasers[3].x - constants.LASER_SPEED,
                                   lasers[3].y - constants.LASER_SPEED)
                    if lasers[1].x < constants.OFF_LEFT_SCREEN:
                        lasers[1].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                    if lasers[2].x < constants.OFF_LEFT_SCREEN:
                        lasers[2].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                    if lasers[3].x < constants.OFF_LEFT_SCREEN:
                        lasers[3].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                    if lasers[1].x == constants.OFF_SCREEN_X and \
                       lasers[2].x == constants.OFF_SCREEN_X and \
                       lasers[3].x == constants.OFF_SCREEN_X:
                        firing_type = 0
                        firing_direction = 0

The third and final chunk of the for loop is the all around shot. This shot sends all eight traveling in different directions from one another. Four are heading straight across the screen, either vertically or horizontally parallel to its edge. The other four are traveling diagonally across the screen relatively towards each of the corners, similar to the two flanking projectiles from the spread shot. The two projectiles traveling parallel to the horizontal edge of the screen are traveling at a heightened speed from the rest of the projectiles. The reason for this is that during early play tests it felt and looked clumsy to have those two lasers leave the screen last because the screen is a rectangle with the horizontal edges longer than the vertical ones. All eight projectiles must be off screen before the lasers are moved back to purgatory. Just like the singular and spread shots, after the lasers have been moved back to purgatory, the type of ammo and firing direction is then reupdated to zero as to not cause problems with future ammo packs collected and lasers fired.

.. code-block:: python
  :linenos:

            # Around shot
            if firing_type == 3:
                if lasers[laser_number].x > -17:
                    lasers[0].move(lasers[0].x, lasers[0].y -
                                   constants.LASER_SPEED)
                    lasers[1].move(lasers[1].x + constants.LASER_SPEED,
                                   lasers[1].y - constants.LASER_SPEED)
                    lasers[2].move(lasers[2].x + constants.EXTRA_LASER_SPEED,
                                   lasers[2].y)
                    lasers[3].move(lasers[3].x + constants.LASER_SPEED,
                                   lasers[3].y + constants.LASER_SPEED)
                    lasers[4].move(lasers[4].x, lasers[4].y +
                                   constants.LASER_SPEED)
                    lasers[5].move(lasers[5].x - constants.LASER_SPEED,
                                   lasers[5].y + constants.LASER_SPEED)
                    lasers[6].move(lasers[6].x - constants.EXTRA_LASER_SPEED,
                                   lasers[6].y)
                    lasers[7].move(lasers[7].x - constants.LASER_SPEED,
                                   lasers[7].y - constants.LASER_SPEED)
                    if lasers[0].y < constants.OFF_TOP_SCREEN:
                        lasers[0].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                    if lasers[1].y < constants.OFF_TOP_SCREEN:
                        lasers[1].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                    if lasers[2].x >= 176:
                        lasers[2].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                    if lasers[3].y > constants.OFF_BOTTOM_SCREEN:
                        lasers[3].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                    if lasers[4].y > constants.OFF_BOTTOM_SCREEN:
                        lasers[4].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                    if lasers[5].y > constants.OFF_BOTTOM_SCREEN:
                        lasers[5].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                    if lasers[6].x <= -17:
                        lasers[6].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                    if lasers[7].y < constants.OFF_TOP_SCREEN:
                        lasers[7].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                    if lasers[0].x == constants.OFF_SCREEN_X and \
                       lasers[1].x == constants.OFF_SCREEN_X and \
                       lasers[2].x == constants.OFF_SCREEN_X and \
                       lasers[3].x == constants.OFF_SCREEN_X and \
                       lasers[4].x == constants.OFF_SCREEN_X and \
                       lasers[5].x == constants.OFF_SCREEN_X and \
                       lasers[6].x == constants.OFF_SCREEN_X and \
                       lasers[7].x == constants.OFF_SCREEN_X:
                        firing_type = 0
                        firing_direction = 0

The final thing you will need is a way to detect if there has been a collision between the lasers and asteroids. This will be done in a way similar to how a player picks up ammo packs. A for loop will itterate through both the asteroids and the lasers to determine if either of their hit boxes ever overlap. Like the ammo-spaceship collision detect, this is to be done in the game loop. If there is an overlap, the hit asteroid will be taken off screen and the proper reset asteroid function will be called. The laser that hit the asteroid will be moved back to purgatory. When any asteroid is hit, the impact sound plays to indicate an asteroid has been destroyed. The score variable also increases by one every time an asteroid is hit with a laser. As there are four different asteroid lists, there has to be four different for loops, one that detects collisions between a laser and an asteroid of its respective list.

.. code-block:: python
  :linenos:

        # This detects if any lasers hit asteroids heading right
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for asteroid_number in range(len(left_asteroids)):
                    if left_asteroids[asteroid_number].x > 0:
                        if stage.collide(left_asteroids[asteroid_number].x + 1,
                                         left_asteroids[asteroid_number].y + 1,
                                         left_asteroids[asteroid_number].x + 15,
                                         left_asteroids[asteroid_number].y + 15,
                                         lasers[laser_number].x + 3,
                                         lasers[laser_number].y + 3,
                                         lasers[laser_number].x + 13,
                                         lasers[laser_number].y + 13):
                            left_asteroids[asteroid_number].move(constants.OFF_SCREEN_X,
                                                                 constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X,
                                                      constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(impact_sound)
                            reset_left_asteroid()
                            asteroid_counter = asteroid_counter + 1

        # This detects if any lasers hit asteroids heading down
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for asteroid_number in range(len(top_asteroids)):
                    if top_asteroids[asteroid_number].x > 0:
                        if stage.collide(top_asteroids[asteroid_number].x + 1,
                                         top_asteroids[asteroid_number].y + 1,
                                         top_asteroids[asteroid_number].x + 15,
                                         top_asteroids[asteroid_number].y + 15,
                                         lasers[laser_number].x + 3,
                                         lasers[laser_number].y + 3,
                                         lasers[laser_number].x + 13,
                                         lasers[laser_number].y + 13):
                            top_asteroids[asteroid_number].move(constants.OFF_SCREEN_X,
                                                                constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X,
                                                      constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(impact_sound)
                            reset_top_asteroid()
                            asteroid_counter = asteroid_counter + 1

        # This detects if any lasers hit asteroids heading left
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for asteroid_number in range(len(right_asteroids)):
                    if right_asteroids[asteroid_number].x > 0:
                        if stage.collide(right_asteroids[asteroid_number].x + 1,
                                         right_asteroids[asteroid_number].y + 1,
                                         right_asteroids[asteroid_number].x + 15,
                                         right_asteroids[asteroid_number].y + 15,
                                         lasers[laser_number].x + 3,
                                         lasers[laser_number].y + 3,
                                         lasers[laser_number].x + 13,
                                         lasers[laser_number].y + 13):
                            right_asteroids[asteroid_number].move(constants.OFF_SCREEN_X,
                                                                  constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X,
                                                      constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(impact_sound)
                            reset_right_asteroid()
                            asteroid_counter = asteroid_counter + 1

        # This detects if any lasers hit asteroids heading up
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for asteroid_number in range(len(bottom_asteroids)):
                    if bottom_asteroids[asteroid_number].x > 0:
                        if stage.collide(bottom_asteroids[asteroid_number].x + 1,
                                         bottom_asteroids[asteroid_number].y + 1,
                                         bottom_asteroids[asteroid_number].x + 15,
                                         bottom_asteroids[asteroid_number].y + 15,
                                         lasers[laser_number].x + 3,
                                         lasers[laser_number].y + 3,
                                         lasers[laser_number].x + 13,
                                         lasers[laser_number].y + 13):
                            bottom_asteroids[asteroid_number].move(constants.OFF_SCREEN_X,
                                                                   constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X,
                                                      constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(impact_sound)
                            reset_bottom_asteroid()
                            asteroid_counter = asteroid_counter + 1

If you did everything correct you should now be able to fire three different types of lasers and have them destroy asteroids.
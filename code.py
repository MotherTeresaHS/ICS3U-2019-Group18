#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: January 2020
# This is the main game file for Asteroid Dodger for CircuitPython

import ugame
import stage
import board
import neopixel
import time
import random

import constants


def blank_white_reset_scene():
    # this function is the splash scene game loop

    # do house keeping to ensure everythng is setup

    # set up the NeoPixels
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 5, auto_write=False)
    pixels.deinit()  # and turn them all off

    # reset sound to be off
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 160, 120)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 1/2 seconds
        time.sleep(0.5)
        mt_splash_scene()

        # redraw sprite list


def mt_splash_scene():
    # this function is the MT splash scene

    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)

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

    text = []

    text1 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(5, 105)
    text2.text("In association with")
    text.append(text2)

    text3 = stage.Text(width=29, height=14, font=None,
                       palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text3.move(25, 115)
    text3.text("Snakob Studios")
    text.append(text3)

    # get sound ready
    # Use this guide to convert your other sounds to something that will work
    #    https://learn.adafruit.com/microcontroller-compatible-audio-file-
    #    conversion
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 3 seconds
        time.sleep(3.0)
        menu_scene()

        # redraw sprite list


def menu_scene():
    # this function is the menu scene

    # Buttons to keep state information on
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # The image bank for the game
    image_bank_1 = stage.Bank.from_bmp16("gamesprite.bmp")

    # sets the background to image 1 in the bank
    background = stage.Grid(image_bank_1, 10, 8)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_X):
            background.tile(x_location, y_location, 1)

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

    # This list keeps all the sprites
    sprites = []

    # Adding the left and right of the ship to the sprite list
    ship_left = stage.Sprite(image_bank_1, 11, 64, 45)
    sprites.append(ship_left)
    ship_right = stage.Sprite(image_bank_1, 12, 80, 45)
    sprites.append(ship_right)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + sprites + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # update game logic
        if keys & ugame.K_START != 0:  # Start button
            keys = 0
            ugame.K_START = 0
            game_scene()
            pass

        if keys & ugame.K_SELECT != 0:  # Start button
            keys = 0
            ugame.K_SELECT = 0
            rules_scene()
            pass


        # redraw sprite list
        game.render_sprites(sprites)
        game.tick()


def rules_scene():
    # this function is the rules scene

    # The image bank for the game
    image_bank_1 = stage.Bank.from_bmp16("gamesprite.bmp")

    # sets the background to image 1 in the bank
    background = stage.Grid(image_bank_1, 10, 8)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_X):
            background.tile(x_location, y_location, 1)

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

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # update game logic
        if keys & ugame.K_START != 0:  # Start button
            keys = 0
            ugame.K_START = 0
            game_scene()
            pass

        # redraw sprite list


def game_scene():
    # this function is the game scene

    # The image bank for the game
    image_bank_1 = stage.Bank.from_bmp16("gamesprite.bmp")

    # sets the background to image 1 in the bank
    background = stage.Grid(image_bank_1, 10, 8)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_X):
            background.tile(x_location, y_location, 0)

    # This list contains the primary sprites
    sprites = []

    # Creating spaceship sprite
    ship = stage.Sprite(image_bank_1, 14, 75, 56)
    sprites.insert(0, ship)

    # Buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

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

    # This list contains the laser sprites
    lasers = []

    # Generating laser sprites
    for laser_number in range(constants.LASER_CREATION_TOTAL):
        single_laser = stage.Sprite(image_bank_1, 10,
                                            constants.OFF_SCREEN_X,
                                            constants.OFF_SCREEN_Y)
        lasers.append(single_laser)

    # Setting the ammo generation timer and values
    timer = 0
    generation_time = random.randint(1500, 2500)
    ammo_type = 0
    firing_type = 0
    state_of_button = 0

    # Getting sounds ready
    laser_sound = open("laser.wav", 'rb')
    crash_sound = open("crash.WAV", 'rb')
    load_sound = open("load.wav", 'rb')
    impact_sound = open("impact.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # This function randomly generates ammo packs
    def spawn_ammo():
        single_shot.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        spread_shot.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        around_shot.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        type_of_ammo = random.randint(81, 100)
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
        return ammo_variant

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

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = left_asteroids + right_asteroids + top_asteroids \
                  + bottom_asteroids + sprites + lasers + ammo + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # Move ship right
        if keys & ugame.K_RIGHT:
            state_of_button = 2
            if ship.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
            else:
                ship.move(ship.x + constants.SHIP_MOVEMENT_SPEED, ship.y)
            pass

        # Move ship left
        if keys & ugame.K_LEFT:
            state_of_button = 4
            if ship.x < 0:
                ship.move(0, ship.y)
            else:
                ship.move(ship.x - constants.SHIP_MOVEMENT_SPEED, ship.y)
            pass

        # Move ship up
        if keys & ugame.K_UP:
            state_of_button = 1
            if ship.y < 0:
                ship.move(ship.x, 0)
            else:
                ship.move(ship.x, ship.y - constants.SHIP_MOVEMENT_SPEED)
            pass

        # Move ship down
        if keys & ugame.K_DOWN:
            state_of_button = 3
            if ship.y > constants.SCREEN_Y - constants.SPRITE_SIZE:
                ship.move(ship.x, constants.SCREEN_Y - constants.SPRITE_SIZE)
            else:
                ship.move(ship.x, ship.y + constants.SHIP_MOVEMENT_SPEED)
            pass

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

        # update game logic

        # Ammo spawn timer
        for counter in range(1, 61):
            if counter == 60:
                timer = timer + 1
                if timer == generation_time:
                    ammo_type = spawn_ammo()
                    timer = 0
                    generation_time = random.randint(1500, 2500)
                else:
                    continue

        if a_button == constants.button_state["button_released"]:
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

        # Firing lasers
        for laser_number in range(len(lasers)):
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
            # Spread shot
            if firing_type == 2:
                if lasers[1].x > 0 and firing_direction == 1:
                    lasers[1].move(lasers[1].x, lasers[1].y
                                   - constants.LASER_SPEED)
                    lasers[2].move(lasers[2].x + constants.LASER_SPEED, 
                                   lasers[2].y - constants.LASER_SPEED)
                    lasers[3].move(lasers[3].x - constants.LASER_SPEED, 
                                   lasers[3].y - constants.LASER_SPEED)
                    if lasers[1].y < constants.OFF_TOP_SCREEN:
                        lasers[1].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                    if lasers[2].y < constants.OFF_TOP_SCREEN:
                        lasers[2].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                    if lasers[3].y < constants.OFF_TOP_SCREEN:
                        lasers[3].move(constants.OFF_SCREEN_X,
                                       constants.OFF_SCREEN_Y)
                        firing_type = 0
                        firing_direction = 0
                # Right shot
                elif lasers[1].y > 0 and firing_direction == 2:
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
                        firing_type = 0
                        firing_direction = 0
                # Downwards shot
                elif lasers[1].x > 0 and firing_direction == 3:
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
                        firing_type = 0
                        firing_direction = 0
                # Left shot
                elif lasers[1].y > 0 and firing_direction == 4:
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
                        firing_type = 0
                        firing_direction = 0
            # Around shot
            if firing_type == 3:
                if lasers[laser_number].x > 0:
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
                        firing_type = 0
                        firing_direction = 0

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

        # redraw sprite list
        game.render_sprites(left_asteroids + right_asteroids + top_asteroids +
                            bottom_asteroids + sprites + lasers + ammo)
        game.tick()


def game_over_scene(final_score):
    # this function is the game over scene

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # redraw sprite list
        pass  # just a placeholder until you write the code


if __name__ == "__main__":
    blank_white_reset_scene()

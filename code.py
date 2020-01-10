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

    # Creating ammo pack sprites
    single_shot = stage.Sprite(image_bank_1, 15,
                               constants.OFF_SCREEN_X,
                               constants.OFF_SCREEN_Y)
    sprites.append(single_shot)
    spread_shot = stage.Sprite(image_bank_1, 2,
                               constants.OFF_SCREEN_X,
                               constants.SCREEN_GRID_Y)
    sprites.append(spread_shot)
    around_shot = stage.Sprite(image_bank_1, 3, constants.OFF_SCREEN_X,
                               constants.OFF_SCREEN_Y)
    sprites.append(around_shot)

    # Setting the ammo generation timer
    timer = 0
    generation_time = random.randint(10, 30)

    # This function randomly generates ammo packs
    def spawn_ammo():
        single_shot.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        spread_shot.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        around_shot.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        type_of_ammo = random.randint(1, 100)
        if type_of_ammo <= 50:
            single_shot.move(random.randint(0 + constants.SPRITE_SIZE,
                                            constants.SCREEN_X -
                                            constants.SPRITE_SIZE),
                             random.randint(0 + constants.SPRITE_SIZE,
                                            constants.SCREEN_Y -
                                            constants.SPRITE_SIZE))
        elif type_of_ammo >= 51 and type_of_ammo <= 80:
            spread_shot.move(random.randint(0 + constants.SPRITE_SIZE,
                                            constants.SCREEN_X -
                                            constants.SPRITE_SIZE),
                             random.randint(0 + constants.SPRITE_SIZE,
                                            constants.SCREEN_Y -
                                            constants.SPRITE_SIZE))
        elif type_of_ammo >= 81:
            around_shot.move(random.randint(0 + constants.SPRITE_SIZE,
                                            constants.SCREEN_X -
                                            constants.SPRITE_SIZE),
                             random.randint(0 + constants.SPRITE_SIZE,
                                            constants.SCREEN_Y -
                                            constants.SPRITE_SIZE))

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
                  + bottom_asteroids + sprites + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # Move ship right
        if keys & ugame.K_RIGHT:
            if ship.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
            else:
                ship.move(ship.x + constants.SHIP_MOVEMENT_SPEED, ship.y)
            pass

        # Move ship left
        if keys & ugame.K_LEFT:
            if ship.x < 0:
                ship.move(0, ship.y)
            else:
                ship.move(ship.x - constants.SHIP_MOVEMENT_SPEED, ship.y)
            pass

        # Move ship up
        if keys & ugame.K_UP:
            if ship.y < 0:
                ship.move(ship.x, 0)
            else:
                ship.move(ship.x, ship.y - constants.SHIP_MOVEMENT_SPEED)
            pass

        # Move ship down
        if keys & ugame.K_DOWN:
            if ship.y > constants.SCREEN_Y - constants.SPRITE_SIZE:
                ship.move(ship.x, constants.SCREEN_Y - constants.SPRITE_SIZE)
            else:
                ship.move(ship.x, ship.y + constants.SHIP_MOVEMENT_SPEED)
            pass

        # update game logic
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

        # Ammo spawn timer
        for counter in range(1, 61):
            if counter == 60:
                timer = timer + 1
                if timer == generation_time:
                    spawn_ammo()
                    timer = 0
                    generation_time = random.randint(800, 1000)
                else:
                    continue

        # redraw sprite list
        game.render_sprites(left_asteroids + right_asteroids + top_asteroids +
                            bottom_asteroids + sprites)
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

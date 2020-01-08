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

        # redraw sprite list
        pass  # just a placeholder until you write the code


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

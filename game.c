// Copyright (c) 2020 Jacob Bonner All rights reserved.
//
// Created by: Jacob Bonner
// Created on: January 2020
// This is the main game file for Asteroid Dodger for the GameBoy

#include <stdio.h>
#include <gb/gb.h>
#include "menuSceneMap.c"
#include "menuSceneData.c"
#include "snakobSceneMap.c"
#include "snakobSceneData.c"
#include "sprites.c"
#include "gamemap.c"
#include "gameCharacter.c"

struct GameCharacter ship;
UBYTE spritesize = 8;

void performantdelay(UINT8 numloops) {
    // This function is a performance delayer
    UINT8 ii;
    for (ii = 0; ii < numloops; ii++) {
        wait_vbl_done();
    }
}

void fadeout() {
    // This function fades a scene out
    int i;
    for (i = 0; i < 4; i++) {
        switch (i) {
            case 0:
                BGP_REG = 0xE4;
                break;
            case 1:
                BGP_REG = 0xF9;
                break;
            case 2:
                BGP_REG = 0xFE;
                break;
            case 3:
                BGP_REG = 0xFF;
                break;
        }
    performantdelay(50);
    }
}

void fadein() {
    // This function fades a scene in
    int i;
    for (i = 0; i < 3; i++) {
        switch (i) {
            case 0:
                BGP_REG = 0xFE;
                break;
            case 1:
                BGP_REG = 0xF9;
                break;
            case 2:
                BGP_REG = 0xE4;
                break;
        }
    performantdelay(50);
    }
}

// This function assembles games sprites
void moveGameCharacter(struct GameCharacter* character, UINT8 x, UINT8 y) {
    move_sprite(character->spritids[0], x, y);
}

// This function setups up ship
void setupShip() {
    ship.x = 88;
    ship.y = 100;
    ship.width = 8;
    ship.height = 8;

    set_sprite_tile(1, 7);
    ship.spritids[0] = 1;

    moveGameCharacter(&ship, ship.x, ship.y);
}

void main() {
    // Main game functions

    // Sprite data
    set_sprite_data(0, 8, spriteTiles);

    // Setting the Snakob Studios splash screen tiles and data
    set_bkg_data(0, 100, snakobSceneData);
    set_bkg_tiles(0, 0, 20, 18, snakobSceneMap);

    // Displaying the snakob splash scene background
    SHOW_BKG;
    DISPLAY_ON;

    // Waiting for the user to press start to swap and fade out the scenes
    waitpad(J_START);
    fadeout();

    // Setting background tiles and data for menu scene
    set_bkg_data(0, 107, menuSceneData);
    set_bkg_tiles(0, 0, 20, 18, menuSceneMap);

    // Displaying the menu scene background
    SHOW_BKG;
    DISPLAY_ON;

    // Fading in the menu scene
    fadein();

    // Waiting for the player to start the game
    waitpad(J_START);

    // Setting the game background
    set_bkg_data(0, 100, spriteTiles);
    set_bkg_tiles(0, 0, 40, 18, gamemap);

    // Setting up the spaceship sprite
    SHOW_SPRITES;
    SHOW_BKG;
    DISPLAY_ON;

    setupShip();
}

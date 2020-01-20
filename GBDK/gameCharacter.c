// Copyright (c) 2020 Jacob Bonner All rights reserved.
//
// Created by: Jacob Bonner
// Created on: January 2020
// This program displays metasprites for the GameBoy

#include <gb/gb.h>

//generical character structure: id, position, graphics
struct GameCharacter {
	UBYTE spritids[1]; // all characters use 1 sprite
	UINT8 x;
	UINT8 y;
	UINT8 width;
	UINT8 height;
};

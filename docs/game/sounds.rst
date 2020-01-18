.. _sounds:

Sounds
==========

Before I continue on with the lasers, lets talk a bit about adding sound to the game. For Asteroid Dodger, you need 5 distinct sounds:

- Loading sound that plays when a player gets an ammo pack
- Laser sound that plays when a laser is fired
- An ammo spawning sound that plays when an ammo pack appears on the screen
- An impact sound that indicates when an asteroid has been destroyed by a laser
- A crash sound to indicate that an asteroid has struck the player's spaceship

To load the sounds, you need to open up the sounds in your game function. You will then need to define your sound variable, and make sure that the sounds are not muted.

.. code-block:: python
  :linenos:

    # Getting sounds ready
    laser_sound = open("laser.wav", 'rb')
    crash_sound = open("crash.WAV", 'rb')
    ammo_sound = open("ammo.wav", 'rb')
    load_sound = open("load.wav", 'rb')
    impact_sound = open("impact.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

You then need to add them where needed. For example, when you pick up an ammo pack, the load sound should play. Or, when the spawn ammo function is called, the ammo sound plays. You can do this by using the sound.play function and passing it in the sound you want to play. Always make sure a sound.stop is included before you play the new sound as to not distract from a sound that may currently be playing.

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

The above example is that when the spaceship picks up an ammo pack the loading sound plays. As you are programming, you may add sounds that are applicable to the instances they may be needed in.
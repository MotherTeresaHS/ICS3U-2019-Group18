.. _game:

****
Game
****

The following steps are how to create the actual game scene itself. Here is the rundown of what you will be programming: you are controlling a space ship and must dodge on coming asteroids that travel across the screen. The asteroids spawn at random positions off screen. Throughout the game ammo packs will spawn throughout the map. If the ship runs over the ammo pack, the player picks it up and get one type of laser shot according to the colour of the pack they picked up. If the pack is red, the player gets one shot that travels straight out from the ship. If the pack was yellow, the user gets a spread shot with one laser travelling straight out and two others flanking it travelling diagonally. If the pack is blue, eight lasers travel out from the ship in different directions. The user can fire these lasers by pressing the "A" button. The lasers will travel in the direction of the last button pressed on the D-Pad. When a laser collides with an asteroid, both are removed from the scene. When a player hits an asteroid the game ends. The steps below will help you program your game scene according to what has been described here. I would advise you to follow the steps in order. You can find a video of the working game `here <https://www.youtube.com/watch?v=TlK0fTQpyVU>`_. 

.. toctree::
   :maxdepth: 1
   :glob:

   Constants <constants>
   Background <background>
   Space Ship <space_ship>
   Asteroids <asteroids>
   Ammo Packs <ammo_packs>
   Sounds <sounds>
   Lasers <lasers>
   Asteroid Collisions <asteroid_collisions>

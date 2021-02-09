# A Simple Python Game 
This is a simple fun python game where the user has to try not to collide with enemies,that apear from different directions, in order to survive.
The user will randomly be given a chance to eat a reward that will apear on the scree :).
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development:
1) First follow the instruction [here](https://www.codecademy.com/articles/install-python) to install python 
2) Secondely follow these instruction [here](https://www.pygame.org/wiki/GettingStarted) to instal pygame for libraries that will allow you to experiece the game fully
3) Lastly click on "[Downlaod Zip](https://www.instructables.com/Downloading-Code-From-GitHub/)" to get a full copy of this project including the resources used.

## Code Style and Example
The code style used is standard 

The example of the code is shown below:

```python
import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# This creates the player and gives it the image found in this folder (similarly with the enemy image). 

player = pygame.image.load("player_1.png")
player = pygame.transform.scale(player,(150,150))

# This creates the enemies and gives it the image found in this folder (similarly with the enemy image).
enemy = pygame.image.load("enemy_1.png")
enemy = pygame.transform.scale(enemy,(150,150))
ghost = pygame.image.load("ghost.png")
ghost = pygame.transform.scale(ghost,(150,150))
bug = pygame.image.load("enemy.png")
bug = pygame.transform.scale(bug,(150,150))
```

## How To Play ?
1) Double click on the game_project.py and following screen should apear:
  - 
2) Press the:
  - Up key to move up.
  - Down key to move down.
  - Right key to move forward.
  - Left key to move backward.'
3) The aim is to not collide with the following enemies:
   - <img src"https://github.com/mphalane/simple-game-python/blob/master/enemy_1.png" alt="enemy 1" width="200" height="200"/>
   - ![enemey 2](https://github.com/mphalane/simple-game-python/blob/master/ghost.png =50x50)
   - ![enemey 2](https://github.com/mphalane/simple-game-python/blob/master/enemy.png =50x50)
   
4) If you collide with any enemy objects the user loses :(, and the game ends.

5) If you collide with any reward objects the user wins :), and the game ends.
   - ![reward object](https://github.com/mphalane/simple-game-python/blob/master/reward.png)
   

# In this example.py you will learn how to make a very simple game using the pygame library.
# One of the best ways of learning to program is by writing games.
# Pygame is a collection of modules in one package.
# You will need to install pygame.
# To do so:
# 1) open the command line interface on your computer,
# 2) cd to the directory that this task is located in,
# 3) follow the instructions here: https://www.pygame.org/wiki/GettingStarted
# 4) if you need help using pip, see here: https://projects.raspberrypi.org/en/projects/using-pip-on-windows

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

# This creates the prize and gives it the image found in this folder (similarly with the enemy image).
prize = pygame.image.load("reward.png")
prize = pygame.transform.scale(prize,(100,100))

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

#Player Dimensions
image_height = player.get_height()
image_width = player.get_width()
#Enemies Dimensions
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
ghost_height = ghost.get_height()
ghost_width = ghost.get_width()
bug_height = bug.get_height()
bug_width = bug.get_width()
#Prize Dimensions
prize_height = prize.get_height()
prize_width = prize.get_width()


print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

# Store the positions of the player and enemy as variables so that you can change them later. 

playerXPosition = 100
playerYPosition = 50

# Make the enemy start off screen and at a random y position.

enemyXPosition =  screen_width
enemyYPosition =  random.randint(0, screen_height - enemy_height)

# Make the bug start off screen and at a random x position.
ghostYPosition =  screen_height
ghostXPosition =  random.randint(0, screen_width - ghost_width)

# Make the ghost start off screen and at a random x position.
bugYPosition =  0
bugXPosition =  random.randint(0,screen_width - bug_width)

# Make the reward appear at a random y position.
prizeYPosition =  random.randint(0, screen_height - prize_height)
prizeXPosition =  random.randint(0, screen_width - prize_width)

#make
# This checks if the up or down key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False. 
# Boolean values are True or False values that can be used to test conditions and test states that are binary, i.e. either one way or the other. 

keyUp= False
keyDown = False
keyRight= False
keyLeft = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play.

#This generates random number from 0 to 100
#So that we can randomly display enemies based on weather this number is odd or even
randnumber=random.randint(0,100)
even=randnumber%2

#This is a 1/0 (int boolen) that flags if the enemy is at the end of the screen or not 
endofscreen=0
#This generates random number between 2 and 6
#This number determines when the prizes after ( after "n" enemies)
rewardnow=random.randint(2,6)
print(f'{rewardnow}')

#This intializes the reward counter that counters the number of enemies to reach the endofscreen
rewardcount=0

#This intializes the reward timer that delays the prizes (apear and disapear)
rewardtimer=0

while 1: # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). In Python the int 1 has the boolean value of 'true'. In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the bool(...) function to see what boolean value types have. You will learn more about while loop structers later. 

    
    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).

    #Check id reward counter is equal to the value of reward now
    #If so show the prize
    #else show the enemies
    if rewardcount==rewardnow:
        screen.blit(prize, (prizeXPosition, prizeYPosition))
    else:
        #Check if the randnumber is even and grater than 45
        #if so show enemy
        if even==0 and (randnumber>45):
            screen.blit(enemy, (enemyXPosition, enemyYPosition))
        #Else if the randnumber is even and less than 45
        #if so show bug
        elif even==0 and randnumber<45:
            screen.blit(bug, (bugXPosition, bugYPosition))
        #If Odd show ghost
        else:
            screen.blit(ghost, (ghostXPosition, ghostYPosition))
    
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1
    if keyLeft == True:        
       if playerXPosition > 0 : # This makes sure that the user does not move the player out the window from the left.
            playerXPosition -= 1      
    if keyRight == True:
        if playerXPosition < screen_width - image_width:# This makes sure that the user does not move the player out the window from the right.
            playerXPosition += 1

            
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    #Checks if the current enemy that is scrolling across the screen is at the endofscreen
    #If so it generates new random number from 0 to 100
    #So that we can randomly display enemies based on weather this number is odd or even
    #and sets endofscreen to 0
    if endofscreen==1:
      randnumber=random.randint(0,100)
      even=randnumber%2
      endofscreen=0
      print(f'rand-number is :{randnumber}')

    if rewardcount==rewardnow:
      #Bounding box for the enemy:
      #print("I am prize")
      
        prizeBox = pygame.Rect(prize.get_rect())
        prizeBox.top = prizeYPosition
        prizeBox.left = prizeXPosition

        #Increment timer
        rewardtimer+=1

        #Displays prize until rewardtimer = 2000
        #If rewardtimer = 2000 intitailize all variables and generate new random variables
        if rewardtimer==2000:
            reward=random.randint(3,8)
            endofscreen=1
            rewardcount=0
            rewardtimer=0
            prizeYPosition =  random.randint(0, screen_height - prize_height)
            prizeXPosition =  random.randint(0, screen_width - prize_width)
        #Test collision of the boxes:    
        if playerBox.colliderect(prizeBox):
             #Display Winning status to the user: 
             print("You Win!!!!")
             # Quite game and exit window: 
             pygame.quit()
             exit(0)

    else:
        #Test collision of the boxes:
        if even==0 and (randnumber>45):
            # Bounding box for the enemy:
            #print("I am enemy")
            enemyBox = pygame.Rect(enemy.get_rect())
            enemyBox.top = enemyYPosition
            enemyBox.left = enemyXPosition
            if playerBox.colliderect(enemyBox):
        
                # Display losing status to the user: 
                
                print("You lose!")
               
                # Quite game and exit window: 
                
                pygame.quit()
                exit(0)
                 # If the enemy is off the screen the user wins the game:
        
            if enemyXPosition < 0 - enemy_width:
                
                print("endofline-even")
                endofscreen=1
                enemyXPosition =  screen_width
                enemyYPosition =  random.randint(0, (screen_height - enemy_height))
                print(f'{endofscreen}')
                rewardcount+=1
                rewardtimer=0
         
            
            # Make enemy approach the player.
            
            enemyXPosition -= 0.7
        elif even==0 and randnumber<45:
            #Bounding box for the enemy:
            #print("I am bug")
            bugBox = pygame.Rect(bug.get_rect())
            bugBox.top = bugYPosition
            bugBox.left = bugXPosition
            if playerBox.colliderect(bugBox):
        
                # Display losing status to the user: 
                
                print("You lose!")
               
                # Quite game and exit window: 
                
                pygame.quit()
                exit(0)
                 # If the enemy is off the screen the user wins the game:
        
            if bugYPosition > bug_height + screen_height:
                
                print("endofline-even")
                endofscreen=1
                bugYPosition =  0
                bugXPosition =  random.randint(0,screen_width - bug_width)
                print(f'{endofscreen}')
                rewardcount+=1
                rewardtimer=0
            
            # Make enemy approach the player.
            
            bugYPosition += 0.7    
        else:
            # Bounding box for the ghost:
            #print("I am ghost")
            ghostBox = pygame.Rect(ghost.get_rect())
            ghostBox.top = ghostYPosition
            ghostBox.left = ghostXPosition
            if playerBox.colliderect(ghostBox):
        
                # Display losing status to the user: 
                
                print("You lose!")
               
                # Quite game and exit window: 
                
                pygame.quit()
                exit(0)
                 # If the enemy is off the screen the user wins the game:
        
            if ghostYPosition < 0 - ghost_height:

                # Make the ghost start off screen and at a random x position.
                print("endofline-odd")
                endofscreen=1
                print(f'{endofscreen}')
                ghostYPosition =  screen_height
                ghostXPosition =  random.randint(0, (screen_width - ghost_width))
                rewardcount+=1
                rewardtimer=0
            # Make enemy approach the player.
            
            ghostYPosition -= 0.5
            
    # ================The game loop logic ends here. =============
  

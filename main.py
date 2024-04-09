import pygame #importing pygame module: basically the core functions which are a part of the bigger pygame library
# import is like opening your recipe book to the page that contains the instructions for using the Pygame module.
# By importing Pygame, you're making those instructions available in your code.

pygame.init() #initalizes modules: this basically prepares the environment for you to be able to code the game
# think of init like preheating the oven, gathering the ingredients, greasing the pans

# defining the screen: dimensions, creating screen, setting caption
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

paul_vel = 10 #determines how fast the players, aliens, etc will move


paul = pygame.image.load('/Users/omarsiddiqui/Desktop/player.png') #paul to the image you put at this location
paul_rect = paul.get_rect() # Creates a rectanlge as a bounding box or representation of where the image is located and how large it is.
# This container helps you manage position, size, and movement of the image on screen
# You need rect for every object that you need to manage the position, size, and collision of
feyd1 = pygame.image.load('/Users/omarsiddiqui/Desktop/feyd.png')
feyd1_rect = feyd1.get_rect()
feyd1_vel = 2 #Don't do this with a float, it gets funky

feyd2 = pygame.image.load('/Users/omarsiddiqui/Desktop/feyd.png')
feyd2_rect = feyd2.get_rect()
feyd2_vel = 3

feyd3 = pygame.image.load('/Users/omarsiddiqui/Desktop/feyd.png')
feyd3_rect = feyd3.get_rect()
feyd3_vel = 1

feyd4 = pygame.image.load('/Users/omarsiddiqui/Desktop/feyd.png')
feyd4_rect = feyd4.get_rect()
feyd4_vel = 4

run = True #setting it initially to True so that False will end the game
while run: #this is the loop of the actual game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    paul_rect.y = 450
    userInput = pygame.key.get_pressed() #adjust paul image movement based on player input
    if userInput[pygame.K_LEFT] and paul_rect.x >= 0:
        paul_rect.x -= paul_vel #TODO: make it not go out of bounds
    if userInput[pygame.K_RIGHT] and paul_rect.x <= screen_width - paul_rect.width: #TODO: make it not go out of bounds
        paul_rect.x += paul_vel

    feyd1_rect.y = 100
    feyd1_rect.x += feyd1_vel
    if feyd1_rect.x < (0 ) or feyd1_rect.x > (screen_width - feyd1_rect.width):
        feyd1_vel *= -1

    feyd2_rect.y = 120
    feyd2_rect.x += feyd2_vel
    if feyd2_rect.x < (0) or feyd2_rect.x > (screen_width - feyd2_rect.width):
        feyd2_vel *= -1

    feyd3_rect.y = 140
    feyd3_rect.x += feyd3_vel
    if feyd3_rect.x < (0) or feyd3_rect.x > (screen_width - feyd3_rect.width):
        feyd3_vel *= -1

    feyd4_rect.y = 115
    feyd4_rect.x += feyd4_vel
    if feyd4_rect.x < (0) or feyd4_rect.x > (screen_width - feyd4_rect.width):
        feyd4_vel *= -1

    # example of OOP: you created the object Paul, and now the attributes that someone made in the pygame library
    # for the created object can be used like x and y

    screen.fill((0, 0, 0))  # Fill the screen with black, basically updating the screen so new visuals can be displayed
    screen.blit(paul, paul_rect)  # allows you to draw image onto another surface-"blit" = "block transfer"
    # drawing image "paul" on the screen at the position and size defined by paul_rect
    screen.blit(feyd1,feyd1_rect)
    screen.blit(feyd2, feyd2_rect)
    screen.blit(feyd3, feyd3_rect)
    screen.blit(feyd4, feyd4_rect)
    pygame.display.update() #reflects changes to the screen. Without this, you'd have to wait until you run the game again for the screen to fully update

pygame.quit()

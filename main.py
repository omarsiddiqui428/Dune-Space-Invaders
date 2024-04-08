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

vel = 10 #determines how fast the players, aliens, etc will move


paul = pygame.image.load('/Users/omarsiddiqui/Desktop/player.png') #paul to the image you put at this location
paul_rect = paul.get_rect() # Creates a rectanlge as a bounding box or representation of where the image is located and how large it is.
# This container helps you manage position, size, and movement of the image on screen
# You need rect for every object that you need to manage the position, size, and collision of
feyd = pygame.image.load('/Users/omarsiddiqui/Desktop/feyd.png')
feyd_rect = feyd.get_rect()

run = True #setting it initially to True so that False will end the game
while run: #this is the loop of the actual game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    feyd_rect.x += .5 #want it to move back and forth, so it will move left when it gets to edge of screen
    #check position?
    #Do something where it then goes +- until it hits the left most side of the screen, then goes back to right
    #do this for multiple feyds- could even do multiple characters
    


    userInput = pygame.key.get_pressed() #adjust paul image movement based on player input
    if userInput[pygame.K_LEFT]:
        paul_rect.x -= vel
    if userInput[pygame.K_RIGHT]:
        paul_rect.x += vel
    if userInput[pygame.K_UP]:
        paul_rect.y -= vel
    if userInput[pygame.K_DOWN]:
        paul_rect.y += vel

    # example of OOP: you created the object Paul, and now the attributes that someone made in the pygame library
    # for the created object can be used like x and y

    screen.fill((0, 0, 0))  # Fill the screen with black, basically updating the screen so new visuals can be displayed
    screen.blit(paul, paul_rect)  # allows you to draw image onto another surface-"blit" = "block transfer"
    # drawing image "paul" on the screen at the position and size defined by paul_rect
    screen.blit(feyd,feyd_rect)
    pygame.display.update() #reflects changes to the screen. Without this, you'd have to wait until you run the game again for the screen to fully update

pygame.quit()

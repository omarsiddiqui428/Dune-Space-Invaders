import pygame
pygame.init()

#Screen details
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dune Space Invaders")


#Paul details
paul = pygame.image.load('/Users/omarsiddiqui/Desktop/player.png') #paul to the image you put at this location
paul_rect = paul.get_rect()
paul_vel = 10

#Enemy details- Feyd Rauthas'
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

#laser object
laser = pygame.image.load('/Users/omarsiddiqui/Desktop/laserbullet.png')
laser_rect = laser.get_rect()
laser_vel = 5

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Paul screen location + player key details
    paul_rect.y = 450
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT] and paul_rect.x >= 0:
        paul_rect.x -= paul_vel
    if userInput[pygame.K_RIGHT] and paul_rect.x <= screen_width - paul_rect.width:
        paul_rect.x += paul_vel
    if userInput[pygame.K_SPACE]:
        laser_rect.x = paul_rect.x + 45
        laser_rect.y = paul_rect.y - 60
        laser_rect.y -= laser_vel


    #Feyd Rauthas' screen location + movement details TODO: delete this comment, but these could be made into functions to make more efficient
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

    #screen updates
    screen.fill((0, 0, 0))
    screen.blit(paul, paul_rect)
    screen.blit(feyd1,feyd1_rect)
    screen.blit(feyd2, feyd2_rect)
    screen.blit(feyd3, feyd3_rect)
    screen.blit(feyd4, feyd4_rect)
    screen.blit(laser, laser_rect)
    pygame.display.update()

pygame.quit()

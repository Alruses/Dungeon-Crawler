import pygame, sys
from pygame.locals import *
from level import *
from player import *
from tile import *
from controller import *

findcontrolers(1,1)

#initalize pygame. Pygame is a visual output.
pygame.init()

#set up the screen.
size = (width, height) = (pygame.display.Info().current_w/2, pygame.display.Info().current_h/2)

screen = pygame.display.set_mode(size)

#clock is going to control the refresh rate of the screen
clock = pygame.time.Clock()
backgroundColor = (55,255,55)

images = {"wa": "images/tiles/wall33.gif", "f": "images/tiles/roomFloor13.gif"}
player = Player("images/beings/nightdwarf.gif", (64, 64))

#homework for this week:
    #make the movement events for your various keys
    #instantiate a player
#Optional:
    #make a "door" class in Tiles (inherits from tile, something to enter and exit levels)


def main():
    global screen
    ranLev = RandomLevel(images)
    while True:
        #this is our main game loop
        #tick the clock
        #check if any events have happened i.e. press a button on keyboard, click your mouse, exit program, etc.
        #update all the graphics
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_F1:
                    screen = pygame.display.set_mode(size, FULLSCREEN)
                elif event.key == K_ESCAPE:
                    screen = pygame.display.set_mode(size)
                #elif event.key == K_UP:
                    #player.

        ranLev.update()
        screen.fill(backgroundColor)
        ranLev.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()




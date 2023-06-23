import pygame, sys
from pygame.locals import *
from tile import *



#initalize pygame. Pygame is a visual output.
pygame.init()

#set up the screen.
size = (width, height) = (pygame.display.Info().current_w/2, pygame.display.Info().current_h/2)

screen = pygame.display.set_mode(size)

#clock is going to control the refresh rate of the screen
clock = pygame.time.Clock()
backgroundColor = (55,255,55)



def main():
    global screen
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
        screen.fill(backgroundColor)
        pygame.display.flip()

if __name__ == "__main__":
    main()

#for homework, try intialising a couple of tiles and placing them into your game window. Try with a couple diff pictures, and with a few different types.

#open world - move between different levels. Lower levels are harder.
#player, enemies, power ups, exit square.
#levels themselves - building the levels.
    #big overworld with dungeons.

#one class for level - each level made of a bunch of tiles.


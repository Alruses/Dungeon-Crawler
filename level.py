#level class -
    #info we import - such as size, num of tiles,
    #methods - draw and update

import pygame, random
from tile import *

class Level(pygame.sprite.Sprite):
    #size is a tuple that contains a set of dimensions
    #scrollable
    def __init__(self, size, canScroll):
        super().__init__()
        self.size = size
        self.canScroll = canScroll

        #sprite groups - data structures (like lists)
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.traps = pygame.sprite.Group()
        self.ledges = pygame.sprite.Group()

    def draw(self, screen):
        self.walls.draw(screen)
        self.floors.draw(screen)

#random level is a "subclass" of level
class RandomLevel(Level):
    def __init__(self, images):
        sizeW = random.randint(15, 45)
        sizeH = random.randint(15, 45)
        scroll_bool = sizeW > 30 or sizeH > 30

        super().__init__((sizeW, sizeH), scroll_bool)
        self.generateLevel(images)
        self.w = sizeW
        self.h = sizeH

    def generateLevel(self, images):
        #make a matrix with size of the level
        game_map = []
        for i in range(self.w):
            game_map.append(["wa"] * self.h)

            #wa = wall
            #fl = floor
            #wandering level generation algorithim -
                #make everything into a wall
                #determine what % of level is floor.
                #pick a starting tile
                #moving in random directions (n,s,e,w) converting walls to floors until target number of floors is reached

        #to do half
        floorNum = int(round((self.w * self.h)//2))

        #min amount + random
        #floorNum = int(round(self.w * self.h//4 + random.randint(5, 20)))

        count = 0

        while count < floorNum:
            #homework: plan out the wandering generation algorithim
                #pick a random direciton after each check
                #also check if tile is a wall or floor
                #bonus: check if its an outer wall and skip those


#class blankLevel(Level)
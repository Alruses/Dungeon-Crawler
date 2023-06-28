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
        currTile = [1,1]
        while count < floorNum:
            #this ensures our starting tile stays a floor
            if game_map[1][1] != "f":
                game_map[1][1] = "f"
                count += 1
            #this piece of code turns whatever the currently selected tile into the floor if it isn't one already
            if game_map[currTile[0]][currTile[1]] != "f":
                game_map[currTile[0]][currTile[1]] = "f"
                count += 1

            #pick a random direction to move in, then adjust the values of currTile to match
            move = random.randint(1,4)
            if move == 1 and currTile[0] > 2:
                currTile[0] -= 1
            elif move == 2 and currTile[0] < (self.h - 3):
                currTile[0] += 1
            elif move == 3 and currTile[0] < (self.w - 3):
                currTile[1] += 1
            elif move == 4 and currTile[0] > 2:
                currTile[1] -= 1

        for i in range(len(game_map)):
            for j in range(len(game_map[i])):
                if game_map[i][j] == "wa":
                    #add to sprite group - Instantiate a tile here
                    self.walls.add(Tile(images["wa"], (i*32, j*32), "wall"))
                elif game_map[i][j] == "f":
                    #add to other sprite group - Instantiate a tile here
                    self.floors.add(Tile(images["f"], (i*32, j*32), "floor"))

#class blankLevel(Level)
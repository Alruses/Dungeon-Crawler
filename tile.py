#no obstacle tiles?
import pygame
#wall, image, trap, ledge (hole takes you to lower floor?)

class Tile(pygame.sprite.Sprite): #superclass - class we're inheriteng information from
    #path - file we use for the sprite image
    #pos - x,y position we place the sprite at.
    def __init__(self, path, pos):
        super().__init__() #initalize superclass - in this case, Pygame.Sprite
        self.path = path
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

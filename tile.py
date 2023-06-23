#no obstacle tiles?
import pygame
#wall, image, trap, ledge (hole takes you to lower floor?)

class Tile(pygame.sprite.Sprite):
    #path - file we use for the sprite image
    #pos - x,y position we place the sprite at.
    def __init__(self, path, pos, type):
        super().__init__()
        self.path = pygame.image.load(path)
        self.pos = pos
        self.type = type
        if self.type == "obstacle" or self.type == "ledge":
            self.moveable = True
        else:
            self.moveable = False

        self.rect = self.image.get_rect()
        self.rect.topleft = pos
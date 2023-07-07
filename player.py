import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, path, pos):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.movement = [0,0] #x speed and y speed
        #except for the level attribute, this is an example of a very common pygame sprite that cna move
        self.level = None

    def update(self):
        self.rect.move_ip(self.movement)
        #collision goes here

        self.movement[0] = 0
        self.movement[1] = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def change_x(self, change):
        self.movement[0] = change

    def change_y(self, change):
        self.movement[1] = change
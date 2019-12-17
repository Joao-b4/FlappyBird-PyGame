import pygame
from pygame.locals import *

class Ground(pygame.sprite.Sprite):

    def __init__(self, width, height, game_speed,screen_height, x_position):
        pygame.sprite.Sprite.__init__(self)
        self.game_speed = game_speed

        self.image = pygame.image.load('./assets/sprites/base.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(width,height))
        self.mask = pygame.mask.from_surface(self.image)
        
        self.rect = self.image.get_rect()
        self.rect[1] = screen_height - height
        self.rect[0] = x_position

    def update(self):
        self.rect[0] -= self.game_speed


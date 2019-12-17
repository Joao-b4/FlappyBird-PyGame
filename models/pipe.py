import pygame
from pygame.locals import *

class Pipe(pygame.sprite.Sprite):

    def __init__(self,pipe_width,pipe_height,inverted,x_position,y_size,screen_heigth,game_speed):
        pygame.sprite.Sprite.__init__(self)

        self.game_speed = game_speed

        self.image = pygame.image.load("./assets/sprites/pipe-red.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (pipe_width,pipe_height))
        self.rect = self.image.get_rect()
        self.rect[0] = x_position

        if inverted:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect[1] = - (self.rect[3] - y_size)
        else:
            self.rect[1] = screen_heigth - y_size
        
        self.mask = pygame.mask.from_surface(self.image)


    def update(self):
        self.rect[0] -= self.game_speed 


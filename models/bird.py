import pygame
from pygame.locals import *

class Bird(pygame.sprite.Sprite):
    def __init__(self,screen_width,screen_height,speed,gravity):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.gravity = gravity
        self.images = [
                pygame.image.load('./assets/sprites/bluebird-upflap.png').convert_alpha(),
                pygame.image.load('./assets/sprites/bluebird-midflap.png').convert_alpha(),
                pygame.image.load('./assets/sprites/bluebird-downflap.png').convert_alpha()
            ]
        self.current_image = 0

        self.image = pygame.image.load('./assets/sprites/bluebird-upflap.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        
        self.rect = self.image.get_rect()
        self.rect[0] = screen_width / 2
        self.rect[1] = screen_height / 2


    def update(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[self.current_image] 
        
        self.speed += self.gravity

        #update height
        self.rect[1] += self.speed
    
    def bump(self):
       self.speed = -self.speed
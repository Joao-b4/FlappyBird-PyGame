import pygame
import random
from pygame.locals import *
from models.bird import Bird
from models.ground import Ground
from models.pipe import Pipe

SCREEN_WIDTH  = 400 
SCREEN_HEIGHT = 500

GROUND_WIDTH  = SCREEN_WIDTH*2 
GROUND_HEIGHT = 80

PIPE_WIDTH  = 80
PIPE_HEIGHT = 400
PIPE_GAP = 200

SPEED = 10
GRAVITY = 1
GAME_SPEED = 10

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

BACKGROUND = pygame.image.load("./assets/sprites/background-day.png")
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH,SCREEN_HEIGHT))

def is_off_screen(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

def get_random_pipes(x_position):
    size = random.randint(100,300)
    pipe = Pipe(PIPE_WIDTH, PIPE_HEIGHT, False, x_position, size, SCREEN_HEIGHT, GAME_SPEED)
    pipe_inverted = Pipe(PIPE_WIDTH, PIPE_HEIGHT, True, x_position, SCREEN_HEIGHT - size - PIPE_GAP, SCREEN_HEIGHT, GAME_SPEED)
    return (pipe, pipe_inverted)

bird_group = pygame.sprite.Group()
bird = Bird(SCREEN_WIDTH,SCREEN_HEIGHT,SPEED,GRAVITY)
bird_group.add(bird)

ground_group = pygame.sprite.Group()
for i in range(2):
    ground = Ground(GROUND_WIDTH,GROUND_HEIGHT,GAME_SPEED,SCREEN_HEIGHT, 2 * SCREEN_WIDTH * i)
    ground_group.add(ground)

pipe_group = pygame.sprite.Group()
for i in range(2):
    pipes = get_random_pipes(SCREEN_WIDTH * i +600,) 
    pipe_group.add(pipes[0])
    pipe_group.add(pipes[1])

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bird.bump()

    screen.blit(BACKGROUND, (0,0))
    
    if is_off_screen(ground_group.sprites()[0]):
        ground_group.remove(ground_group.sprites()[0])

        new_group = Ground(GROUND_WIDTH,GROUND_HEIGHT,GAME_SPEED,SCREEN_HEIGHT,GROUND_WIDTH - 20)
        ground_group.add(new_group)

    if is_off_screen(pipe_group.sprites()[0]):
        pipe_group.remove(pipe_group.sprites()[0])
        pipe_group.remove(pipe_group.sprites()[0])

        pipes = get_random_pipes(SCREEN_WIDTH*2)
        pipe_group.add(pipes[0])
        pipe_group.add(pipes[1])


    bird_group.update()
    bird_group.draw(screen)

    pipe_group.update()
    pipe_group.draw(screen)


    ground_group.update()
    ground_group.draw(screen)


    if (pygame.sprite.groupcollide(bird_group,ground_group,False,False,pygame.sprite.collide_mask) or pygame.sprite.groupcollide(bird_group,pipe_group,False,False,pygame.sprite.collide_mask)):
        input()
    
    pygame.display.update() 
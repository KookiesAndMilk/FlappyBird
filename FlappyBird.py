#Flappy Bird en Pygame
import pygame, sys
pygame.init()
screen = pygame.display.set_mode((288,512))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('sprites/background-day.png').convert()

floor_surface = pygame.image.load('sprites/base.png').convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface,(0,0))
    screen.blit(floor_surface,(0,0))

    pygame.display.update()
    clock.tick(120)

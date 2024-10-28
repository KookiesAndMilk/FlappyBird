#Flappy Bird en Pygame
import pygame, sys
def draw_floor():
    screen.blit(floor_surface,(floor_x_position,450))
    screen.blit(floor_surface,(floor_x_position + 288,450))


pygame.init()
screen = pygame.display.set_mode((288,512))
clock = pygame.time.Clock()

#game variables
gravity = 0.25
bird_movement = 0


bg_surface = pygame.image.load('sprites/background-day.png').convert()

floor_surface = pygame.image.load('sprites/base.png').convert()

floor_x_position = 0

bird_surface = pygame.image.load('sprites/pinkbird-midflap.png').convert_alpha()
bird_rect = bird_surface.get_rect(center = (40, 240))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 12

    screen.blit(bg_surface,(0,0))

    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, bird_rect)
    floor_x_position -= 1
    draw_floor()
    if floor_x_position <= -288:
        floor_x_position = 0
    
    
    
    pygame.display.update()
    clock.tick(120)

#Flappy Bird en Pygame
import pygame, sys, random
def draw_floor():
    screen.blit(floor_surface,(floor_x_position,450))
    screen.blit(floor_surface,(floor_x_position + 288,450))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (300,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (300,random_pipe_pos - 150 ))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 512:
            screen.blit(pipe_surface,pipe)
        else: 
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)

def check_collision(pipes):

    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    
    if bird_rect.top <= -50 or bird_rect.bottom >= 450:
        return False
    
    return True        

def rotate_bird (bird):
    new_bird = pygame.transform.rotozoom(bird,-bird_movement *2, 1)
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center= (40, bird_rect.centery))
    return new_bird, new_bird_rect

def score_display():
    score_surface = game_font.render(str('Score'), True,(255,255,255))
    score_rect = score_surface.get_rect(center = (144,100))
    screen.blit(score_surface,score_rect)

pygame.init()
screen = pygame.display.set_mode((288,512))
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.ttf', 40)

#game variables
gravity = 0.25
bird_movement = 0
game_active = True
jump_strenght = -8
high_score = 0

bg_surface = pygame.image.load('sprites/background-day.png').convert()

floor_surface = pygame.image.load('sprites/base.png').convert()

floor_x_position = 0

#bird_surface = pygame.image.load('sprites/pinkbird-midflap.png').convert_alpha()
#bird_rect = bird_surface.get_rect(center = (40, 240))
bird_downflap = pygame.image.load('sprites/pinkbird-downflap.png').convert_alpha ()
bird_midflap = pygame.image.load('sprites/pinkbird-midflap.png').convert_alpha ()
bird_upflap = pygame.image.load('sprites/pinkbird-upflap.png').convert_alpha ()
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames [bird_index]
bird_rect = bird_surface.get_rect(center = (40, 240) )

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)
 
pipe_surface = pygame.image.load('sprites/pipe-brown.png')
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,800)
pipe_height = [320,280,200]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = jump_strenght 
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (40,240)
                bird_movement = 0
        
        if event.type == SPAWNPIPE and game_active:
            pipe_list.extend(create_pipe())
        
        if event.type== BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
            bird_surface, bird_rect = bird_animation()

    screen.blit(bg_surface,(0,0))

    if game_active:

    #Bird movement
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)
        game_active = check_collision(pipe_list)

        #Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        score_display

    floor_x_position -= 1
    draw_floor()
    if floor_x_position <= -288:
        floor_x_position = 0
    
    
    
    pygame.display.update()
    clock.tick(120)

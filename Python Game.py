import pygame
from sys import exit
from random import randint
w_width = 1440
w_height = 720
pygame.init()
screen = pygame.display.set_mode((w_width,w_height))
Clock = pygame.time.Clock()

#background
bg_surface = pygame.Surface((w_width,w_height))
bg_surface.fill('#476fff')


enemy_surface = pygame.Surface((200,100))
enemy_surface.fill('red')
enemy_x_pos = 1200
enemy_y_pos = randint(0,720)
enemy_rect = enemy_surface.get_rect(bottomright = (enemy_x_pos,enemy_y_pos))

player_surf = pygame.Surface((100,100))
player_surf.fill('green')
player_rect = player_surf.get_rect(center = (300,400))
player_grav = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            player_grav -= 150
    enemy_y_pos = randint(0,720)
    screen.blit(bg_surface,(0,0))
    screen.blit(enemy_surface,enemy_rect)
    screen.blit(player_surf,player_rect)
    enemy_rect.x -= 1
    player_grav += 0.6
    player_rect.y = player_grav
    if enemy_rect.right <= 0: 
        enemy_rect.x = enemy_x_pos
        enemy_rect.y = enemy_y_pos
    pygame.display.update()
    Clock = (60)

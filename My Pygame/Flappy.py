import pygame
import random
import threading
import math
import time








print("EPILEPSY WARNING! PROCEED AT YOUR OWN RISK")














pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(100, 100)
enemy_pos = pygame.Vector2(random.randint(10, screen_width-10), random.randint(10, screen_height-10))
y_dt = 0
x_dt = 0
enemy_vel = 3
friction = 0.9
accel = 0.5
max_dt = 5

def handle_keys():
    global x_dt, y_dt

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        if y_dt > -max_dt:
            y_dt -= accel
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        if y_dt < max_dt:
            y_dt += accel
    else:
        y_dt *= friction

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if x_dt > -max_dt:
            x_dt -= accel
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if x_dt < max_dt:
            x_dt += accel
    else:
        x_dt *= friction

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    handle_keys()

    player_pos.x += x_dt
    player_pos.y += y_dt

    # Screen wrap around
    if player_pos.x >= screen_width:
        player_pos.x = 10
    if player_pos.y >= screen_height:
        player_pos.y = 10
    if player_pos.x <= 0:
        player_pos.x = screen_width - 10
    if player_pos.y <= 0:
        player_pos.y = screen_height - 10

    # Enemy movement
    if enemy_pos.y < player_pos.y:
        enemy_pos.y += enemy_vel
    else:
        enemy_pos.y -= enemy_vel

    if enemy_pos.x < player_pos.x:
        enemy_pos.x += enemy_vel
    else:
        enemy_pos.x -= enemy_vel

    # Draw everything
    screen.fill("white")
    pygame.draw.circle(screen, "blue", player_pos, 35)
    pygame.draw.circle(screen, "red", enemy_pos, 30)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()

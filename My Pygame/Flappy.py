import pygame
import random
import threading
import math
import time








print("EPILEPSY WARNING! PROCEED AT YOUR OWN RISK")














pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
running = True
key_handler = None
player_pos = pygame.Vector2(100,100)
enemy_pos = pygame.Vector2(random.randint(10,screen_width-10),random.randint(10,screen_height-10))
y_dt = 0
x_dt = 0
enemy_vel = 3
friction = 1
accel = 1.1
max_dt = 5


def handle_keys():
    global x_dt, y_dt, player_pos,keys

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        if y_dt > -max_dt:
            y_dt -= accel
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        if y_dt < max_dt:
            y_dt += accel
    else:
        if not(y_dt > -0.5 and y_dt < 1.6):
            if y_dt < 1:
                y_dt += friction                
            elif y_dt > 1:
                y_dt -= friction

        else:
            y_dt = 0

        
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x += x_vel
        if x_dt > -max_dt:
            x_dt -= accel
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos.x += x_vel
        if x_dt < max_dt:
            x_dt += accel
    if not(x_dt >= -1 and x_dt <= 1) :
        player_pos.x += x_vel
        if x_dt < 1:
            x_dt += friction

        elif x_dt > 1:
            x_dt -= friction
    else:
        x_dt = 0

    player_pos.y += y_vel
    player_pos.x += x_vel
    
    if player_pos.x >= screen_width:
        player_pos.x = 10
    if player_pos.y >= screen_height:
        player_pos.y = 10
    if player_pos.x <= 0:
        player_pos.x = screen_width -10
    if player_pos.y <= 0:
        player_pos.y = screen_height - 10

    if enemy_pos.y < player_pos.y:
        enemy_pos.y += enemy_vel
    else:
        enemy_pos.y -= enemy_vel

    if enemy_pos.x < player_pos.x:
        enemy_pos.x += enemy_vel
    else:
        enemy_pos.x -= enemy_vel

    


while running:
    y_vel = 3*y_dt
    x_vel = 3*x_dt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    screen.fill("white")
    pygame.draw.circle(screen, "blue", player_pos, 35, width = 50)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_k]:
        print("X-dt: " , x_dt)
        print("y_dt: ",y_dt)
        print("x_vel: ",x_vel)
        print("y_vel: ",y_vel)
        time.sleep(2)
    key_handler = threading.Thread(target = handle_keys)
    key_handler.start()

    #pygame.draw.circle(screen,"red", enemy_pos,30)
    pygame.display.flip()

    clock.tick(60)

key_handler.join()
pygame.quit()

import pygame
import random
import threading
import math
import time


pygame.init()
pygame.font.init()
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
enemy_vel = 1
friction = 0.01
accel = 0.05
max_dt = 50
level_x = 0
level_y = 0
my_font=pygame.font.SysFont("Comic Sans MS", 15)


def handle_keys():
    global x_dt, y_dt, player_pos,keys, level_x, level_y

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        if y_dt > -max_dt:
            y_dt -= accel
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        if y_dt < max_dt:
            y_dt += accel
    else:
        if not(y_dt > -(friction+0.1) and y_dt < (friction + 0.1)):
            if y_dt < 0:
                y_dt += friction                
            elif y_dt > 0:
                y_dt -= friction

        else:
            y_dt = 0

        
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if x_dt > -max_dt:
            x_dt -= accel
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if x_dt < max_dt:
            x_dt += accel
    else:
        if not(x_dt >= -(friction + 0.1) and x_dt <= (friction + 0.1)) :
            if x_dt < 0:
                x_dt += friction

            elif x_dt > 0:
                x_dt -= friction
        else:
            x_dt = 0

    player_pos.y += y_vel
    player_pos.x += x_vel
    
    """if player_pos.x >= screen_width+30:
        player_pos.x = 30
        level_x+=1
    if player_pos.y >= screen_height+30:
        player_pos.y = 30
        level_y-=1
    if player_pos.x <= -30:
        player_pos.x = screen_width - 30
        level_x -= 1
    if player_pos.y <= -30:
        player_pos.y = screen_height - 30
        level_y +=1"""
    if player_pos.x >= screen_width+30:
        player_pos.x = -29
        level_x+=1
    if player_pos.y >= screen_height+30:
        player_pos.y = -29
        level_y-=1
    if player_pos.x <= -30:
        player_pos.x = screen_width+29
        level_x -= 1
    if player_pos.y <= -30:
        player_pos.y = screen_height+29
        level_y +=1

    

    


while running:
    y_vel = 3*y_dt
    x_vel = 3*x_dt
    text_surface = my_font.render(f"{level_x}, {level_y}",False,(0,0,0))
    enemy_dist = math.sqrt(math.fabs(player_pos.y-enemy_pos.y)**2 + math.fabs(player_pos.x - enemy_pos.x)**2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    enemy_pos.y = (enemy_pos.y*(enemy_dist-enemy_vel) + player_pos.y*enemy_vel)/enemy_dist

    enemy_pos.x = (enemy_pos.x*(enemy_dist-enemy_vel) + player_pos.x*enemy_vel)/enemy_dist
    
    screen.fill("white")
    screen.blit(text_surface, (0,0))
    if (math.fabs(x_dt) + math.fabs(y_dt)) > 1:
        i = int(math.fabs(x_dt) + math.fabs(y_dt))
        for t in range(0,i):
            pygame.draw.circle(screen, "cyan", (player_pos.x-t*0.5*x_vel,player_pos.y-t*0.5*y_vel), 35-35*t/i, width = 50)
    pygame.draw.circle(screen, "blue", player_pos, 35, width = 50)

        
    """
    pygame.draw.circle(screen, "blue", (player_pos.x+screen_width,player_pos.y), 35, width = 50)
    pygame.draw.circle(screen, "blue", (player_pos.x-screen_width,player_pos.y), 35, width = 50)
    pygame.draw.circle(screen, "blue", (player_pos.x,player_pos.y+screen_height), 35, width = 50)
    pygame.draw.circle(screen, "blue", (player_pos.x,player_pos.y-screen_height), 35, width = 50)
    
    pygame.draw.circle(screen, "blue", (player_pos.x+screen_width,player_pos.y+screen_height), 35, width = 50)
    pygame.draw.circle(screen, "blue", (player_pos.x-screen_width,player_pos.y-screen_height), 35, width = 50)
    pygame.draw.circle(screen, "blue", (player_pos.x-screen_width,player_pos.y+screen_height), 35, width = 50)
    pygame.draw.circle(screen, "blue", (player_pos.x+screen_width,player_pos.y-screen_height), 35, width = 50)
    """
    keys = pygame.key.get_pressed()


    if keys[pygame.K_k]:
        print("X-dt: " , x_dt)
        print("y_dt: ",y_dt)
        print("x_vel: ",x_vel)
        print("y_vel: ",y_vel)
        print("enemy_dist: ",enemy_dist)
        time.sleep(2)
    key_handler = threading.Thread(target = handle_keys)
    key_handler.start()

    pygame.draw.circle(screen,"red", enemy_pos,30)
    pygame.ACTIVEEVENT
    pygame.display.flip()

    clock.tick(60)

key_handler.join()
pygame.quit()

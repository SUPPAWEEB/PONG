import pygame
import time
import random
pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT= 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

player = pygame.Rect((35,300,15,100))
enemy = pygame.Rect((1150,300,15,100))
ballcolor = (255, 255, 255)  
ball_radius = 19
ball_position = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
ball_velocity = [0.5, 0.5]
playerscore = 0
enemyscore = 0
run = True
font = pygame.font.Font(None, 36)
bigfont = pygame.font.Font(None, 200)
Pscore = font.render(str(playerscore), True, (255, 255, 255))
Escore = font.render(str(enemyscore),True, (255,255,255))
gg = bigfont.render(str("You Win"),True,(255,255,255))
bg = bigfont.render(str("You Lose"),True,(255,255,255))


def AIlol():
    if ball_position[1] < enemy.y + enemy.height // 2:
        if enemy.top > 0:
            if random.randint(1, 3) == 1:  
                enemy.move_ip(0, -1)
    elif ball_position[1] > enemy.y + enemy.height // 2:
        if enemy.bottom < SCREEN_HEIGHT:
            if random.randint(1, 3) == 1:  
                enemy.move_ip(0, 1)


while run: 
    screen.fill((0,0,0))
    screen.blit(Pscore, ((870,120)))
    screen.blit(Escore,((330,120)))
    pygame.draw.circle(screen, ballcolor, ball_position, ball_radius)
    pygame.draw.rect(screen,(255,255,255),enemy)
    pygame.draw.rect(screen,(255,255,255),player)
    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    ball_rect = pygame.Rect(ball_position[0] - ball_radius, ball_position[1] - ball_radius, ball_radius * 2, ball_radius * 2)
    
    AIlol()

    if ball_position[0] - ball_radius < 0:  
        enemyscore+=1
        Pscore = font.render(str(enemyscore), True, (255, 255, 255))
        ball_position = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
        ball_velocity = [-0.5,-0.5]
        
    elif ball_position[0] + ball_radius > SCREEN_WIDTH: 
        playerscore+=1
        Escore = font.render(str(playerscore), True, (255, 255, 255))
        ball_position = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
        ball_velocity = [0.5, 0.5]
        

    if ball_position[1] - ball_radius < 0 or ball_position[1] + ball_radius > SCREEN_HEIGHT:
        ball_velocity[1] *= -1  


    key = pygame.key.get_pressed()
    if key[pygame.K_w] ==True:
     if player.top > 0:
      player.move_ip(0,-1)
    elif key[pygame.K_s]  ==True:
     if player.bottom < SCREEN_HEIGHT:
        player.move_ip(0,1)


    if ball_rect.colliderect(player):
        ball_velocity[0] *= -1
    if ball_rect.colliderect(enemy):
        ball_velocity[0] *= -1



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

    if playerscore == 10:
        screen.fill((0, 0, 0))
        screen.blit(gg, (SCREEN_WIDTH // 2 - gg.get_width() // 2, SCREEN_HEIGHT // 2 - gg.get_height() // 2))
        pygame.display.update()
        time.sleep(5)  
        run = False  
    if enemyscore == 10:
        screen.fill((0, 0, 0))
        screen.blit(bg, (SCREEN_WIDTH // 2 - gg.get_width() // 2, SCREEN_HEIGHT // 2 - gg.get_height() // 2))
        pygame.display.update()
        time.sleep(5)  
        run = False  
        
       
       

pygame.quit()

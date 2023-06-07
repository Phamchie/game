import pygame 
import random


pygame.init()

screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

logo = pygame.image.load('code/Anonymous.png')
pygame.display.set_icon(logo)

pygame.display.set_caption("Game Debut By Chien")

background = pygame.image.load('code/map_game.png')
pygame.transform.scale(background, (700, 500))

set_player = pygame.image.load('code/devil1.png')
set_player = pygame.transform.scale(set_player, (int(set_player.get_width() * 0.2), (int(set_player.get_height() * 0.2 ))))

rows = 40
cols = 40

player_x = 1
player_y = 1

target_x = random.randint(0, 50) * 0.5
target_y = random.randint(0, 50) * 0.5

target1_x = random.randint(0, 50) * 0.5
target1_y = random.randint(0, 50) * 0.5

set_target1 = pygame.image.load('code/df.png')
set_target1 = pygame.transform.scale(set_target1, (int(set_target1.get_width() * 0.2), (int(set_target1.get_height() * 0.2))))

set_target2 = pygame.image.load('code/df.png')
set_target2 = pygame.transform.scale(set_target2, (int(set_target2.get_width() * 0.2), (int(set_target2.get_height() * 0.2))))

font = pygame.font.Font(None, 50)
kill = 0
txt = font.render("KILL :" + str(kill), True, ('red'))

speed = 10

game = True
while game:
    screen.blit(background, (6, 6))
    screen.blit(txt, (10, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rows -= speed
            if event.key == pygame.K_RIGHT:
                rows += speed
            if event.key == pygame.K_UP:
                cols -= speed
            if event.key == pygame.K_DOWN:
                cols += speed

            rows -= speed
            rows += speed
            cols -= speed
            cols += speed

            player_rect = pygame.Rect(player_x, player_y, set_player.get_width(), set_player.get_height())
            enemy1_rect = pygame.Rect(target_x, target_y, set_target1.get_width(), set_target1.get_height())
            enemy2_rect = pygame.Rect(target1_x, target1_y, set_target2.get_width(), set_target2.get_height())

            if player_rect.colliderect(enemy1_rect):
                kill += 1
                target_x = random.randint(0, 600) * 0.5
                target_y = random.randint(0, 400) * 0.5

            if player_rect.colliderect(enemy2_rect):
                kill += 1 
                target1_x = random.randint(300, 600) * 0.5
                target1_y = random.randint(300, 600) * 0.5
        
        screen.blit(set_player, (rows, cols))
        screen.blit(set_target1, (target_x, target_y))
        screen.blit(set_target2, (target1_x, target1_y))
        pygame.draw.rect(screen, ('blue'), (rows, cols, player_x, player_y))
        pygame.draw.rect(screen, ('red'), (target_x, target_y, player_x, player_y))
        pygame.draw.rect(screen, ('red'), (target1_x, target1_y, player_x, player_y))
        pygame.display.update()

pygame.quit()

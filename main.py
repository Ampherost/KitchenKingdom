import pygame
import sys

pygame.init()

TILE_SIZE = 32

tilemap = [
    [0, 1, 1, 0, 2],
    [1, 0, 2, 1, 0],
    [0, 1, 0, 2, 1],
    [2, 0, 1, 0, 1],
    [1, 1, 2, 1, 0]
]



ScreenWidth = 800
ScreenHeight = 1200

screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))

player = pygame.Rect((50, 50, 50, 50))

gameRunning = True
while gameRunning:

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), player)

    input = pygame.key.get_pressed()
    if input[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif input[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif input[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif input[pygame.K_s] == True:
        player.move_ip(0, 1)
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
    
    pygame.display.update()

pygame.quit()
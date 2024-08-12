import pygame
import sys

pygame.init()

ScreenWidth = 800
ScreenHeight = 600
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))

try:
    mainCharacterSprite = pygame.image.load("assets/images/mainCharacter/walking/character.png")
    print("Image loaded successfully!")
except pygame.error as e:
    print(f"Failed to load image: {e}")
    sys.exit()

player = mainCharacterSprite

player_position = [50, 50]  

gameRunning = True
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_position[0] -= 1  # left
    if keys[pygame.K_d]:
        player_position[0] += 1  # right
    if keys[pygame.K_w]:
        player_position[1] -= 1  # up
    if keys[pygame.K_s]:
        player_position[1] += 1  # down

    screen.fill((0, 0, 0))

    screen.blit(player, player_position)

    pygame.display.flip()

pygame.quit()

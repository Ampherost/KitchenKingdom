import pygame
import sys

pygame.init()

# Set up the screen
ScreenWidth = 800
ScreenHeight = 600
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))

# Load the sprite sheet
try:
    sprite_sheet = pygame.image.load("assets/images/mainCharacter/walking/character.png")
    print("Sprite sheet loaded successfully!")
except pygame.error as e:
    print(f"Failed to load sprite sheet: {e}")
    sys.exit()

# Define constants for the sprite dimensions
SPRITE_WIDTH = 50
SPRITE_HEIGHT = 50

# Function to extract a sprite from the sprite sheet
def get_sprite(sheet, x, y, width, height):
    sprite = pygame.Surface((width, height), pygame.SRCALPHA)
    sprite.blit(sheet, (0, 0), (x, y, width, height))
    return sprite

# Extract individual sprites (assuming they are arranged in a grid on the sheet)
sprite_down = get_sprite(sprite_sheet, 0, 0, SPRITE_WIDTH, SPRITE_HEIGHT)  # Default sprite
sprite_left = get_sprite(sprite_sheet, SPRITE_WIDTH, 0, SPRITE_WIDTH, SPRITE_HEIGHT)
sprite_right = get_sprite(sprite_sheet, 2 * SPRITE_WIDTH, 0, SPRITE_WIDTH, SPRITE_HEIGHT)
sprite_up = get_sprite(sprite_sheet, 3 * SPRITE_WIDTH, 0, SPRITE_WIDTH, SPRITE_HEIGHT)

# Set up the initial position and default sprite
player_position = [50, 50]
player_sprite = sprite_down

# Main game loop
gameRunning = True
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

    # Handle input and change the sprite based on direction
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:  # Left
        player_position[0] -= 1
        player_sprite = sprite_left
    elif keys[pygame.K_d]:  # Right
        player_position[0] += 1
        player_sprite = sprite_right
    elif keys[pygame.K_w]:  # Up
        player_position[1] -= 1
        player_sprite = sprite_up
    elif keys[pygame.K_s]:  # Down
        player_position[1] += 1
        player_sprite = sprite_down

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the player sprite at the current position
    screen.blit(player_sprite, player_position)

    # Update the display
    pygame.display.flip()

pygame.quit()

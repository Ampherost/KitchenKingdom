# game.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from sprites import load_sprite_sheet, get_sprite
from map import create_tile_map  # Correct import from map.py

def run_game():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Kitchen Kingdom")

    # Load sprite sheet and individual sprites
    sprite_sheet = load_sprite_sheet("assets/images/mainCharacter/walking/character.png")
    sprite_down = get_sprite(sprite_sheet, 0, 0, 50, 50, 1.5)
    sprite_left = get_sprite(sprite_sheet, 50, 0, 50, 50, 1.5)
    sprite_right = get_sprite(sprite_sheet, 100, 0, 50, 50, 1.5)
    sprite_up = get_sprite(sprite_sheet, 150, 0, 50, 50, 1.5)

    # Create the player
    player = Player(sprite_down, sprite_left, sprite_right, sprite_up, [50, 50])

    tile_map = create_tile_map()

    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        keys = pygame.key.get_pressed()
        player.move(keys)

        screen.fill((0, 0, 0))
        tile_map.draw(screen)

        player.draw(screen)
        pygame.display.flip()

    pygame.quit()

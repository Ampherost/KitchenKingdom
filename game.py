import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from sprites import load_sprite_sheet, load_animation_frames
from map import create_tile_map

def run_game():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Kitchen Kingdom")

    # Load the sprite sheet
    sprite_sheet = load_sprite_sheet("assets/images/mainCharacter/walking/character.png")

    # Load animation frames for each direction
    frames_down = load_animation_frames(sprite_sheet, 0, 0, 48, 48, 4)   # Assuming 4 frames for walking down
    frames_left = load_animation_frames(sprite_sheet, 0, 96, 48, 48, 4)  # 4 frames for walking left
    frames_right = load_animation_frames(sprite_sheet, 0, 144, 48, 48, 4) # 4 frames for walking right
    frames_up = load_animation_frames(sprite_sheet, 0, 48, 48, 48, 4)   # 4 frames for walking up

    # Create the player with the animation frames
    player = Player(frames_down, frames_left, frames_right, frames_up, [50, 50])

    tile_map = create_tile_map()

    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        keys = pygame.key.get_pressed()
        player.move(keys)

        # Update player animation
        player.update()

        # Render everything
        screen.fill((0, 0, 0))
        tile_map.draw(screen)
        player.draw(screen)
        pygame.display.flip()

    pygame.quit()


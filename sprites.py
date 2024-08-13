# sprites.py
import pygame

def load_sprite_sheet(path):
    try:
        sprite_sheet = pygame.image.load(path).convert_alpha()
        print("Sprite sheet loaded successfully!")
        return sprite_sheet
    except pygame.error as e:
        print(f"Failed to load sprite sheet: {e}")
        raise SystemExit(e)

def get_sprite(sheet, x, y, width, height, scale_factor=1):
    sprite = pygame.Surface((width, height), pygame.SRCALPHA)
    sprite.blit(sheet, (0, 0), (x, y, width, height))
    if scale_factor != 1:
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)
        sprite = pygame.transform.scale(sprite, (new_width, new_height))
    return sprite

def load_animation_frames(sheet, start_x, start_y, width, height, num_frames):
    """Extracts multiple frames from a sprite sheet."""
    frames = []
    for i in range(num_frames):
        # Calculate the x position of each frame
        x = start_x + i * width
        y = start_y
        # Extract the frame from the sprite sheet
        frame = sheet.subsurface(pygame.Rect(x, y, width, height))
        frames.append(frame)
    return frames


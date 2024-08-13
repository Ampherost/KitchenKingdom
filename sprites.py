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


def load_animation_frames(sheet, start_x, start_y, width, height, num_frames, scale_factor=1):
    frames = []
    for i in range(num_frames):
        # Extract the frame from the sprite sheet
        frame = sheet.subsurface(pygame.Rect(start_x + i * width, start_y, width, height))
        
        # Scale the frame
        if scale_factor != 1:
            scaled_width = int(width * scale_factor)
            scaled_height = int(height * scale_factor)
            frame = pygame.transform.scale(frame, (scaled_width, scaled_height))
        
        frames.append(frame)
    return frames



# player.py
import pygame
from settings import PLAYER_SPEED
from sprites import load_animation_frames

class Player:
    def __init__(self, frames_down, frames_left, frames_right, frames_up, position):
        self.animations = {
            'down': frames_down,
            'left': frames_left,
            'right': frames_right,
            'up': frames_up
        }
        
        self.current_animation = 'down'
        self.current_frame = 0
        self.animation_speed = 350  # milliseconds between frames
        self.last_update = pygame.time.get_ticks()
        self.image = self.animations[self.current_animation][self.current_frame]
        self.rect = self.image.get_rect(topleft=position)

    def move(self, keys):
        if keys[pygame.K_a]:
            self.current_animation = 'left'
            self.rect.x -= 1  # Move left
        elif keys[pygame.K_d]:
            self.current_animation = 'right'
            self.rect.x += 1  # Move right
        elif keys[pygame.K_w]:
            self.current_animation = 'up'
            self.rect.y -= 1  # Move up
        elif keys[pygame.K_s]:
            self.current_animation = 'down'
            self.rect.y += 1  # Move down

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.animations[self.current_animation])
            self.image = self.animations[self.current_animation][self.current_frame]

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)


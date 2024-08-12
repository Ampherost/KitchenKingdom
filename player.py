# player.py
import pygame
from settings import PLAYER_SPEED

class Player:
    def __init__(self, sprite_down, sprite_left, sprite_right, sprite_up, position):
        self.sprites = {
            'down': sprite_down,
            'left': sprite_left,
            'right': sprite_right,
            'up': sprite_up
        }
        self.current_sprite = self.sprites['down']
        self.position = position

    def move(self, keys):
        if keys[pygame.K_a]:  # Left
            self.position[0] -= PLAYER_SPEED
            self.current_sprite = self.sprites['left']
        elif keys[pygame.K_d]:  # Right
            self.position[0] += PLAYER_SPEED
            self.current_sprite = self.sprites['right']
        elif keys[pygame.K_w]:  # Up
            self.position[1] -= PLAYER_SPEED
            self.current_sprite = self.sprites['up']
        elif keys[pygame.K_s]:  # Down
            self.position[1] += PLAYER_SPEED
            self.current_sprite = self.sprites['down']

    def draw(self, screen):
        screen.blit(self.current_sprite, self.position)

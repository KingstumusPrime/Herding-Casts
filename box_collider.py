import pygame
from settings import *

class Box(pygame.sprite.Sprite):
    def __init__(self, pos, groups, type, count, height) -> None:
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE, height))
        self.image.fill((178,107,0))
        self.rect = self.image.get_rect(topleft=pos)
        self.count = 0.0
        self.type = type
        self.max = count

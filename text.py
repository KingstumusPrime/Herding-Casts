from itertools import count
import settings
import pygame
from settings import *

class Text(pygame.sprite.Sprite):
    def __init__(self, pos, groups, type, link) -> None:
        super().__init__(groups)
        self.link = link
        self.type = type
        self.image = FONT.render(f"1", True, white, None)
        self.rect = self.image.get_rect(topleft=pos)
        self.count = 0.0
        self.max = 0
        self.Filled = False
        self._layer= 1

    def update(self):
        for i in self.link:
            if i.type == self.type:
                self.count = i.count
                self.max = i.max
            if not self.count.is_integer():
                self.count += 0.5
        if self.count == self.max and not self.Filled:
            self.Filled = True
            settings.FILLED += 1
        self.image = FONT.render(f"{str(int(self.count))}/{self.max}", True, white, None)
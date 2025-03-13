from email.mime import image
import pygame
from settings import *
from time import sleep

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites) -> None:
        super().__init__(groups)
        sleep(0.1)
        self._layer = 1000
        self.image = pygame.Surface((TILE_SIZE + 5, TILE_SIZE * 2), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2()
        self.speed = 3
        self.gravity = 0.8
        self.jump_speed = 18
        self.collision_sprites = collision_sprites
        self.type = "Manager"
        self.on_floor = False
    
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        
        if keys[pygame.K_UP] and self.on_floor:
            self.direction.y = -self.jump_speed

    def horizontal_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect) and sprite is not self:
                if self.direction.x < 0:
                    if type(sprite).__name__ != "Box":
                        self.rect.left = sprite.rect.right
                    else:
                        pass
                if self.direction.x > 0:
                    if type(sprite).__name__ != "Box":
                        self.rect.right = sprite.rect.left
                    else:
                        pass

    def verticle_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect) and sprite is not self:
                if self.direction.y > 0:
                    if type(sprite).__name__ != "Box":
                        self.rect.bottom = sprite.rect.top
                        self.direction.y = 0
                        self.on_floor = True
                    else:
                        pass
                if self.direction.y < 0:
                    if type(sprite).__name__ != "Box":
                        self.rect.top = sprite.rect.bottom
                        self.direction.y = 0
                    else:
                        pass
        if self.on_floor and self.direction.y != 0:
            self.on_floor = False

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.image.blit(PLAYER, (0,0))
        self.image.blit(PLAYER, (50,0))
        self.input()
        self.rect.x += self.direction.x * self.speed
        self.horizontal_collisions()
        self.apply_gravity()
        self.verticle_collisions()

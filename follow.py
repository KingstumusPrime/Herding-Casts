import pygame
from settings import *
import time

class Follow(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites, type , art) -> None:
        super().__init__(groups)
        time.sleep(0.01)
        self.type = type
        self.art = art
        self.image = pygame.Surface((art.get_width(), art.get_height()))
        self.direction = pygame.math.Vector2()
        self.speed = 3
        self.rect = self.image.get_rect(topleft=pos)
        self.gravity = 0.8
        self.jump_speed = 18
        self.collision_sprites = collision_sprites
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
                    if type(sprite).__name__ != "Box" or self.type != "Manager" and self.type != sprite.type:
                        self.rect.left = sprite.rect.right
                    else:
                        self.kill()
                        sprite.count += 0.5
                if self.direction.x > 0:
                    if type(sprite).__name__ != "Box" or self.type != "Manager" and self.type != sprite.type:
                        self.rect.right = sprite.rect.left
                    else:
                        self.kill()
                        sprite.count += 0.5

    def verticle_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect) and sprite is not self:
                if self.direction.y > 0:
                    if type(sprite).__name__ != "Box" or self.type != "Manager" and self.type != sprite.type:
                        self.rect.bottom = sprite.rect.top
                        self.direction.y = 0
                        self.on_floor = True
                    else:
                        self.kill()
                        sprite.count += 0.5
                if self.direction.y < 0:
                    if type(sprite).__name__ != "Box" or self.type != "Manager" and self.type != sprite.type:
                        self.rect.top = sprite.rect.bottom
                        self.direction.y = 0
                    else:
                        self.kill()
                        sprite.count += 0.5
        if self.on_floor and self.direction.y != 0:
            self.on_floor = False
    
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.image.blit(self.art, (0,0))
        self.input()
        self.rect.x += self.direction.x * self.speed
        self.horizontal_collisions()
        self.apply_gravity()
        self.verticle_collisions()

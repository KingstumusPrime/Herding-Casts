import pygame

from settings import *
from tile import Tile
from images.player import Player
from follow import Follow
from box_collider import Box
import settings
from text import Text
class Level:
    def __init__(self, level_map, level) -> None:
        self.level = level_map
        self.level_num = level
        self.display_surface = pygame.display.get_surface()
        self.player_sprites = pygame.sprite.Group()
        self.visible_sprites = CameraGroup(self.player_sprites)
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.box_sprites = pygame.sprite.Group()
        self.setup_level()

    def setup_level(self):
        for row_index, row in enumerate(self.level):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if col == 'X':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites])
                if col == 'P':
                    self.player = Player((x,y),[self.visible_sprites, self.active_sprites, self.player_sprites,self.collision_sprites], self.collision_sprites)
                    if self.level_num == 0:
                        Follow((x - 50,y),[self.visible_sprites, self.active_sprites, self.player_sprites,self.collision_sprites], self.collision_sprites, "A", pygame.image.load(("./images/bulk.png")))
                    elif self.level_num == 1:
                        Follow((x - 50,y),[self.visible_sprites, self.active_sprites, self.player_sprites,self.collision_sprites], self.collision_sprites, "A", pygame.image.load(("./images/ben.png")))
                        Follow((x - 90,y),[self.visible_sprites, self.active_sprites, self.player_sprites,self.collision_sprites], self.collision_sprites, "B", pygame.image.load(("./images/dario.png")))
                        Follow((x - 140,y),[self.visible_sprites, self.active_sprites, self.player_sprites,self.collision_sprites], self.collision_sprites, "A", pygame.image.load(("./images/rysu.png")))
                        Follow((x - 190,y),[self.visible_sprites, self.active_sprites, self.player_sprites,self.collision_sprites], self.collision_sprites, "B", pygame.image.load(("./images/squige.png")))
                    elif self.level_num == 2:
                        Follow((x - 50,y),[self.visible_sprites, self.active_sprites, self.player_sprites,self.collision_sprites], self.collision_sprites, "B", pygame.image.load(("./images/pig_fam_pegga.png")))
                        Follow((x - 90,y),[self.visible_sprites, self.active_sprites, self.player_sprites,self.collision_sprites], self.collision_sprites, "B", pygame.image.load(("./images/pig_fam_storge.png")))
                        Follow((x - 140,y),[self.visible_sprites, self.active_sprites, self.player_sprites,self.collision_sprites], self.collision_sprites, "A", pygame.image.load(("./images/goon_1.png")))
                        Follow((x - 190,y),[self.visible_sprites, self.active_sprites, self.player_sprites,self.collision_sprites], self.collision_sprites, "A", pygame.image.load(("./images/goon_2.png")))
                        Follow((x - 230,y),[self.visible_sprites, self.active_sprites, self.player_sprites,self.collision_sprites], self.collision_sprites, "B", pygame.image.load(("./images/pig_fam_mom.png")))
                        Follow((x - 270,y),[self.visible_sprites, self.active_sprites, self.player_sprites,self.collision_sprites], self.collision_sprites, "A", pygame.image.load(("./images/goon_3.png")))
                        Follow((x - 320,y),[self.visible_sprites, self.active_sprites, self.player_sprites,self.collision_sprites], self.collision_sprites, "B", pygame.image.load(("./images/pig_fam_Dad.png")))
                if col == 'A':
                    if self.level_num == 0:
                        Box((x,y), [self.visible_sprites, self.collision_sprites, self.box_sprites], 'A', 1, TILE_SIZE * 4)
                    elif self.level_num == 1:
                            Box((x,y), [self.visible_sprites, self.collision_sprites, self.box_sprites], 'A', 2, TILE_SIZE * 3)
                    elif self.level_num == 2:
                            Box((x,y), [self.visible_sprites, self.collision_sprites, self.box_sprites], 'A', 3, TILE_SIZE * 3)
                if col == 'B':
                    if self.level_num == 0:
                        Box((x,y), [self.visible_sprites, self.collision_sprites, self.box_sprites], 'B', 0, 0)
                    elif self.level_num == 1:
                        Box((x,y), [self.visible_sprites, self.collision_sprites, self.box_sprites], 'B', 2, TILE_SIZE * 4)
                    elif self.level_num == 2:
                        Box((x,y), [self.visible_sprites, self.collision_sprites, self.box_sprites], 'B', 4, TILE_SIZE * 4)
                if col == "b":
                    Text((x,y), [self.visible_sprites, self.active_sprites], "B", self.box_sprites)
                if col == "a":
                    Text((x,y), [self.visible_sprites, self.active_sprites], "A", self.box_sprites)
    def reset(self):
        self.visible_sprites.reset()
        for i in self.visible_sprites:
            i.kill()
        for i in self.collision_sprites:
            i.kill()
        for i in self.active_sprites:
            i.kill()

                    

            



    def run(self):
        self.active_sprites.update()
        self.visible_sprites.custom_draw(self.player)

class CameraGroup(pygame.sprite.Group):
    def __init__(self, players) -> None:
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(100,300)

        # center cam
        # self.half_w = self.display_surface.get_size()[0]/2
        # self.half_h = self.display_surface.get_size()[1]/2

        # box cam
        cam_left = CAMERA_BORDERS['left']
        self.fall_time = 0
        self.players = players
        self.follow_fall = 0
        cam_top = CAMERA_BORDERS['top']
        cam_width = self.display_surface.get_width() - (cam_left + CAMERA_BORDERS['right'])
        cam_hieght = self.display_surface.get_height() - (cam_top + CAMERA_BORDERS['bottom'])

        self.camera_rect = pygame.Rect(cam_left, cam_top, cam_width, cam_hieght)


    def custom_draw(self, player):
        # self.offset.x = player.rect.centerx - self.half_w
        # self.offset.y = player.rect.centery - self.half_h
        if player.on_floor:
            self.fall_time = 0
        # get camera pos
        if player.rect.left < self.camera_rect.left:
            self.camera_rect.left = player.rect.left
        if player.rect.right > self.camera_rect.right:
            self.camera_rect.right = player.rect.right
        if player.rect.top > self.camera_rect.top:
            self.camera_rect.top = player.rect.top
            self.fall_time += 0.1
            if self.fall_time > 2:
                self.fall_time = 0
                settings.RESTART = True
        if player.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = player.rect.bottom

        self.offset = pygame.math.Vector2(self.camera_rect.left - CAMERA_BORDERS['left'],
        self.camera_rect.top - CAMERA_BORDERS['top'])

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

        for i in self.players:
            if i.rect.top > self.camera_rect.top:
                self.camera_rect.top = i.rect.top
                self.follow_fall += 0.1
                self.fall_time += 0.1
                if self.follow_fall > 2:
                    self.follow_fall = 0
                    settings.RESTART = True
    def reset(self):
        self.offset = pygame.math.Vector2(100,300)

        cam_left = CAMERA_BORDERS['left']
        self.fall_time = 0
        cam_top = CAMERA_BORDERS['top']
        cam_width = self.display_surface.get_width() - (cam_left + CAMERA_BORDERS['right'])
        cam_hieght = self.display_surface.get_height() - (cam_top + CAMERA_BORDERS['bottom'])

        self.camera_rect = pygame.Rect(cam_left, cam_top, cam_width, cam_hieght)
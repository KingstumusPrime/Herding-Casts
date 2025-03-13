from operator import le
import time
import asyncio
import pygame, sys
import os
from level import Level
import settings

# had to delete
# def resource_path(relative_path):
#     try:
#     # PyInstaller creates a temp folder and stores path in _MEIPASS
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")

#     return os.path.join(base_path, relative_path)


async def main():
    pygame.init()


    level_select = False
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HIEGHT))
    clock = pygame.time.Clock()

    Menu = True
    buttons = []
    index = 0
    while index < len(settings.INTRO):
        screen.blit(settings.INTRO[index], (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            index += 1
            if index >= len(settings.INTRO):
                break
            screen.blit(settings.INTRO[index], (0,0))
            time.sleep(0.2)
        pygame.display.update()
        clock.tick(60)


    while True:
        if level_select:
            screen.blit(pygame.image.load(("./images/menu.png")), (0,0  ))
            buttons = []
            for x in range(3):
                play_btn = pygame.Surface((70, 70))
                play_btn.fill(settings.TILE_COLOR)
                play_btn_rect = play_btn.get_rect(center=(500 + x * 100, settings.SCREEN_HIEGHT/2))
                screen.blit(play_btn, play_btn_rect)

                text = settings.FONT_L.render(str(x + 1), True, (255,255,255))
                text_rect = text.get_rect(center=(500 + x * 100, settings.SCREEN_HIEGHT/2))
                screen.blit(text, text_rect)
                buttons.append(play_btn_rect)


            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    for index, i in enumerate(buttons):
                        if i.collidepoint(pos):
                            settings.LEVEL = index
                            level = Level(settings.LEVELS[settings.LEVEL], settings.LEVEL)
                            level_select = False

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


        elif Menu:
            screen.fill((0,0,0))
            image = pygame.image.load("images/menu.png")
            screen.blit(image, (0,0))


            play_btn = pygame.image.load("images/play_btn.png")
            play_btn_rect = play_btn.get_rect(center=(settings.SCREEN_WIDTH/2, 400))
            screen.blit(play_btn, play_btn_rect)



            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    # get a list of all sprites that are under the mouse cursor
                    if play_btn_rect.collidepoint(pos):
                        Menu = False
                        level_select = True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            

            

        else:
            screen.blit(settings.BACKGROUNDS[settings.LEVEL], (0,0))
            level.run()
            if settings.RESTART == True:
                settings.RESTART = False
                level.reset()
                level.setup_level()
            if settings.LEVEL == 0:
                count = 1
            else:
                count = 2
            if settings.FILLED == count:
                settings.FILLED = 0
                settings.LEVEL += 1
                level.reset()
                level = Level(settings.LEVELS[settings.LEVEL], settings.LEVEL)
                level.player.kill()
                for sprite in level.player_sprites.sprites():
                    sprite.kill()
                level.setup_level()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



        pygame.display.update()
        await asyncio.sleep(0)
        clock.tick(60)
asyncio.run(main())
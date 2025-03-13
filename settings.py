from pickle import FALSE
from xmlrpc.client import TRANSPORT_ERROR
import pygame

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)


LEVELS = []

# LEVEL_MAP_1 = [
# '                                                                  ',
# '                                                                  ',
# '                                                                  ',
# '                                                                  ',
# '                                                                  ',
# '                                                                  ',
# '                                                                  ',
# '                                                                  ',
# '                                                                  ',
# '                                                                  ',
# '                                                                  ',
# '                                                                  ',
# '      P                                                A     a    ',
# '                                          XX                     X',
# '                                         XXX           XXXXXXXXXXX',
# '                                        XXXX   XX      B     b  X ',
# '                                       XXXXX   XXX              X',
# 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXX '
# ]


LEVEL_MAP_1 = [
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'X                                      ',
'X                            XXXXXXXXXX',
'X                            A         ',
'X       XXXXXXX                        ',
'X       X     X                    a   ',
'X       X  P  X        X               ',
'XXXXXXXXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXX'
]




LEVELS.append(LEVEL_MAP_1)

LEVEL_MAP_2 = [
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'X                           A  X     ',
'X                              X  a  ',
'X                              X     ',  
'X                              X     ',
'X         P                XXXXXXXXXXXXXX',
'X                          B  X   b  ',
'X                             X      ',
'X    X              X   X     X      ',
'XXXXXXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXXXXX'
]


LEVELS.append(LEVEL_MAP_2)

LEVEL_MAP_3 = [
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'                                       ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'X                                                   X',
'X                                         A    a    X',
'X            P         X                            X',
'X                     XX               XXXXXXXXXXXXXX',
'X                    XXX                  B         X',
'X                   XXXX        XX              b   X',
'X                  XXXXX     X  XXXX                X',
'XXXXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXXXXXXXXXXX'
]


LEVELS.append(LEVEL_MAP_3)

FILLED = 0


TILE_SIZE = 32
SCREEN_WIDTH = 1280
SCREEN_HIEGHT = 720

BG_COLOR = '#060c17'
PLAYER_COLOR = '#C4F7FF'
TILE_COLOR = (73,61,61)

CAMERA_BORDERS = {
    'left': 75,
    'right': 75,
    'top': 900,
    'bottom':28
}
FONT = pygame.font.Font('pixeloid-font/PixeloidSansBold-RpeJo.ttf', 32)
FONT_L = pygame.font.Font('pixeloid-font/PixeloidSansBold-RpeJo.ttf', 84)
PLAYER = pygame.image.load(("./player.png"))

LEVEL = 0
RESTART = False


sound = pygame.mixer.music.load(("./soundtrack.wav"))
pygame.mixer.music.play()

INTRO = [pygame.image.load(("./images/intro_1.png")),pygame.image.load(("./images/intro_2.png")),pygame.image.load(("./images/intro_3.png")),pygame.image.load(("./images/intro_4.png"))]
BACKGROUNDS = [pygame.image.load(("./images/Background_1.png")), pygame.image.load(("./images/Background_2.png")),pygame.image.load(("./images/Background_3.png")),]

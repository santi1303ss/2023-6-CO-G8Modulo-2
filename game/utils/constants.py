import pygame
import os

pygame.init()
pygame.mixer.init()

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
TEXT_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
BULLET_ENEMY_TYPE = 'enemy'


SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/ovni2.png"))
OVNI = pygame.image.load(os.path.join(IMG_DIR, "Enemy/ovni.png"))

FONT_STYLE = 'freesansbold.ttf'
FONT_TITLE = os.path.join(TEXT_DIR, 'Other/fuente_1.ttf')
FONT_BODY = os.path.join(TEXT_DIR, 'Other/fuente_2.ttf')

#Sounds
#BURST_ENEMY_SOUND = os.path.join(SOUND_DIR, "shoot_sound.wav")

WALLPAPER= pygame.image.load(os.path.join(IMG_DIR, "Other/Track.JPG"))
WALLPAPER2= pygame.image.load(os.path.join(IMG_DIR, "Other/Track1.JPG"))
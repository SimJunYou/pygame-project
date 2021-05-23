from pygame import freetype, USEREVENT

# Import pg.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_w,
    K_a,
    K_s,
    K_d,
    K_ESCAPE,
    K_BACKSPACE,
    KEYDOWN,
    QUIT,
)

# Movement sets
P1_MOVE = {"L": K_LEFT,
           "R": K_RIGHT,
           "U": K_UP,
           "D": K_DOWN}
P2_MOVE = {"L": K_a,
           "R": K_d,
           "U": K_w,
           "D": K_s}

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 0, 255)
BLUE = (0, 255, 0)

# Events
REMOVE_INV = USEREVENT + 1
HEAL = USEREVENT + 2

# Game constants
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1000
FPS = 60

# Fonts
freetype.init()
FONT = freetype.SysFont("Mono", 24)

# Player specific constants
P1_SPRITE = "milk_sprite.png"
P1_ALT_SPRITE = "milk_alt_sprite.png"
P1_SIZE = (100, 130)
P1_ALT_SIZE = (150, 180)
P1_START = (100, 800)
P1_SPEED = {"max_y": 30,
            "max_x": 7,
            "accel": 1,
            "jump": 25}

P2_SPRITE = "mocha_sprite.png"
P2_SIZE = (110, 150)
P2_START = (1000, 800)
P2_SPEED = {"max_y": 30,
            "max_x": 5,
            "accel": 1,
            "jump": 22}

# Player globals
FRICTION = 1
GRAVITY = 1
DMG_ALPHA = 150

# Platforms
# 1. Middle
# 2. Floor
PLATFORM_COORDS = (((400, 300), (200, 20)),\
                   ((1080, 720), (200, 20)),
                   ((1280, 520), (20, 200)))
                   #((0,SCREEN_HEIGHT-50), (SCREEN_WIDTH, 50)))

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
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024
FPS = 60
BACKGROUND = "assets/background.png"
LEFT_T = "assets/tiles/grassCliffLeft.png"
CENTER_T = "assets/tiles/grassMid.png"
RIGHT_T = "assets/tiles/grassCliffRight.png"

# Fonts
freetype.init()
FONT = freetype.SysFont("Mono", 24)

# Player specific constants
P1_SPRITE = "assets/milk_sprite.png"
P1_ALT_SPRITE = "assets/milk_alt_sprite.png"
P1_SIZE = (60, 75)
P1_ALT_SIZE = (75, 83)
P1_START = (100, 900)
P1_SPEED = {"max_y": 30,
            "max_x": 7,
            "accel": 1,
            "jump": 25}

P2_SPRITE = "assets/mocha_sprite.png"
P2_SIZE = (70, 90)
P2_START = (800, 900)
P2_SPEED = {"max_y": 30,
            "max_x": 5,
            "accel": 1,
            "jump": 22}

# Player globals
FRICTION = 1
GRAVITY = 1
DMG_ALPHA = 150

# Level layout
LEVEL_1 = ('................................',
           '................................',
           '................................',
           '................................',
           '................................',
           '................................',
           '................................',
           '................................',
           '................................',
           '................................',
           '................................',
           '................................',
           '................................',
           '................................',
           '................................',
           '................................',
           '....<===================>.......', 
           '................................',
           '................................',
           '................................',
           '................................',
           '................................',
           '................................',
           '....<======>....................', 
           '................................',
           '................................', 
           '................................', 
           '................................', 
           '.............<==========>.......', 
           '................................', 
           '................................', 
           '................................')

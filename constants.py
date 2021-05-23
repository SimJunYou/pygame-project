from pygame import freetype

freetype.init()

# Import pg.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 0, 255)
BLUE = (0, 255, 0)

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
FONT = freetype.SysFont("Mono", 24)

# Sprites
SPRITE_1 = "milk_sprite.png"
SPRITE_2 = "mocha_sprite.jpg"

# Movement
MAX_Y_SPEED = 20
MAX_X_SPEED = 5
ACCEL = 1
JUMP_SPEED = 20
FRICTION = 1
GRAVITY = 1

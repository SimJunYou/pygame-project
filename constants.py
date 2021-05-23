from pygame import freetype

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

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define constants for player width and height
PLAYER_WIDTH = 25
PLAYER_HEIGHT = 75
MAX_Y_SPEED = 20
MAX_X_SPEED = 10
ACCEL = 0.5
JUMP_SPEED = 20
FRICTION = 1
GRAVITY = 1

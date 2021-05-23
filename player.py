import pygame as pg
from constants import *

class Player(pg.sprite.Sprite):
    def __init__(self, startX, startY):
        super(Player, self).__init__()
        temp = pg.image.load("sprite.png").convert()
        temp.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pg.transform.scale(temp, (200, 200))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(startX, startY)
        self.latest = None

        self.xspeed = 0
        self.yspeed = 0

    def update(self, pressedKeys):
        self.update_speed(pressedKeys)

        self.rect.move_ip(self.xspeed, self.yspeed)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
            if not pressedKeys[K_RIGHT]:
                self.xspeed = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            if not pressedKeys[K_LEFT]:
                self.xspeed = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def update_speed(self, pressedKeys):
        if pressedKeys[K_UP] and self.isOnFloor():
            self.yspeed = -JUMP_SPEED
        else:
            self.yspeed += GRAVITY

        if pressedKeys[K_LEFT] and self.rect.left >= 0:
            self.xspeed -= ACCEL
        elif pressedKeys[K_RIGHT] and self.rect.right <= SCREEN_WIDTH:
            self.xspeed += ACCEL
        else:
            if self.xspeed > 0:
                self.xspeed -= FRICTION
            elif self.xspeed < 0:
                self.xspeed += FRICTION

        if self.yspeed >= MAX_Y_SPEED:
            self.yspeed = MAX_Y_SPEED
        elif self.yspeed <= -MAX_Y_SPEED:
            self.yspeed = -MAX_Y_SPEED
        if self.xspeed >= MAX_X_SPEED:
            self.xspeed = MAX_X_SPEED
        elif self.xspeed <= -MAX_X_SPEED:
            self.xspeed = -MAX_X_SPEED

    def isOnFloor(self):
        return self.rect.bottom >= SCREEN_HEIGHT


def testPlayer():
    # Initialize pg
    pg.init()

    # Get clock object
    clock = pg.time.Clock()

    # Create the screen object
    # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(WHITE)
    player = Player(100, 100)

    # Fonts
    FONT = freetype.SysFont("Mono", 24)

    # Variable to keep the main loop running
    running = True

    # Main loop
    while running:
        for event in pg.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

        # Get all the keys currently pressed
        pressed_keys = pg.key.get_pressed()

        # Update the player sprite based on user keypresses
        player.update(pressed_keys)

        # Fill the screen with white
        screen.fill(WHITE)

        # Draw the player on the screen
        screen.blit(player.surf, player.rect)

        # Write player speed
        FONT.render_to(screen, (40, 40), f"{player.xspeed, player.yspeed}", BLACK)

        # Update the display
        pg.display.flip()

        # Limit to 40FPS
        clock.tick(40)

if __name__ == "__main__":
    testPlayer()
    

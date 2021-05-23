import pygame as pg
from constants import *

class Player(pg.sprite.Sprite):
    def __init__(self, startX, startY):
        super(Player, self).__init__()
        temp = pg.image.load(SPRITE_1).convert()
        temp.set_colorkey(BLACK, RLEACCEL)
        self.surf = pg.transform.scale(temp, (200, 200))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(startX, startY)
        self.dir = "R"
        self.latest = None

        self.xspeed = 0
        self.yspeed = 0

    def update(self, pressedKeys):
        self.update_speed(pressedKeys)
        self.update_orientation(pressedKeys)

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

    def update_orientation(self, pressedKeys):
        if pressedKeys[K_LEFT] and self.dir == "R":
            self.dir = "L"
            self.surf = pg.transform.flip(self.surf, True, False)
        elif pressedKeys[K_RIGHT] and self.dir == "L":
            self.dir = "R"
            self.surf = pg.transform.flip(self.surf, True, False)


    def isOnFloor(self):
        return self.rect.bottom >= SCREEN_HEIGHT

if __name__ == "__main__":
    print("Wrong file run!")
    

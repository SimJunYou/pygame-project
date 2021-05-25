import pygame as pg
from constants import *

class Player(pg.sprite.Sprite):
    def __init__(self, startX, startY, mvt, img, size, speeds):
        super(Player, self).__init__()

        temp = pg.image.load(img).convert_alpha()
        temp.set_colorkey(BLACK, RLEACCEL)
        self.surf = pg.transform.scale(temp, size)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(startX, startY)

        self.dir = "R"
        self.xspeed = 0
        self.yspeed = 0
        self.speeds = speeds
        self.canJump = False
        self.inTile = False

        self.isDamaged = False
        self.health = 100
        self.hasAltVer = False
        self.inAltVer = False

        self.L = mvt["L"]
        self.R = mvt["R"]
        self.U = mvt["U"]
        self.D = mvt["D"]

    def add_alt_surf(self, img, size):
        temp = pg.image.load(img).convert()
        self.alt_surf = pg.transform.scale(temp, size)
        self.hasAltVer = True

    def update(self, pressedKeys):
        self.update_movement(pressedKeys)
        self.update_orientation(pressedKeys)
        # Collision is handled outside the update method
        self.change_surf()

        self.rect.move_ip(self.xspeed, self.yspeed)

    def change_surf(self):
        if self.hasAltVer and not self.inAltVer and self.health <= 50:
            self.surf.set_alpha(None)
            self.surf, self.alt_surf = self.alt_surf, self.surf
            if self.isDamaged:
                self.surf.set_alpha(DMG_ALPHA)
            self.inAltVer = True
            
            # Keep position
            center = self.rect.center
            self.rect = self.surf.get_rect()
            self.rect.center = center

        elif self.hasAltVer and self.inAltVer and self.health > 50:
            self.surf.set_alpha(None)
            self.surf, self.alt_surf = self.alt_surf, self.surf
            if self.isDamaged:
                self.surf.set_alpha(DMG_ALPHA)
            self.inAltVer = False

            # Keep position
            center = self.rect.center
            self.rect = self.surf.get_rect()
            self.rect.center = center

    # For update of position from player movement
    def update_movement(self, pressedKeys):
        if pressedKeys[self.U] and self.canJump:
            self.yspeed = -self.speeds["jump"]
            self.canJump = False
        elif self.rect.bottom < SCREEN_HEIGHT:
            self.yspeed += GRAVITY
        else:
            self.yspeed = 0
            self.rect.bottom = SCREEN_HEIGHT
            self.canJump = True

        if pressedKeys[self.L] and self.rect.left >= 0:
            self.xspeed -= self.speeds["accel"]
        elif pressedKeys[self.R] and self.rect.right <= SCREEN_WIDTH:
            self.xspeed += self.speeds["accel"]
        else:
            if self.xspeed > 0:
                self.xspeed -= FRICTION
            elif self.xspeed < 0:
                self.xspeed += FRICTION

        if self.yspeed >= self.speeds["max_y"]:
            self.yspeed = self.speeds["max_y"]
        elif self.yspeed <= -self.speeds["max_y"]:
            self.yspeed = -self.speeds["max_y"]
        if self.xspeed >= self.speeds["max_x"]:
            self.xspeed = self.speeds["max_x"]
        elif self.xspeed <= -self.speeds["max_x"]:
            self.xspeed = -self.speeds["max_x"]

    # Flip the player sprite depending on direction
    def update_orientation(self, pressedKeys):
        flip = False
        if pressedKeys[self.L] and self.dir == "R":
            self.dir = "L"
            flip = True
        elif pressedKeys[self.R] and self.dir == "L":
            self.dir = "R"
            flip = True

        if flip:
            if self.isDamaged:
                self.surf.set_alpha(None)
            self.surf = pg.transform.flip(self.surf, True, False)
            if self.isDamaged:
                self.surf.set_alpha(DMG_ALPHA)

    # For collisions with platforms only
    def update_collision(self, tile, pressedKeys):
        # Find previous location
        top = self.rect.top - self.yspeed
        bottom = self.rect.bottom - self.yspeed
        left = self.rect.left - self.xspeed
        right = self.rect.right - self.xspeed

        # On platform or on floor
        if bottom <= tile.rect.top and not pressedKeys[self.D]:
            self.rect.bottom = tile.rect.top
            self.canJump = True # Only can jump if on a platform
            self.yspeed = 0
        '''
        elif left >= tile.rect.right and tile.isRight():
            self.rect.left = tile.rect.right
            if not pressedKeys[self.R]:
                self.xspeed = 0

        elif right <= tile.rect.left and tile.isLeft():
            self.rect.right = tile.rect.left
            if not pressedKeys[self.L]:
                self.xspeed = 0
        '''

    def set_damaged(self):
        if not self.isDamaged:
            self.health -= 20
            self.surf.set_alpha(DMG_ALPHA)
            self.isDamaged = True

    def clear_damaged(self):
        if self.isDamaged:
            self.surf.set_alpha(None)
            self.isDamaged = False

    def heal(self):
        if self.health < 100:
            self.health += 1

    def is_defeated(self):
        return self.health <= 0


if __name__ == "__main__":
    print("Wrong file run!")
    

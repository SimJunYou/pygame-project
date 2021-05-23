import pygame as pg
from constants import *

class Platform(pg.sprite.Sprite):
    def __init__(self, pos, size):
        super(Platform, self).__init__()
        self.surf = pg.Surface(size)
        self.surf.fill(BLACK)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos)



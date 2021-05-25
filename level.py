import pygame as pg
from constants import *
'''
class Platform(pg.sprite.Sprite):
    def __init__(self, pos, size):
        super(Platform, self).__init__()
        self.surf = pg.Surface(size)
        self.surf.fill(BLACK)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos)
'''

class Tile(pg.sprite.Sprite):
    def __init__(self, pos, img, tileType):
        super(Tile, self).__init__()
        self.surf = pg.transform.scale(img, (32, 32))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(pos)
        self.type = tileType

    def isRight(self):
        return self.type == ">"

    def isLeft(self):
        return self.type == "<"


class Level():
    def __init__(self, layout):
        self.tiles = self.generate(layout)

    def generate(self, layout):
        left = pg.image.load(LEFT_T).convert_alpha()
        center = pg.image.load(CENTER_T).convert_alpha()
        right = pg.image.load(RIGHT_T).convert_alpha()
        for img in (left, center, right):
            img.set_colorkey(BLACK, RLEACCEL)

        tile_grp = pg.sprite.Group()

        # Layout is a 32x32 grid
        # Each grid cell is a 32x32 sized sprite
        for y, row in enumerate(layout):
            for x, cell in enumerate(row):
                if cell == ".":
                    continue
                elif cell == "<":
                    tile = Tile((x*32,y*32), left, cell)
                elif cell == "=":
                    tile = Tile((x*32,y*32), center, cell)
                elif cell == ">":
                    tile = Tile((x*32,y*32), right, cell)
                tile_grp.add(tile)

        return tile_grp

    def draw_tiles_onto_bg(self, bg):
        for tile in self.tiles:
            bg.blit(tile.surf, tile.rect)

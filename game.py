import pygame as pg
from player import Player
from level import Level
from constants import *

# These only need to be initialized once throughout
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def init():
    global milk, mocha, player_grp, background, level

    # Clear the screen
    screen.fill(WHITE)
    background = pg.image.load(BACKGROUND).convert()

    # Remake the game objects
    player_grp = pg.sprite.Group()
    platform_grp = pg.sprite.Group()

    milk = Player(*P1_START, P1_MOVE, P1_SPRITE, P1_SIZE, P1_SPEED)
    mocha = Player(*P2_START, P2_MOVE, P2_SPRITE, P2_SIZE, P2_SPEED)
    player_grp.add(milk)
    player_grp.add(mocha)

    milk.add_alt_surf(P1_ALT_SPRITE, P1_ALT_SIZE)

    level = Level(LEVEL_1)
    level.draw_tiles_onto_bg(background)

    # Add events
    pg.time.set_timer(HEAL, 1000)

def main():
    # Variable to keep the main loop running
    running = True

    # To slow down health increase
    ticker = 0

    # Main loop
    while running:
        for event in pg.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False # Quit
                elif event.key == K_BACKSPACE:
                    init() # Reset
                    continue
            elif event.type == QUIT:
                running = False
            elif event.type == REMOVE_INV:
                milk.clear_damaged()
            elif event.type == HEAL:
                milk.heal()

        pressed_keys = pg.key.get_pressed()     
        for each_player in player_grp:
            each_player.update(pressed_keys)
            hit_list = pg.sprite.spritecollide(each_player, level.tiles, False)
            for each_tile in hit_list:
                each_player.update_collision(each_tile, pressed_keys)

        if not milk.isDamaged and pg.sprite.collide_circle(milk, mocha):
            milk.set_damaged()
            pg.time.set_timer(REMOVE_INV, 4000, True)
            if milk.is_defeated():
                running = False

        # Refresh and draw
        screen.blit(background, (0,0))
        for entity in player_grp:
            screen.blit(entity.surf, entity.rect)
        FONT.render_to(screen, (40, 40),\
            f"Milk's diet: {milk.health}%", BLACK)

        # Update the display and limit FPS
        pg.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    init()
    main()

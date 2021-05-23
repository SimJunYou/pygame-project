# Import the pygame module
import pygame as pg
from player import Player
from constants import *

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)
player = Player(100, 100)

def main():
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

        pressed_keys = pg.key.get_pressed()
        player.update(pressed_keys)

        # Refresh and draw
        screen.fill(WHITE)
        screen.blit(player.surf, player.rect)
        FONT.render_to(screen, (40, 40),\
            f"{player.xspeed, player.yspeed}", BLACK)

        # Update the display and limit FPS
        pg.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

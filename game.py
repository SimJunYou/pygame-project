# Import the pygame module
import pygame as pg
import player
import constants

# Initialize pg
pg.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

screen.fill(WHITE)
box = pg.Surface((50, 50))
screen.blit(box, (100, 100))
rect = box.get_rect()


def main():
    # Variable to keep the main loop running
    running = True

    # Main loop
    while running:
        pg.display.flip()
        for event in pg.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_UP:
                    box.fill(BLUE)
                    screen.blit(box, (100, 100))
                elif event.key == K_DOWN:
                    box.fill(BLACK)
                    screen.blit(box, (100, 100))
                elif event.key == K_LEFT:
                    box.fill(RED)
                    screen.blit(box, (100, 100))
                elif event.key == K_RIGHT:
                    box.fill(GREEN)
                    screen.blit(box, (100, 100))
            elif event.type == QUIT:
                running = False

if __name__ == "__main__":
    main()

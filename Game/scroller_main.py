import pygame
from gamebanner import GameBanner
from shapetransformation import Point
# Global constants
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)

 
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
def main():
    """ Main Program """
    pygame.display.set_caption("Scroll Game")
    pygame.init()
 
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    
    # set the background of my game starting screen
    screen.fill(PURPLE)
    screen_midpoint = Point(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    banner = GameBanner(screen_midpoint)
    banner.draw(screen, "SCROLL GAME", RED, WHITE)
    
    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True 
        clock.tick(60)
        pygame.display.flip()
    
    pygame.quit()
 
if __name__ == "__main__":
    main()
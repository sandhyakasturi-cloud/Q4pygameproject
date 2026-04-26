import pygame
from gamebanner import GameBanner
from startbutton import StartButton
from shapetransformation import Point
from gamesprite import GameSprite
# Global constants
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
LIGHTGRAY = (221, 221, 221)

 
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
    start = StartButton(screen_midpoint)
    start.draw(screen, "Start Game", LIGHTGRAY, BLACK )

    #create player sprite
    player = GameSprite()

    clock = pygame.time.Clock()

    done = False
    while not done:
        mouse_x = mouse_y = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True 
            elif event.type == pygame.MOUSEBUTTONUP:
                 pos = pygame.mouse.get_pos()
                 mouse_x = pos[0]
                 mouse_y = pos[1]
        
        if mouse_x != None and mouse_y != None:
            if  start.isClicked(mouse_x, mouse_y):
                background_image = pygame.image.load("Game/bluesky.jpeg").convert()
                screen.blit(background_image,[0,0])
                player.draw(screen, screen_midpoint.x-player.width/2, screen_midpoint.y+200)
                start.visible = False
        clock.tick(60)
        pygame.display.flip()
    
    pygame.quit()
 
if __name__ == "__main__":
    main()
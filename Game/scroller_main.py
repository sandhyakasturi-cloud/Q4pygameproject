import pygame
import sys
from gamebanner import GameBanner
from startbutton import StartButton
from shapetransformation import Point
from player import Player
from level import Level
from gamesprite import GameSprite

# --- Constants ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)
LIGHTGRAY = (221, 221, 221)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():
    """ Main Program """
    pygame.init()
    pygame.display.set_caption("Scroll Game")
    
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    # Menu setup
    screen_midpoint = Point(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    banner = GameBanner(screen_midpoint)
    start = StartButton(screen_midpoint)

    # Initialize Player & Level
    player = Player("Game/monstersprite.png", 69, 69)
    player.rect.x, player.rect.y = 150, 100 
    level = Level()


    try:
        background_image = pygame.image.load("Game/bluesky.jpeg").convert()
        background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    except:
        background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        background_image.fill((135, 206, 235))

    done = False
    while not done:
        mouse_x = mouse_y = None
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True 
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos, pos
            
            # This captures the UP tap even if RIGHT is currently held
            if not start.visible:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player.jump()

        if not start.visible:
            # Check horizontal keys held down
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.go_left()
            elif keys[pygame.K_RIGHT]:
                player.go_right()
            else:
                player.stop()

            # Physics Update (Gravity and Movement)
            player.update(level)

            # Camera Scrolling thresholds
            if player.rect.right >= 500:
                diff = player.rect.right - 500
                player.rect.right = 500
                level.shift_world(-diff)
            elif player.rect.left <= 150:
                diff = 150 - player.rect.left
                player.rect.left = 150
                level.shift_world(diff)

            # game images in order of display
            screen.blit(background_image, (0,0))
            level.draw(screen)
            screen.blit(player.image, player.rect)

            # Death Check: Reset if falling off
            if player.rect.top > SCREEN_HEIGHT:
                start.visible = True
                level = Level() # Re-generate level
                player = Player("Game/monstersprite.png", 69, 69) # Reset player
                player.rect.x, player.rect.y = 150, 100
        
        # draw the menu again so the player can restart the game
        else:
            screen.fill(PURPLE)
            banner.draw(screen, "SCROLL GAME", RED, WHITE)
            start.draw(screen, "Start Game", LIGHTGRAY, BLACK)

            if mouse_x is not None and mouse_y is not None:
                if start.isClicked(mouse_x, mouse_y):
                    start.visible = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Rectangle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height,color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.change_x = -5
    def  move(self):
        self.rect.topleft = (self.rect.left,self.rect.top+self.change_x)

class Circle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height,radius, color):
        super().__init__()
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.circle(self.image,color, (width/2,height/2),radius)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y-radius/2)
        self.change_y = 5
    def  move(self):
        self.rect.topleft = (self.rect.left,self.rect.top+self.change_y)


# Create Sprites
rect = Rectangle(0, 450, 50, 50,RED)
circle = Circle(0, 160, 60, 60,30,GREEN)

all_sprites = pygame.sprite.Group()
all_sprites.add(rect)
all_sprites.add(circle)

rect_group = pygame.sprite.Group()
rect_group.add(rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    circle.move();
    all_sprites.update();

    hits = pygame.sprite.spritecollide(circle, rect_group, False)
    bFlip = False;
    if hits:
        font = pygame.font.SysFont("Arial", 36)
        text_surface = font.render("Bounced", True,BLUE)
        text_rect = text_surface.get_rect()
        screen.blit(text_surface, text_rect,text_rect)
        circle.change_y = -circle.change_y
        bFlip = True
    elif circle.change_y < 0:
        #circle.change_y -=0.1
        if circle.rect.y <= 160:
            circle.change_y = -circle.change_y
    elif circle.change_y >= 0:
        if circle.rect.y <= 160:
            #circle.change_y +=0.1
            pass
        elif circle.rect.y >= 450:
            circle.change_y = -circle.change_y

    
    # Draw
    all_sprites.draw(screen)
 
    if bFlip:
        pygame.display.flip()
        pygame.time.wait(500)
    
    pygame.display.flip()
    screen.fill(WHITE)
    clock.tick(60)

pygame.quit()
sys.exit()

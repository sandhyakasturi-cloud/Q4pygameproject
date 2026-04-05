"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import math
import random


def movejump(x):
    speed = 1000
    center = 60
    height = 100
    y = 1/speed*math.pow(x-center,2)+height
    return y

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()
 
class Shape:
    def __init__(self):        
        self.x = 50
        self.y = 50
        self.change_x = 5
        self.change_y = 5
    def move(self):
        self.x += self.change_x;
        self.y = movejump(self.x) 
 
        if self.x > 649 or self.x < 0:
            self.change_x = self.change_x * -1
        if self.y > 449 or self.y < 0:
            self.change_x = self.change_x * -1
    def draw (self, screen):
        pass
class Rect(Shape):
    def draw (self, screen):
        pygame.draw.rect(screen, WHITE, [self.x, self.y, 50, 50])
class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.y = 180
        self.change_x = 3

    def draw (self, screen):
        pygame.draw.circle(screen, WHITE, [self.x, self.y], 30)
circle = Circle()
rect = Rect()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    screen.fill(BLACK)

    rect.move()
    rect.draw(screen)
    circle.move()
    circle.draw(screen)
    pygame.display.flip()
    
    clock.tick(60)
 
pygame.quit()
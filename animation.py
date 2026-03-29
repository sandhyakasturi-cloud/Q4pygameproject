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
 

rect_x = 50
rect_y = 50
rect_change_x = 5
rect_change_y = 5
while not done:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
   
    screen.fill(BLACK)
 
   
 
    rect_x += rect_change_x;
    rect_y = movejump(rect_x) 
 

    if rect_x > 649 or rect_x < 0:
        rect_change_x = rect_change_x * -1
    if rect_y > 449 or rect_y < 0:
        rect_change_x = rect_change_x * -1
   

    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])

    pygame.display.flip()
    
    clock.tick(60)
 
pygame.quit()
import pygame
from gamesprite import GameSprite
import random

class Level:
    def __init__(self):
        self.blocks = []

        spriteSheet = pygame.image.load("Game/blocksspritesheet.png").convert_alpha()
        
        # make block sprites
        level = []

        start_x = 0
        start_y = 0
        end_x   = 729
        end_y   = 249
        s_w = 80
        s_h = 80
        x_new = start_x
        y_new = start_y
        for row in range(100):
            for col in range(100):
                x = start_x + s_w * ((col+1) % 9) 
                y = start_y + s_h * ((row+1) % 3)
                block = GameSprite(spriteSheet,s_w,s_h,(x,y,s_w,s_h))
                self.blocks.append(block)
                x_new = x_new + x
                y_new = y_new
                level.append([x_new*0.3,500])

 
        # Go through the array above and add platforms
        self.platforms_list = pygame.sprite.Group()
        for platform in level:
            block = self.blocks[random.randint(0,len(self.blocks)-1)]
            block.rect.x = platform[0]
            block.rect.y = platform[1]
            #plant.player = self.player
            self.platforms_list.add(block)

        # How far this world has been scrolled left/right
        self.world_shift = 0

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platforms_list.update()
        #self.enemy_list.update()
 
    def draw(self, screen):
        # Draw everything on this level.
        self.platforms_list.draw(screen)
        #self.enemy_list.draw(screen)
 
    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll
        everything: """
 
        # Keep track of the shift amount
        self.world_shift += shift_x
 
        # Go through all the sprite lists and shift
        for floorItems in self.platforms_list:
            floorItems.rect.x += shift_x
 
        #for enemy in self.enemy_list:
            #enemy.rect.x += shift_x

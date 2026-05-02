import pygame
import random
from gamesprite import GameSprite 
from coin import Coin

class Level:
    def __init__(self):
        self.platforms_list = pygame.sprite.Group()
        self.coin_list = pygame.sprite.Group()
        self.world_shift = 0

        # Load the spritesheet
        try:
            spriteSheet = pygame.image.load("Game/blocksspritesheet.png").convert_alpha()
        except:
            spriteSheet = pygame.Surface((800, 800))
            spriteSheet.fill((255, 0, 255))

        s_w, s_h = 80, 80
        block_templates = []
        for row in range(3):
            for col in range(9):
                block_templates.append((col * s_w, row * s_h, s_w, s_h))

        # Fixed position so the player always has a place to land
        style = block_templates[0] 
        for i in range(4): # Slightly wider start
            block = GameSprite(spriteSheet, s_w, s_h, style)
            block.rect.x = 80 + (i * s_w) 
            block.rect.y = 450 
            self.platforms_list.add(block)

        current_x = 450 
        last_y = 450 # Track height to prevent impossible climbs

        for _ in range(50):
            p_width = random.randint(2, 4)
            
            # Limit vertical spacing of the plafroms to allow jumping between platforms
            p_y = random.randint(max(200, last_y - 100), min(480, last_y + 100))
            
            style = random.choice(block_templates)

            for i in range(p_width):
                block = GameSprite(spriteSheet, s_w, s_h, style)
                block.rect.x = current_x + (i * s_w)
                block.rect.y = p_y
                self.platforms_list.add(block)
                coinpercent = random.randint(1, 100)
                if coinpercent <= 40:
                    coin = Coin("Game/coin.jpg",56, 72)
                    coin.rect.x = block.rect.x
                    coin.rect.y = block.rect.y - block.height - block.height*random.randint(0,2)
                    self.coin_list.add(coin)

            # We set the space between the platforms so that the player can make the jump.
            gap = random.randint(120, 240)
            current_x += (p_width * s_w) + gap
            last_y = p_y # Update height for the next platform

        # create the final platform
        style = block_templates[1] # Choose a specific style for the finish
        final_ground_width = 10 # Make it wide so it's hard to miss
        
        ground_y = 520
        final_block_x = current_x
        for i in range(final_ground_width):
            block = GameSprite(spriteSheet, s_w, s_h, style)
            block.rect.x = current_x + (i * s_w)
            final_block_x = block.rect.x
            block.rect.y = ground_y # Place it low on the screen
            self.platforms_list.add(block)
            
        # Store the finish line X coordinate so we can check for a win later
        self.finish_line_x = current_x
        self.limit = current_x

        self.treasure_chest = GameSprite("Game/treasurechest.png", 150,103)
        self.treasure_chest.rect.x = final_block_x - 150
        self.treasure_chest.rect.y = ground_y - 105
        self.platforms_list.add(self.treasure_chest)

    def draw(self, screen):
        self.platforms_list.draw(screen)
        for sprite in self.coin_list:
            sprite.switch()
        self.coin_list.draw(screen)

    def shift_world(self, shift_x):
        self.world_shift += shift_x
        for sprite in self.platforms_list:
            sprite.rect.x += shift_x
        for sprite in self.coin_list:
            sprite.rect.x += shift_x
        

    
import pygame
from gamesprite import GameSprite

class Player(GameSprite):
    def __init__(self, file, width, height, sheetLoc=None):
        super().__init__(file, width, height, sheetLoc)
        self.change_x = 0
        self.change_y = 0
        self.gravity = 0.5
        self.jump_speed = -12
        self.speed = 7

    def update(self, level):
        # 1. Apply Gravity
        self.change_y += self.gravity
        
        # 2. Move Vertically
        self.rect.y += self.change_y

        # 3. Vertical Collision
        hit_list = pygame.sprite.spritecollide(self, level.platforms_list, False)
        for block in hit_list:
            if self.change_y > 0: # Falling down
                self.rect.bottom = block.rect.top
                self.change_y = 0 # This allows the jump() check to pass
            elif self.change_y < 0: # Hitting head
                self.rect.top = block.rect.bottom
                self.change_y = 0

        # 4. Move Horizontally
        self.rect.x += self.change_x

    def jump(self):
        # Instead of change_y == 0, check if it's very small 
        # OR check a dedicated "on_ground" boolean.
        if abs(self.change_y) <= 0.5: 
            self.change_y = self.jump_speed


    def go_left(self):
        self.change_x = -self.speed
    def go_right(self):
        self.change_x = self.speed
    def stop(self):
        self.change_x = 0

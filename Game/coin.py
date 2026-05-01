import pygame
from gamesprite import GameSprite

class Coin(GameSprite):
    coin1 = None
    coin2 = None

    def __init__(self, file, width, height):
        super().__init__(file, width, height, None)
        flipAfter = None
        Coin.coin1 = self.image
        self.flipAfter = 60

        sprite = pygame.image.load("Game/coin2.jpg").convert_alpha() 

        first_color = sprite.get_at((0, 0))
        # 2. Set the colorkey
        sprite.set_colorkey(first_color)

        # 3. Create target surface with transparent alpha
        Coin.coin2 = pygame.Surface([self.width,self.height], pygame.SRCALPHA)
        Coin.coin2.blit(sprite, [0,0])
    
        self.coinList = [Coin.coin1,Coin.coin2]
        self.coinIndex = 0

    def switch(self):
        self.flipAfter = self.flipAfter - 1
        if self.flipAfter <= 0:
            self.coinIndex = ~self.coinIndex
            self.image = self.coinList[self.coinIndex]
        if self.flipAfter <= 0:
            self.flipAfter = 60

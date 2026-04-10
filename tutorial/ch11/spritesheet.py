import pygame

WHITE = (255, 255, 255)

class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """
 
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()
 
 
    def get_image(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(WHITE)
        return image
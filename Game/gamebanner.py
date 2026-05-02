import pygame
from shapetransformation import Point,ShapeTransformations

class GameBanner(list):
    def __init__(self,screen_midpoint:Point):
        super().__init__()
        self.width = 700
        self.height = 200
        banner_v1 = Point(screen_midpoint.x-self.width//2,screen_midpoint.y - self.height//2)
        banner_image = [banner_v1.x, banner_v1.y,self.width,self.height]
        self.extend(banner_image)

    def draw(self, screen, text, bannerColor, textColor):
        my_font = pygame.font.SysFont('Impact', 80,True)
        text_surface = my_font.render(text, True, textColor)
        pygame.draw.ellipse(screen,bannerColor,self)
        textX = ShapeTransformations.midPoint(self[0],self[0]+self[2])
        textY = ShapeTransformations.midPoint(self[1],self[1]+self[3])
        text_width = my_font.size(text)[0] // 2
        text_height = my_font.size(text)[1] // 2
        textPoint = Point(textX-text_width,textY-text_height)
        screen.blit(text_surface, textPoint)
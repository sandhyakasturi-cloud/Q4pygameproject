import pygame
from shapetransformation import Point,ShapeTransformations

class StartButton(list):
    def __init__(self,screen_midpoint:Point):
        super().__init__()
        self.distance = 100
        self.width = 200
        self.height = 50
        self.visible = False
        button_v1 = Point(screen_midpoint.x-self.width//2,screen_midpoint.y + self.distance + self.height//2)
        button_image = [button_v1.x, button_v1.y,self.width,self.height]
        self.extend(button_image)

    def draw(self, screen, text, buttonColor, textColor):
        my_font = pygame.font.SysFont('Arial', 20,True)
        text_surface = my_font.render(text, True, textColor)
        pygame.draw.rect(screen,buttonColor,self)
        textX = ShapeTransformations.midPoint(self[0],self[0]+self[2])
        textY = ShapeTransformations.midPoint(self[1],self[1]+self[3])
        text_width = my_font.size(text)[0] // 2
        text_height = my_font.size(text)[1] // 2
        textPoint = Point(textX-text_width,textY-text_height)
        screen.blit(text_surface, textPoint)
        self.visible = True

    def isClicked(self, x,y):
        if not self.visible or x is None or y is None:
            return False

        bx = self[0] 
        by = self[1] 
        width = bx + self.width
        height = by + self.height
        if x >= bx and x <= width and y >= by and y <= height:
            return True
        return False
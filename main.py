import pygame
import sys

class Square(pygame.sprite.Sprite):

    def __init__(self, x, y, h, w, image):
        '''
          Initalizes Square attributes
          args:
             x:(int) a number, x coordinate on screen
             y:(int) a number, y coordinate on screen
             image: (image) an image
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale((pygame.image.load(image).convert_alpha()), (h,w))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
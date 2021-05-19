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


class Controller:
    def __init__(self, width=1700, height=920):
        '''
        set up the window
        args: 
              width: (int) the width of the window, defaulted to 1700
              height: (int) the height of the window, defaulted to 920
        '''

        #screen
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()


    def mainLoop(self):
        '''
        start the game
        '''
        while True:
            self.gameLoop()

    def gameLoop(self):
        pygame.key.set_repeat(1,10)

        while True:

            #exit button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()




            #redraw the entire screen

            self.background = pygame.transform.scale((pygame.image.load("src/red.png")), (1700,920))
            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()




def main():
    main_window = Controller()
    main_window.mainLoop()
main()
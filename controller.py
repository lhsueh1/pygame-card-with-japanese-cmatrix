import pygame
import sys
from src import Square



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

        #square
        self.square = pygame.sprite.Group()

        for row in range(43):
            for line in range(23):
                x = 0 + 40 * row
                y = 0 + 40 * line
                self.square.add(Square.Square(x, y, 40, 40, "src/aqua.png"))

        #line
        self.line = pygame.sprite.Group()
        for row in range(1, 43):
            x = 0 + 40 * row
            y = 0
            self.line.add(Square.Square(x, y, 5, 920, "src/line_v.png"))
        for line in range(1, 23):
            x = 0
            y = 0 + 40 * line
            self.line.add(Square.Square(x, y, 1700, 5, "src/line_h.png"))

        #button
        self.bs = pygame.sprite.Group()
        bx = 42 * 40
        by = 0
        self.bs.add(Square.Square(bx, by, 40, 40, "src/pink.png"))

        #killed
        self.deadS = pygame.sprite.Group()

    def mainLoop(self):
        '''
        start the game
        '''
        # while True:
        #     self.gameLoop()
        self.cmatrixLoop()


    def gameLoop(self):
        pygame.key.set_repeat(1,10)

        while True:

            #exit button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.components = pygame.sprite.Group((self.square,) + (self.line,))

            #click square disappear
            for i in self.square:
                if pygame.mouse.get_pressed()[0] and i.rect.collidepoint(pygame.mouse.get_pos()):
                    self.square.remove(i)
                    self.deadS.add(i)

                for j in self.bs:
                    if pygame.mouse.get_pressed()[0] and j.rect.collidepoint(pygame.mouse.get_pos()):
                        self.square.add(self.deadS)
                        self.deadS.empty()


            #redraw the entire screen

            self.background = pygame.transform.scale((pygame.image.load("src/red.png")), (1700,920))
            self.screen.blit(self.background, (0, 0))
            self.components.draw(self.screen)
            self.bs.draw(self.screen)
            pygame.display.flip()


    def cmatrixLoop(self):
        pygame.key.set_repeat(1,10)

        while True:

            #exit button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.components = pygame.sprite.Group((self.square,) + (self.line,))

            word = ['流れてく 時の中ででも 気だるさが ほらグルグル廻って']


            for i in range(27):
                self.paint(word[i], i * 20)


            #redraw the entire screen

            self.background = pygame.transform.scale((pygame.image.load("src/red.png")), (1700,920))
            self.screen.blit(self.background, (0, 0))
            self.components.draw(self.screen)
            self.bs.draw(self.screen)
            pygame.display.flip()



    def paint(self, text, y):
        # 4.1 初始化字型
        pygame.font.init()

        # 4.2 設定字型樣式 （ps: wryh.ttf是字型庫的檔案，和專案檔案放到一個資料夾中）
        font = pygame.font.Font("src/jf-openhuninn-1.1.ttf", 12)
        # 4.3 迴圈迭代
        for i in range(0,10):
            # 4.4 設定繪製內容
            fontRead = font.render(text,True,(0,0,0))
            # 4.5 設定繪製內容的座標
            screen.blit(fontRead,(0,y))  # 將字串繪製到該視窗上



def main():
    main_window = Controller()
    main_window.mainLoop()
main()

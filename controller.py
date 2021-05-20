import pygame
import sys
import time
from src import Square
import random


class Controller:
    def __init__(self, width=2560, height=1440):
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
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
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

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
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

            w, h = pygame.display.get_surface().get_size()

            self.background = pygame.transform.scale((pygame.image.load("src/red.png")), (w,h))
            self.screen.blit(self.background, (0, 0))
            self.components.draw(self.screen)
            self.bs.draw(self.screen)
            pygame.display.flip()


    def cmatrixLoop(self):
        pygame.key.set_repeat(1,10)

        f = open("src/bad_apple.txt", encoding="utf-8")
        texts = f.readlines()

        for k in range(len(texts)):
            for jk in range(58 - len(texts[k])):
                space = ['按', '空', '白', '鍵']
                #texts[k] += " "
                texts[k] += space[random.randint(0, len(space)-1)]

        random.shuffle(texts)

        random_list = []
        for k in range(58):
            n = random.randint(1,100)
            random_list.append(n)

        i = 0

        w, h = pygame.display.get_surface().get_size()

        while True:

            #exit button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        sys.exit()


            self.components = pygame.sprite.Group((self.square,) + (self.line,))




            #redraw the entire screen
            self.background = pygame.transform.scale((pygame.image.load("src/kinda_black.png")), (w,h))

            # after making the background fill in black, set width to fit size of words
            h = h - (h % 25)


            if i == 0:
                self.screen.blit(self.background, (0, 0))


            #self.components.draw(self.screen)
            #self.bs.draw(self.screen)
            #pygame.display.flip()


            # word = "流れてく時の中ででも気だるさがほらグルグル廻って私から離れる心も見えないわそう知らない？"
            # word_count = len(word)



            pygame.font.init()
            font = pygame.font.Font("src/jf-openhuninn-1.1.ttf", 24)

            # rows
            for j in range(w//30):
                ranged_j = j % len(texts)
                ranged_i = i % (len(texts[ranged_j]) - 1)
                if i >= (h / 25): # screen height /25 max words per column
                    self.paint_blank(j, i, random_list[ranged_j], h)
                else:
                    self.paint_word(font, texts[ranged_j][ranged_i], j, i, random_list[ranged_j],h)


            pygame.display.update()
            time.sleep(0.05)

            if i < ((h / 25) * 2 - 1):
                i += 1
            else:
                i = 0

                random.shuffle(texts)

                random_list = []
                for k in range(58):
                    n = random.randint(1,100)
                    random_list.append(n)


    # Deal with one single word
    def paint_word(self, font, word,j, i, yy,h):
        fontRead = font.render(word, True,(random.randint(180,255),random.randint(180,255),random.randint(180,255)))
        self.screen.blit(fontRead,(30 * j, (yy * 25 + 25*i) % h))

    def paint_blank(self, j, i ,yy, h):
        blank = pygame.transform.scale((pygame.image.load("src/kinda_black.png")), (30,25))
        self.screen.blit(blank,(30 * j, (yy * 25 + 25*i) % h))



def main():
    main_window = Controller()
    main_window.mainLoop()
main()

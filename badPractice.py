import pygame
import sys
import time
import random
import src


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
    def __init__(self, width=1120, height=672):
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


        #black
        self.black = pygame.sprite.Group()
        squareSize = 49
        for row in range(pygame.display.get_window_size()[0]//squareSize+2):
            for column in range((pygame.display.get_window_size()[1])//squareSize + 2):
                x = 0 + squareSize * row
                y = 0 + squareSize * column
                self.black.add(Square(x, y, squareSize, squareSize, "src/black.png"))               

        #dead black
        self.deadB = pygame.sprite.Group()

        #button
        self.buttons = pygame.sprite.Group()
        self.show = Square(pygame.display.get_window_size()[0]-squareSize, 0, squareSize, squareSize, "src/pink.png")
        self.buttons.add(self.show)

        #balloon
        self.balloon = Square(0, 0, 120, 224, "src/balloon.png")
        self.ribbon = Square(0, 0, 120, 120, "src/ribbon.png")

        #unicorn
        self.unicorns = pygame.sprite.Group()
        self.unicorn = Square(890, 460, 212, 273, "src/uni.png")
        self.unicorns.add(self.unicorn)
        # for i in range(25):
        #     x = random.randrange(-140, pygame.display.get_window_size()[0]-200)
        #     y = random.randrange(-70, pygame.display.get_window_size()[1]-300)
        #     self.unicorns.add(Square(x, y, 212, 273, "src/uni.png"))

        pygame.font.init()

        file = open("src/card.txt", encoding="utf-8")

        self.card1 = file.readline()
        self.card2 = file.readline()
        self.card3 = file.readline()
        self.card4 = file.readline()
        self.card5 = file.readline()

        self.card6 = file.readline()
        self.card7 = file.readline()
        self.card8 = file.readline()

        self.card9 = file.readline()
        self.card10 = file.readline()
        self.card11 = file.readline()

        self.card12 = file.readline()
        self.card13 = file.readline()
        self.card14 = file.readline()

        self.card15 = file.readline()
        self.card16 = file.readline()
        self.card17 = file.readline()
        self.card18 = file.readline()
        self.card19 = file.readline()
        self.card20 = file.readline()

        file.close()


        font = pygame.font.Font("src/jf-openhuninn-1.1.ttf", 20)
        self.fontRead1 = font.render(self.card1, False,(0,0,0))
        self.fontRead2 = font.render(self.card2, False,(0,0,0))
        self.fontRead3 = font.render(self.card3, False,(0,0,0))
        self.fontRead4 = font.render(self.card4, False,(0,0,0))
        self.fontRead5 = font.render(self.card5, False,(0,0,0))
        self.fontRead6 = font.render(self.card6, False,(0,0,0))
        self.fontRead7 = font.render(self.card7, False,(0,0,0))
        self.fontRead8 = font.render(self.card8, False,(0,0,0))
        self.fontRead9 = font.render(self.card9, False,(0,0,0))
        self.fontRead10 = font.render(self.card10, False,(0,0,0))
        self.fontRead11 = font.render(self.card11, False,(0,0,0))
        self.fontRead12 = font.render(self.card12, False,(0,0,0))
        self.fontRead13 = font.render(self.card13, False,(0,0,0))
        self.fontRead14 = font.render(self.card14, False,(0,0,0))
        self.fontRead15 = font.render(self.card15, False,(0,0,0))
        self.fontRead16 = font.render(self.card16, False,(0,0,0))
        self.fontRead17 = font.render(self.card17, False,(0,0,0))
        self.fontRead18 = font.render(self.card18, False,(0,0,0))
        self.fontRead19 = pygame.font.Font("src/jf-openhuninn-1.1.ttf", 30).render(self.card19, False,(0,0,0))
        self.fontRead20 = pygame.font.Font("src/jf-openhuninn-1.1.ttf", 16).render(self.card20, False,(0,0,0))

        self.state = "PAGE0"
        self.spaceCheck = False 


    def startLoop(self):

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
            while self.state == "PAGE0":
                #exit button
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()    

                    if event.type == pygame.KEYDOWN and self.spaceCheck:
                        if event.key == pygame.K_SPACE:
                            self.state = "PAGE1"
                
                if pygame.mouse.get_pressed()[0] and self.unicorn.rect.collidepoint(pygame.mouse.get_pos()):
                    self.spaceCheck = True


                # after making the background fill in black, set width to fit size of words
                #self.components = pygame.sprite.Group((self.square,) + (self.line,))

                h = h - (h % 25)

                if i == 0:
                    self.screen.blit(self.background, (0, 0))

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


                self.background = pygame.transform.scale((pygame.image.load("src/kinda_black.png")), (w,h))
                #self.screen.blit(self.background, (0, 0))
                self.unicorns.draw(self.screen)
                #pygame.display.update()

            if (self.state == "PAGE1") or (self.state == "PAGE2"):
                self.background = pygame.transform.scale((pygame.image.load("src/red.png")), pygame.display.get_window_size())
                self.screen.blit(self.background, (0, 0))
                y = 56
                a = 28
                self.background.blit(self.fontRead1,(70,y))
                y+=a+14
                self.background.blit(self.fontRead2,(70,y))
                y+=a
                self.background.blit(self.fontRead3,(70,y))
                y+=a
                self.background.blit(self.fontRead4,(70,y))
                y+=a
                self.background.blit(self.fontRead5,(70,y))
                y+=a+14
                self.background.blit(self.fontRead6,(70,y))
                y+=a
                self.background.blit(self.fontRead7,(70,y))
                y+=a
                self.background.blit(self.fontRead8,(70,y))
                y+=a+14
                self.background.blit(self.fontRead9,(70,y))
                y+=a
                self.background.blit(self.fontRead10,(70,y))
                y+=a
                self.background.blit(self.fontRead11,(70,y))
                y+=a+14
                self.background.blit(self.fontRead12,(70,y))
                y+=a
                self.background.blit(self.fontRead13,(70,y))
                y+=a
                self.background.blit(self.fontRead14,(70,y))
                y+=a+14
                self.background.blit(self.fontRead15,(70,y))
                y+=a
                self.background.blit(self.fontRead16,(70,y))
                y+=a
                self.background.blit(self.fontRead17,(70,y))
                y+=a
                self.background.blit(self.fontRead18,(70,y))
                self.background.blit(self.fontRead19, (840, y))
                self.background.blit(self.fontRead20, (945, y+30))

                if self.state == "PAGE1":
                    self.state = "PAGE1-1"
                if self.state == "PAGE2":
                    self.state = "PAGE2-1"

            while self.state == "PAGE1-1":
                #exit button
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                for i in self.black:
                    if i.rect.collidepoint(pygame.mouse.get_pos()):
                        self.black.remove(i)
                        self.deadB.add(i)

                self.show.rect.y = 0
                if pygame.mouse.get_pressed()[0] and self.show.rect.collidepoint(pygame.mouse.get_pos()):
                    #time.sleep(0.3)
                    self.state = "PAGE2"


                #redraw the entire screen
                self.screen.blit(self.background, (0, 0))
                self.buttons.draw(self.screen)
                self.black.draw(self.screen)
                pygame.display.update()
                self.black.add(self.deadB)
                self.deadB.empty()

                self.background = pygame.transform.scale((pygame.image.load("src/red.png")), pygame.display.get_window_size())
                self.background.blit(self.background, (0, 0))
                y = 56
                a = 28
                self.background.blit(self.fontRead1,(70,y))
                y+=a+14
                self.background.blit(self.fontRead2,(70,y))
                y+=a
                self.background.blit(self.fontRead3,(70,y))
                y+=a
                self.background.blit(self.fontRead4,(70,y))
                y+=a
                self.background.blit(self.fontRead5,(70,y))
                y+=a+14
                self.background.blit(self.fontRead6,(70,y))
                y+=a
                self.background.blit(self.fontRead7,(70,y))
                y+=a
                self.background.blit(self.fontRead8,(70,y))
                y+=a+14
                self.background.blit(self.fontRead9,(70,y))
                y+=a
                self.background.blit(self.fontRead10,(70,y))
                y+=a
                self.background.blit(self.fontRead11,(70,y))
                y+=a+14
                self.background.blit(self.fontRead12,(70,y))
                y+=a
                self.background.blit(self.fontRead13,(70,y))
                y+=a
                self.background.blit(self.fontRead14,(70,y))
                y+=a+14
                self.background.blit(self.fontRead15,(70,y))
                y+=a
                self.background.blit(self.fontRead16,(70,y))
                y+=a
                self.background.blit(self.fontRead17,(70,y))
                y+=a
                self.background.blit(self.fontRead18,(70,y))
                self.background.blit(self.fontRead19, (840, y))
                self.background.blit(self.fontRead20, (945, y+35))

            while self.state == "PAGE2-1":
                #exit button
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                self.show.rect.y = 70

                if pygame.mouse.get_pressed()[0] and self.show.rect.collidepoint(pygame.mouse.get_pos()):
                    #time.sleep(1)
                    self.state = "PAGE1"

                if pygame.mouse.get_pressed()[0]:
                    self.buttons.add(self.balloon)
                    self.balloon.rect.x = pygame.mouse.get_pos()[0]-56
                    self.balloon.rect.y = pygame.mouse.get_pos()[1]-112
                if pygame.mouse.get_pressed()[2]:
                    self.buttons.add(self.ribbon)
                    self.ribbon.rect.x = pygame.mouse.get_pos()[0]-56
                    self.ribbon.rect.y = pygame.mouse.get_pos()[1]-56


                #redraw the entire screen

                self.screen.blit(self.background, (0, 0))
                self.buttons.draw(self.screen)
                pygame.display.update()
                self.buttons.remove(self.balloon)
                self.buttons.remove(self.ribbon)

    def paint_word(self, font, word,j, i, yy,h):
        fontRead = font.render(word, True,(random.randint(180,255),random.randint(180,255),random.randint(180,255)))
        self.screen.blit(fontRead,(30 * j, (yy * 25 + 25*i) % h))
        self.unicorns.draw(self.screen)

    def paint_blank(self, j, i ,yy, h):
        blank = pygame.transform.scale((pygame.image.load("src/kinda_black.png")), (30,25))
        self.screen.blit(blank,(30 * j, (yy * 25 + 25*i) % h))
        self.unicorns.draw(self.screen)





def main():
    main_window = Controller()
    main_window.startLoop()
main()
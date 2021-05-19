import pygame
import sys
import time

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
    def __init__(self, width=1600, height=960):
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
        squareSize = 70
        for row in range(1700//squareSize):
            for column in range(920//squareSize + 2):
                x = 0 + squareSize * row
                y = 0 + squareSize * column
                self.black.add(Square(x, y, squareSize, squareSize, "src/black.png"))               

        #dead black
        self.deadB = pygame.sprite.Group()

        #button
        self.buttons = pygame.sprite.Group()
        self.show = Square(1600-squareSize, 0, squareSize, squareSize, "src/pink.png")
        self.buttons.add(self.show)

        #balloon
        self.balloon = Square(0, 0, 171, 320, "src/balloon.png")

        pygame.font.init()
        self.card1 = "Dear麗莎"
        self.card2 = "生日快樂(*´ω`)人(´ω`*)"
        self.card3 = "我成大第一個(或唯一?)的朋朋！我們也這樣玩了一個大一了，從上學期每個星期二的超趕午餐、星期五"
        self.card4 = "的餐廳抉擇，到這學期「不知道」「那茶朵吧」的星期二五，還有每次都變波哥的珍妮花，我們就這樣"
        self.card5 = "愉快地遠離育樂街覓食，真的有幸然後一起吃喝重新探索成大！"

        self.card6 = "也因為很意外地認識了，讓我有機會體驗很多原本以為無緣的大學生日常，像第一次上大學一樣，比你幼"
        self.card7 = "稚地各種新奇興奮，雖然明年可能沒辦法再一起吐嘈抱怨，但我們還是要保持聯絡歐，我好想知道接下來"
        self.card8 = "有幾個人成功轉走哈哈哈，而且身為一個孤僻鄙視周圍的人，可以找到一個一起玩鬧八卦的夥伴真的很開心！"

        self.card9 = "身份爆出來雖然是個小意外，但很慶幸又多了一個可以講話的人了！也感謝你不嫌棄聽我講一些奇怪的、"
        self.card10 = "資工宅的東西(˙︶˙)如果以後電腦有問題也可以問我（？（看哪這可是工具人系裡很大很大的flag歐，"
        self.card11 = "敝人意思意思嫌棄完還是會努力解惑的XD"

        self.card12 = "19歲最後一年青少年呢（嗚嗚怎麼這麼年輕´oωo`）大家都說9字尾會衰，但才沒有呢，看我們玩得多開心(？"
        self.card13 = "大學就是要這樣在很熱的太陽下玩鬧呀，然後遇到各種神奇的人類、體驗各種神奇的事情，然後盡情體驗"
        self.card14 = "跟發現，期待你之後的燦爛生活！"

        self.card15 = "最後完全沒有料到會是在這種情況下做出一個這麼具有遠距精神的卡片XD"
        self.card16 = "這次前面做了一個經典的cmatrix，因為日文不是我看得懂的，所以如果有奇怪的東西出現，記得跟我說，"
        self.card17 = "我拿去找寫的人算帳。然後這邊我堅持叫做拿手電筒照的牆壁（雖然好像有點沒fu）反正我努力了(ovo)"
        self.card18 = "希望你會喜歡，然後有「啊！這就是有個資工朋友的感覺！」XD <3"
        self.card19 = "亦絢ˊˇˋ"
        self.card20 = "5/22/2021"


        font = pygame.font.Font("src/jf-openhuninn-1.1.ttf", 22)
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
        self.fontRead19 = pygame.font.Font("src/jf-openhuninn-1.1.ttf", 35).render(self.card19, False,(0,0,0))
        self.fontRead20 = pygame.font.Font("src/jf-openhuninn-1.1.ttf", 18).render(self.card20, False,(0,0,0))


    def mainLoop(self):
        '''
        start the game
        '''
        self.gameLoop()

    def gameLoop(self):
        pygame.key.set_repeat(1,100)

        while True:
            #exit button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


            for i in self.black:
                if i.rect.collidepoint(pygame.mouse.get_pos()):
                    self.black.remove(i)
                    self.deadB.add(i)



            if pygame.mouse.get_pressed()[0] and self.show.rect.collidepoint(pygame.mouse.get_pos()):
                time.sleep(0.3)
                self.everythingLoop()


            #redraw the entire screen
            self.background = pygame.transform.scale((pygame.image.load("src/red.png")), (1600,960))
            self.screen.blit(self.background, (0, 0))
            y = 80
            a = 40
            self.screen.blit(self.fontRead1,(100,y))
            y+=a+20
            self.screen.blit(self.fontRead2,(100,y))
            y+=a
            self.screen.blit(self.fontRead3,(100,y))
            y+=a
            self.screen.blit(self.fontRead4,(100,y))
            y+=a
            self.screen.blit(self.fontRead5,(100,y))
            y+=a+20
            self.screen.blit(self.fontRead6,(100,y))
            y+=a
            self.screen.blit(self.fontRead7,(100,y))
            y+=a
            self.screen.blit(self.fontRead8,(100,y))
            y+=a+20
            self.screen.blit(self.fontRead9,(100,y))
            y+=a
            self.screen.blit(self.fontRead10,(100,y))
            y+=a
            self.screen.blit(self.fontRead11,(100,y))
            y+=a+20
            self.screen.blit(self.fontRead12,(100,y))
            y+=a
            self.screen.blit(self.fontRead13,(100,y))
            y+=a
            self.screen.blit(self.fontRead14,(100,y))
            y+=a+20
            self.screen.blit(self.fontRead15,(100,y))
            y+=a
            self.screen.blit(self.fontRead16,(100,y))
            y+=a
            self.screen.blit(self.fontRead17,(100,y))
            y+=a
            self.screen.blit(self.fontRead18,(100,y))
            self.screen.blit(self.fontRead19, (1200, y))
            self.screen.blit(self.fontRead20, (1350, y+35))


            self.buttons.draw(self.screen)

            self.black.draw(self.screen)
            pygame.display.update()
            self.black.add(self.deadB)
            self.deadB.empty()

    def everythingLoop(self):
        #pygame.key.set_repeat(10)
        while True:
            #exit button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            if pygame.mouse.get_pressed()[0] and self.show.rect.collidepoint(pygame.mouse.get_pos()):
                time.sleep(0.3)
                self.gameLoop()

            if pygame.mouse.get_pressed()[0]:
                self.buttons.add(self.balloon)
                self.balloon.rect.x = pygame.mouse.get_pos()[0]-80
                self.balloon.rect.y = pygame.mouse.get_pos()[1]-160


           #redraw the entire screen
            self.background = pygame.transform.scale((pygame.image.load("src/red.png")), (1600,960))
            self.screen.blit(self.background, (0, 0))
            y = 80
            a = 40
            self.screen.blit(self.fontRead1,(100,y))
            y+=a+20
            self.screen.blit(self.fontRead2,(100,y))
            y+=a
            self.screen.blit(self.fontRead3,(100,y))
            y+=a
            self.screen.blit(self.fontRead4,(100,y))
            y+=a
            self.screen.blit(self.fontRead5,(100,y))
            y+=a+20
            self.screen.blit(self.fontRead6,(100,y))
            y+=a
            self.screen.blit(self.fontRead7,(100,y))
            y+=a
            self.screen.blit(self.fontRead8,(100,y))
            y+=a+20
            self.screen.blit(self.fontRead9,(100,y))
            y+=a
            self.screen.blit(self.fontRead10,(100,y))
            y+=a
            self.screen.blit(self.fontRead11,(100,y))
            y+=a+20
            self.screen.blit(self.fontRead12,(100,y))
            y+=a
            self.screen.blit(self.fontRead13,(100,y))
            y+=a
            self.screen.blit(self.fontRead14,(100,y))
            y+=a+20
            self.screen.blit(self.fontRead15,(100,y))
            y+=a
            self.screen.blit(self.fontRead16,(100,y))
            y+=a
            self.screen.blit(self.fontRead17,(100,y))
            y+=a
            self.screen.blit(self.fontRead18,(100,y))
            self.screen.blit(self.fontRead19, (1200, y))
            self.screen.blit(self.fontRead20, (1350, y+35))


            self.buttons.draw(self.screen)

            pygame.display.flip()
            self.buttons.remove(self.balloon)




def main():
    main_window = Controller()
    main_window.mainLoop()
main()
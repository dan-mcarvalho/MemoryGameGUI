import pygame
import random
import time
from cards import Cartas
from pygame.locals import *
from sys import exit

if __name__ == '__main__':

    pygame.init()

    tela = pygame.display.set_mode((800, 600), 0, 32)
    pygame.display.set_caption("Jogo da memoria vermes")
    clock = pygame.time.Clock()

    flip_image = pygame.image.load('paimon.jpg')
    flip_image = pygame.transform.scale(flip_image, (190, 190))

    sla = pygame.image.load('sla.jpg')
    slaR = pygame.transform.scale(sla, (190, 190))

    chosen = []
    chosen_pos = []
    chosen_rec = []

    jogada = 'PRIMEIRA'

    img1 = pygame.image.load('sprites/barbara.png')
    img2 = pygame.image.load('sprites/benett.png')
    img3 = pygame.image.load('sprites/fischl.png')
    img4 = pygame.image.load('sprites/keqing.png')
    img5 = pygame.image.load('sprites/noelle.png')
    img6 = pygame.image.load('sprites/albedo.png')

    img1 = pygame.transform.scale(img1, (190, 190))
    img2 = pygame.transform.scale(img2, (190, 190))
    img3 = pygame.transform.scale(img3, (190, 190))
    img4 = pygame.transform.scale(img4, (190, 190))
    img5 = pygame.transform.scale(img5, (190, 190))
    img6 = pygame.transform.scale(img6, (190, 190))

    sprites = [img1, img2, img3, img4, img5, img6]

    positions = [(0, 0), (200, 0), (400, 0), (600, 0),
                 (0, 200), (200, 200), (400, 200), (600, 200),
                 (0, 400), (200, 400), (400, 400), (600, 400)]


    def create_board():
        pass


    def set_unflipcards():
        for pos in positions:
            tela.blit(flip_image, (pos))


    cards_position = [0, 0, 0, 0,
                      0, 0, 0, 0,
                      0, 0, 0, 0]

    rect1 = Rect((0, 0), (200, 200))
    rect2 = Rect((200, 0), (200, 200))
    rect3 = Rect((400, 0), (200, 200))
    rect4 = Rect((600, 0), (200, 200))

    rect5 = Rect((0, 200), (200, 200))
    rect6 = Rect((200, 200), (200, 200))
    rect7 = Rect((400, 200), (200, 200))
    rect8 = Rect((600, 200), (200, 200))

    rect9 = Rect((0, 400), (200, 200))
    rect10 = Rect((200, 400), (200, 200))
    rect11 = Rect((400, 400), (200, 200))
    rect12 = Rect((600, 400), (200, 200))

    rec = [rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9, rect10, rect11, rect12]


    def shuffle_card():
        print('yahallo')
        rand_card = random.choice(sprites)
        while rand_card in chosen:
            if chosen.count(rand_card) < 2:
                break
            else:
                rand_card = random.choice(sprites)

        chosen.append(rand_card)

        return rand_card


    carta1 = Cartas(shuffle_card(), positions[0], rec[0], 0)
    carta2 = Cartas(shuffle_card(), positions[1], rec[1], 0)
    carta3 = Cartas(shuffle_card(), positions[2], rec[2], 0)
    carta4 = Cartas(shuffle_card(), positions[3], rec[3], 0)
    carta5 = Cartas(shuffle_card(), positions[4], rec[4], 0)
    carta6 = Cartas(shuffle_card(), positions[5], rec[5], 0)
    carta7 = Cartas(shuffle_card(), positions[6], rec[6], 0)
    carta8 = Cartas(shuffle_card(), positions[7], rec[7], 0)
    carta9 = Cartas(shuffle_card(), positions[8], rec[8], 0)
    carta10 = Cartas(shuffle_card(), positions[9], rec[9], 0)
    carta11 = Cartas(shuffle_card(), positions[10], rec[10], 0)
    carta12 = Cartas(shuffle_card(), positions[11], rec[11], 0)

    all_cards = [carta1, carta2, carta3, carta4, carta5, carta6, carta7, carta8, carta9, carta10, carta11, carta12]

    def click_test():
        global check, jogada
        global last_card
        for p in rec:
            if e.type == MOUSEBUTTONDOWN and p.collidepoint(mouse_pos):
                for c in all_cards:
                    if p == c.rect:
                        tela.blit(c.value, c.pos)
                        c.flip = 1
                        if jogada == 'PRIMEIRA':
                            print(jogada)
                            last_card = c
                            jogada = 'SEGUNDA'

                        else:
                            print(jogada)
                            print(c.rect)
                            print(last_card.rect)
                            jogada = 'PRIMEIRA'
                            check = c.check_card(last_card)
                            print(check)

                            if check is False:
                                print(c.flip)
                                c.flip = 0
                                print(c.flip)
                                print(last_card.flip)
                                last_card.flip = 0
                                print(last_card.flip)
                                tela.blit(flip_image,c.pos)
                                tela.blit(flip_image, last_card.pos)






    def confirm():
        pass


    set_unflipcards()
    i=0
    while True:
        mouse_pos = pygame.mouse.get_pos()

        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                exit()

            if e.type == MOUSEBUTTONDOWN:
                click_test()
        pygame.display.flip()

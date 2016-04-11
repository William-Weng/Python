#-*- coding: UTF-8 -*-

backgroundImage = './images/python.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), pygame.NOFRAME, 32)
background = pygame.image.load(backgroundImage).convert()

x, y = 0, 0
move_x, move_y = 0, 0

while True:

    mods = pygame.key.get_mods()

    for event in pygame.event.get():

        if event.type == KEYDOWN:  # 按下鍵盤時…

            if event.key == K_LEFT:  # 按←的話，就往左邊移動一格
                move_x, move_y = -1, 0
            elif event.key == K_RIGHT:  # 按→的話，就往右邊移動一格
                move_x, move_y = 1, 0
            elif event.key == K_UP:  # 按↑的話，就往上邊移動一格
                move_x, move_y = 0, -1
            elif event.key == K_DOWN:  # 按↓的話，就往下邊移動一格
                move_x, move_y = 0, 1
            elif event.key == K_q and KMOD_CTRL & mods:  # 按下CTRL+Q就離開
                exit()

        elif event.type == KEYUP:  # 放開了鍵盤，圖就不要動了
            move_x, move_y = 0, 0

        x, y = x + move_x, y + move_y  # 計算出新的坐標

        screen.fill((0, 0, 0))
        screen.blit(background, (x, y))  # 在新的位置上畫圖

        pygame.display.update()

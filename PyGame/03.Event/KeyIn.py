#-*- coding: UTF-8 -*-

backgroundImage = './images/python.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
ScreenSize = pygame.display.list_modes() # 取得所有解析度的list
screen = pygame.display.set_mode(ScreenSize[5], NOFRAME, 32) # 取第5個解析度來用
background = pygame.image.load(backgroundImage).convert()

x, y = 0, 0
moveX, moveY = 0, 0
isFullScreen = False

while True:
    mods = pygame.key.get_mods()

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        if event.type == KEYDOWN:  # 按下鍵盤時…

            if event.key == K_LEFT:  # 按←的話，就往左邊移動一格
                moveX, moveY = -1, 0
            elif event.key == K_RIGHT:  # 按→的話，就往右邊移動一格
                moveX, moveY = 1, 0
            elif event.key == K_UP:  # 按↑的話，就往上邊移動一格
                moveX, moveY = 0, -1
            elif event.key == K_DOWN:  # 按↓的話，就往下邊移動一格
                moveX, moveY = 0, 1
            elif event.key == K_q and KMOD_CTRL & mods:  # 按下CTRL+Q就離開
                exit()
            elif event.key == K_f and KMOD_CTRL & mods:  # 按下CTRL+F就切換全螢幕
                screen = pygame.display.set_mode(ScreenSize[5 if isFullScreen else 0], 0 if isFullScreen else FULLSCREEN, 32)
                isFullScreen = not isFullScreen

        elif event.type == KEYUP:  # 放開了鍵盤，圖就不要動了
            moveX, moveY = 0, 0

        x, y = x + moveX, y + moveY  # 計算出新的坐標

        screen.fill((0, 0, 0))
        screen.blit(background, (x, y))  # 在新的位置上畫圖

        pygame.display.update()

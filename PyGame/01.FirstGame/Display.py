#-*- coding: UTF-8 -*-

import pygame
import random
import sys

screen = pygame.display.set_mode((640, 480))  # 設定畫面大小
clock = pygame.time.Clock()  # 做一個計時器
isRunning = True

pygame.display.set_caption("我的PyGame第一支程式")  # 設定視窗標題

while (isRunning):

    # 如果按下視窗右上角的[X]就不玩了
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # pygame.QUIT = 12
            isRunning = False

    # 設定畫面上的點位置(x,y)
    x = random.randint(0, screen.get_width() - 1)
    y = random.randint(0, screen.get_height() - 1)

    # 設定畫面上點的顏色(red, green, blue)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    screen.set_at((x, y), (red, green, blue))  # 設定點的位置跟顏色
    clock.tick(20)  # 一秒跑一次
    pygame.display.flip()  # 顯示在螢幕上

pygame.quit()  # 離開
sys.exit()  # 關閉

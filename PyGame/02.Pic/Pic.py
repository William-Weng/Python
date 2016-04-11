#-*- coding: UTF-8 -*-

import pygame
from sys import exit
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 453), RESIZABLE, 32)  # 設定畫面大小／可以改變視窗大小／顏色32bits
pygame.display.set_caption('Python-Pygame')  # 設定標題

bgPic = pygame.image.load('./images/python.png').convert()  # 載入背景圖
mousePic = pygame.image.load('./images/mouse.png').convert_alpha()  # 載入圖片（含透明度）

while True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            exit()

    x, y = pygame.mouse.get_pos()  # 取得鼠標的位置
    x, y = x - mousePic.get_width() / 2, y - mousePic.get_height() / 2  # 取得中心點，讓鼠標在圖形的正中央

    screen.blit(bgPic, (0, 0))  # 把圖畫上去
    screen.blit(mousePic, (x, y))

    pygame.display.update()  # 更新畫面

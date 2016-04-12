# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
pygame.display.set_caption('簡單的跑馬燈')  # 設定標題

screenSize = (640, 453)
screen = pygame.display.set_mode(screenSize, 0, 32)

font = pygame.font.Font("./fonts/kaiu.ttf", 36)

text_surface = font.render("ヽ(✿ﾟ▽ﾟ)ノ 讚", True, (0, 0, 255))

x, y = 0, (screenSize[1] - text_surface.get_height()) / 2 # 讓文字在畫面Y軸的中心點

background = pygame.image.load("./images/python.png").convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))

    x -= 0.1 # 讓文字移動的速度，方向是→

    if x < -text_surface.get_width(): # 如果文字框不見了，也就是x在文字框最後面的時候，就歸零
        x = screenSize[0]

    screen.blit(text_surface, (x, y))

    pygame.display.update()

#-*- coding: UTF-8 -*-

import pygame
from pygame.locals import *
from sys import exit

from random import *
from math import pi

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
points = []
screen.fill((255, 255, 255))

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            # 按任意鍵可以清屏並把點回覆到原始狀態
            points = []
            screen.fill((255, 255, 255))
        if event.type == MOUSEBUTTONDOWN:
            screen.fill((255, 255, 255))
            # 畫隨機矩形
            rc = (randint(0, 255), randint(0, 255), randint(0, 255))
            rp = (randint(0, 639), randint(0, 479))
            rs = (639 - randint(rp[0], 639), 479 - randint(rp[1], 479))
            pygame.draw.rect(screen, rc, Rect(rp, rs))
            # 畫隨機圓形
            rc = (randint(0, 255), randint(0, 255), randint(0, 255))
            rp = (randint(0, 639), randint(0, 479))
            rr = randint(1, 200)
            pygame.draw.circle(screen, rc, rp, rr)
            # 獲得當前鼠標點擊位置
            x, y = pygame.mouse.get_pos()
            points.append((x, y))
            # 根據點擊位置畫弧線
            angle = (x / 639.) * pi * 2.
            pygame.draw.arc(screen, (0, 0, 0), (0, 0, 639, 479), 0, angle, 3)
            # 根據點擊位置畫橢圓
            pygame.draw.ellipse(screen, (0, 255, 0), (0, 0, x, y))
            # 從左上和右下畫兩根線連接到點擊位置
            pygame.draw.line(screen, (0, 0, 255), (0, 0), (x, y))
            pygame.draw.line(screen, (255, 0, 0), (640, 480), (x, y))
            # 畫點擊軌跡圖
            if len(points) > 1:
                pygame.draw.lines(screen, (155, 155, 0), False, points, 2)
            # 和軌跡圖基本一樣，只不過是閉合的，因為會覆蓋，所以這裡註釋了
            # if len(points) >= 3:
            #    pygame.draw.polygon(screen, (0, 155, 155), points, 2)
            # 把每個點畫明顯一點
            for p in points:
                pygame.draw.circle(screen, (155, 155, 155), p, 3)

    pygame.display.update()

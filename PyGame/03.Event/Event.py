#-*- coding: UTF-8 -*-

import pygame
from sys import exit
from pygame.locals import *

pygame.init()
ScreenSize = (640, 480)
BlueColor = (0, 255, 255)
RedColor = (255, 0, 0)

screen = pygame.display.set_mode(ScreenSize, RESIZABLE, 32)  # 設定畫面大小／可以改變視窗大小／顏色深度32bits
pygame.display.set_caption('Pygame-Event')  # 設定標題

font = pygame.font.SysFont("arial", 16)
line_height = font.get_linesize()  # 取得行高
event_text = []  # list

while True:

    event = pygame.event.wait()  # 等一下，有事件才動作
    event_text.append(str(event))  # 把事件的名稱記下來

    event_text = event_text[int(-ScreenSize[1] / line_height):] # 只要留下螢幕上行數的數量就可以了

    if event.type == QUIT:
        exit()

    screen.fill(BlueColor)

    x, y = 0, ScreenSize[1]  # 從最底下一行開始印

    for text in reversed(event_text):  # 倒著排序，一行一行印出來
        y -= line_height  # 移一行，印一行
        screen.blit(font.render(text, True, RedColor), (x, y))  # 把字放上去

    pygame.display.update()

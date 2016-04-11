#-*- coding: UTF-8 -*-

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
backgroundImage = './images/python.png'
screenSize = (640, 480)
screen = pygame.display.set_mode(screenSize, RESIZABLE, 32)
background = pygame.image.load(backgroundImage).convert()

while True:
    event = pygame.event.wait()
    if event.type == QUIT:
        exit()
    if event.type == VIDEORESIZE: # 改變視窗大小的話…
        screenSize = event.size # 取得當前的視窗大小
        screen = pygame.display.set_mode(screenSize, RESIZABLE, 32) # 設定視窗大小
        pygame.display.set_caption("Window resized to " + str(event.size)) # 把當前的視窗大小設定在標題上

    screen_width, screen_height = screenSize

    for y in range(0, screen_height, background.get_height()): # 把背景圖依(高/寬)貼滿螢幕
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background, (x, y))

    pygame.display.update()

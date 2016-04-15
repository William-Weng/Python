#-*- coding: UTF-8 -*-

background_image_filename = './images/sushiplate.jpg'
sprite_image_filename = './images/fugu.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

# sprite的起始x坐標
x = 0.

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, 100))
    x += 0.1  # 如果你的機器性能太好以至於看不清，可以把這個數字改小一些

    # 如果移動出屏幕了，就搬到開始位置繼續
    if x > 640:
        x = 0

    pygame.display.update()

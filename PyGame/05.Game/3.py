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

# Clock對象
clock = pygame.time.Clock()

x = 0
# 速度（像素/秒）
speed = 250

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0,0))
    screen.blit(sprite, (x, 100))

    time_passed = clock.tick(1) # 24fps
    time_passed_seconds = time_passed / 1000.0

    distance_moved = time_passed_seconds * speed
    x += distance_moved

    # 想一下，這裡減去640和直接歸零有何不同？
    if x > 640:
        x -= 640
        #x=0

    pygame.display.update()

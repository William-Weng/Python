#-*- coding: UTF-8 -*-

background_image_filename = './images/sushiplate.jpg'
sprite_image_filename = './images/fugu.png'

import pygame
from pygame.locals import *
from sys import exit
from classes.gameobjects import vector2

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

position = vector2(100.0, 100.0)
heading = vector2()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, position)

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    # 參數前面加*意味著把列表或元組展開
    destination = vector2(*pygame.mouse.get_pos()) - vector2(*sprite.get_size()) / 2
    # 計算魚兒當前位置到鼠標位置的向量
    vector_to_mouse = vector2.from_points(position, destination)
    # 向量規格化
    vector_to_mouse.normalized()

    # 這個heading可以看做是魚的速度，但是由於這樣的運算，魚的速度就不斷改變了
    # 在沒有到達鼠標時，加速運動，超過以後則減速。因而魚會在鼠標附近晃動。
    heading = heading + (vector_to_mouse * .6)

    position += heading * time_passed_seconds
    pygame.display.update()

#-*- coding: UTF-8 -*-

import pygame

pygame.init()

allColors = pygame.Surface((4096, 4096), depth=24)  # 4096 * 4096 * 24bits 的白紙 ==> bland_alpha_surface = pygame.Surface((256, 256), flags=SRCALPHA, depth=32)

for r in range(256):  # rgb ==> (0,0,0) ~ (255,255,255)
    print(r + 1, "out of 256")
    x, y = (r & 0b1111) * 256, (r >> 0b100) * 256

    for g in range(256):
        for b in range(256):
            allColors.set_at((x + g, y + b), (r, g, b))

pygame.image.save(allColors, "allColors.bmp")

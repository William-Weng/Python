#-*- coding: UTF-8 -*-

import pygame

pygame.init()

myName = "William Weng"
myName2 = "小小兵"
myName3 = "塔矢アキラ"

fonts = pygame.font.get_fonts()  # 取得系統內的字型列表

myFontEn = pygame.font.SysFont("arial", 64)
myFontCht = pygame.font.SysFont("NotoSansDeseret-Regular.ttf", 64)
myFontJp = pygame.font.Font("./fonts/NotoSansDeseret-Regular.ttf", 64)

nameSurfaceEn = myFontEn.render(myName, True, (0, 0, 0))
nameSurfaceCht = myFontCht.render(myName2, True, (0, 0, 0), (255, 255, 0))
nameSurfaceJp = myFontJp.render(myName3, True, (0, 0, 0), (255, 255, 0))

pygame.image.save(nameSurfaceEn, "name.png")
pygame.image.save(nameSurfaceCht, "name2.png")
pygame.image.save(nameSurfaceJp, "name3.png")

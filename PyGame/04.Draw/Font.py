#-*- coding: UTF-8 -*-

import pygame

pygame.init()

myNameEn = "William-Weng"
myNameCht = "小小兵"
myNameJp = "はたの ゆい"

#fonts = pygame.font.get_fonts()  # 取得系統內的字型列表
#print('kaiu' in fonts)  # 檢查有沒有該字型 ==> Windows 標楷體

myFontEn = pygame.font.SysFont("arial", 64) # 取得系統字型
myFontCht = pygame.font.SysFont("kaiu.ttf", 64) # Windows 標楷體
myFontJp = pygame.font.Font("./fonts/kaiu.ttf", 64) # 取得外部字型 ==> Windows 標楷體

nameSurfaceEn = myFontEn.render(myNameEn, True, (0, 0, 0)) # 產生文字輸出
nameSurfaceCht = myFontJp.render(myNameCht, True, (0, 0, 0), (255, 255, 0))
nameSurfaceJp = myFontJp.render(myNameJp, True, (0, 0, 0), (0, 255, 255))

pygame.image.save(nameSurfaceEn, "myNameEn.png")
pygame.image.save(nameSurfaceCht, "myNameCht.png")
pygame.image.save(nameSurfaceJp, "myNameJp.png")

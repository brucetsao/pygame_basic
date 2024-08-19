# 這段程式碼定義了一個名為 Bullet 的類別，
# 該類別用於控制子彈的生成、
# 移動、
# 顯示和狀態管理。
# 此類別繼承自 pygame.sprite.Sprite，
# 這是一個 Pygame 的基礎類別，用於處理遊戲中的精靈物件。


import sys, time
import random

import pygame
from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT

# 定義子彈類別，繼承自 Pygame 的精靈類
class Bullet(pygame.sprite.Sprite):
    __Width = 32  # 子彈的寬度
    __Height = 32  # 子彈的高度
    __Alive = False  # 子彈初始狀態為不存活
    __PosX = 0  # 子彈的初始X座標
    __PosY = 0  # 子彈的初始Y座標
    __imgpath = './images/bullet.png'  # 子彈圖片路徑

    def __init__(self, pos_x, pos_y, widow_width, window_height):
        super().__init__()
        # 載入子彈圖片並轉換其 alpha 通道以便支援透明度
        self.raw_image = pygame.image.load(self.__imgpath).convert_alpha()
        # 將圖片縮放到指定的寬度和高度
        self.image = pygame.transform.scale(self.raw_image, (self.__Width, self.__Height))

        # 設定子彈的初始位置
        self.__PosX = pos_x
        self.__PosY = pos_y
        # 獲取圖片的矩形區域
        self.rect = self.image.get_rect()
        # 將矩形區域的左上角座標設置為子彈的初始位置
        self.rect.topleft = (self.__PosX, self.__PosY)
        self.width = self.__Width
        self.height = self.__Height
        self.widow_width = widow_width
        self.window_height = window_height

    # 繪製子彈
    def show(self, canvas, play_x, play_y):
        if self.__Alive:
            # 如果子彈存活，則在畫布上繪製子彈
            canvas.blit(self.image, (play_x, play_y))

    # 檢查子彈是否被擊中
    def __Checkkilled(self, x, y):
        # 檢查 x, y 是否在子彈的範圍內
        if x >= self.__PosX:
            if x <= (self.__PosX + self.__Width):
                if y <= (self.__PosY + self.__Height):
                    if y >= self.__PosY:
                        return True  # 如果 x, y 落在子彈範圍內，返回 True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    # 子彈被摧毀
    def Killed(self):
        if self.__Alive:
            self.__Alive = False  # 將子彈狀態設為不存活

    # 子彈爆炸（目前未實現）
    def __Explode(self):
        aa = 1

    # 檢查子彈是否準備好發射
    def isReady(self):
        if not self.__Alive:
            return True  # 如果子彈不存活，則表示準備好發射
        else:
            return False

    # 發射子彈
    def Fire(self):
        if not self.__Alive:
            self.__Alive = True  # 將子彈狀態設為存活

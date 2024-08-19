# 這段程式碼定義了一個名為 Enemy 的類別，
# 該類別用於控制敵人的生成、
# 移動、
# 顯示和狀態管理。
# 此類別繼承自 pygame.sprite.Sprite，
# 這是一個 Pygame 的基礎類別，
# 用於處理遊戲中的精靈物件。
# 敵人會在遊戲中隨機生成位置，
# 並根據隨機生成的移動距離進行左右移動，
# 當碰到牆壁時會改變移動方向並向下移動。

import sys, time
import random

import pygame
from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT

# 定義敵人類別，繼承自 Pygame 的精靈類
class Enemy(pygame.sprite.Sprite):
    __Width = 64    # 敵人角色的寬度
    __Height = 64   # 敵人角色的高度
    __Alive = True  # 記錄敵人是否存活
    __PosX = 0      # 敵人的 X 座標
    __PosY = 0      # 敵人的 Y 座標
    __MoveX = 0     # 敵人橫向移動的間距
    __MoveY = 0     # 敵人縱向移動的間距
    __MoveDir = 1   # 敵人橫向移動的方向，1 表示向右，0 表示向左
    __imgpath = './images/enemy.png'  # 敵人的圖片路徑

    # 設定敵人的位置
    def __setpos(self):
        self.rect.topleft = (self.__PosX, self.__PosY)

    # 初始化敵人角色
    def __init__(self, pos_x, pos_y, widow_width, window_height):
        super().__init__()
        # 載入敵人的圖片並轉換其 alpha 通道以支援透明度
        self.raw_image = pygame.image.load(self.__imgpath).convert_alpha()
        # 將圖片縮放到指定的寬度和高度
        self.image = pygame.transform.scale(self.raw_image, (self.__Width, self.__Height))

        # 設定敵人的初始位置
        self.__PosX = pos_x
        self.__PosY = pos_y
        # 獲取圖片的矩形區域
        self.rect = self.image.get_rect()
        # 設定敵人的寬度和高度
        self.width = self.__Width
        self.height = self.__Height
        # 設定遊戲窗口的寬度和高度
        self.widow_width = widow_width
        self.window_height = window_height
        # 設定敵人的初始位置
        self.__setpos()
        # 隨機設置敵人的橫向移動距離
        self.__MoveX = random.randint(3, 8)
        # 隨機設置敵人的縱向移動距離
        self.__MoveY = random.randint(6, 12)

    # 繪製敵人角色
    def show(self, canvas):
        if self.__Alive:
            # 如果敵人存活，則在畫布上繪製敵人
            canvas.blit(self.image, self.rect)

    # 檢查敵人是否被擊中
    def __Checkkilled(self, x, y):
        # 檢查 x, y 是否在敵人的範圍內
        if x >= self.__PosX:
            if x <= (self.__PosX + self.__Width):
                if y <= (self.__PosY + self.__Height):
                    if y >= self.__PosY:
                        return True  # 如果 x, y 落在敵人範圍內，返回 True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    # 敵人被摧毀
    def Killed(self, x, y):
        if self.__Alive:
            if self.__Checkkilled(x, y):
                # 如果敵人被擊中，則設置為不存活並進行爆炸效果
                self.__Alive = False
                self.__Explode()

    # 敵人爆炸（目前未實現）
    def __Explode(self):
        aa = 1

    # 檢查敵人是否移動到左右邊界
    def CheckWall(self):
        if self.__PosX >= self.widow_width:
            # 如果敵人超過右邊界，則改變方向並向下移動
            self.__MoveDir = 0
            self.__PosY += self.__MoveY
        if self.__PosX <= 0:
            # 如果敵人超過左邊界，則改變方向並向下移動
            self.__MoveDir = 1
            self.__PosY += self.__MoveY

    # 控制敵人的移動
    def Move(self):
        if self.__MoveDir == 1:
            # 根據方向控制敵人橫向移動
            self.__PosX += self.__MoveX
        else:
            self.__PosX -= self.__MoveX
        self.__setpos()
        self.CheckWall()  # 檢查是否觸碰到牆壁並改變移動方向

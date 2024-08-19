# 這段代碼定義了一個名為 Player 的類，
# 用於表示遊戲中的玩家飛機。
# 它提供了飛機的載入、
# 顯示和檢測是否被擊中的基本功能。
# 該類別使用 pygame.sprite.Sprite 作為基類，
# 以便整合到 Pygame 的精靈系統中

import sys, time
import random

import pygame
from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT

class Player(pygame.sprite.Sprite):
    # 定義玩家飛機的寬度和高度
    __Width = 64
    __Height = 64
    # 玩家飛機的狀態，初始設定為存活
    __Alive = True
    # 玩家飛機的初始位置
    __PosX = 0
    __PosY = 0
    # 玩家飛機圖像的路徑
    __imgpath = './images/player.png'

    def __init__(self, pos_x, pos_y, widow_width, window_height):
        super().__init__()  # 初始化父類別
        # 載入玩家飛機的圖片並轉換為支持透明度
        self.raw_image = pygame.image.load(self.__imgpath).convert_alpha()
        # 調整圖片的大小為預設寬度和高度
        self.image = pygame.transform.scale(self.raw_image, (self.__Width, self.__Height))

        # 設定飛機的初始位置
        self.__PosX = pos_x
        self.__PosY = pos_y
        # 取得飛機圖片的矩形區域
        self.rect = self.image.get_rect()
        # 將矩形區域的左上角設置為飛機的初始位置
        self.rect.topleft = (self.__PosX, self.__PosY)
        # 設定飛機的寬度和高度
        self.width = self.__Width
        self.height = self.__Height
        # 設定視窗的寬度和高度
        self.widow_width = widow_width
        self.window_height = window_height

    def show(self, canvas: object, play_x, play_y) -> object:
        """
        在畫布上顯示玩家飛機
        :param canvas: 畫布對象
        :param play_x: 飛機的X座標
        :param play_y: 飛機的Y座標
        """
        if self.__Alive:  # 如果飛機是存活狀態
            # 在指定位置繪製飛機
            canvas.blit(self.image, (play_x, play_y))

    def __Checkkilled(self, x, y):
        """
        檢查指定的座標是否位於飛機上，用於檢測飛機是否被擊中
        :param x: X座標
        :param y: Y座標
        :return: 如果擊中則返回True，否則返回False
        """
        if x >= self.__PosX:
            if x <= (self.__PosX + self.__Width):
                if y <= (self.__PosY + self.__Height):
                    if y >= self.__PosY:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def Killed(self, x, y):
        """
        檢查並更新飛機的生命狀態
        :param x: X座標
        :param y: Y座標
        """
        if self.__Alive:  # 如果飛機是存活狀態
            # 如果被擊中，將飛機狀態設為死亡並觸發爆炸效果
            if self.__Checkkilled(x, y):
                self.__Alive = False
                self.__Explode()

    def __Explode(self):
        """
        處理飛機爆炸的效果，目前未實作
        """
        aa = 1  # 占位符號，目前未實作具體爆炸效果

import sys, time
import random

import pygame
from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT

class Mosquito(pygame.sprite.Sprite):
    def __init__(self, width, height, random_x, random_y, widow_width, window_height):
        # 繼承自 Pygame 的 Sprite 類別，這樣可以使用 Pygame 的精靈功能
        super().__init__()

        # 載入蚊子的圖片，並支援透明背景
        self.raw_image = pygame.image.load('./images/mosquito.jpg').convert_alpha()

        # 將圖片縮小到指定的寬度和高度
        self.image = pygame.transform.scale(self.raw_image, (width, height))

        # 獲取蚊子圖片的矩形區域，用於定位和碰撞檢測
        self.rect = self.image.get_rect()

        # 設置蚊子的初始位置，位置由傳入的 random_x 和 random_y 決定
        self.rect.topleft = (random_x, random_y)

        # 設置蚊子的寬度和高度
        self.width = width
        self.height = height

        # 設置遊戲視窗的寬度和高度
        self.widow_width = widow_width
        self.window_height = window_height

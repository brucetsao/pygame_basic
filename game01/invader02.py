import sys
import random
import pygame
from pygame.locals import QUIT
from Enemy import *  # 導入敵人相關的模組
from Player import *  # 導入玩家相關的模組
#import pygame.mixer as player  # 加入音樂播放器（此行已註解）
from pygame import mixer

# 定義視窗的寬度和高度
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 定義顏色為白色 (R:255, G:255, B:255)
WHITE = (255, 255, 255)

# 設定每秒鐘的幀數 (FPS: Frames Per Second)
FPS = 60

# 初始化敵人列表為空
enemy = []

# 玩家初始位置
playX = 400
playY = 520
playerX_change = 0

def get_random_position(window_width, window_height, image_width, image_height):
    """
    隨機生成一個位置，這個位置用於放置敵人或其他物件。
    確保物件不會超出視窗邊界。
    """
    # 隨機生成 X 位置
    random_x = random.randint(image_width, window_width - image_width)
    # 隨機生成 Y 位置
    random_y = random.randint(image_height, window_height - image_height)

    return random_x, random_y

def initenemy():
    """
    初始化敵人，將 8 個敵人加入敵人列表。
    每個敵人的 X 位置會隨著索引不同而變化。
    """
    for x in range(0, 8):
        enemy.append(Enemy(0 + x * 100, 10, WINDOW_WIDTH, WINDOW_HEIGHT))
        # 將敵人添加到列表中，可以顯示在畫面上

def showenemy(canvas):
    """
    在畫布上顯示所有敵人。
    """
    for x in enemy:
        x.show(canvas)

def showplayer(canvas, px, py):
    """
    在畫布上顯示玩家角色。
    """
    master.show(canvas, px, py)

# 初始化 Pygame
pygame.init()
#初始化所有 Pygame 模組，這是使用 Pygame 開發遊戲的必備步驟。

# 創建一個 800x600 像素的視窗
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 設置視窗標題
pygame.display.set_caption('太空大作戰')
#設置視窗的標題為 "太空大作戰"。
#創建一個視窗，尺寸為 800x600 像素。

# 加載背景圖片並將其繪製到視窗上
background = pygame.image.load('./images/background.png')
#加載背景圖片
screen.blit(background, (0, 0))
#將背景圖片繪製到視窗上，位置在 (0, 0)。

# 初始化敵人
initenemy()
#創建並初始化 8 個敵人並加入 enemy 列表中。

# 創建玩家對象，創建玩家角色對象。
master = Player(playX, playY, WINDOW_WIDTH, WINDOW_HEIGHT)

# 加載並播放背景音樂，-1 代表循環播放
mixer.music.load("./music/background.wav")
#加載背景音樂檔案。
mixer.music.play(-1)
#播放背景音樂並設置循環播放（-1 代表無限循環）。

# 遊戲主循環
running = True
while running:  #遊戲主循環，會持續執行，直到 running 被設置為 False。這裡處理所有的遊戲更新和顯示。
    # 填充視窗背景顏色為黑色 (RGB: 0, 0, 0)
    screen.fill((0, 0, 0))
    #將視窗的背景顏色設置為黑色，這是每一幀更新畫面之前清除之前畫面的一步。

    # 繪製背景圖片
    screen.blit(background, (0, 0))

    # 顯示所有敵人
    showenemy(screen)

    # 顯示玩家角色
    showplayer(screen, playX, playY)

    # 更新顯示
    pygame.display.update()
    #更新顯示，將繪製的內容顯示到屏幕上。
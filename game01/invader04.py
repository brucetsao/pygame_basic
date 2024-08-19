# 這段代碼實現了一個簡單的太空射擊遊戲。
# 主要包括玩家控制、
# 敵人生成與移動、
# 子彈發射等功能，
# 並使用了 Pygame 來實現遊戲的顯示與音效。

import sys
import random
import pygame
from pygame.locals import QUIT
from Enemy import *  # 導入敵人類別
from Player import *  # 導入玩家類別
from Bullet import *  # 導入子彈類別
from pygame import mixer  # 導入音樂模組

# 定義視窗大小
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 定義顏色
WHITE = (255, 255, 255)

# 定義幀率
FPS = 60

# 定義遊戲變數
enemy = []  # 用來儲存敵人的列表
playX = 400  # 玩家初始X座標
playY = 520  # 玩家初始Y座標
playerX_change = 0  # 玩家X方向移動變量
bulletX = 0  # 子彈初始X座標
bulletY = 480  # 子彈初始Y座標
bulletX_change = 0  # 子彈X方向移動變量
bulletY_change = 10  # 子彈Y方向移動變量
bullet_state = "ready"  # 子彈狀態（準備好或正在射擊）

# 隨機產生一個位置
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

# 發射子彈
def fire_bullet(canvas, x, y):
    global bullet_state
    bullet_state = "fire"  # 將子彈狀態設為 "fire"
    bullet.show(canvas, x, y)  # 在畫布上顯示子彈
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


# 創建玩家和子彈物件
master = Player(playX, playY, WINDOW_WIDTH, WINDOW_HEIGHT)
bullet = Bullet(playX, playY, WINDOW_WIDTH, WINDOW_HEIGHT)

# 播放背景音樂
mixer.music.load("./music/background.wav")
mixer.music.play(-1)  # 無限循環播放音樂

# 遊戲循環
running = True
while running:
    screen.fill((0, 0, 0))  # 填充螢幕背景為黑色
    screen.blit(background, (0, 0))  # 繪製背景圖片

    # 更新並顯示每個敵人
    for x in enemy:
        x.Move()  # 移動敵人
        x.show(screen)  # 繪製敵人

    showplayer(screen, playX, playY)  # 繪製玩家

    # 處理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # 若收到QUIT事件，退出遊戲

        # 檢測按鍵按下事件
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5  # 若按下左鍵，玩家左移
            if event.key == pygame.K_RIGHT:
                playerX_change = 5  # 若按下右鍵，玩家右移
            if event.key == pygame.K_SPACE:
                if bullet.isReady():
                    bullet.Fire()  # 發射子彈
                    bullet_state = "fire"
                    bulletX = playX + 16  # 設置子彈X座標
                    bulletY = playY  # 設置子彈Y座標

        # 檢測按鍵釋放事件
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0  # 釋放左或右鍵，停止玩家移動

    # 更新玩家X座標
    playX += playerX_change
    if playX <= 0:  # 若玩家超出左邊界
        playX = 0
    elif playX >= 736:  # 若玩家超出右邊界
        playX = 736

    # 子彈移動
    if bulletY <= 0:  # 若子彈超出上邊界
        bulletY = 480  # 重置子彈Y座標
        bullet_state = "ready"  # 重置子彈狀態
        bullet.Killed()  # 殺死子彈

    if bullet_state == "fire":  # 若子彈處於發射狀態
        fire_bullet(screen, bulletX, bulletY)  # 繪製子彈
        bulletY -= bulletY_change  # 子彈向上移動

    pygame.display.update()  # 更新螢幕顯示

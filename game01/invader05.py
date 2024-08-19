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
    # 填充螢幕背景為黑色 (RGB: 0, 0, 0)
    screen.fill((0, 0, 0))
    #每一幀重新填充背景為黑色，這樣可以清除上幀的內容。

    # 繪製背景圖片到視窗的 (0, 0) 位置
    screen.blit(background, (0, 0))
    #將背景圖片繪製到視窗上，以 (0, 0) 作為繪製的起點。

    # 更新並顯示每個敵人
    for x in enemy:
        x.Move()  # 調用敵人的移動方法，使敵人移動
        #調用敵人的 Move 方法，讓敵人進行移動。
        x.show(screen)  # 繪製敵人到視窗上
        #在視窗上繪製敵人。

    # 繪製玩家角色
    showplayer(screen, playX, playY)
    #繪製玩家角色。

    # 處理所有事件
    for event in pygame.event.get():    #獲取所有待處理的事件（如按鍵、鼠標點擊等）。
        # 檢測是否收到退出事件 (QUIT)
        if event.type == pygame.QUIT:   #檢查是否收到退出事件（點擊關閉視窗按鈕）。
            running = False  # 若收到退出事件，將 running 設置為 False，退出遊戲循環

        # 檢測按鍵按下事件
        if event.type == pygame.KEYDOWN:    #檢查是否有按鍵被按下，並根據按鍵設置玩家的移動方向。
            # 若按下左鍵，設置玩家移動方向為左
            if event.key == pygame.K_LEFT:  #設置玩家的移動速度，根據按下的方向鍵設置為左移或右移。
                playerX_change = -5  # 玩家向左移動的速度

            # 若按下右鍵，設置玩家移動方向為右
            if event.key == pygame.K_RIGHT:
                playerX_change = 5  # 玩家向右移動的速度

            # 若按下空白鍵，檢查子彈是否可以發射
            if event.key == pygame.K_SPACE: #檢查是否按下空白鍵，若子彈準備發射則設置子彈的發射狀態和位置。
                if bullet.isReady():  # 檢查子彈是否準備好發射
                    bullet.Fire()  # 發射子彈
                    bullet_state = "fire"  # 設置子彈狀態為發射中
                    bulletX = playX + 16  # 設置子彈的 X 座標 (玩家位置 + 16)
                    bulletY = playY  # 設置子彈的 Y 座標 (玩家位置)

        # 檢測按鍵釋放事件
        if event.type == pygame.KEYUP:  #檢查按鍵是否被釋放，若釋放左鍵或右鍵，則停止玩家的移動
            # 若釋放了左鍵或右鍵，停止玩家移動
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0  # 玩家停止移動

    # 更新玩家的 X 座標
    playX += playerX_change #更新玩家的 X 座標，根據玩家的移動速度調整位置
    # 檢查玩家是否超出視窗左邊界
    if playX <= 0:  #檢查子彈是否超出視窗的上邊界，若是，則重置子彈的位置和狀態。
        playX = 0  # 將玩家位置設置為視窗左邊界
    # 檢查玩家是否超出視窗右邊界
    elif playX >= 736:
        playX = 736  # 將玩家位置設置為視窗右邊界

    # 子彈移動邏輯
    if bulletY <= 0:  # 若子彈超出視窗上邊界
        bulletY = 480  # 重置子彈的 Y 座標至視窗底部
        bullet_state = "ready"  # 重置子彈狀態為準備發射
        bullet.Killed()  # 呼叫子彈的 "Killed" 方法，處理子彈的死亡或回收

    # 若子彈處於發射狀態
    if bullet_state == "fire":
        fire_bullet(screen, bulletX, bulletY)  # 繪製子彈
        bulletY -= bulletY_change  # 使子彈向上移動 (減少 Y 座標)

    # 更新顯示，將所有畫面變化顯示到螢幕上
    pygame.display.update()
    #更新顯示，將所有畫面變化顯示到螢幕上。

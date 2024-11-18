import sys  #使用作業系統用到的套件
import pygame  # 匯入 PyGame 套件
import math #使用常用數學函式套件
import random   #使用亂數功能之套件
from Player import *  # 匯入自定義的 Player 類別
from pygame.locals import *  # 匯入 Pygame 的所有常數和函數，主要可以使用到鍵盤常數變數

FPS = 30  # 設定每秒更新幀數（Frame Per Second）

#遊戲初始化：使用 pygame.init() 初始化 Pygame，並設置遊戲視窗的大小和標題
pygame.init()  # 啟動 PyGame 套件

screen = pygame.display.set_mode((800, 600))  # 建立一個 800x600 的遊戲視窗
# screen 為視窗變數，用來存取建立的視窗
# 視窗變數 = pygame.display.set_mode(視窗寬度尺寸:pixels，視窗高度尺寸:pixels)

pygame.display.set_caption("PyGame 操控功能介紹:建立一個小精靈(吃豆人)可以上下左右鍵移動的角色")
# pygame.display.set_caption() 用來設定視窗標題

screen.fill((0, 0, 0))  # 用黑色 (RGB: 0, 0, 0) 填充整個視窗背景
# 視窗變數.fill(RGB變數參數)

#精靈（吃豆人）創建：透過 Player 類來創建吃豆人，並隨機設置初始位置。該精靈將加入到精靈群組中
# 創建一個玩家精靈並隨機設置其初始位置，並加入精靈群組
pac = Player('./images/ball.png', 'PacMan', random.randint(50, screen.get_width()), random.randint(50, screen.get_height()), screen)
# pac 是主角吃豆人的 Player 類別的實例，設定角色的圖像、名稱、初始位置等
# 使用隨機位置來放置吃豆人

clock = pygame.time.Clock()  # 創建一個時鐘對象，用來控制遊戲循環的幀率

# 創建精靈群組
all_sprites = pygame.sprite.Group()

# 將玩家精靈加入精靈群組
all_sprites.add(pac)

pygame.key.set_repeat(0, 500)  # 設置按鍵重複時間，0 表示立即重複，500 毫秒之後觸發下一次按鍵重複

# 設定遊戲主循環是否離開或在遊戲進行程序之控制變數
running = True #設定遊戲主循環是否離開或在遊戲進行程序之控制變數

# 遊戲主循環迴圈
while running:
    #事件處理：處理玩家的按鍵輸入，透過上下左右鍵控制吃豆人的移動，當按下 ESC 鍵時退出遊戲
    for event in pygame.event.get():
        # pygame.event.get() 會取得所有的事件，例如滑鼠移動、按下按鍵等
        # 每次迴圈會檢查每個事件變數
        if event.type == pygame.QUIT:   #是否按下結束按鈕，按下的話，結束遊戲
            # 如果事件類型是 pygame.QUIT，表示點擊了關閉按鈕
            #遊戲結束：當遊戲主循環結束時，執行 pygame.quit() 關閉視窗並退出遊戲。
            running = False  # 設定遊戲狀態為 False，終止主循環
            # 當遊戲狀態變為 False，會跳出迴圈並結束遊戲

    # 取得當前按鍵的狀態
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:  # 如果按下 ESC 鍵，退出遊戲
        sys.exit()  # 系統退出，關閉遊戲視窗
        #遊戲結束：當遊戲主循環結束時，執行 pygame.quit() 關閉視窗並退出遊戲。
    if keys[K_UP]:
        pac.Up()  # 如果按下上鍵，讓吃豆人向上移動
    if keys[K_DOWN]:
        pac.Down()  # 如果按下下鍵，讓吃豆人向下移動
    if keys[K_RIGHT]:
        pac.Right()  # 如果按下右鍵，讓吃豆人向右移動
    if keys[K_LEFT]:
        pac.Left()  # 如果按下左鍵，讓吃豆人向左移動

    #畫面更新：在每個遊戲循環中，更新精靈狀態並將它們繪製在螢幕上，然後更新顯示
    # 更新所有精靈的狀態
    all_sprites.update()

    # 填充背景為白色(重畫遊戲視窗背景)
    screen.fill((255, 255, 255))

    # 在視窗上繪製所有精靈
    all_sprites.draw(screen)

    # 更新螢幕顯示
    pygame.display.flip()

    # 控制幀率
    clock.tick(20)

# 離開遊戲並關閉 Pygame
pygame.quit()

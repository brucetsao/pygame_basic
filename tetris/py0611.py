import sys  # 使用作業系統用到的套件
import pygame  # 匯入 PyGame 套件
import math  # 使用常用數學函式套件
import random  # 使用亂數功能之套件
from Hammers import *  # 匯入自定義的 Hammers 類別
from pygame.locals import *  # 匯入 Pygame 的所有常數和函數，主要可以使用到鍵盤常數變數

# 定義一個檢查座標是否在螢幕範圍內的函數
def CheckinScreen(x, y, x1, y1):
    if (x >= 0) & (x <= x1):  # 檢查 X 座標是否在螢幕範圍內
        if (y >= 0) & (y <= y1):  # 檢查 Y 座標是否在螢幕範圍內
            return True
        else:
            return False
    else:
        return False

FPS = 30  # 設定每秒更新幀數（Frame Per Second）

# 初始化與視窗設置：程式先使用 pygame.init() 初始化 Pygame，並設置了一個 800x600 的遊戲視窗。視窗背景初始為黑色，並設置了標題
pygame.init()  # 啟動 PyGame 套件

screen = pygame.display.set_mode((800, 600))  # 建立一個 800x600 的遊戲視窗
# screen 為視窗變數，用來存取建立的視窗
scrx = screen.get_width()  # 獲取視窗寬度
scry = screen.get_height()  # 獲取視窗高度

pygame.display.set_caption("PyGame 滑鼠操控功能介紹:建立打地鼠鎚子的角色，並隨滑鼠按鈕判斷鎚子狀態")
# pygame.display.set_caption() 用來設定視窗標題

screen.fill((0, 0, 0))  # 用黑色 (RGB: 0, 0, 0) 填充整個視窗背景
# 視窗變數.fill(RGB變數參數)

# 精靈（鎚子）創建：透過 Hammer 類別程式中的Player()類別來創建鎚子，並隨機設置初始位置。該精靈將加入到精靈群組中
#鎚子角色的建立：透過 Player 類別來創建鎚子角色，並隨機設置初始位置，鎚子的圖片會根據滑鼠按下狀態切換
hammer = Player('./images/hummer1.png', 'Hammer', 0,0, screen)
# hammer 是鎚子的 Player 類別的實例，設定角色的圖像、名稱、初始位置等
# 使用隨機位置來放置鎚子
hammer.loadimage('./images/hummer2.png')  # 加載第二張圖像
clock = pygame.time.Clock()  # 創建一個時鐘對象，用來控制遊戲循環的幀率

# 創建精靈群組
all_sprites = pygame.sprite.Group()

# 將玩家精靈加入精靈群組
all_sprites.add(hammer)

# 設定遊戲主循環是否離開或在遊戲進行程序之控制變數
running = True  # 設定遊戲主循環是否離開或在遊戲進行程序之控制變數

# 遊戲主遊戲迴圈：在主迴圈中，程式會持續檢查事件、獲取滑鼠位置和按鈕狀態，根據滑鼠位置移動鎚子，並在畫面上更新鎚子的位置和外觀。
while running:
    # 事件處理：處理玩家的按鍵輸入，當按下關閉按鈕時退出遊戲
    for event in pygame.event.get():
        # pygame.event.get() 會取得所有的事件，例如滑鼠移動、按下按鍵等
        # 每次迴圈會檢查每個事件變數
        if event.type == pygame.QUIT:  # 是否按下結束按鈕，按下的話，結束遊戲
            running = False  # 設定遊戲狀態為 False，終止主循環

    # 獲取滑鼠當前位置
    pos = pygame.mouse.get_pos()    # 獲取滑鼠當前位置
    print(pos, screen.get_size())  # 顯示滑鼠位置與螢幕大小
    hammer.setPos(pos[0], pos[1])  # 根據滑鼠位置設定鎚子的位置

    # 檢查滑鼠按鈕狀態
    mousebutton = pygame.mouse.get_pressed() # 獲取滑鼠按鍵狀態
    print("mouse status is ", mousebutton)  #印出滑鼠按鍵按鍵狀態內容(True為按下，False為沒按下)
    if mousebutton[0]:  # 如果滑鼠左鍵按下，切換圖像
        hammer.imagnumber = 2   #切換圖像為第二張
    else:
        hammer.imagnumber = 1   #切換圖像為第一張

    # 畫面更新：更新精靈狀態並將它們繪製在螢幕上
    all_sprites.update()  # 更新所有精靈的狀態

    # 填充背景為白色（重畫遊戲視窗背景）
    screen.fill((255, 255, 255))

    # 在視窗上繪製所有精靈
    all_sprites.draw(screen)

    # 更新螢幕顯示
    pygame.display.flip()

    # 控制幀率
    clock.tick(20)

# 離開遊戲並關閉 Pygame
pygame.quit()

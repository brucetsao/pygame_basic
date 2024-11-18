import pygame  #匯入PyGame套件
import math
import random
from Player import *
from pygame.locals import *

FPS = 30

pygame.init()  #啟動PyGame套件
screen = pygame.display.set_mode((800, 600))
#screen為視窗變數，來使用建立的視窗
#視窗變數 = pygame.display.set_mode(視窗寬度尺寸:pixels，視窗高度尺寸:pixels)

pygame.display.set_caption("PyGame Sprite 功能介紹:畫出一個來回移動矩形Sprite")
#pygame.display.set_caption(視窗標題的內容)

screen.fill((0, 0, 0))
#視窗變數.fill(RGB變數參數)
pygame.key.set_repeat(26)         # 重复按键


# 創建一個玩家精靈並加入群組
pac =  Player('./images/ball.png','PacMan' ,random.randint(50,screen.get_width()), random.randint(50,screen.get_height()),screen)
# all_sprites.add(player)
clock = pygame.time.Clock()

# 創建精靈群組
all_sprites = pygame.sprite.Group()

# 創建一個玩家精靈並加入群組

all_sprites.add(pac)

# 設定遊戲主循環
running = True
while running:
    for event in pygame.event.get():
        # pygame.event.get()是一個滑鼠移動、動作、按下、放開….等所有事件集合
        # event 迴圈找出每一個事件變數
        if event.type == pygame.QUIT:
            # pygame.QUIT就是按到系統結束按鈕
            running = False  # 設定pygame視窗正常運行之控制參數，並設為False
            # 設定pygame視窗正常運行之控制參數，並設為False，會離開迴圈
    # 更新所有精靈
    all_sprites.update()

    # 畫面填充背景為白色顏色
    screen.fill((255, 255, 255))

    # 繪製所有精靈
    all_sprites.draw(screen)

    # 更新顯示
    pygame.display.flip()

    # 控制幀率
    clock.tick(30)

pygame.quit()  # 離開且關閉pygame視窗
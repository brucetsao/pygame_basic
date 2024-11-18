import sys
import pygame  #匯入PyGame套件
from pygame.locals import *

pygame.init()  #啟動PyGame套件
screen = pygame.display.set_mode((800, 600))
#screen為視窗變數，來使用建立的視窗
#視窗變數 = pygame.display.set_mode(視窗寬度尺寸:pixels，視窗高度尺寸:pixels)

pygame.display.set_caption("PyGame Sound 功能介紹:按下h鍵發出球撞到的聲音")
#pygame.display.set_caption(視窗標題的內容)

# 畫面填充背景為白色顏色
screen.fill((255, 255, 255))
#視窗變數.fill(RGB變數參數)
pygame.display.update()

hit_sound = pygame.mixer.Sound('./music/ballhit.wav') #載入科學小飛俠主題曲的音樂檔

running = True
while running:
    for event in pygame.event.get():
        # pygame.event.get()是一個滑鼠移動、動作、按下、放開….等所有事件集合
        # event 迴圈找出每一個事件變數
        if event.type == pygame.QUIT:
            # pygame.QUIT就是按到系統結束按鈕
            running = False  # 設定pygame視窗正常運行之控制參數，並設為False
            # 設定pygame視窗正常運行之控制參數，並設為False，會離開迴圈
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]: sys.exit()
    if keys[K_h]:
        hit_sound.play(1)

pygame.quit()  # 離開且關閉pygame視窗


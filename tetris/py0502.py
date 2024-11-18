import sys
import pygame  #匯入PyGame套件
from pygame.locals import *

pygame.init()  #啟動PyGame套件
screen = pygame.display.set_mode((800, 600))
#screen為視窗變數，來使用建立的視窗
#視窗變數 = pygame.display.set_mode(視窗寬度尺寸:pixels，視窗高度尺寸:pixels)

pygame.display.set_caption("PyGame Mixer 功能介紹:播放科學小飛俠主題曲")
#pygame.display.set_caption(視窗標題的內容)

#視窗變數.fill(RGB變數參數)
screen.fill((255, 255, 255))

pygame.mixer.music.load('./music/ninja.mp3') #載入科學小飛俠主題曲的音樂檔
pygame.mixer.music.play(loops=1)        # 無限循環播放音樂

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
    if keys[K_p]:
        pygame.mixer.music.pause()
    if keys[K_c]:
        pygame.mixer.music.unpause()


pygame.quit()  # 離開且關閉pygame視窗


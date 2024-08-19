import sys
import pygame
from pygame.locals import QUIT

# 初始化 pygame 模組
pygame.init()

# 建立視窗畫布，大小為 800x600 像素
window_surface = pygame.display.set_mode((800, 600))

# 設置視窗的標題為 'Hello World:)'
pygame.display.set_caption('Hello World:)')

# 清除畫面並填滿背景色為白色 (RGB: 255, 255, 255)
window_surface.fill((255, 255, 255))

# 宣告一個字體物件，用於顯示文字
# `None` 表示使用預設系統字體，60 是字體大小
head_font = pygame.font.SysFont(None, 60)

# 渲染文字 'Hello World!'，True 表示使用抗鋸齒，文字顏色為黑色 (RGB: 0, 0, 0)
# `render` 方法會回傳一個 surface 物件，這個 surface 上繪製了文字
text_surface = head_font.render('Hello World!', True, (0, 0, 0))

# 將文字 surface 繪製到視窗畫布上，(10, 10) 是文字顯示的位置
window_surface.blit(text_surface, (10, 10))

# 更新螢幕顯示，將所有繪製操作呈現在視窗上
# 若不更新，畫面上元素不會顯示
pygame.display.update()

# 事件迴圈，用於監聽和處理各種事件
while True:
    # 迭代處理所有事件
    for event in pygame.event.get():
        # 如果事件類型是 QUIT，表示使用者關閉了視窗
        if event.type == QUIT:
            # 退出 pygame 模組
            pygame.quit()

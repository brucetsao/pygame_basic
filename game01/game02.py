import sys

import pygame
from pygame.locals import QUIT
# 初始化
pygame.init()
#初始化 Pygame 模組。這是 Pygame 應用程序的標準開場白，確保所有的模組正常運行。
window_surface = pygame.display.set_mode((800, 600))
# 產生一個視窗， 800x600 解析度
#創建一個窗口，尺寸為 800x600 像素。這個窗口就是遊戲的主顯示區域。

# 設置視窗標題為 Bruce Game:)
pygame.display.set_caption('Bruce Game')
# 清除畫面並填滿背景色(r,g,b)
#設置視窗的標題，這會在視窗上方顯示，讓使用者知道這個應用程式的名稱。

window_surface.fill((255, 255, 255))
#將視窗背景設置為白色（RGB 全部為 255）。這相當於清空畫布並用白色填充。

# 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）
pygame.display.update()
#刷新整個視窗以顯示更新後的內容。這一步對於任何圖形顯示都是必需的

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
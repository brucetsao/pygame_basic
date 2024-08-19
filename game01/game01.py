import sys

import pygame

# 初始化 Pygame，這行會初始化所有 Pygame 模組
pygame.init()
#初始化 Pygame 模組。這是 Pygame 應用程序的標準開場白，確保所有的模組正常運行。

# 創建一個視窗物件，大小為 800x600 像素
window_surface = pygame.display.set_mode((800, 600))
#創建一個窗口，尺寸為 800x600 像素。這個窗口就是遊戲的主顯示區域。

# 設置視窗的標題為 'Bruce Game'
pygame.display.set_caption('Bruce Game')
#設置視窗的標題，這會在視窗上方顯示，讓使用者知道這個應用程式的名稱。

# 清除視窗並填滿背景色為白色 (R:255, G:255, B:255)
window_surface.fill((255, 255, 255))
#將視窗背景設置為白色（RGB 全部為 255）。這相當於清空畫布並用白色填充。

# 更新整個顯示屏幕，這是必須的以使所有繪製的元素顯示在螢幕上
pygame.display.update()
#刷新整個視窗以顯示更新後的內容。這一步對於任何圖形顯示都是必需的。

# 主循環，遊戲不會結束，除非程式被強制中止
while True:
    # 這裡的 `a=1` 並沒有實際用途，只是保持循環不斷進行
    a = 1
    #這是遊戲的主循環，會持續執行以保持應用程式運行。在這段程式中，沒有事件處理或遊戲邏輯，只有一個空循環
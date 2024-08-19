import sys, time    #匯入系統操作和時間處理模組。
import random   #匯入隨機數字生成模組。

import pygame   #匯入 pygame 模組，用於遊戲開發。
from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT
#從 pygame.locals 模組中匯入常量和事件類型。

#設置窗口的寬度、高度、背景顏色、蚊子圖片的寬度和高度、幀率等參數
# 設置窗口的寬度和高度
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
# 設置背景顏色為白色 (RGB: 255, 255, 255)
WHITE = (255, 255, 255)
# 蚊子圖片的寬度和高度
IMAGEWIDTH = 300
IMAGEHEIGHT = 200
# 每秒幀數
FPS = 60

#生成保證蚊子完全顯示在窗口內的隨機位置
def get_random_position(widow_width, window_height, image_width, image_height):
    """
    生成一個隨機位置，保證蚊子完全顯示在窗口內部
    :param widow_width: 窗口的寬度
    :param window_height: 窗口的高度
    :param image_width: 蚊子圖片的寬度
    :param image_height: 蚊子圖片的高度
    :return: 隨機生成的 x, y 位置
    """
    random_x = random.randint(image_width, widow_width - image_width)
    random_y = random.randint(image_height, window_height - image_height)

    return random_x, random_y

#蚊子的類別，繼承自 pygame 的 Sprite 類別，用於顯示蚊子圖片並管理其位置
class Mosquito(pygame.sprite.Sprite):
    """
    蚊子的類別，繼承自 pygame 的 Sprite 類別
    """

    #蚊子對象的初始化方法，包括載入圖片、設置位置等。
    def __init__(self, width, height, random_x, random_y, widow_width, window_height):
        """
        初始化蚊子對象
        :param width: 蚊子的寬度
        :param height: 蚊子的高度
        :param random_x: 隨機生成的 x 位置
        :param random_y: 隨機生成的 y 位置
        :param widow_width: 窗口的寬度
        :param window_height: 窗口的高度
        """
        super().__init__()
        # 設置蚊子的圖片（重生狀態）
        self.relive()
        # 將圖片縮放到指定的寬度和高度
        self.image = pygame.transform.scale(self.raw_image, (width, height))
        # 獲取圖片的矩形區域
        self.rect = self.image.get_rect()
        # 設置圖片的位置
        self.rect.topleft = (random_x, random_y)
        self.width = width
        self.height = height
        self.widow_width = widow_width
        self.window_height = window_height

    def dead(self): #設置蚊子為死亡狀態，載入死亡圖片
        """
        設置蚊子為死亡狀態，載入死亡圖片
        """
        self.raw_image = pygame.image.load('mosquitodead.png').convert_alpha()

    def relive(self):   #設置蚊子為生存狀態，載入正常圖片。
        """
        設置蚊子為生存狀態，載入正常圖片
        """
        self.raw_image = pygame.image.load('mosquito.png').convert_alpha()
        #設置蚊子為生存狀態，載入正常圖片。

def main():
    """
    遊戲的主函數
    """
    pygame.init()

    # 創建窗口畫布
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    #創建遊戲窗口，大小為 800x600 像素。
    pygame.display.set_caption('Mosquito War')
    #設置窗口標題為 'Mosquito War'。

    #獲取蚊子的隨機位置。
    # 獲取蚊子的隨機位置
    random_x, random_y = get_random_position(WINDOW_WIDTH, WINDOW_HEIGHT, IMAGEWIDTH, IMAGEHEIGHT)
    # 創建蚊子對象
    mosquito = Mosquito(IMAGEWIDTH, IMAGEHEIGHT, random_x, random_y, WINDOW_WIDTH, WINDOW_HEIGHT)
    #創建蚊子對象。

    # 設置一個定時事件，用於重新生成蚊子
    reload_mosquito_event = USEREVENT + 1   #設置自定義事件 ID，用於重新生成蚊子
    pygame.time.set_timer(reload_mosquito_event, 300)  # 每300毫秒觸發一次事件
    #設置定時器，每 300 毫秒觸發一次重新生成蚊子的事件。


    points = 0  # 初始分數，初始化分數為 0。
    # 創建字體物件，用於顯示分數和打中提示
    my_font = pygame.font.SysFont(None, 30) #創建字體物件，用於顯示分數。
    my_hit_font = pygame.font.SysFont(None, 40) #創建字體物件，用於顯示打中提示文字。
    hit_text_surface = None #初始化打中提示文字為 None
    main_clock = pygame.time.Clock()    #創建時鐘對象，用於控制遊戲循環的幀率。

    while True: #遊戲主循環，不斷檢測事件並更新畫面。
        # 事件處理循環
        for event in pygame.event.get():    #迭代事件，處理窗口關閉、鼠標點擊等。
            if event.type == QUIT:
                # 當用戶關閉視窗時退出遊戲，若事件類型為 QUIT，則退出遊戲。
                pygame.quit()
                sys.exit()
            elif event.type == reload_mosquito_event:   #若事件類型為自定義的重新生成蚊子事件，則重新生成蚊子。
                # 當觸發定時事件時，重新生成蚊子
                mosquito.kill()  # 刪除當前蚊子
                # 獲取新的隨機位置
                random_x, random_y = get_random_position(WINDOW_WIDTH, WINDOW_HEIGHT, IMAGEWIDTH, IMAGEHEIGHT)
                # 創建新的蚊子對象
                mosquito = Mosquito(IMAGEWIDTH, IMAGEHEIGHT, random_x, random_y, WINDOW_WIDTH, WINDOW_HEIGHT)
            elif event.type == MOUSEBUTTONDOWN: #若事件類型為鼠標點擊，則檢查是否點擊到蚊子，並更新分數。
                # 當使用者點擊鼠標時檢查是否點擊到蚊子
                if random_x < pygame.mouse.get_pos()[0] < random_x + IMAGEWIDTH and random_y < pygame.mouse.get_pos()[1] < random_y + IMAGEHEIGHT:
                    # 如果點擊到蚊子，將其設置為死亡狀態
                    mosquito.dead()
                    mosquito.update()
                    # 獲取新的隨機位置
                    random_x, random_y = get_random_position(WINDOW_WIDTH, WINDOW_HEIGHT, IMAGEWIDTH, IMAGEHEIGHT)
                    # 創建新的蚊子對象
                    mosquito = Mosquito(IMAGEWIDTH, IMAGEHEIGHT, random_x, random_y, WINDOW_WIDTH, WINDOW_HEIGHT)
                    # 顯示打中提示文字
                    hit_text_surface = my_hit_font.render('Hit!!', True, (0, 0, 0))
                    points += 5  # 增加分數
                    mosquito.kill()

        # 填充背景顏色為白色
        window_surface.fill(WHITE)

        # 顯示分數
        text_surface = my_font.render('Points: {}'.format(points), True, (0, 0, 0))
        # 在窗口上繪製蚊子和分數
        window_surface.blit(mosquito.image, mosquito.rect)
        #在窗口上繪製蚊子圖片。
        window_surface.blit(text_surface, (10, 0))
        #在窗口上繪製分數文字。

        # 顯示打中提示文字
        if hit_text_surface:    #若有打中提示文字，顯示它並重置為 None。
            window_surface.blit(hit_text_surface, (10, 10))
            hit_text_surface = None

        # 更新顯示
        pygame.display.update() #更新顯示窗口的內容。
        # 控制遊戲循環的幀率
        main_clock.tick(FPS)    #控制遊戲循環的幀率為 60 FPS。

# 程式入口點
if __name__ == '__main__':
    main()  #當此模組作為主程序執行時，調用 main() 函數開始遊戲。

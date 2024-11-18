import pygame   #匯入PyGame套件
from pygame.math import Vector2     #向量的運算套件


class MySprite(pygame.sprite.Sprite):   #繼承pygame.sprite.Sprite類別
    def __init__(self): #類別初始化程序
        pygame.sprite.Sprite.__init__(self) #執行母類別初始化程序
        self.master_image = None  # 精靈的主序列圖（包含多個動畫幀）
        self.image = None  # 當前顯示的幀圖（Surface 對象）
        self.rect = None  # 當前幀圖的矩形區域（Rect 對象）
        self.topleft = 0, 0  # 當前幀圖的左上頂點坐標
        self.area = 0  # 當前顯示的幀圖序號
        self.area_width = 1  # 單個幀圖的寬度
        self.area_height = 1  # 單個幀圖的高度
        self.first_area = 0  # 動畫幀圖的起始區域
        self.last_area = 0  # 動畫幀圖的終止區域
        self.columns = 1  # 每行的幀圖數（即列數）
        self.old_area = -1  # 上一次繪製的幀圖序號
        self.last_time = 0  # 上一次幀圖繪製的時間
        self.is_move = False  # 移動標識（是否在移動）
        self.vel = Vector2(0, 0)  # 移動速度（使用二維向量）

    def _get_dir(self):
        #回傳(動畫幀圖的起始區域,動畫幀圖的終止區域)
        return (self.first_area, self.last_area)

    def _set_dir(self, direction):
        self.first_area = direction * self.columns  # 計算起始幀的序號
        self.last_area = self.first_area + self.columns - 1 #算出後面RECT的位置區域，計算終止幀的序號

    # 通過設置動畫方向來控制幀圖的區間
    direction = property(_get_dir, _set_dir)

    def load_img(self, filename, width, height, columns):
        """加載序列（精靈）圖"""
        self.master_image = pygame.image.load(filename).convert_alpha()  # 加載並處理圖像
        # 將整個精靈序列圖載入
        self.area_width = width  # 設置單個幀圖的寬度
        self.area_height = height  # 設置單個幀圖的高度
        self.rect = pygame.Rect(0, 0, width, height)  # 定義最左上角幀圖的矩形區域
        self.columns = columns  # 設置幀圖的列數
        rect = self.master_image.get_rect()
        self.last_area = (rect.width // width) - 1  # 計算動畫的最後一幀序號

    def update(self, current_time, rate=20):
        """更新動畫幀圖"""
        if not self.is_move:
            # 如果沒有移動，使用默認的幀圖
            self.area = self.first_area = self.last_area
            self.vel = (0, 0)  # 停止移動

        # 控制幀圖的更新速率
        if current_time > self.last_time + rate:
            self.area += 1  # 更新到下一幀
            # 如果超出動畫的幀區間，重置為起始幀
            if self.area > self.last_area:
                self.area = self.first_area
            if self.area < self.first_area:
                self.area = self.first_area
            self.last_time = current_time  # 更新上一次更新的時間

        # 僅在幀圖編號變化時才更新圖像
        if self.area != self.old_area:
            area_x = (self.area % self.columns) * self.area_width  # 計算當前幀的 X 位置
            area_y = (self.area // self.columns) * self.area_height  # 計算當前幀的 Y 位置
            rect = pygame.Rect(area_x, area_y, self.area_width, self.area_height)  # 定義幀圖的矩形區域
            # 從精靈序列圖中裁切當前幀圖的子區域
            try:
                self.image = self.master_image.subsurface(rect)  # 獲取當前幀圖的子圖
            except Exception as e:  # 處理裁切錯誤的例外情況
                print(e + " \n圖片裁剪超出範圍........")
            self.old_area = self.area  # 記錄當前幀圖的編號

    def draw(self, screen):
        """在螢幕上繪製當前幀圖"""
        # 將當前幀圖繪製到螢幕的當前位置
        screen.blit(self.image, self.rect)

    def move(self):
        """根據速度移動幀圖的位置"""
        self.rect.move_ip(self.vel)  # 移動矩形區域的位置
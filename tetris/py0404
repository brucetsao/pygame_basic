import pygame  #匯入PyGame套件
import math

pygame.init()  #啟動PyGame套件
screen = pygame.display.set_mode((800, 600))
#screen為視窗變數，來使用建立的視窗
#視窗變數 = pygame.display.set_mode(視窗寬度尺寸:pixels，視窗高度尺寸:pixels)

pygame.display.set_caption("PyGame Sprite 功能介紹:產生一個球，全方位移動")
#pygame.display.set_caption(視窗標題的內容)

screen.fill((0, 0, 0))


#視窗變數.fill(RGB變數參數)

# 創建精靈類別
class Player(pygame.sprite.Sprite):
    _xpos = 0  #精靈類別:Player的x座標
    _ypos = 0  #精靈類別:Player的y座標
    _dirXway = 1  #精靈類別:Player的x座標的移動方向，1=向右，-1=向左
    _dirYway = 1  #精靈類別:Player的y座標的移動方向，1=向下，-1=向上
    _movedistance = 5  #精靈類別:Player的x座標的移動間距
    _scr = screen

    def __init__(self, image_path, x, y, scr):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image = pygame.image.load(image_path)#載入圖片
        self.image.convert_alpha()	#改變alpha值
        self.rect = self.image.get_rect()	#取得圖形大小位置
        self._xpos = x	#設定起始X座標位置
        self._ypos = y	#設定起始Y座標位置
        self.rect.x = self._xpos  #設定精靈類別位置為物件_xpos
        self.rect.y = self._ypos  #設定精靈類別位置為物件_ypos
        self.rect.topleft = (self._xpos, self._ypos)  # 設定初始位置
        self._scr = scr

    def update(self):
        # 更新精靈的位置，這裡我們讓它向右移動
        if self._dirXway == 1:	#如果向右
            if self._dirYway == 1:	#如果向下
                self._xpos += self._movedistance    #向右移動
                self._ypos += self._movedistance    #向下移動
                self.rect.x = self._xpos  #設定精靈類別位置為物件xpos
                self.rect.y = self._ypos  #設定精靈類別位置為物件ypos
            else:	#如果向上
                self._xpos += self._movedistance    #向右移動
                self._ypos -= self._movedistance    #向上移動
                self.rect.x = self._xpos  #設定精靈類別位置為物件xpos
                self.rect.y = self._ypos  #設定精靈類別位置為物件ypos
        else:	#如果向左
            if self._dirYway == 1:	#如果向下
                self._xpos -= self._movedistance    #向左移動
                self._ypos += self._movedistance    #向下移動
                self.rect.x = self._xpos  #設定精靈類別位置為物件xpos
                self.rect.y = self._ypos  #設定精靈類別位置為物件ypos
            else:	#如果向下
                self._xpos -= self._movedistance    #向左移動
                self._ypos -= self._movedistance    #向上移動
                self.rect.x = self._xpos  #設定精靈類別位置為物件xpos
                self.rect.y = self._ypos  #設定精靈類別位置為物件ypos

        if (self.rect.x + self.rect.width) > self._scr.get_width():#判斷右邊界
            self._dirXway = -1  #轉向左邊
        if self.rect.x < 1: #判斷左邊界
            self._dirXway = 1   #轉向右邊
        if (self.rect.y + self.rect.height) > self._scr.get_height():   #判斷下邊界
            self._dirYway = -1  #轉向上邊
        if self.rect.y < 1: #判斷上邊界
            self._dirYway = 1    #轉向下邊

# 創建一個玩家精靈
player = Player('./images/ball.png', 0, 0,screen)

# 創建精靈群組
all_sprites = pygame.sprite.Group()

# 將創建的玩家精靈並加入群組
all_sprites.add(player)

# 設定遊戲主循環
clock = pygame.time.Clock()


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

    # 畫面填充背景顏色
    screen.fill((255, 255, 255))

    # 繪製所有精靈
    all_sprites.draw(screen)

    # 更新顯示
    pygame.display.flip()

    # 控制幀率
    clock.tick(30)

pygame.quit()  # 離開且關閉pygame視窗

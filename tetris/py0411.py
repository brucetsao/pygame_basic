import pygame  #匯入PyGame套件
import math


pygame.init()  #啟動PyGame套件
screen = pygame.display.set_mode((800, 600))
#screen為視窗變數，來使用建立的視窗
#視窗變數 = pygame.display.set_mode(視窗寬度尺寸:pixels，視窗高度尺寸:pixels)

pygame.display.set_caption("PyGame Sprite 功能介紹:畫出一個來回移動矩形Sprite")
#pygame.display.set_caption(視窗標題的內容)

screen.fill((0, 0, 0))
#視窗變數.fill(RGB變數參數)

# 創建精靈類別
class Player(pygame.sprite.Sprite):
    _xpos=0 #精靈類別:Player的x座標
    _ypos=0 #精靈類別:Player的y座標
    _dirXway = 1  #精靈類別:Player的x座標的移動方向，1=向右，-1=向左
    _movedistance = 5 #精靈類別:Player的x座標的移動間距
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.convert_alpha()
        self.image.set_alpha(255)
        self.image.fill((0, 128, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        self.rect.x= self._xpos #設定精靈類別位置為物件xpos
        self.rect.y= self._ypos #設定精靈類別位置為物件ypos

    def update(self):
        # 更新精靈的位置，這裡我們讓它向右移動
        if self._dirXway ==1 :
            self._xpos += self._movedistance
            self.rect.x= self._xpos #設定精靈類別位置為物件xpos
            if (self.rect.x+self.rect.width) > screen.get_width() :
                self._dirXway = -1
        else:
            self._xpos -= self._movedistance
            self.rect.x= self._xpos #設定精靈類別位置為物件xpos
            if self.rect.x < 1 :
                self._dirXway = 1

# 創建精靈群組
all_sprites = pygame.sprite.Group()

# 創建一個玩家精靈並加入群組
player = Player()
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

import pygame  #匯入PyGame套件
import math
from MySprite import *
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

# 創建精靈類別
class Player(MySprite):
    _xpos=0 #精靈類別:Player的x座標
    _ypos=0 #精靈類別:Player的y座標
    _dirXway = 1  #精靈類別:Player的x座標的移動方向，1=向右，-1=向左
    _movedistance = 5 #精靈類別:Player的x座標的移動間距
    def __init__(self):
        super().__init__()
        # self.image = pygame.Surface((50, 50))
        # #self.image = pygame.image.load('./images/ball.png')
        # self.image.convert_alpha()
        #self.image.set_alpha(255)
        #self.image.fill((0, 128, 255))
        #self.rect = self.image.get_rect()
        # self.rect.center = (100, 100)
        # self.rect.x= self._xpos #設定精靈類別位置為物件xpos
        # self.rect.y= self._ypos #設定精靈類別位置為物件ypos



# 創建一個玩家精靈並加入群組
player = Player()
player.load_img("./images/PacmanAni.png", 100, 100, 1)
# all_sprites.add(player)
clock = pygame.time.Clock()

# 創建精靈群組
all_sprites = pygame.sprite.Group()

# 創建一個玩家精靈並加入群組

all_sprites.add(player)

# 設定遊戲主循環
running = True
while running:
    screen.fill((255, 255, 255))
    ticks = pygame.time.get_ticks()
    if pygame.event.wait().type in [QUIT]: exit()
    keys = pygame.key.get_pressed()   # 键盘轮询
    if keys[pygame.K_ESCAPE]: exit()
    dir = [keys[K_DOWN], keys[K_LEFT], keys[K_RIGHT], keys[K_UP], (0, 4), (-4, 0), (4, 0), (0, -4)]
    for k, v in enumerate(dir[0:4]):  # 判断移动方向
        if v:
            player.direction = k
            player.vel = dir[k + 4]
            player.is_move = v
            break
    else:                             # 无移动
        player.is_move = False
    player.update(ticks, 90)    # 更新
    player.draw(screen)         # 绘制
    player.move()               # 移动
    pygame.display.update()
    clock.tick(FPS)

import pygame   #匯入PyGame套件
import time
pygame.init()  #啟動PyGame套件
screen = pygame.display.set_mode((800,600))
#screen為視窗變數，來使用建立的視窗
#視窗變數 = pygame.display.set_mode(視窗寬度尺寸:pixels，視窗高度尺寸:pixels)

pygame.display.set_caption("PyGame繪圖功能介紹:矩形功能(連續縮小五個矩形寬)")
#pygame.display.set_caption(視窗標題的內容)

screen.fill((0,0,0))
#視窗變數.fill(RGB變數參數)

bg = pygame.Surface(screen.get_size())
#建立畫布變數(與視窗一樣大小) = pygame.Surface(screen.get_size())
#與視窗一樣大小 ==>pygame.Surface(screen.get_size()

bg = bg.convert()
#畫布變數 = 畫布變數.convert()
n=5
#共劃出n=5個矩形
xl = int(screen.get_width()/(n*2))
#寬度縮小漸距為總寬度/(n=5個矩形 *對稱兩倍)
yl = int(screen.get_height()/(n*2))
#高度縮小漸距為總高度/(n=5個矩形 *對稱兩倍)

for m in range(0,n):
    print(m)
    print("POS :(%d,%d)" %  (0+xl*m+1, 0+yl*m+1))#列印繪出(X,Y)座標值
    print("Width :(%d,%d)" %  (screen.get_width()-m*2*xl-1, screen.get_height()-m*2*yl-1))#列印繪出(WIDTH,HEIGHT)矩形大小值
    pygame.draw.rect(bg, (0,0,255), [0+xl*m+1, 0+yl*m+1, screen.get_width()-m*2*xl-1, screen.get_height()-m*2*yl-1], 1)
    # 座標點X: 0 + m * 2(雙邊縮小) * xl(寬度縮小值) + 1(向右移一點)
    # 座標點Y: 0 + m * 2(雙邊縮小) * yl(高度縮小值) + 1(向下移一點)
    # 寬度W: screen.get_width():總寬度 - m * 2(雙邊縮小) * xl(寬度縮小值) + -1(向左移一點)
    # 高度H: screen.get_height:總高度 - m * 2(雙邊縮小) * yl(高度縮小值) + -1(向上移一點)

    screen.blit(bg, (0,0))
    #將bg畫布繪製在視窗上，就是把打X圖片畫到視窗
    pygame.display.update()
    #視窗變數.display.update()

running = True
#設定pygame視窗正常運行之控制參數，並設為True不會離開迴圈
while running:  #用running來控制pygame視窗使否正常運行
    for event in pygame.event.get():
    # pygame.event.get()是一個滑鼠移動、動作、按下、放開….等所有事件集合
        #event 迴圈找出每一個事件變數
        if event.type == pygame.QUIT:
            # pygame.QUIT就是按到系統結束按鈕
            running = False #設定pygame視窗正常運行之控制參數，並設為False
            #設定pygame視窗正常運行之控制參數，並設為False，會離開迴圈
pygame.quit()   #離開且關閉pygame視窗


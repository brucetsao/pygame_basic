import pygame   #匯入PyGame套件
import math
pygame.init()  #啟動PyGame套件
screen = pygame.display.set_mode((800,600))
#screen為視窗變數，來使用建立的視窗
#視窗變數 = pygame.display.set_mode(視窗寬度尺寸:pixels，視窗高度尺寸:pixels)

pygame.display.set_caption("PyGame繪圖功能介紹:橢圓形功能")
#pygame.display.set_caption(視窗標題的內容)

screen.fill((0,0,0))
#視窗變數.fill(RGB變數參數)

bg = pygame.Surface(screen.get_size())
#建立畫布變數(與視窗一樣大小) = pygame.Surface(screen.get_size())
#與視窗一樣大小 ==>pygame.Surface(screen.get_size()

bg = bg.convert()
#畫布變數 = 畫布變數.convert()
w= screen.get_width()#螢幕寬度
h= screen.get_height()#螢幕高度
x= int(w/2)#取中心位置
y= int(h/2)#取中心位置
#橢圓形圓心(x,y) = (int(screen.get_width()/2),int(screen.get_height()/2))

wr= int(screen.get_width()/2)#wr橢圓形寬度半徑
hr= int(screen.get_height()/2)#hr橢圓形高度半徑
#wr橢圓形寬度半徑
#hr橢圓形高度半徑
# 左上角x坐標=橢圓形圓心x座標-wr橢圓形寬度半徑 or 左上角X座標+(向右多1點 pixel)
# 左上角y坐標=橢圓形圓心y座標+hr橢圓形高度半徑 or 左上角Y座標+(向下多1點 pixel)
# X軸長度=螢幕寬度w -(左右縮1點 pixel)
# Y軸長度螢幕高度h -(左右縮1點 pixel)

pygame.draw.ellipse(bg, (0,0,255), (1,1,w-2,h-2), 1)
# 左上角x坐標=橢圓形圓心x座標-wr橢圓形寬度半徑 or 左上角X座標+(向右多1點 pixel)
# 左上角y坐標=橢圓形圓心y座標+hr橢圓形高度半徑 or 左上角Y座標+(向下多1點 pixel)


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
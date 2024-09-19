import pygame  #匯入PyGame套件
import math

pygame.init()  #啟動PyGame套件
screen = pygame.display.set_mode((800, 600))
#screen為視窗變數，來使用建立的視窗
#視窗變數 = pygame.display.set_mode(視窗寬度尺寸:pixels，視窗高度尺寸:pixels)

pygame.display.set_caption("PyGame繪圖功能介紹:畫出正N邊形之多邊形於畫面上")
#pygame.display.set_caption(視窗標題的內容)

screen.fill((0, 0, 0))
#視窗變數.fill(RGB變數參數)

bg = pygame.Surface(screen.get_size())
#建立畫布變數(與視窗一樣大小) = pygame.Surface(screen.get_size())
#與視窗一樣大小 ==>pygame.Surface(screen.get_size()

bg = bg.convert()
#畫布變數 = 畫布變數.convert()

pi = 3.14#圓周率
point=[]    #多邊形端短(X,Y)的陣列

w = screen.get_width()  #螢幕寬度
h = screen.get_height()  #螢幕高度
x= int(w/2) #取多邊形中心點於螢幕寬度中間
y = int(h/2)    #取多邊形中心點於螢幕高度中間

print("Polygon Center:(%d,%d)" % (x, y))    #印出正N邊形的中心點
r = min(int(w/2),int(h/2))-2  #計算出#印出正N邊形的中心點到任一端點的長度
#取多邊形中心點之外接圓的接點距離，以長寬一半較短的

print("Polygon radius:",y)


n=6 #正多邊形之邊數值
for theta in range(0,n):#迴圈產生正N邊形的美一端點的座標
    xx = x + int(math.cos((2*pi)/n*theta) * r)  #產生正N邊形的美一端點的座標:X
    yy = y + int(math.sin((2*pi)*(theta/n)) * r)    #產生正N邊形的每一端點的座標:Y
    point.append((xx, yy)) # N邊形第N個端點座標點
    print("Point:(%d,%d)" % (xx,yy))    #印出正N邊形的每一端點的座標:(X,Y)
pygame.draw.polygon(bg, (0, 0, 255), point, 1)  #畫出正N邊形之多邊形於畫面上

screen.blit(bg, (0, 0))
# 將bg畫布繪製在視窗上，就是把打X圖片畫到視窗
pygame.display.update()
# 視窗變數.display.update()

running = True
# 設定pygame視窗正常運行之控制參數，並設為True不會離開迴圈
while running:  # 用running來控制pygame視窗使否正常運行
    for event in pygame.event.get():
        # pygame.event.get()是一個滑鼠移動、動作、按下、放開….等所有事件集合
        # event 迴圈找出每一個事件變數
        if event.type == pygame.QUIT:
            # pygame.QUIT就是按到系統結束按鈕
            running = False  # 設定pygame視窗正常運行之控制參數，並設為False
            # 設定pygame視窗正常運行之控制參數，並設為False，會離開迴圈
pygame.quit()  # 離開且關閉pygame視窗

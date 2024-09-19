import pygame   #匯入PyGame套件
pygame.init()  #啟動PyGame套件
screen = pygame.display.set_mode((800,600))
#screen為視窗變數，來使用建立的視窗
#視窗變數 = pygame.display.set_mode(視窗寬度尺寸:pixels，視窗高度尺寸:pixels)

pygame.display.set_caption("PyGame繪圖功能介紹")
#pygame.display.set_caption(視窗標題的內容)

screen.fill((0,0,0))
#視窗變數.fill(RGB變數參數)

bg = pygame.Surface(screen.get_size())
#建立畫布變數(與視窗一樣大小) = pygame.Surface(screen.get_size())
#與視窗一樣大小 ==>pygame.Surface(screen.get_size()

bg = bg.convert()
#畫布變數 = 畫布變數.convert()

for y in range(0,int(screen.get_height()/50)):
    pygame.draw.line(bg,(0,0,255),(0,y*50),(screen.get_width(),y*50),1)
    #(0,第n條線 (n-1) * 50)為左邊座標,(screen.get_width(),第n條線 (n-1) * 50)為右邊座標

for x in range(0,int(screen.get_width()/50)):
    pygame.draw.line(bg,(0,0,255),(x*50,0),(x*50,screen.get_width()),1)
    #(x*50,第n條線 (n-1) * 50)為左邊座標,(screen.get_width(),第n條線 (n-1) * 50)為右邊座標

#pygame.draw.line(bg,(0,0,255),(0,screen.get_height()),(screen.get_width(),0),0)
#(0,screen.get_height()為左下角座標,screen.get_width(),0為右上角座標

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


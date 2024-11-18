import pygame   #匯入PyGame套件
pygame.init()  #啟動PyGame套件
screen = pygame.display.set_mode((800,600))
#screen為視窗變數，來使用建立的視窗
#視窗變數 = pygame.display.set_mode(視窗寬度尺寸:pixels，視窗高度尺寸:pixels)

pygame.display.set_caption("曹建國老師第一個繪圖視窗標題")
#pygame.display.set_caption(視窗標題的內容)
print("Current font amount is %d" % len(pygame.font.get_fonts()))
#印出目前系統字型總個數
print("----------------------------------------------------------------")
for fontname in pygame.font.get_fonts():   #取得目前系統擁有的字型
    #從取得目前系統擁有的字型 一一取出，存在fontname變數內
    print(fontname) #列印取到的字型

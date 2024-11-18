import pygame   #匯入PyGame套件
from pygame.math import Vector2     #向量的運算套件


# 創建精靈類別
class Player(pygame.sprite.Sprite):
    _xpos = 0  #精靈類別:Player的x座標
    _ypos = 0  #精靈類別:Player的y座標
    _dirXway = 1  #精靈類別:Player的x座標的移動方向，1=向右，-1=向左
    _dirYway = 1  #精靈類別:Player的y座標的移動方向，1=向下，-1=向上
    _movedistance = 5  #精靈類別:Player的x座標的移動間距
    _scr = screen #精靈物件所處的畫面參考繪圖之Surface

    def __init__(self, image_path,nn ,x, y, scr):
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
        self._scr = scr	#類別內參考繪圖之Surface
        self.__move=self._movedistance	#外部可以讀寫的移動距離屬性
        self.__Name = nn

        @property  # 設定下面為屬性的讀取
        def move(self):
            return self.__move  # 回傳__move屬性內容

        @move.setter  # 設定下面為屬性的寫入
        def move(self, cc):
            self.__move = cc  ##設定__move屬性內容
            self._movedistance = self.__move
        # 將__move屬性設定給實際移動的變數_movedistance

        @property  # 設定下面為屬性的讀取
        def Name(self):
            return self.__Name  # 回傳__Name屬性內容

        @move.setter  # 設定下面為屬性的寫入
        def Name(self, cc):
            self.__Name = cc  ##設定__Name屬性內容

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

    def bounce(self):   # 反彈，就是_dirXway與_dirYway反向(*-1)
        # 更新精靈的位置，這裡我們讓它向右移動
        self._dirXway = self._dirXway * (-1)    #該物件X軸反向
        self._dirYway = self._dirYway * (-1)    #該物件Y軸反向
        print(self.__Name,"is collided")


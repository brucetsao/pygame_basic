import pygame   #匯入PyGame套件
from pygame.math import Vector2     #向量的運算套件


# 創建精靈類別
class Player(pygame.sprite.Sprite):
    _xpos = 0  #精靈類別:Player的x座標
    _ypos = 0  #精靈類別:Player的y座標
    _scr = pygame.rect  #設定參考視窗pygame的畫布，預設為pygame.rect

    def __init__(self, image_path,nn ,x, y, scr):#類別的init()建構式
        super().__init__() #執行pygame.sprite.Sprite母類別的init()建構式
        self.image = pygame.Surface((50, 50))   #預設精靈圖片畫布
        self.image = pygame.image.load(image_path)#載入圖片
        self.image.convert_alpha()	#改變alpha值
        self.rect = self.image.get_rect()	#取得圖形大小位置
        self.rect.size = self.image.get_size() #設定精靈尺寸為載入圖片大小的尺寸
        self._xpos = x	#設定起始X座標位置
        self._ypos = y	#設定起始Y座標位置
        self.rect.x = self._xpos  #設定精靈類別位置為物件_xpos
        self.rect.y = self._ypos  #設定精靈類別位置為物件_ypos
        self.rect.topleft = (self._xpos, self._ypos)  # 設定精靈物件初始位置
        self._scr = scr	#精靈類別內參考繪圖之Surface(畫布)
        self.XDistance = self.rect.width #設定X軸移動距離，並設定內容為取得精靈大小之 寬度
        self.YDistance = self.rect.height  #設定Y軸移動距離，並設定內容為取得精靈大小之 高度
        self.Name = nn    #設定精靈物件名稱為傳入精靈名稱之內容
        print(self.XDistance,self.YDistance)    #列印出X軸移動距離與Y軸移動距離

    @property  # 設定下面為XMove屬性的讀取
    def XDistance(self):
        return self.__XDistance  # 回傳__XDistance屬性內容

    @XDistance.setter  # 設定下面為XDistance屬性的寫入
    def XDistance(self, cc):
        self.__XDistance = cc  ##設定__XDistance屬性內容

    # 將__XMove屬性設定給實際移動的變數_XDistance

    @property  # 設定下面為YDistance屬性的讀取
    def YDistance(self):
        return self.__XDistance  # 回傳__YDistance屬性內容

    @YDistance.setter  # 設定下面為屬性的寫入
    def YDistance(self, cc):
        self.__YDistance = cc  ##設定__YDistance屬性內容

    # 將__YMove屬性設定給實際移動的變數_YDistance

    @property  # 設定下面為屬性的讀取
    def Name(self):
        return self.__Name  # 回傳__Name屬性內容

    @Name.setter  # 設定下面為屬性的寫入
    def Name(self, cc):
        self.__Name = cc  ##設定__Name屬性內容

    def update(self):   #更新精靈自動化動作程序
        # 更新精靈的位置，這裡我們讓它向右移動
        pass    #目前不動作

    def Right(self):
        # 更新精靈的位置，這裡我們讓它向右移動
        if (self.rect.x + self.rect.width+self.__XDistance) < self._scr.get_width() :
            self._xpos += self.__XDistance
            self.rect.x = self._xpos  #設定精靈類別位置為物件_xpos
            print("right") #印出移動右方訊息

    def Left(self):
        # 更新精靈的位置，這裡我們讓它向左移動
        if self.rect.x > self.__XDistance :
            self._xpos -= self.__XDistance
            self.rect.x = self._xpos  #設定精靈類別位置為物件_xpos
            print("left") #印出移動左方訊息

    def Down(self):
        # 更新精靈的位置，這裡我們讓它向下移動
        if (self.rect.y + self.rect.height+self.__YDistance) < self._scr.get_height() :
            self._ypos += self.__YDistance
            self.rect.y = self._ypos  #設定精靈類別位置為物件_xpos
            print("down") #印出移動下方訊息

    def Up(self):
        # 更新精靈的位置，這裡我們讓它向上移動
        if self.rect.y > self.__YDistance :
            self._ypos -= self.__YDistance
            self.rect.y = self._ypos  #設定精靈類別位置為物件_xpos
            print("up") #印出移動上方訊息



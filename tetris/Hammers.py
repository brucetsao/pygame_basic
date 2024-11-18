import pygame   #匯入PyGame套件
from pygame.math import Vector2     #向量的運算套件


# 創建精靈類別
class Player(pygame.sprite.Sprite):
    _xpos = 0  #精靈類別:Player的x座標
    _ypos = 0  #精靈類別:Player的y座標
    _scr = pygame.rect  #設定參考視窗pygame的畫布
    _count = 1  #目前有精靈腳色圖片張數
    _images = []    #精靈腳色圖片的陣列
    __imagnumber=1  #目前取用第X張精靈腳色圖片
    __Visible = False   #是否顯示(暫無使用)
    def __init__(self,image_path, nn ,x, y, scr):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self._images.append( pygame.image.load(image_path))
        self.image = self._images[0]  # 載入圖片
        self.image.convert_alpha()	#改變alpha值
        self.rect = self.image.get_rect()	#取得圖形大小位置
        self.rect.size = self.image.get_size() #設定精靈尺寸為載入圖片大小的尺寸
        self._xpos = x	#設定起始X座標位置
        self._ypos = y	#設定起始Y座標位置
        self.rect.x = self._xpos  #設定精靈類別位置為物件_xpos
        self.rect.y = self._ypos  #設定精靈類別位置為物件_ypos
        self.rect.topleft = (self._xpos, self._ypos)  # 設定精靈物件初始位置
        self._scr = scr	#精靈類別內參考繪圖之Surface(畫布)
        self.name = nn    #設定精靈物件名稱為傳入精靈名稱之內容


    def loadimage(self,image_path):  # 更新精靈自動化動作程序
        self._images.append( pygame.image.load(image_path))
        self._count = self._count +1

    @property  # 設定下面為屬性的讀取
    def name(self):
        return self.__name  # 回傳__Name屬性內容

    @name.setter  # 設定下面為屬性的寫入
    def name(self, cc):
        self.__name = cc  ##設定__name屬性內容

    @property  # imagnumber
    def imagnumber(self):
        return self.__imagnumber  # 回傳__imagnumber屬性內容

    @imagnumber.setter  # 設定下面為屬性的寫入
    def imagnumber(self, cc):
        if cc <=  self._count :
            self.__imagnumber = cc  #設定目前顯示第__imagnumber張圖片
            self.image = self._images[self.__imagnumber - 1]  # 載入圖片
            self.image.convert_alpha()  # 改變alpha值
            self.rect = self.image.get_rect()  # 取得圖形大小位置
            self.rect.size = self.image.get_size()  # 設定精靈尺寸為載入圖片大小的尺寸

        else:
            print("超越圖片大小")

    @property  # 設定下面為屬性的讀取
    def Visible(self):
        return self.__Visible  # 回傳__Name屬性內容

    @Visible.setter  # 設定下面為屬性的寫入
    def Visible(self, cc):
        self.__Visible = cc  ##設定__Visible屬性內容

    def update(self):   #更新精靈自動化動作程序
        # 更新精靈的位置
        self.rect.x = self._xpos - self.image.get_width() /2  #設定精靈物件位置為物件_xpos
        self.rect.y = self._ypos - self.image.get_height() /2  #設定精靈物件位置為物件_ypos


    def setPos(self,x,y):
        self._xpos = x	#設定精靈物件起始X座標位置
        self._ypos = y	#設定精靈物件起始Y座標位置
        # self.rect.x = self._xpos - self.image.get_width() /2  #設定精靈類別位置為物件_xpos
        # self.rect.y = self._ypos - self.image.get_height() /2  #設定精靈類別位置為物件_ypos


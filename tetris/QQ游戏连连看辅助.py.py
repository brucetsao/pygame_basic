import win32api
import win32gui
import win32con
from PIL import ImageGrab
import time
import random
from PIL import Image
from collections import Counter
blocks_x=19
blocks_y=11

name='QQ游戏 - 连连看角色版'
hwnd = win32gui.FindWindow(None,name)
if hwnd:
	print("成功找到窗口...")
else:
	print("没有找到窗口，请重试...")
	input("按回车键退出")
	exit()
win32gui.SetForegroundWindow(hwnd,)
time.sleep(0.05)
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
rect=(left+14, top+181,left+603, top+566)
img=ImageGrab.grab().crop(rect)
def shengcheng():
	vaz=[]
	for y in range(blocks_y):
		for x in range(blocks_x):
			quare=img.crop((x * 31, y * 35, (x + 1) * 31, (y + 1) * 35))
			square=quare.crop((8,8,25,28))
			dian=square.getcolors()
			vaz.append(dian)
#生成二维数组
	vaz1=vaz.copy()
	aaa=1
	for va in vaz:	
		ccc=0
		for qa in vaz1:
			if va==qa:
				vaz1[ccc]=aaa
			ccc+=1
		aaa=aaa+1
	xxx=Counter(vaz1)
	xz=max(zip(xxx.values(),xxx.keys()))
	iia=[]
	va11=[]
	for ia in vaz1:
		if ia==xz[1]:
			iia.append(0)
		else:
			iia.append(ia)
		if len(iia)==blocks_x:
			va11.append(iia)
			iia=[]
	return(va11)
def hengx(x,y,x1,y1,va11):
	if y!=y1:
		return False
	if x==x1:
		return False	
	minx=min(x,x1)
	maxx=max(x,x1)
	#判断纵向相邻
	if (maxx-minx)==1:
		return True
	#判断联通
	for i in range(minx+1,maxx):
		if va11[y][i]!=0:
			return False
	return True
#判断纵向
def zongx(x,y,x1,y1,va11):
	if x!=x1:
		return False
	if y==y1:
		return False
	miny=min(y,y1)
	maxy=max(y,y1)
	#判断纵向相邻
	if (maxy-miny)==1:
		return True
	#判断联通
	for i in range(miny+1,maxy):
		if va11[i][x]!=0:
			return False
	return True		
#一个拐角
def guai1(x,y,x1,y1,va11):
	if x==x1 or y==y1:
		return False
	if va11[y][x1]==0:
		if zongx(x1,y,x1,y1,va11) and hengx(x1, y, x, y, va11):
			return True	
	if va11[y1][x]==0:
		if hengx(x,y1,x1,y1,va11) and zongx(x, y1, x, y, va11):
			return True	
	return False
def guai2(x,y,x1,y1,va11):
	vz=[]
	for yy in range(y+1,11):
		if va11[yy][x]==0:
			vz.append((x,yy))
		else:
			break
	for yy in range(y-1,0,-1):
		if va11[yy][x]==0:
			vz.append((x,yy))
		else:
			break
	for xx in range(x+1,19):
		if va11[y][xx]==0:
			vz.append((xx,y))
		else:
			break
	for xx in range(x-1,0,-1):
		if va11[y][xx]==0:
			vz.append((xx,y))
		else:
			break
	if vz==[]:
		return False
	for z in vz:
		if guai1(z[0],z[1],x1,y1,va11) or zongx(z[0],z[1],x1,y1,va11) or hengx(z[0],z[1],x1,y1,va11):
			return True
	return False
def panduan(x,y,x1,y1,va11):
	if zongx(x,y,x1,y1,va11):
		return True
	if hengx(x,y,x1,y1,va11):
		return True
	if guai1(x,y,x1,y1,va11):
		return True
	if guai2(x,y,x1,y1,va11):
		return True
	return False

def dianji(x,y):

	win32api.SetCursorPos((x*31+15+rect[0],y*35+rect[1]+15))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	time.sleep(0.02)#延迟



Q1=0
va11=shengcheng()
for xxxx in range(300):
	for y in range(11):
		for x in range(19):
			if va11[y][x]==0:
				continue
			for y1 in range(11):
				for x1 in range(19):
					if va11[y1][x1]==0:
						continue
					if va11[y][x]==va11[y1][x1] and (x,y)!=(x1,y1):			
						if panduan(x,y,x1,y1,va11):
							#鼠标点击
							dianji(x,y)
							dianji(x1,y1)
							va11[y][x]=0
							va11[y1][x1]=0
	if  va11.count([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])==11:
		print('完成')
		input("按回车键键退出")
		exit()
print("如果未消除完，请保持游戏窗口在最上方并勿与本窗口重叠")
input("按回车键退出")
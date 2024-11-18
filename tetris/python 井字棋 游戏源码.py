from tkinter import *
import time
import tkinter.messagebox

tk = Tk()
tk.title("井字棋")
tk.resizable(0, 0)  # 不能随意改变棋盘大小
tk.wm_attributes("-topmost", 1)  # 画布窗口始终放在最上面
canvas = Canvas(tk, width=800, height=800, bd=0, highlightthickness=0)  # 画布的宽是800,高是800,确保画布没有边框
canvas.pack()  # 让画布按前面的调整大小
tk.update()

redorgreen = 0
colorx = "green"
position = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
overornot = 0

# 画棋盘
lines = [100, 300, 500, 700]
for i in lines:
    canvas.create_line(100, i, 700, i)
    canvas.create_line(i, 100, i, 700)

# canvas.bind('<Button-1>', baction)  # 落子
# print(k)


def action(event):
    global redorgreen, colorx
    global overornot

    if overornot == 1:  # 判断胜负是否已分
        tkinter.messagebox.showinfo("提示", "游戏已结束")
        return
    if (event.x <= 100 or event.x >= 700 or event.y <= 100 or event.y >= 700):  # 判断是否在棋盘内部落子
        tkinter.messagebox.showinfo("提示", "请下在棋盘内")
        return
    if redorgreen == 0:
        redorgreen = 1
        colorx = "red"
    else:
        redorgreen = 0
        colorx = "green"

    a = 100
    for i in range(0, 3):
        for j in range(0, 3):
            if event.x > 100 + i * 200 and event.x < 100 + (i + 1) * 200 and event.y < 100 + (
                    j + 1) * 200 and event.y > 100 + j * 200:
                if position[i][j] == 0:
                    canvas.create_oval(100 + i * 200, 100 + j * 200, 100 + (i + 1) * 200, 100 + (j + 1) * 200,
                                       fill=colorx)
                    if colorx == "red":
                        position[i][j] = 1
                    else:
                        position[i][j] = 2
                else:
                    tkinter.messagebox.showinfo("提示", "请勿重复下子")
                    if redorgreen == 0:
                        redorgreen = 1
                    else:
                        redorgreen = 0
                        return

        if (position[0][0] == position[0][1] == position[0][2] == 1) \
            or (position[1][0] == position[1][1] == position[1][2] == 1)\
            or (position[2][0] == position[2][1] == position[2][2] == 1)\
            or (position[0][0] == position[1][0] == position[2][0] == 1)\
            or (position[0][1] == position[1][1] == position[2][1] == 1)\
            or (position[0][2] == position[1][2] == position[2][2] == 1)\
            or (position[0][0] == position[1][1] == position[2][2] == 1)\
            or (position[0][2] == position[1][1] == position[2][0] == 1):
            tkinter.messagebox.showinfo("提示", "游戏结束,红方胜利")
            tk.title("井字棋-游戏结束红方胜利")
            overornot = 1

        if (position[0][0] == position[0][1] == position[0][2] == 2) \
            or (position[1][0] == position[1][1] == position[1][2] == 2)\
            or (position[2][0] == position[2][1] == position[2][2] == 2)\
            or (position[0][0] == position[1][0] == position[2][0] == 2)\
            or (position[0][1] == position[1][1] == position[2][1] == 2)\
            or (position[0][2] == position[1][2] == position[2][2] == 2)\
            or (position[0][0] == position[1][1] == position[2][2] == 2)\
            or (position[0][2] == position[1][1] == position[2][0] == 2):
            tkinter.messagebox.showinfo("提示", "游戏结束,绿方胜利")
            tk.title("井字棋-游戏结束绿方胜利")
            overornot = 1

canvas.bind('<Button-1>', action)  # 落子
# print(k)
while 1:
    tk.update_idletasks()
    tk.update()  # 动画初始化
    time.sleep(0.01)  # 游戏刷新间隔

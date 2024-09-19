1# 17.	案例:石头剪刀布
# 2：石头剪子布的游戏是人机大战 机器随机给出  人按照需求填写

import random

i = 0  # 统计一共比较的次数
u = 0  # 统计自己赢的次数
j = 0  # 统计机器人赢的次数
while True:
    play = ["石头", "剪刀", "布"]
    num = int(input("请输入对应的数字：1：石头，2：剪刀，3：布\n到第%i局了！人%i\t机%i\n" % (i + 1, u, j)))
    p = random.choice(play)

    if num == 1:
        i += 1
        if p == "石头":
            print("平")
            u += 0
        elif p == "剪刀":
            print("赢")
            u += 1
        elif p == "布":
            print("输")
            j += 1
    elif num == 2:
        i += 1
        if p == "石头":
            print("输")
            j += 1
        elif p == "剪刀":
            print("平")
            u += 0
        elif p == "布":
            print("赢")
            u += 1
    elif num == 3:
        i += 1
        if p == "石头":
            print("赢")
            u += 1
        elif p == "剪刀":
            print("输")
            j += 1
        elif p == "布":
            print("平")
            u += 0
    else:
        print("请按照对应的数字输入：")

    if i >= 3:
        if u >= 3:
            print("你赢了")
            print("局数：%i\n比分：人%i\t机%i")
            break
        elif j >= 3:
            print("你输了")
            print("局数：%i\n比分：人%i\t机%i")
            break

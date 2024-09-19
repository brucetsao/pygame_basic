import random
import time

###提示语部分
print('你好，我是机器人小埋，我们来玩个猜年龄的小游戏吧～(◆◡◆)')
time.sleep(2)

print('''
=============================
   干物妹！うまるちゃんの年齢
=============================
''')
time.sleep(1)


print('小埋的真实年龄在1到10之间哦～')
time.sleep(1)


print('不过，你只有5次机会哦～')
time.sleep(1)


print('下面，请输入小埋的年龄吧：')


#在下面【】补充完整一条语句，实现“从0至10产生一个随机整数，并赋值给变量age”
age = random.randint(1,10)
#生成随机年龄


#在【】补充完整
#设置次数
for guess in range(1,6):

   #输入玩家猜测的年龄
    choice = int(input())

    #判读玩家输入的年龄是否等于正确的年龄
    if choice < age:
        print('小埋的提示：你猜小了（；´д｀）ゞ。。。。')

    elif choice > age:
        print('小埋的提示：乃猜大了惹(＞﹏＜)～～')

    else:
        print('猜了'+str(guess)+'次，你就猜对惹～hiu(^_^A;)～～～')
        break

#判断猜测次数
if choice == age:
    print('搜噶～那么小埋下线了～拜拜～（￣︶￣）↗')

else:
    print('哎呀～你还是木有猜对啊～但是你只有5次机会诶～怎么办啊～')
    print('那好吧～心软的小埋只好告诉你，我才'+str(age)+'岁哦～(*/ω＼*)')

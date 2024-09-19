import random
import time
import os
print("你好，现在你有10秒的时间记忆下列物品及其编号")
things=["苹果","香蕉","橙子","梨子","猕猴桃","柚子","猴魁","铁观音","彩蛋","复活节"]
for i in range(10):
    print(i,":",things[i])
time.sleep(10)
i=os.system("cls")
n=0
t2=random.sample(things,5)
for i in t2:
    ans=int(input(i+"的编号是："))
    if i==things[ans]:
        n=n+1
print("\n你一共答对了",n,"次")
input("\n按回车键结束程序")

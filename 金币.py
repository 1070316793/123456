import random
num = random.randint(0,10)
print("猜数字游戏，猜对一次给奖励10000金币，猜错了扣500，只有10次机会。")
i = 1
cishu = 0
yve= 10000000
while i <= 10:
    i = i + 1
    cishu = cishu + 1
    jinbi = yve - (cishu * 500)
    shuzi = input("请输入数字：")
    shuzi = int(shuzi)
    if shuzi < num :
        print("小了，扣除500金币","余额:",jinbi)
    elif shuzi > num :
        print("大了","扣除500金币","余额:",jinbi)
    else :
        print("恭喜你猜中了，奖励10000个金币","共输入了",cishu,"次","余额:",jinbi+500+10000)

        break





'''
1.购物小条的商品重复打印问题
2.10张联想电脑 0.5，  20老干妈优惠券 0.1 ， 15 华为优惠券 0.6
  随机抽取一张优惠券，在结算的时候进行打折，进行结算。
'''
shop = [
    ["lenovo PC",5000],
    ["Mac pc",12000],
    ["HUAWEI  WATCH PRO 20",2000],
    ["机械革命",15000],
    ["老干妈",7.5],
    ["卫龙辣条",3],
    ["西瓜",2]
]

import random
num = random.randint(1,45)
if num in[1,2,3,4,5,6,7,8,9,10]:
    print("联想电脑五折")
    e = 0
    Z = 0.5
elif num in [11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]:
    print("老干妈一折")
    e = 4
    Z = 0.1
elif num in [31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]:
    print("华为六折")
    e = 2
    Z = 0.6


mycart = []
money = input("请输入您本月工资：")
money = int(money)
i = 1
k = 0
a = 1
while i <= 20:
    for key, value in enumerate(shop):
        print(key, value)
    chose = input("请输入您想要的商品：")
    if chose.isdigit():
        chose = int(chose)
        if chose >= len(shop):
            print("没有改号商品！请重新输入！")
        else:
            if money >= shop[chose][1]:#如果商品的钱小于我的工资
                mycart.append(shop[chose])#购物车内的商品由字符串组成
                if chose == e and a == 1:
                    a += 1
                    money = money - shop[chose][1] * Z
                else:
                    money = money - shop[chose][1] #支付金额等于工资减去商品的价格栏的数字
                print("恭喜，添加成功！您的余额还剩",money)
            else:
                print("穷鬼，钱不够了，别瞎弄！买其他商品吧！")
    elif chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break
    else:
        print("对不起，您输入错误，别瞎弄！")
    i = i + 1


print("以下是您的购物小条，请拿好！")
print("---------------------------------------")
mydict = dict()
for key,value  in enumerate(mycart):
    if value[0] in mydict:#如果购物车内的商品名字
        tmp = mydict[value[0]]#赋值
        tmplist = str(tmp).split("*")#tmp为可分割的字符串，
        cnt = int(tmplist[1]) + 1
        mydict[value[0]] = str(value[1]) + "*" + str(cnt)
    else:
        mydict[value[0]] = str(value[1]) + '*1'
for key in mydict:
    print(key,mydict[key])
print("------------------------------------1000---")
print("您的余额还剩：￥",money)












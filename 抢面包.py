from threading import Thread
import time

# 全局变量
bread = 0
class x(Thread):
    username = ""
    cname = ""
    money = float(0)
    bao = 0
    m = 0
    def run(self) -> None:
        global bread
        while True:
            if self.username:
                if bread < 500:
                    bread = bread + 1
                    self.bao += 1
                    print(self.username,"造了面包",self.bao,"个")
                elif bread == 500:
                    print("满了")
                    time.sleep(2)
                    if bread == 500:
                        break
                elif bread == 0:
                    print("稍等！")
                    time.sleep(2)
            elif self.cname:
                if self.money >= 2.5:
                    self.money -= 2.5
                    self.m += 1
                    print("余额还有",self.money)
                    print(self.cname,"买了",self.m,"个！")
                elif self.money < 2.5:
                    print("余额不足")
                    break
a1 = x()
a1.username = "1"

a2 = x()
a2.username = "2"

a3 = x()
a3.username = "3"

b1 = x()
b1.money = 3000
b1.cname = "yi"
b2 = x()
b2.money = 3000
b2.cname = "yi1"
b3 = x()
b3.money = 3000
b3.cname = "yi2"
b4 = x()
b4.money = 3000
b4.cname = "yi3"
b5 = x()
b5.money = 3000
b5.cname = "yi4"
b6 = x()
b6.money = 3000
b6.cname = "yi5"
a1.start()
a2.start()
a3.start()
b1.start()
b2.start()
b3.start()
b4.start()
b5.start()
b6.start()





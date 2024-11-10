import random  # 导入random模块
print("-" * 50)#欢迎界面
print("欢迎来到 Yao 的《猜数游戏》")
print("规则一：系统每次会自动生成一个1~10之间的随机数")
print("规则二:每次游戏最多只能猜三次")
print("规则三:进入游戏或者继续玩,输入: yes或者y")
print("规则四：离开游戏，输入：no或者n")
print("-" * 50)

#定义游戏次数变量
     #游戏次数
n = 0
while True:        #出现错误可以继续循环
    order = input('请输入是否开始游戏:\t')
    if order == 'yes' or order == 'y':  # 用户想玩游戏
        n += 1
        print(f'正式开始第{n}次游戏哦')
        number = random.randint(1,10)    # 生成一个随机数

        for i in range(1,4): #1 ， 2， 3 用户最多可以猜三次  i是其中的一次
            my_sum = int(input('请你输入你所猜的数字:'))
            if my_sum == number:
                print(f'恭喜你 运气之子 答案就是{my_sum}')
                break                       #猜对数字之后终止
            elif my_sum > number:
                print(f'你猜的数字太大啦 还剩下{3-i}次 try again嘻嘻')
            else:
                print(f'你猜的数字太小啦 还剩下{3-i}次 please try')
        else:   #三次都猜错啦，不再进入for循环
            print(f'你三次都猜错啦宝宝 答案是{number}哦')

    elif order == 'no' or order == 'n':   # 用户不想玩游戏
        print(f'game over 宝宝    你一共进行了{n}次游戏哦')
        break
    else:
        print('请输入正确的指令')
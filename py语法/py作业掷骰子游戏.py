

import random

def DAME():
        a_list = []
        numbers=3
        while numbers>0:
            point=random.randrange(1,7)
            a_list.append(point)
            numbers=numbers-1
        #计算机掷骰子


        if 11 <= sum(a_list) <= 18:
            right='Big'
        if 3 <= sum(a_list) <= 10:
            right='Small'
        #生成正确答案

        #游戏正式开始：
        print("<<<<< GAME STARTS! >>>>>")
        print("Big or Samll: ")

        while True:  # 使用while循环来持续等待正确输入
            Your_answers = input()
            if Your_answers == 'Big' or Your_answers == 'Small':
                break  # 当输入正确时跳出循环
            else:
                print("输入结果错误，请您重新输入：")
                print("Big or Small")

        print("<<<<< ROLE THE DICE! >>>>>")
        if Your_answers == right:
            print("Congratulations! You are right! Points are [",a_list[0], a_list[1], a_list[2],"]")
            a_list.clear()
            print("Do you want to continue? y or n")
            A_small_game()
        elif Your_answers != right:
            print("The points are [", a_list[0], a_list[1], a_list[2], "] You Lose!")
            a_list.clear()
            print("Do you want to continue? y or n")
            A_small_game()

def A_small_game():
    b_list=['y','n']

    while True:
        print("请输入：")
        Your_inputting = input()
        if Your_inputting == b_list[0] or Your_inputting == b_list[-1]:
            break
        else:
            print("输入错误，请重新输入：")
            print("y or n")


    if Your_inputting==b_list[0]:
        DAME()
    if Your_inputting==b_list[-1]:
        return

print("游戏说明如下：")
print("这是一个简单的掷骰子猜大小的游戏，计算机依次掷骰子三次，并将三次的结果相加。")
print("玩家需猜测大小，11<=总值<=18为“大”，3<=总值<=10为“小”")
print("您只需输入“Big”或者“Small”来表示您的猜测结果")
print("无论是否猜测正确，输入y会继续游戏，输入n退出游戏。游戏开始同上操作")
A_small_game()







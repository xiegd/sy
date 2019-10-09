import random
def guess():
    while True:
        global time
        num1 = input('请输入一个数字：')
        if num1.isnumeric() == True:
            time += 1
            if eval(num1) > num2:
                print('遗憾，太大了')
            elif eval(num1) < num2:
                print('遗憾，太小了')
            else:
                print('预测{}次，你猜中了！'.format(time))
                break
        else:
            print('输入内容必须为整数！')
            continue
num2 = random.randint(0,100)
time = 0
guess()
    

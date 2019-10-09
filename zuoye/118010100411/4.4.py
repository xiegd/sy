import random
num2 = random.randint(0,100)
time = 0
while True:
    num1 = eval(input('请输入一个数字：'))
    time += 1
    if num1 > num2:
        print('遗憾，太大了')
    elif num1 < num2:
        print('遗憾，太小了')
    else:
        print('预测{}次，你猜中了！'.format(time))
        break

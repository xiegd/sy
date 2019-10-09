import random
a = b = c = 10000
i = j = 0
while a:
    num = random.randint(1,3)
    num_car = random.randint(1,3)
    if num == num_car:
        i += 1
    a -= 1
while b:
    num_car = random.randint(1,3)
    while True:
        num2 = random.randint(1,3)
        if num2 == num_car:
            continue
        else:
            break
    nums = [num_car,num2]
    num = random.choice(nums)
    if num == num_car:
        j += 1
    b -= 1
print('不能更换:{:.4f},能更换:{:.4f}'.format(i/c,j/c))
    

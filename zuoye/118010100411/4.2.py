str = input('请输入一串字符:')
e = num = space = other = 0
for char in str:
    if 'a' < char < 'z' or 'A' < char < 'Z':
        e += 1
    elif '0' < char < '9':
        num += 1
    elif char == ' ':
        space += 1 
    else:
        other += 1
print('英文字符数{},数字数{},空格数{},其他字符数{}'.format(e,num,space,other))

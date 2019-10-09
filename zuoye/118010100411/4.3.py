a,b = eval(input('输入两个数字，逗号隔开：'))
if a < b:
    m,n = b,a
else:
    m,n = a,b
r = m % n
while m % n:
    m,n = n,r
    r = m % n
bei = a * b / n
print('最小公倍数{:},最大公约数{:.0f}'.format(n,bei))

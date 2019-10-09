for i in range(0,11):
    if i%5 == 0:
        for a in range(0,11):
            if a%5 == 0:
                print('+',end = ' ')
            else:
                print('-',end = ' ')
        print('\n')
    else:
        for b in range(0,11):
            if b%5 == 0:
                print('|',end = ' ')
            else:
                print(' ',end = ' ')
        print('\n')

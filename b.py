x = input().split()

i, y = map(int, x)

w = i*y

if w % 2 == 0:
    print('Even')
else:
    print('Odd')
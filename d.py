i = int(input())
y = list(map(int, input().split()))

cnt = -1
is_flag = True
while is_flag:
    cnt += 1
    for x ,a in enumerate(y, 0):
        if (a%2) == 0:
            w = a/2
            y[x] = w
        else:
            is_flag = False
print(cnt)
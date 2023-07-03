def num2lst_n(num,digits=1):
    digits_l = []
    while True:
        digits_l.insert(0,num % 10**digits)
        num //= 10**digits
        if num == 0:
            return digits_l

i = int(input())
total = 0
for x in num2lst_n(i):
    if x == 1:
        total += 1

print(total)
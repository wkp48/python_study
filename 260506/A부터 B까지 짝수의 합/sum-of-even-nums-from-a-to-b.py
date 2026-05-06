a, b = map(int, input().split())
ls_num = []
total = 0
if a <= b:
    for i in range(a, b+1):
        if a < b+1:

            ls_num.append(a)
            a += 1
else:
    for i in range(b, a+1):
        if b < a+1:
            ls_num.append(b)
            b += 1

for num in ls_num:
    if num % 2 == 0:
        total += num

print(f"{total}")
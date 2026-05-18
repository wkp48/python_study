result = []
a, b = map(int, input().split())
result.append(a)
while True:
    if a % 2 != 0:
        a *= 2
    else:
        a += 3
    if a > b:
        break

    result.append(a)

print(*result)
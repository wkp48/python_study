repeat_num = int(input())


for i in range(1, repeat_num + 1):
    total_sum = 0
    a, b = map(int, input().split())

    for j in range(a, b+1):
        if j % 2 == 0:
            total_sum += j
    print(f"{total_sum}")

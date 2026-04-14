a,b,c = map(int, input().split())

sum = a+b+c
average = (a+b+c) // 3
sum_minus = sum - average

print(f"{sum}")
print(f"{average}")
print(f"{sum_minus}")
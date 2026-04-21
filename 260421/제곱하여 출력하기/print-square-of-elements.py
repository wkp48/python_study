count = int(input())
user_input = list(map(int,input().split()))
result = []
for i in user_input:
    result.append(i ** 2)

print(*result)
user_input = list(map(int, input().split()))

for x in range(8):
    user_input.append((user_input[-2] + user_input[-1]) % 10)

print(*user_input)
    
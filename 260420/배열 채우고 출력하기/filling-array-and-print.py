user_input = list(input().split())
reverse = ""
for x in range(len(user_input)):
    reverse += user_input.pop()

print(f"{reverse}")
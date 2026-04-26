user_input = input()
list_input = list(user_input)
list_input[1] = "a"
list_input[-2] = "a"
result = "".join(list_input)
print(f"{result}")
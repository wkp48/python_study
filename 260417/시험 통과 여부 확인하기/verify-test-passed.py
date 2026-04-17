user_input = int(input())

if user_input >= 80:
    print("pass")
else:
    print(f"{80 - user_input} more score")
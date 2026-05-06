user_input = [int(input()) for i in range(10)]
third_num = 0
five_num = 0

for num in user_input:
    if num % 3 == 0:
        third_num += 1
        if num % 5 == 0:
            five_num += 1
    elif num % 5 == 0:
        five_num += 1
print(f"{third_num} {five_num}")
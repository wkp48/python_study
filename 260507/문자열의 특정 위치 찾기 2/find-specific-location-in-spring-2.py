fruits = ["apple", "banana", "grape", "blueberry", "orange"]
user_input = input()
cnt = 0

for i in fruits:
    if i[2] == user_input or i[3] == user_input:
        cnt += 1
        print(f"{i}")
print(f"{cnt}")
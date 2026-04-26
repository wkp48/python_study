count = int(input())
user_num = list(map(int, input().split()))

for i in reversed(user_num):
    if i % 2 == 0:
        print(f"{i}", end = " ")
    else :
        pass
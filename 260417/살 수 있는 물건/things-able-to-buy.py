user_money = int(input())
book = 3000
mask = 1000

if user_money >= 3000:
    print(f"book")
elif 1000 <= user_money < 3000:
    print(f"mask")
else:
    print("no")
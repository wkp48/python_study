a,b,c = map(int, input().split())

if a < b and b < c and a < c:
    print(f"{b}")
elif b < a and a < c and b < c:
    print(f"{a}")
else:
    print(f"{c}")
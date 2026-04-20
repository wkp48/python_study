a,b,c = map(int, input().split())

if a < b and b < c and a < c:
    print(f"{b}")
elif b < a and a < c and b < c:
    print(f"{a}")
elif a < c and c < b and a < c:
    print(f"{c}")
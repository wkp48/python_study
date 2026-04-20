a,b,c = map(int, input().split())

if b < a < c or c <= a <= b:
    print(f"{a}")
elif a <= b <= c or c <= b <= a:
    print(f"{b}")
elif a <= c <= b or b <= c <= a:
    print(f"{c}")
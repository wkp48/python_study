a, b= map(str, input().split())

if len(a) == len(b):
    print(f"same")
elif len(a) > len(b):
    print(*{a}, len(a))
elif len(a) < len(b):
    print(*{b}, len(b))
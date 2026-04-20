a_math,a_eng = map(int, input().split())
b_math,b_eng = map(int, input().split())

if a_math > b_math and a_eng > b_eng:
    print(f"1")
else:
    print(f"0")
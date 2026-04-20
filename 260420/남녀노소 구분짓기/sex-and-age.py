gender = int(input())
age = int(input())

if gender == 0:
    if age >= 19:
        print(f"MAN")
    else:
        print(f"BOY")
elif gender == 1:
    if age >= 19:
        print(f"WOMAN")
    else:
        print(f"GIRL")
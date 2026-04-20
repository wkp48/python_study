gender = int(input())
age = int(input())

if gender == 0 and age >= 19:
    print(f"MAN")
elif gender == 1 and age >= 19:
    print(f"WOMAN")
elif gender == 0 and age <= 19:
    print(f"BOY")
elif gender == 1 and age <= 19:
    print(f"GIRL")
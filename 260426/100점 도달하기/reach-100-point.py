score = int(input())

for count in range(score, 101):
    if count >= 90:
        print(f"A", end=" ")
    elif count >= 80:
        print(f"B", end=" ")
    elif count >= 70:
        print(f"C", end=" ")
    elif count >= 60:
        print(f"D", end=" ")
    else:
        print(f"F", end=" ")

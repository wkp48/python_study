while True:
    user_input = int(input())

    if user_input < 25:
        print(f"Higher")
    elif user_input == 25:
        print(f"Good")
        break
    else:
        print(f"Lower")
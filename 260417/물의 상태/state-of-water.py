input_temperature = int(input())

if input_temperature < 0:
    print(f"ice")
elif input_temperature >= 100:
    print(f"vapor")
else:
    print(f"water")
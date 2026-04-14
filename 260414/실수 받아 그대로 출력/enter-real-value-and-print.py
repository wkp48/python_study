user_input = float(input())
limit_score = 0 <= user_input <= 50
if limit_score == True:
    print(f"{user_input:.2f}")
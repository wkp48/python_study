num = int(input())
total_sum = 0  # 파이썬 내장함수 이름인 'sum' 대신 다른 이름(total_sum 등)을 쓰는 것이 안전합니다.

for i in range(1, 101):
    total_sum += i       # 1. 일단 1부터 차례대로 더합니다.
    
    if total_sum >= num: # 2. 만약 방금 더한 결과가 N(num) 이상이 되었다면?
        print(i)         # 3. 목표를 넘기게 만든 '방금 더한 그 숫자(i)'를 출력하고
        break
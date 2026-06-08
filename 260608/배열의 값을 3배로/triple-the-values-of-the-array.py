rows = 3
cols = 3

if 0 <= rows <= 3 and 0 <= cols <= 3:
    for i in range(rows):
        # 한 줄을 입력받아 리스트로 만듦
        matrix = list(map(int, input().split()))
        
        # 3배 한 값을 담을 빈 리스트 생성
        mul_matrix = [] 
        
        # 입력받은 리스트의 각 요소를 돌면서 3을 곱해 추가
        for j in range(cols):
            mul_matrix.append(matrix[j] * 3) 
            
        # 완성된 줄을 출력
        print(*mul_matrix)
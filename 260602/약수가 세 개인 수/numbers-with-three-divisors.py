start, end = map(int, input().split())
count = 0
# Please write your code here.
for i in range(start, end + 1):
   
    meansure = []
    for j in range(1, i+1):
        if i % j == 0:
            meansure.append(j)
    if len(meansure) == 3:
        count += 1
print(f"{count}")
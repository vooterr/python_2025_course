arr = [2, 4, 1, 3, 2, 5, 2, 1, 3, 1]

best_sum = 0
p1 = 0
p2 = len(arr) - 1

while (p1 != p2):
    best_sum = max(best_sum, min(arr[p1], arr[p2]) * (p2 - p1))
    if (arr[p1] < arr[p2]):
        p1+=1
    else:
        p2-=1
print(best_sum)


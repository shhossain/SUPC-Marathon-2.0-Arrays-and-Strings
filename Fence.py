planks_size, piano_size = list(map(int, input().split()))
planks = list(map(int, input().split()))

newList = [0]
# culmulative sum of the list
sum_val = 0
for i in range(len(planks)):
    sum_val += planks[i]
    newList.append(sum_val)

score_val = None
score_index = None
for i in range(len(planks)):
    k = i + piano_size
    if k > len(planks):
        break
    val = newList[k] - newList[i]
    
    if score_val is None or val < score_val:
        score_val = val
        score_index = i

final_val = score_index + 1
print(final_val)

from collections import defaultdict

arr = [2,1,3,3,3,2]

dic = defaultdict(list)
result = []

for i in range(len(arr)):
    currentGroup = dic[arr[i]]
    if (len(currentGroup) + 1) == arr[i]:
        result.append(currentGroup + [i])
        dic[arr[i]] = []
    else:
        dic[arr[i]] = currentGroup + [i]

print(result)

from collections import defaultdict
nums = [1,3,4,1,2,3,1]
dic = defaultdict(int)

result = []

for el in nums:
    dic[el] += 1
    if len(result) < dic[el]:
        result.append([el])
    else:
        result[dic[el]-1].append(el)

print(result)
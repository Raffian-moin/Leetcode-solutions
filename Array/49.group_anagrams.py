from collections import defaultdict
nums = ["a"]

dic = defaultdict(list)

result = []

for el in nums:
    sor = ''.join(sorted(el))
    dic[sor].append(el)

print(dic.values())
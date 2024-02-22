n = 1
trusts = [[1, 3], [2, 3]]
frequency = [0]*(n+1)
flag = [0]*(n+1)

for i in range(len(trusts)):
    frequency[trusts[i][1]] += 1
    flag[trusts[i][0]] = 1

count = 0
for i in range(1, n + 1):
    if frequency[i] == n-1 and flag[i] == 0:
        ans = i

print(ans)
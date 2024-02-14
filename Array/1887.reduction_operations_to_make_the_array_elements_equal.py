nums = [1,1,2,2,3]
nums.sort()
length = len(nums)
ans = 0

for i in range(length - 1, 0, -1):
    if nums[i] != nums[i - 1]:
        ans += length - i

print(ans)
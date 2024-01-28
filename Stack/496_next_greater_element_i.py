nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

stack = [nums2[-1]]
greater_elements = {}
greater_elements[nums2[-1]] = -1

for i in range(len(nums2) - 2, -1, -1):
    while len(stack) and nums2[i] > stack[-1]:
        stack.pop()

    if len(stack):
        greater_elements[nums2[i]] = stack[-1]
    else:
        greater_elements[nums2[i]] = -1
    stack.append(nums2[i])

for i in range(len(nums1)):
    nums1[i] = greater_elements[nums1[i]]

print(nums1)
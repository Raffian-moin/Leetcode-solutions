arr = [1, 2, 3, 5]
largest = 0
secondLargest = 0
largestIndex = -1

for i in range(len(arr)):
    if arr[i] > largest:
        secondLargest = largest
        largest = arr[i]
        largestIndex = i

    if arr[i] > secondLargest and arr[i] < largest:
        secondLargest = arr[i]


if largest / 2 < secondLargest:
    largestIndex = -1

print(largestIndex)
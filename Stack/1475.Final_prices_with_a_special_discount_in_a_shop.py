prices = list(map(int, input().split()))
stack = [prices[-1]]

for i in range(len(prices) -2, -1, -1):
    current = prices[i]
    while len(stack) and current < stack[-1]:
        stack.pop()
    
    if len(stack):
        prices[i] = current - stack[-1]

    stack.append(current)

print(prices)
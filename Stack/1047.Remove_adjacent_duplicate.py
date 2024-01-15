s = "aaaaaab"
stack = []
result = ""

for ch in s:
    if len(stack) > 0 and stack[len(stack)-1] == ch:
        stack.pop()
    else:
        stack.append(ch)

print(("").join(stack))
class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for ch in s:
            if len(stack) == 0:
                stack.append(ch)
                continue
                
            if ch == "B" and stack[len(stack)-1] == "A":
                stack.pop()
            elif ch == "D" and stack[len(stack)-1] == "C":
                stack.pop()
            else:
                stack.append(ch)
            
        return len(stack)
        
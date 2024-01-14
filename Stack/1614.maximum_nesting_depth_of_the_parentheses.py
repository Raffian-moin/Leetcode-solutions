class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        current_count = 0

        for ch in s:
            if ch == "(":
                current_count += 1
            elif ch == ")":
                current_count -= 1
            
            depth = max(depth, current_count)

        return depth
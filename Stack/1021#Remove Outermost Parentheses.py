class Solution:
    stack = []
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.isEmpty():
            self.stack.pop()

    def peek(self):
        if not self.isEmpty():
            return self.stack[len(self.stack)-1]

    def isEmpty(self):
        if len(self.stack) == 0:
            return True

    def size(self):
        return len(self.stack)

    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        for ch in s:
            if ch == "(":
                self.push(ch)
                if self.size() > 1:
                    result += ch
            elif ch == ")":
                self.pop()
                if self.size() > 0:
                    result += ch

        return result

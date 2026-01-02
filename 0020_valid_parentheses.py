class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        stack = []

        for p in s:
            if p in '({[':
                stack.append(p)
            elif stack and stack[-1] == pairs[p]:
                stack.pop()
            else:
                return False

        return not stack

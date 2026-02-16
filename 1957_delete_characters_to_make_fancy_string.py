class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []

        for ch in s:
            if len(stack) >= 2 and stack[-1] == ch and stack[-2] == ch:
                pass
            else:
                stack.append(ch)

        return ''.join(stack)

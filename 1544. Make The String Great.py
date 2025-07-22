class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for ch in s:
            if stack and stack[-1].islower() != ch.islower() and stack[-1].lower() == ch.lower():
                stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack)

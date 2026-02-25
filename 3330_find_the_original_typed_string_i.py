class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        stack = []

        for ch in word:
            if stack and stack[-1] == ch:
                ans += 1
            else:
                stack.append(ch)

        return ans

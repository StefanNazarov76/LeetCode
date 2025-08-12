class Solution:
    def reformat(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        digits = [c for c in s if c.isdigit()]

        if abs(len(letters) - len(digits)) > 1:
            return ''

        if len(letters) > len(digits):
            first, second = letters, digits
        else:
            first, second = digits, letters

        ans = []
        for i in range(len(s)):
            if i % 2 == 0:
                ans.append(first.pop())
            else:
                ans.append(second.pop())

        return ''.join(ans)

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = []

        for ch in s:
            if ch.isalpha():
                letters.append(ch)

        ans = ''
        for ch in s:
            if ch.isalpha():
                ans += letters.pop()
            else:
                ans += ch

        return ans

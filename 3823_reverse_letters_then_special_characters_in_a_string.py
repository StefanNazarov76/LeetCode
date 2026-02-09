class Solution:
    def reverseByType(self, s: str) -> str:
        letters = []
        special = []

        for ch in s:
            if ch.isalpha():
                letters += ch
            else:
                special += ch

        ans = ''
        for ch in s:
            if ch.isalpha():
                ans += letters.pop()
            else:
                ans += special.pop()

        return ans

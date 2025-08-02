class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []

        for i in s:
            if i in 'aeiouAEIOU':
                vowels.append(i)

        ans = ''
        for i in s:
            if i in 'aeiouAEIOU':
                ans += vowels.pop()
            else:
                ans += i

        return ans

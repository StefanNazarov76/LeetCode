class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = [ch for ch in s if ch in 'AEIOUaeiou']
        vowels.sort(reverse=True)
        ans = ''

        for ch in s:
            if ch in 'AEIOUaeiou':
                ans += vowels.pop()
            else:
                ans += ch

        return ans

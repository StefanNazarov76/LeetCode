class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        indexes = []

        for i in range(len(s)):
            if s[i].lower() in 'aeiou':
                vowels.append(s[i])
                indexes.append(i)

        vowels.sort()

        ans = list(s)
        for i in range(len(vowels)):
            ans[indexes[i]] = vowels[i]

        return ''.join(ans)

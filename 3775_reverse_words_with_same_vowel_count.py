class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        vowels_count = sum(1 for ch in s[0] if ch in 'aeiou')

        for i in range(1, len(s)):
            if vowels_count == sum(1 for ch in s[i] if ch in 'aeiou'):
                s[i] = s[i][::-1]

        return ' '.join(s)

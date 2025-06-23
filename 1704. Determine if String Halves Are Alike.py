class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        left = s[:len(s) // 2]
        right = s[len(s) // 2:]

        left_vowels = 0
        right_vowels = 0

        for i in range(len(left)):
            if left[i] in 'aeiouAEIOU':
                left_vowels += 1

            if right[i] in 'aeiouAEIOU':
                right_vowels += 1

        return left_vowels == right_vowels

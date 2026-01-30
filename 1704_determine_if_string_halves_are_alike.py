class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        left = s[:len(s) // 2]
        right = s[len(s) // 2:]

        vowels_left = 0
        vowels_right = 0

        for i in range(len(left)):
            if left[i] in 'aeiouAEIOU':
                vowels_left += 1

            if right[i] in 'aeiouAEIOU':
                vowels_right += 1

        return vowels_left == vowels_right

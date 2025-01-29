class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'aeiou'
        s = s.lower()

        a = s[:len(s) // 2]
        b = s[len(s) // 2:]

        a_sum = 0
        b_sum = 0

        for i in range(len(s) // 2):
            if a[i] in vowels:
                a_sum += 1

            if b[i] in vowels:
                b_sum += 1

        return a_sum == b_sum

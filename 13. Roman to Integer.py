class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        ans = 0
        i = len(s) - 1

        while i >= 0:
            if i - 1 >= 0 and roman_map[s[i]] > roman_map[s[i - 1]]:
                ans += roman_map[s[i]] - roman_map[s[i - 1]]
                i -= 2
            else:
                ans += roman_map[s[i]]
                i -= 1

        return ans

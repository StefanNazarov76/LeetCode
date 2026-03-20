class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counter = sorted(Counter(s).items())
        ans = ''
        mid = ''

        for char, freq in counter:
            if freq % 2 != 0:
                mid = char
            ans += char * (freq // 2)

        return ans + mid + ans[::-1]

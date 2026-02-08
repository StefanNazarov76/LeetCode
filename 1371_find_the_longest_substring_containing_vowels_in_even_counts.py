class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)
        vowels = 'aeiou'

        prefix = [{v: 0 for v in vowels}]

        for ch in s:
            prev = prefix[-1].copy()
            if ch in vowels:
                prev[ch] += 1
            prefix.append(prev)

        ans = 0

        for i in range(n):
            for j in range(n, i, -1):
                if j - i <= ans:
                    break

                ok = True
                for v in vowels:
                    if (prefix[j][v] - prefix[i][v]) % 2 != 0:
                        ok = False
                        break

                if ok:
                    ans = j - i
                    break

        return ans

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        counter = 0

        for i in range(0, len(s)):
            for j in range(i, len(s)):
                substring = s[i:j + 1]

                if substring.count('0') <= k or substring.count('1') <= k:
                    counter += 1
                else:
                    break

        return counter

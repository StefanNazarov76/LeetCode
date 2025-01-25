class Solution:
    def minimumChairs(self, s: str) -> int:
        c = 0
        max = 0

        for i in s:
            if i == 'E':
                c += 1
                if max < c:
                    max = c
            else:
                c -= 1

        return max
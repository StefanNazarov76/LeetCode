class Solution:
    def partitionString(self, s: str) -> int:
        counter = 1
        curr = ''

        for i in s:
            if i in curr:
                curr = i
                counter += 1
            else:
                curr += i

        return counter

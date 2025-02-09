class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max = -sys.maxsize

        for s in strs:
            if s.isdigit():
                if int(s) > max:
                    max = int(s)
            else:
                if len(s) > max:
                    max = len(s)

        return max
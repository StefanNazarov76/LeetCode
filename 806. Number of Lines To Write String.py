class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        d = dict(zip('abcdefghijklmnopqrstuvwxyz', widths))
        lines = 0
        pixels = 0

        for i in s:
            pixels += d[i]

            if pixels > 100:
                pixels = d[i]
                lines += 1

        return lines + 1, pixels

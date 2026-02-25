class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        pixels = 0

        for ch in s:
            w = widths[ord(ch) - 97]

            if pixels + w > 100:
                pixels = w
                lines += 1
            else:
                pixels += w

        return [lines, pixels]

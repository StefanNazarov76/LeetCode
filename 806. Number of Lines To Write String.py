class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        width = 0

        for letter in s:
            width += widths[ord(letter) - ord('a')]

            if width > 100:
                lines += 1
                width = widths[ord(letter) - ord('a')]

        return [lines, width]

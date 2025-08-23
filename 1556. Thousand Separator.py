class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        first = len(s) % 3
        result = s[:first]

        for v in range(first, len(s), 3):
            result += '.' + str(s[v: v + 3])

        if result[0] == '.':
            return result[1:]

        return result

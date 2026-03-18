class Solution:
    def processStr(self, s: str) -> str:
        result = ''

        for ch in s:
            match ch:
                case '*':
                    result = result[:-1]
                case '#':
                    result = result + result
                case '%':
                    result = result[::-1]
                case _:
                    result += ch

        return result

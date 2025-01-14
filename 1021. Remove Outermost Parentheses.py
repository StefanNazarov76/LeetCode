class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        counter = 0
        res = []

        for ch in s:
            if ch == '(':
                counter += 1
                if counter != 1:
                    res.append(ch)
            else:
                counter -= 1
                if counter != 0:
                    res.append(ch)

        return ''.join(res)

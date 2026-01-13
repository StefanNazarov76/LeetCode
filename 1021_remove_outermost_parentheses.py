class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ''
        depth = 0

        for p in s:
            if p == '(':
                if depth > 0:
                    ans += p

                depth += 1

            else:
                depth -= 1

                if depth > 0:
                    ans += p

        return ans

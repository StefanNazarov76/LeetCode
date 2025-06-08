class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ''
        counter = 1

        for i in s[1:]:
            if counter == 0:
                counter += 1
                continue

            if i == '(':
                counter += 1
            else:
                counter -= 1

            if counter != 0:
                ans += i

        return ans

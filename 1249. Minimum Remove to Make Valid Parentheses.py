class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_cnt = 0
        ans = []

        for i in s:
            if i == '(':
                open_cnt += 1
            elif i == ')':
                if open_cnt <= 0:
                    continue
                else:
                    open_cnt -= 1
            ans.append(i)

        if open_cnt > 0:
            ans.reverse()

            for i in range(open_cnt):
                ans.remove('(')

            ans.reverse()

        return ''.join(ans)

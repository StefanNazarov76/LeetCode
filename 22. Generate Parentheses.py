class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(curr, open_cnt, close_cnt):
            if len(curr) == n * 2:
                ans.append(curr)
                return

            if open_cnt < n:
                backtrack(curr + '(', open_cnt + 1, close_cnt)

            if close_cnt < open_cnt:
                backtrack(curr + ')', open_cnt, close_cnt + 1)

        backtrack('', 0, 0)
        return ans

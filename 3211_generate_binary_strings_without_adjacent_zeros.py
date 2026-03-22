class Solution:
    def validStrings(self, n: int) -> List[str]:
        def backtrack(ans, n):
            if n == 1:
                return ans

            temp = []
            for s in ans:
                if s[-1] == '0':
                    temp.append(s + '1')
                else:
                    temp.append(s + '0')
                    temp.append(s + '1')

            return backtrack(temp, n - 1)

        return backtrack(['0', '1'], n)

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(ans, n):
            if n == 1:
                return ans

            temp = []
            for s in ans:
                if s[-1] == 'a':
                    temp.append(s + 'b')
                    temp.append(s + 'c')
                elif s[-1] == 'b':
                    temp.append(s + 'a')
                    temp.append(s + 'c')
                else:
                    temp.append(s + 'a')
                    temp.append(s + 'b')

            return backtrack(temp, n - 1)

        strings = backtrack(['a', 'b', 'c'], n)
        strings.sort()

        if k <= len(strings):
            return strings[k - 1]
        else:
            return ''

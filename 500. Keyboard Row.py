class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []

        for i in words:
            flag = False

            if i[0].lower() in 'qwertyuiop':
                row = 'qwertyuiop'
            elif i[0].lower() in 'asdfghjkl':
                row = 'asdfghjkl'
            else:
                row = 'zxcvbnm'

            for j in i.lower():
                if j not in row:
                    flag = True
                    break

            if not flag:
                ans.append(i)

        return ans
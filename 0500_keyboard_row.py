class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = 'qwertyuiop'
        second_row = 'asdfghjkl'
        third_row = 'zxcvbnm'
        ans = []

        for w in words:
            temp = w.lower()

            row = ''

            if temp[0] in first_row:
                row = first_row
            elif temp[0] in second_row:
                row = second_row
            elif temp[0] in third_row:
                row = third_row

            for ch in temp:
                if ch not in row:
                    break
            else:
                ans.append(w)

        return ans

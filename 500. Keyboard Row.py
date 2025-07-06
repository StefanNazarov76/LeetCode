class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []

        for w in words:
            ans.append(w)
            w = w.lower()

            if w[0] in 'qwertyuiop':
                row = 'qwertyuiop'
            elif w[0] in 'asdfghjkl':
                row = 'asdfghjkl'
            else:
                row = 'zxcvbnm'

            for ch in set(w[1:]):
                if ch not in row:
                    ans.pop()
                    break

        return ans
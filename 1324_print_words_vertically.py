class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        n = max(len(w) for w in s)
        ans = []

        for i in range(n):
            temp = ''

            for w in s:
                if i < len(w):
                    temp += w[i]
                else:
                    temp += ' '

            ans.append(temp.rstrip())
        return ans

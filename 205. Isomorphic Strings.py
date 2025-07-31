class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def encode(word):
            pattern = {}
            res = ''
            n = 0

            for i in word:
                if i not in pattern:
                    pattern[i] = str(n)
                    n += 1

                res += pattern[i]
                res += ' '

            return res

        return encode(s) == encode(t)

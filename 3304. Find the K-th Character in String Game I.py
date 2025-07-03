class Solution:
    def kthCharacter(self, k: int) -> str:
        s = 'a'

        while len(s) < k:
            temp = ''

            for i in s:
                if i == 'z':
                    temp += 'a'
                else:
                    temp += chr(ord(i) + 1)

            s += temp

        return s[k - 1]
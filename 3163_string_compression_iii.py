class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        last = word[0]
        cnt = 1

        for c in word[1:]:
            if c == last and cnt < 9:
                cnt += 1
            else:
                comp.append(str(cnt) + last)
                last = c
                cnt = 1

        comp.append(str(cnt) + last)
        return ''.join(comp)

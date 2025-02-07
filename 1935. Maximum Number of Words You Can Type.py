class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res = 0

        for w in text.split():
            flag = False

            for l in brokenLetters:
                if l in w:
                    flag = True
                    break

            if not flag:
                print(w)
                res += 1

        return res

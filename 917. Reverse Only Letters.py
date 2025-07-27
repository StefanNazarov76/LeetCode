class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = []
        ans = []
        index = 0

        for i in s:
            if i.isalpha():
                letters.append(i)
        letters.reverse()

        for i in s:
            if i.isalpha():
                ans.append(letters[index])
                index += 1
            else:
                ans.append(i)

        return ''.join(ans)

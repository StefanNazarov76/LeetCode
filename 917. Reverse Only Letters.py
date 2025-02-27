class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = []
        letters = []
        not_letters = []

        for i in s:
            if i.isalpha():
                letters.append(i)
            else:
                not_letters.append(i)

        not_letters.reverse()

        for i in s:
            if i.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(not_letters.pop())

        return ''.join(ans) 

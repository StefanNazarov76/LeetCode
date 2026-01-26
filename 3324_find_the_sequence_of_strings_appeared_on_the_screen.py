class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ans = []

        for ch in target:
            temp = ''

            if ans:
                temp = ans[-1]

            for i in range(97, ord(ch) + 1):
                ans.append(temp + chr(i))

        return ans

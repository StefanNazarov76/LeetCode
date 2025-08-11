class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = Counter({'l': 2, 'o': 2, 'b': 1, 'a': 1, 'n': 1})
        counter = Counter(text)
        ans = 0

        while counter >= balloon:
            ans += 1
            counter -= balloon

        return ans

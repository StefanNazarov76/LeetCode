class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0

        for i in range(len(words)):
            if words[i][::-1] in words[i + 1::]:
                ans += 1

        return ans

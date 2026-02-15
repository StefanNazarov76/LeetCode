class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ans = 0

        for w in words[left:right + 1]:
            if w[0] in 'aeiou' and w[-1] in 'aeiou':
                ans += 1

        return ans

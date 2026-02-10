class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = ['']

        for ch in s:
            if ch.isalpha():
                ans = [a + ch.lower() for a in ans] + [a + ch.upper() for a in ans]
            else:
                ans = [a + ch for a in ans]

        return ans

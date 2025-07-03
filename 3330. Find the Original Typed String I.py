class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        counter = 0
        char = word[0]

        for i in word[1:]:
            if i != char:
                ans += counter
                char = i
                counter = 0
            else:
                counter += 1

        return ans + counter

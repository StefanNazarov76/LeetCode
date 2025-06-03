class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = len(words)

        for word in words:
            for letter in word:
                if letter not in allowed:
                    ans -= 1
                    break

        return ans
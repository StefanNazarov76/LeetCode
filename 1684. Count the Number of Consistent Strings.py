class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = len(words)
        for w in words:
            for ch in w:
                if ch not in allowed:
                    count = count - 1
                    break
        return count

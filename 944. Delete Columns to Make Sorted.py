class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        columns = zip(*strs)
        return sum(list(col) != sorted(col) for col in columns)

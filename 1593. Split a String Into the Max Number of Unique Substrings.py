class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start: int, seen: set) -> int:
            if start == len(s):
                return 0

            max_count = 0
            for end in range(start + 1, len(s) + 1):
                substr = s[start:end]

                if substr not in seen:
                    seen.add(substr)
                    max_count = max(max_count, 1 + backtrack(end, seen))
                    seen.remove(substr)

            return max_count

        return backtrack(0, set())

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = []

        for query in queries:
            i = 0
            match = True

            for ch in query:
                if i < len(pattern) and ch == pattern[i]:
                    i += 1
                elif ch.isupper():
                    match = False
                    break

            if i != len(pattern):
                match = False

            ans.append(match)

        return ans

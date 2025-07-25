class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = Counter(digits)
        ans = set()

        for h in range(1, 10):
            for t in range(0, 10):
                for o in range(0, 10, 2):
                    used = Counter([h, t, o])

                    if any([used[i] > freq[i] for i in used]):
                        continue

                    ans.add(h * 100 + t * 10 + o)

        return sorted(ans)

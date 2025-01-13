class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = []

        for _, n in sorted(zip(heights, names), reverse=True):
            res.append(n)

        return res

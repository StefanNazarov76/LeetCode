class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)

        for num, freq in sorted(counter.items(), reverse=True):
            if num == freq:
                return num

        return -1

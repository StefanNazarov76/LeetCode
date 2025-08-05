class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        baskets.reverse()
        counter = 0

        for f in fruits:
            for i in range(len(baskets) - 1, -1, -1):
                if baskets[i] >= f:
                    baskets.pop(i)
                    break
            else:
                counter += 1

        return counter

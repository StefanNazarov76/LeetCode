class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []

        for i in range(len(boxes)):
            sum = 0

            for j, b in enumerate(boxes):
                if b == '1':
                    sum += abs(i - j)

            ans.append(sum)

        return ans

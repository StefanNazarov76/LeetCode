class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []

        for i in range(len(boxes)):
            moves = 0

            # left
            for j in range(0, i + 1):
                if boxes[j] == '1':
                    moves += i - j

            # right
            for k in range(i, len(boxes)):
                if boxes[k] == '1':
                    moves += k - i

            ans.append(moves)

        return ans

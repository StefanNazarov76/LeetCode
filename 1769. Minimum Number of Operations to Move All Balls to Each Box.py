class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ops = []
        cur_ops = 0
        left = 0
        right = 0

        for i, b in enumerate(boxes):
            if b == '1':
                cur_ops += i
                left += 1

        for b in boxes:
            ops.append(cur_ops)
            if b == '1':
                left -= 1
                right += 1
            cur_ops = cur_ops - left + right

        return ops

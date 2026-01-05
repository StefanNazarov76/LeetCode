class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_abs_num = float('inf')
        total_sum = 0
        neg_count = 0

        for row in matrix:
            for num in row:
                if num < 0:
                    neg_count += 1

                min_abs_num = min(abs(num), min_abs_num)
                total_sum += abs(num)

        if neg_count % 2 == 0:
            return total_sum
        else:
            return total_sum - 2 * min_abs_num

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = 0
        max_area = 0

        for rec in dimensions:
            diagonal = sqrt(rec[0] * rec[0] + rec[1] * rec[1])

            if diagonal > max_diagonal:
                max_diagonal = diagonal
                max_area = rec[0] * rec[1]

            elif diagonal == max_diagonal:
                max_area = max(max_area, rec[0] * rec[1])

        return max_area

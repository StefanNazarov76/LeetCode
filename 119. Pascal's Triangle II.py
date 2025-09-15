class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for i in range(1, rowIndex + 1):
            prev = row[-1]
            next_val = prev * (rowIndex - i + 1) // i
            row.append(next_val)

        return row

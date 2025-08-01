class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]

        for _ in range(1, numRows):
            prev = ans[-1]
            row = [1]

            for i in range(len(prev) - 1):
                row.append(prev[i] + prev[i + 1])

            row.append(1)
            ans.append(row)

        return ans

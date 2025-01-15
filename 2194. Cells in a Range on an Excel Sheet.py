class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        res = []

        for cur_col in range(ord(s[0]), ord(s[3]) + 1):
            for cur_row in range(int(s[1]), int(s[4]) + 1):
                res.append(f'{chr(cur_col)}{cur_row}')

        return res

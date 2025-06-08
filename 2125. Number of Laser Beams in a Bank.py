class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0

        for i in range(len(bank)):
            r1 = bank[i].count('1')

            for j in range(i + 1, len(bank)):
                r2 = bank[j].count('1')

                if r2 > 0:
                    ans += r1 * r2
                    break

        return ans
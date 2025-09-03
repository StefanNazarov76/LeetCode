class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            chunks = [s[i:i + k] for i in range(0, len(s), k)]
            s = ''

            for chunk in chunks:
                chunk_sum = sum(int(d) for d in chunk)
                s += str(chunk_sum)

        return s

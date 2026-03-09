class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            temp = ''

            for i in range(0, len(s), k):
                group = s[i:i + k]
                group_sum = sum(int(d) for d in group)
                temp += str(group_sum)

            s = temp
        return s

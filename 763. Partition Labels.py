class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partitions = {}

        for i in range(len(s)):
            if s[i] in partitions:
                partitions[s[i]][1] = i
            else:
                partitions[s[i]] = [i, i]

        arr = [value for value in partitions.values()]
        arr.sort()
        endValue = arr[0][1]
        res = [arr[0]]
        for begin, end in arr[1:]:
            if res[-1][1] >= begin:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([begin, end])

        ans = []
        for x, y in res:
            ans.append(y - x + 1)
        return ans

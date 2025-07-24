class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)
        min_num = num.replace(num[0], '0')

        max_num = num
        for i in num:
            if i != '9':
                max_num = num.replace(i, '9')
                break

        return int(max_num) - int(min_num)

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = []

        temp = ''
        for i in s:
            if i.isdigit():
                temp += i
            elif temp:
                nums.append(int(temp))
                temp = ''

        if temp:
            nums.append(int(temp))

        return nums == sorted(set(nums))

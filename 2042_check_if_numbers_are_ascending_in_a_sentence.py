class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        numbers = [int(word) for word in s.split(' ') if word.isnumeric()]

        prev = numbers[0]

        if len(numbers) == 1:
            return True

        for num in numbers[1:]:
            if num <= prev:
                return False
            prev = num
        return True

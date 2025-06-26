class Solution:
    def hasSameDigits(self, s: str) -> bool:
        numbers = [int(i) for i in s]

        while len(numbers) != 2:
            curr = []

            for i in range(len(numbers) - 1):
                curr.append((numbers[i] + numbers[i + 1]) % 10)

            numbers = curr

        return numbers[0] == numbers[1]

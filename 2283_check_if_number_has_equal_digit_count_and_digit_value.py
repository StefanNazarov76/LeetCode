class Solution:
    def digitCount(self, num: str) -> bool:
        counter = Counter(num)

        for i, digit in enumerate(num):
            if counter[str(i)] != int(digit):
                return False

        return True

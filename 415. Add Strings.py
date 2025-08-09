class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = []

        num1 = num1[::-1]
        num2 = num2[::-1]

        carry = 0
        i = 0

        while i < len(num1) or i < len(num2) or carry:
            d1 = int(num1[i]) if i < len(num1) else 0
            d2 = int(num2[i]) if i < len(num2) else 0

            total = d1 + d2 + carry
            carry = total // 10
            ans.append(str(total % 10))

            i += 1

        return ''.join(ans[::-1])

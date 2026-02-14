class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        balance = 0

        for ch in s:
            if ch == '(':
                balance += 1
            else:
                if balance > 0:
                    balance -= 1
                else:
                    ans += 1
        return ans + balance

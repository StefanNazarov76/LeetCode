class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        order = {
            'electronics': 0,
            'grocery': 1,
            'pharmacy': 2,
            'restaurant': 3
        }

        valid = []

        for i in range(len(code)):
            if not isActive[i]:
                continue

            if businessLine[i] not in order:
                continue

            if not code[i] or not all(c.isalnum() or c == '_' for c in code[i]):
                continue

            valid.append(i)

        valid.sort(key=lambda i: (order[businessLine[i]], code[i]))

        return [code[i] for i in valid]

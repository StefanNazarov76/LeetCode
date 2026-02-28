class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = min_penalty = customers.count('Y')
        best_hour = 0

        for i, c in enumerate(customers):
            penalty += 1 if c == 'N' else -1

            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = i + 1

        return best_hour

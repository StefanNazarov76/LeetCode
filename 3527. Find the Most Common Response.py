class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        responses = [resp for row in responses for resp in set(row)]
        counter = Counter(responses)

        max_count = max(counter.values())
        most_common_responses = [r for r, c in counter.items() if c == max_count]

        return sorted(most_common_responses)[0]

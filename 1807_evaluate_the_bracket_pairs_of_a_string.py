class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge = {p[0]: p[1] for p in knowledge}

        is_open = False
        ans = ''
        key = ''

        for ch in s:
            if ch == '(':
                is_open = True
                key = ''

            elif ch == ')':
                is_open = False
                ans += knowledge.get(key, '?')

            elif is_open:
                key += ch

            else:
                ans += ch

        return ans

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        s = s.replace('(', ' (').replace(')', ') ').split()
        knowledge = dict(knowledge)

        for i in range(len(s)):
            if s[i][0] == '(':
                key = s[i][1:-1]
                s[i] = knowledge.get(key, '?')

        return ''.join(s)

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        counter = 0

        for i in items:
            if ruleKey == 'type' and i[0] == ruleValue:
                counter += 1
            elif ruleKey == 'color' and i[1] == ruleValue:
                counter += 1
            elif ruleKey == 'name' and i[2] == ruleValue:
                counter += 1

        return counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_s = Counter(s)
        counter_t = Counter(t)

        if counter_s == counter_t:
            return 0
        else:
            return sum((counter_s - counter_t).values()) +  sum((counter_t - counter_s).values())

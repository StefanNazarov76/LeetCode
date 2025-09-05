class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def convert_to_mins(time):
            hours, mins = time.split(':')
            return hours * 60 + mins

        return min(convert_to_mins(event1[1]), convert_to_mins(event2[1])) >= max(convert_to_mins(event1[0]), convert_to_mins(event2[0]))

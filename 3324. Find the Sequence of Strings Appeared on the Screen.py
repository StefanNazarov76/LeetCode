class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ans = []
        string = ''

        for i in range(0, len(target)):
            start = 97
            curr_string = string

            while True:
                curr_string = string + chr(start)
                ans.append(curr_string)

                if chr(start) == target[i]:
                    break

                start += 1

            string = curr_string

        return ans

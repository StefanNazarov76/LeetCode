class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter = Counter(s)
        letters = sorted(counter.keys(), reverse=True)
        ans = ''

        while letters:
            for i in range(len(letters)):
                if counter[letters[i]] > 0:
                    break
            else:
                break

            l = letters[i]

            use = min(counter[l], repeatLimit)
            ans += l * use
            counter[l] -= use

            if counter[l] > 0:
                found = False

                for j in range(i + 1, len(letters)):
                    if counter[letters[j]] > 0:
                        ans += letters[j]
                        counter[letters[j]] -= 1
                        found = True
                        break

                if not found:
                    break

        return ans

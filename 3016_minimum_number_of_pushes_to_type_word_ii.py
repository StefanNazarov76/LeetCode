class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        buttons = 9
        pushes_per_button = 1

        for _, freq in Counter(word).most_common():
            buttons -= 1

            if buttons == 0:
                buttons = 8
                pushes_per_button += 1

            ans += freq * pushes_per_button

        return ans

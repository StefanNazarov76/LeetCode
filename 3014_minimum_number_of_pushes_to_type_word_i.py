class Solution:
    def minimumPushes(self, word: str) -> int:
        buttons_left = 8
        pushes = 1

        keyboard = {}
        ans = 0

        for ch in word:
            if ch not in keyboard:
                if buttons_left == 0:
                    pushes += 1
                    buttons_left = 8

                keyboard[ch] = pushes
                buttons_left -= 1

            ans += keyboard[ch]

        return ans

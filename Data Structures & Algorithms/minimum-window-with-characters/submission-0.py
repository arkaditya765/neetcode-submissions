from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t)
        window = {}

        left = 0
        have = 0
        need_count = len(need)

        best_len = float("inf")
        best_left = 0

        for right in range(len(s)):
            char = s[right]

            window[char] = window.get(char, 0) + 1

            # We have enough of this character
            if char in need and window[char] == need[char]:
                have += 1

            # Window contains everything we need
            while have == need_count:
                # Update best answer
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left

                # Remove left character
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_left:best_left + best_len]
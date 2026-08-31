class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""

        # Count how many of each character we need
        need = {}

        for c in t:
            need[c] = need.get(c, 0) + 1

        # Count characters inside our current window
        window = {}

        left = 0

        # Number of character requirements currently satisfied
        have = 0

        # Number of different characters we need
        required = len(need)

        # Store the best window
        best_left = 0
        best_length = float("inf")

        # Move right pointer through s
        for right in range(len(s)):

            c = s[right]

            # Add c to our window
            window[c] = window.get(c, 0) + 1

            # Did we just satisfy a requirement?
            if c in need and window[c] == need[c]:
                have += 1

            # If all requirements are satisfied,
            # try making the window smaller
            while have == required:

                # Is this the smallest window so far?
                length = right - left + 1

                if length < best_length:
                    best_length = length
                    best_left = left

                # Remove the leftmost character
                left_char = s[left]
                window[left_char] -= 1

                # Did removing it make the window invalid?
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        # No valid window found
        if best_length == float("inf"):
            return ""

        return s[best_left:best_left + best_length]
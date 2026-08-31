class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}
        left = 0
        have = 0
        required = len(need)

        best = ""
        
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == required:
                current = s[left:right + 1]

                if best == "" or len(current) < len(best):
                    best = current

                left_c = s[left]
                window[left_c] -= 1

                if left_c in need and window[left_c] < need[left_c]:
                    have -= 1

                left += 1

        return best
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        have = {}
        formed = 0
        required = len(need)

        left = 0
        best_len = float("inf")
        best_start = 0

        for right, ch in enumerate(s):
            have[ch] = have.get(ch, 0) + 1

            if ch in need and have[ch] == need[ch]:
                formed += 1

            while formed == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left

                left_char = s[left]
                have[left_char] -= 1

                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        return "" if best_len == float("inf") else s[best_start:best_start + best_len]

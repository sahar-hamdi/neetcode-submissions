class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        n = len(sorted_s)
        cnt = 0

        if len(sorted_s) != len(sorted_t):
            return False

        else:
            return sorted_s == sorted_t
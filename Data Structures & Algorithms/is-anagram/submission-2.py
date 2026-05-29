class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        n = len(sorted_s)
        cnt = 0

        if len(sorted_s) != len(sorted_t):
            return False

        else:
            for i in range(n):
                if sorted_s[i] == sorted_t[i]:
                    cnt += 1


            if cnt == n :
                return True
            else:
                return False
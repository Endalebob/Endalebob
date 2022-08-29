class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        @cache
        def rec(s,c):
            if s == n:
                return 1
            if s > n:
                return n
            return min(rec(s+c,c),rec(s+c,s+c)+1)+1
        return rec(1,1)
        
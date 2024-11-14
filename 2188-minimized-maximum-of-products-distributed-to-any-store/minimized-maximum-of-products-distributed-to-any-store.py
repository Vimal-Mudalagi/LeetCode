class Solution:
    def minimizedMaximum(self, n: int, a: List[int]) -> int:
        def pos(L):
            return sum((x + L - 1) // L for x in a) <= n
        
        low, hi = 1, max(a)
        while low < hi:
            mid = (low + hi) >> 1
            if(pos(mid)):
                hi = mid
            else:
                low = mid + 1
        
        return low
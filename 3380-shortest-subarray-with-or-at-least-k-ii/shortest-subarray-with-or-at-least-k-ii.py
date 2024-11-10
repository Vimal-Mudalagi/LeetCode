class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        suffix = {}
        ans = inf

        for a, x in enumerate(nums):
            suffix = {val | x: l for val, l in suffix.items()}
            suffix[x] = a
            
            for val, l in suffix.items():
                if val >= k:
                    ans = min(ans, a - l + 1)
        
        if ans == inf:
            return -1
        return ans

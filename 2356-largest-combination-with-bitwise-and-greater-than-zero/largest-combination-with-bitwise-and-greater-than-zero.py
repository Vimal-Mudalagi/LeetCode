class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_len = 0
        
        for i in range(24):
            x = 1 << i  
            cnt = sum(1 for num in candidates if num & x)  
            max_len = max(max_len, cnt)
        
        return max_len
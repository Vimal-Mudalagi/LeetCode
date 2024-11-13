class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        less=0
        n=len(nums)
        l,r=0,n-1
        while l<r:
            if nums[l]+nums[r]>=lower:
                r-=1
            else:
                less+=(r-l)
                l+=1
        l,r=0,n-1
        more=0
        while l<r:
            if nums[l]+nums[r]<=upper:
                l+=1
            else:
                more+=(r-l)
                r-=1
        return (n*(n-1)//2)-less-more




        
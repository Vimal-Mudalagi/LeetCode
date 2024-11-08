class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n=len(nums)
        prev=[]
        mask=(1<<maximumBit)-1
        for x in nums:
            prev.append(mask^x)
            mask=mask^x
        prev.reverse()
        return prev
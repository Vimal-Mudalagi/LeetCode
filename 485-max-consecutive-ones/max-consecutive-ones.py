class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCount, currentCount = 0, 0
        for n in nums:
            if n == 1:
                currentCount += 1
            else:
                maxCount = max(maxCount, currentCount) 
                currentCount = 0
        maxCount = max(maxCount, currentCount) 
        return maxCount        


        
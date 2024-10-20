class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        maxSum = float('-inf')  
        for num in nums:
            sum += num
            maxSum = max(maxSum, sum)
            if sum < 0:
                sum = 0          
        return maxSum

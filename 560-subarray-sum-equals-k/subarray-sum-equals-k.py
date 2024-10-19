class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefixSum = {0: 1}
        currentSum = 0
        count = 0
        
        for num in nums:
            currentSum += num
            
            if currentSum - k in prefixSum:
                count += prefixSum[currentSum - k]
            
            if currentSum in prefixSum:
                prefixSum[currentSum] += 1
            else:
                prefixSum[currentSum] = 1
        
        return count

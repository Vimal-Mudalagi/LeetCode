class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        prefixSum=0
        sumFreq={0:1}
        for i in range(len(nums)):
            prefixSum+=nums[i]
            if prefixSum-k in sumFreq:
                count+=sumFreq[prefixSum-k]
            if prefixSum in sumFreq:
                sumFreq[prefixSum]+=1
            else:
                sumFreq[prefixSum]=1
        return count

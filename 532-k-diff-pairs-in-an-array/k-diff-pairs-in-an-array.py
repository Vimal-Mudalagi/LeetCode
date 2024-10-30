class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0        
        countMap = {}
        for num in nums:
            countMap[num] = countMap.get(num, 0) + 1     
        count = 0
        for num in countMap:
            if k == 0:
                if countMap[num] > 1:
                    count += 1
            else:
                if (num + k) in countMap:
                    count += 1       
        return count

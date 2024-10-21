class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet=set(nums)
        longestSeq=0
    
        for num in nums:
            if num-1 not in numSet:
                currentNum=num
                count=1
                while currentNum+1 in numSet:
                    currentNum+=1
                    count+=1
                longestSeq=max(longestSeq, count)
        return longestSeq
                
                
              

              
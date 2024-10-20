class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element = None
        count = 0
  
        for num in nums:
          if count == 0:
            element = num
            count = 1
          elif num == element:
            count += 1
          else:
            count -= 1
        count = 0
        for num in nums:
         if num == element:
            count += 1
         if count > len(nums) // 2:
          return element
        else:
         return -1
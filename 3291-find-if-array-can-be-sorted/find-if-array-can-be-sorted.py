from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        def setBits(num):
            count = 0
            for i in range(31, -1, -1):
                if ((num >> i) & 1) == 1:
                    count += 1
            return count

        def check(nums):
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
            return True
        count = [setBits(num) for num in nums]

        n = len(nums)
        k = 0
        while k < n:
            for i in range(1, n):
                if count[i] == count[i - 1] and nums[i] < nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i] 
            if check(nums):
                return True
            k += 1

        return False
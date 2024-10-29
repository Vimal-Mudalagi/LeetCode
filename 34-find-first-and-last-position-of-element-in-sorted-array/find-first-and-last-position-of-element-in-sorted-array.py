class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findFirst(nums, target):
            low, high = 0, len(nums) - 1
            first = -1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    first = mid
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return first
        
        def findLast(nums, target):
            low, high = 0, len(nums) - 1
            last = -1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] == target:
                    last = mid
                    low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return last

        return [findFirst(nums, target), findLast(nums, target)]

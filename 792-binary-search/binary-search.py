class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lft,rgt = 0,len(nums) - 1
        while lft <= rgt:
            mid=(lft + rgt) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                lft=mid+1
            else:
                rgt=mid-1
        return -1

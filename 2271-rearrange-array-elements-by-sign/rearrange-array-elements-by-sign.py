class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        pos = [x for x in nums if x >= 0]  
        neg = [x for x in nums if x < 0]  
        
        i, p, q = 0, 0, 0  
        while p < len(pos) and q < len(neg):
            if i % 2 == 0:
                nums[i] = pos[p]
                p += 1
            else:
                nums[i] = neg[q]
                q += 1
            i += 1
        while p < len(pos):
            nums[i] = pos[p]
            p += 1
            i += 1        
        while q < len(neg):
            nums[i] = neg[q]
            q += 1
            i += 1        
        return nums

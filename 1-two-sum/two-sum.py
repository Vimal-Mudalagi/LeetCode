class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        original_i = {num: idx for idx, num in enumerate(nums)}
        sorted_arr = sorted(nums)
       
        left, right = 0, len(sorted_arr) - 1
        while left < right:
            current_sum = sorted_arr[left] + sorted_arr[right]
            if current_sum == target:
                num1, num2 = sorted_arr[left], sorted_arr[right] 
                if num1 == num2:
                    first_i = nums.index(num1)
                    second_i = nums.index(num2, first_i + 1)
                else:
                    first_i = original_i[num1]
                    second_i = original_i[num2]
                
                return [first_i, second_i]
            
            elif current_sum < target:
                left += 1  
            else:
                right -= 1 
        return []

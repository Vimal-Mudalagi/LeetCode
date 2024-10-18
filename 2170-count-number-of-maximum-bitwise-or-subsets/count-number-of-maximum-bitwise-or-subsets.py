class Solution(object):
    def countMaxOrSubsets(self, nums):
        maxOR = 0
        count = [0]  

        for num in nums:
            maxOR |= num

        def backtrack(index, currentOR):
            if index == len(nums):
                if currentOR == maxOR:
                    count[0] += 1
                return

            backtrack(index + 1, currentOR | nums[index])
            backtrack(index + 1, currentOR)

        backtrack(0, 0)
        return count[0]


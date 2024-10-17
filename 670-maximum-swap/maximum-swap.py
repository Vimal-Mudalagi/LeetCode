class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = list(str(num))
        n = len(digits)
        maxValueIdx = n - 1  
        swapLeft = -1 
        swapRight = -1  
        
        for i in range(n - 2, -1, -1):
            if digits[i] > digits[maxValueIdx]:
                maxValueIdx = i
            elif digits[i] < digits[maxValueIdx]:                
                swapLeft = i
                swapRight = maxValueIdx
        
        if swapLeft != -1:
            digits[swapLeft], digits[swapRight] = digits[swapRight], digits[swapLeft]
        
        return int(''.join(digits))



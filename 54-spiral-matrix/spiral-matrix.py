class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result=[]
        if not matrix:
            return result
        top,btm=0,len(matrix)-1
        left,right=0,len(matrix[0])-1
        while top<=btm and left<=right:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top+=1
            for i in range(top,btm+1):
                result.append(matrix[i][right])
            right-=1
            if top<=btm:
                for i in range(right,left-1,-1):
                    result.append(matrix[btm][i])
                btm-=1
            if left<=right:
                for i in range(btm,top-1,-1):
                    result.append(matrix[i][left])
                left+=1
        return result

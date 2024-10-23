class Solution(object):
    def generate(self,numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        Ptriangle=[]
        for i in range(numRows):
            row=[1]*(i+1)
            for j in range(1,i):
                row[j]=Ptriangle[i-1][j-1]+Ptriangle[i-1][j]
            Ptriangle.append(row)
        return Ptriangle
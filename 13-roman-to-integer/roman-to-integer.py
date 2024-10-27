class Solution(object):
    def romanToInt(self,s):
        """
        :type s: str
        :rtype: int
        """
        romanInt={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total=0
        for i in range(len(s)):
            if i<len(s)-1 and romanInt[s[i]]<romanInt[s[i+1]]:
                total-=romanInt[s[i]]
            else:
                total+=romanInt[s[i]]
        return total

        
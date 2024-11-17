class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        currsum, ans = 0, inf
        q=deque()
        
        for i in range(len(nums)):
            currsum+=nums[i]
            if currsum>=k and i+1<ans: ans=i+1

            while q and currsum-q[0][0]>=k:
                prefix,idx=q.popleft()
                if i-idx<ans: ans=i-idx
                
            while q and q[-1][0]>=currsum: q.pop()
            
            q.append((currsum,i))
            
        return ans if ans!=inf else -1
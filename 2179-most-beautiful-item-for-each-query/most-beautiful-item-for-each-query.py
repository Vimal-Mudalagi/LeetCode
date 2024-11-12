class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key = lambda x : x[0])
        map = {}
        prices = []
        maxi = -1
        for i in items:
            if i[0] not in map:
                prices.append(i[0])
            maxi = max(maxi,i[1])
            map[i[0]] = maxi

        ans = []
        for i in queries:
            if i in map:
                ans.append(map[i])
            else:
                ind = bisect.bisect_left(prices,i)
                if ind == 0:
                    ans.append(0)
                else:
                    key = prices[ind-1]
                    ans.append(map[key])
        return ans

        
        
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        mergedIntervals = []

        for pair in intervals:
            if not mergedIntervals or mergedIntervals[-1][1] < pair[0]:
                mergedIntervals.append(pair)
            else:
                mergedIntervals[-1][1] = max(mergedIntervals[-1][1], pair[1])

        return mergedIntervals

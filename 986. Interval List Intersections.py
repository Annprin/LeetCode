class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        firstI, secondI = 0, 0
        ans = []
        while firstI < len(firstList) and secondI < len(secondList):
            firstStart, firstEnd = firstList[firstI]
            secondStart, secondEnd = secondList[secondI]
            if firstEnd >= secondStart and firstStart <= secondEnd:
                ans.append([max(firstStart, secondStart), min(firstEnd, secondEnd)])
            if firstEnd <= secondEnd:
                firstI += 1
            else:
                secondI += 1
        return ans
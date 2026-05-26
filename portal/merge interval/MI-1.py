'''Interval List Intersections
You are given two lists of closed intervals, firstList and secondList, where:


firstList[i]  = [starti, endi]
secondList[j] = [startj, endj]
Each list of intervals is:

pairwise disjoint
(intervals within the same list do not overlap)

sorted in ascending order by start time

Return the intersection of these two interval lists.

A closed interval [a, b] represents all real numbers x such that:   
a≤x≤b
The intersection of two closed intervals is either:

another closed interval

or empty


Input:
firstList  = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]

Output:
[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]'''
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        result = []

        while i<len(firstList) and j<len(secondList):
            a1, a2 = firstList[i]
            b1, b2 = secondList[j]

            if a1<=b2 and b1<=a2:
                result.append([max(a1, b1), min(a2, b2)])

            if a2<b2:
                i += 1
            else:
                j += 1

        return result
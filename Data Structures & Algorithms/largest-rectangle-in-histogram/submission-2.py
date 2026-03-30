class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        for i,h in enumerate(heights):
            rightMost = i + 1
            height = h
            while rightMost <n and heights[rightMost] >= h:
                rightMost +=1
            leftMost = i
            while leftMost >= 0 and heights[leftMost]>=h:
                leftMost -=1
            leftMost +=1
            rightMost -=1
            max_area = max(max_area, h*(rightMost - leftMost +1))
            
        return max_area
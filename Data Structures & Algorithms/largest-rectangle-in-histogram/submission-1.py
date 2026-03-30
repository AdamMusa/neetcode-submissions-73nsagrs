class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0

        for i in range(n):
            height = heights[i]
            rightMost = i + 1
            
            while rightMost < n and heights[rightMost] >= height:
                rightMost +=1
            
            leftMost = i
            while leftMost >=0 and heights[leftMost] >= height:
                leftMost -=1
            rightMost -=1
            leftMost +=1
            max_area = max(max_area, height*(rightMost - leftMost +1))
        return max_area
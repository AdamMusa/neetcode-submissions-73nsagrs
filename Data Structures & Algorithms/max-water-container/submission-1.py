class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                erea = (j-i)*min(heights[i], heights[j])
                res = max(erea, res)
        return res
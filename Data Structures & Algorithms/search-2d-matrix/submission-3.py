class Solution:
    def search(self, l: int, r: int, matrix: List[List[int]], target):
        if l > r:
            return False
        m = l + (r-l) //2
        if target <= matrix[m][-1] and target >= matrix[m][0]:
            return target in matrix[m]
        if target > matrix[m][-1]:
            return self.search(m +1, r, matrix, target)
        return self.search(l, m-1, matrix, target) 
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.search(0, len(matrix) -1 , matrix, target)
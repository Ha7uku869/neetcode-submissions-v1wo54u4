class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, len(matrix) * len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_row = mid // rows
            mid_col = mid // cols
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
             
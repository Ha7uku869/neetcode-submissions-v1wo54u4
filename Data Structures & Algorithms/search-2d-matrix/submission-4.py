class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix[0])
        col = len(matrix)
        left = 0
        right = row * col - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            mid_col = mid // row
            mid_row = mid % row
            if target == matrix[mid_col][mid_row]:
                return True
            elif target <= matrix[mid_col][mid_row]:
                right = mid - 1
            else:
                left = mid + 1

        return False
            

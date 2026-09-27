class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix[0])
        length = len(matrix) * rowLen
        
        low, high = 0, length - 1
        while low <= high:
            mid = (high - low) // 2 + low
            c, r = mid % rowLen, mid // rowLen
            if matrix[r][c] > target:
                high = mid - 1
            elif matrix[r][c] < target:
                low = mid + 1
            else:
                return True
        return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        row = 0

        while l <= r:
            mid = l + (r - l) // 2
            if matrix[mid][0] > target and matrix[mid][-1] > target:
                r = mid - 1
            elif matrix[mid][0] < target and matrix[mid][-1] < target:
                l = mid + 1
            else:
                row = mid
                break
        
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        return False

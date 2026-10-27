class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        l, r = 0, R * C - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            row, col = mid // C, mid % C
            midNum = matrix[row][col]
            if midNum < target:
                l = mid + 1
            elif midNum > target:
                r = mid - 1
            else:
                return True
        return False


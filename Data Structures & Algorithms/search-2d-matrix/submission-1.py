class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # establish low, high for rows
        low, high = 0, m - 1
        while low <= high:
            i = (high - low) // 2 + low
            firstVal, lastVal = matrix[i][0], matrix[i][n-1]
            if firstVal > target and lastVal > target:
                high = i - 1
            elif firstVal < target and lastVal < target:
                low = i + 1
            else:
                break
        # i will be the row target may be located in
        row = i
        low, high = 0, n - 1
        while low <= high:
            i = (high - low) // 2 + low
            if matrix[row][i] > target:
                high = i - 1
            elif matrix[row][i] < target:
                low = i + 1
            else:
                return True
        return False

        
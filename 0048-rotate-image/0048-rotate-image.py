class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for row in matrix:
            row.reverse()
        n=len(matrix)
        for i in range(n):
            for j in range(n-i):
                matrix[i][j],matrix[n-j-1][n-i-1]=matrix[n-j-1][n-i-1],matrix[i][j]
        return matrix
        """
        Do not return anything, modify matrix in-place instead.
        """
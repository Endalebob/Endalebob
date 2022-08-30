class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mat = copy.deepcopy(matrix)
        R = len(matrix)-1
        for i in range(R+1):
            for j in range(R+1):
                matrix[j][R-i] = mat[i][j]
        
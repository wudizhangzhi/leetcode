#coding=utf8

'''
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1: 
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
Example 2: 
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.

'''
import copy

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        shape = (len(matrix), len(matrix[0])) 
        #matrix_result = copy.copy(matrix)
        for i in range(shape[0]):
            for j in range(shape[1]):
                distance = self.findNearest(matrix, i, j)
                #matrix_result[i][j] = distance
                matrix[i][j] = distance
        return matrix
                    

    def findNearest(self, matrix, i, j, distance=1):
        #print("=== %s  %s ===" % ((i, j), distance))
        if matrix[i][j] == 0:
            return 0
        height = len(matrix)
        width = len(matrix[0])
        for d in range(-distance, distance+1):
            _d = distance - abs(d) 
            if 0 <= i+d <= height-1 and 0 <= j+_d <= width-1:
                #print((i+d, j+_d), '+', matrix[i+d][j+_d])
                if matrix[i+d][j+_d] == 0: 
                    return distance
            if 0 <= i+d <= height-1 and 0 <= j-_d <= width-1:
                #print((i+d, j-_d), '-', matrix[i+d][j-_d])
                if matrix[i+d][j-_d] == 0:
                    return distance
        else:
            if distance < width + height:
                return self.findNearest(matrix, i, j, distance=distance+1)
    def updateMatrix2(self, matrix):
        matrix  = [[10000*i for i in row] for row in matrix]
        for _ in range(4):
            for row in matrix:
                for i in range(1, len(row)): 
                    row[i] = min(row[i], row[i-1]+1) 
            matrix = map(list, zip(*matrix[::-1]))
        return matrix
        
if __name__ == '__main__':
    inputs = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    #inputs = [[0],[0],[0],[0],[0]] 
    sol = Solution()
    #distance = sol.findNearest(inputs, 1, 2)
    #print(distance)
    result = sol.updateMatrix(inputs)
    for i in result:
        print(i)
    result = sol.updateMatrix2(inputs)
    for i in result:
        print(i)


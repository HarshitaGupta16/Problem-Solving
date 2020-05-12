'''
    733. Flood Fill
    https://leetcode.com/problems/flood-fill/
    11/05/2020
    May LeetCoding Challenge
    Day-11
    
    An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
    Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.DFS(image, sr, sc, newColor, image[sr][sc])
        return image
    
    def DFS(self, image: List[List[int]], row: int, col: int, newColor: int, oldColor: int):
        if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] == newColor:
            return 
        if(image[row][col] == oldColor):
            image[row][col] = newColor
            self.DFS(image, row + 1, col, newColor, oldColor)
            self.DFS(image, row - 1, col, newColor, oldColor)
            self.DFS(image, row, col + 1, newColor, oldColor)
            self.DFS(image, row, col - 1, newColor, oldColor)

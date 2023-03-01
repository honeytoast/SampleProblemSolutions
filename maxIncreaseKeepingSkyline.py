"""

Solution to https://leetcode.com/problems/max-increase-to-keep-city-skyline/

There is a city composed of n x n blocks, where each block contains a single
building shaped like a vertical square prism. You are given a 0-indexed n x n
integer matrix grid where grid[r][c] represents the height of the building located
in the block at row r and column c.

A city's skyline is the the outer contour formed by all the building when
viewing the side of the city from a distance. The skyline from each cardinal
direction north, east, south, and west may be different.

We are allowed to increase the height of any number of buildings by any amount
(the amount can be different per building). The height of a 0-height building
can also be increased. However, increasing the height of a building should not
affect the city's skyline from any cardinal direction.

Return the maximum total sum that the height of the buildings can be increased
by without changing the city's skyline from any cardinal direction.

"""

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        output = 0

        rows = len(grid)
        if rows < 0:
            return 0

        # transpose the matrix for easy column access
        columns = [[row[i] for row in grid] for i in range(rows)]

        for row in range(rows):
            for col in range(len(columns)):
                # max_height is the height that grid[row][col] can grow to without modifying the skyline
                max_height = min(max(grid[row]), max(columns[col]))
                diff = max_height - grid[row][col]
                if diff >= 0:
                    output += diff

        return output

if __name__ == '__main__':
    grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    A = Solution()
    print(A.maxIncreaseKeepingSkyline(grid))
    

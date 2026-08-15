class Solution:
    def mark0(self, grid, i, j):
        n = len(grid)
        m = len(grid[0])

        # First: check boundaries
        if i >= n or i < 0 or j >= m or j < 0:
            return

        # Second: check if it is water
        if grid[i][j] != '1':
            return

        grid[i][j] = 'L'

        self.mark0(grid, i-1, j)
        self.mark0(grid, i+1, j)
        self.mark0(grid, i, j+1)
        self.mark0(grid, i, j-1)

    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    self.mark0(grid, i, j)
                    count += 1

        return count
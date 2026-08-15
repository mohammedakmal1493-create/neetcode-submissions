class Solution:
    def mark0(self, grid, i, j):
        n = len(grid)
        m = len(grid[0])

        # 1. Outside the grid?
        if i < 0 or i >= n or j < 0 or j >= m:
            return

    # 2. Not an unvisited island cell?
        if grid[i][j] != '1':
            return

    # 3. Mark as visited
        grid[i][j] = 'L'

    # 4. Go in four directions
        self.mark0(grid, i-1, j)
        self.mark0(grid, i+1, j)
        self.mark0(grid, i, j-1)
        self.mark0(grid, i, j+1)

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
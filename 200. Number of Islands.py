class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        count = 0
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]

        def dfs(i, j):
            if i<0 or j<0 or i>= n or j >= m or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            for di, dj in directions:
                dfs(i + di, j + dj)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        if len(grid) == 0:
            return 0
        def findLoop(row, col):
            while grid[row][col] != 0:
                for row in range(len(grid)):
                    for col in range(len(grid[0])):
                        if grid[row][col] == 1:
                            dfs(row, col)


        def dfs(cur_row, cur_col):
            cnt = 4
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if grid[cur_row + i][cur_col + j] == 1:
                    cnt -= 1
                    dfs(cur_row + i, cur_col + j)
                ans += cnt
            return 0

        findLoop(0, 0)
        return ans
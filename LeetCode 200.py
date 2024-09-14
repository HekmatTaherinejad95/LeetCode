class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # If the grid is empty, return 0
        if not grid or not grid[0]:
            return 0

        # Dimensions of the grid
        rows, cols = len(grid), len(grid[0])

        # Initialize island count
        num_islands = 0

        # Define DFS function to traverse the grid
        def dfs(r, c):
            # Check boundaries and if the current cell is land ('1')
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return
            # Mark the current cell as visited by setting it to '0'
            grid[r][c] = '0'
            # Explore all adjacent cells (up, down, left, right)
            dfs(r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs(r, c + 1)  # Right

        # Iterate over each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell is land, perform DFS
                if grid[r][c] == '1':
                    dfs(r, c)
                    num_islands += 1  # Increment the island count

        return num_islands

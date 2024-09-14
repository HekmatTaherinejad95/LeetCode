class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Check if the grid is empty
        if not grid or not grid[0]:
            return 0

        # Dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        # Define DFS function to compute the area of an island
        def dfs(r, c):
            # Base case: check boundaries and if the cell is land
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0
            # Mark the cell as visited by setting it to 0
            grid[r][c] = 0
            # Initialize area as 1 for the current cell
            area = 1
            # Explore all four directions
            area += dfs(r - 1, c)  # Up
            area += dfs(r + 1, c)  # Down
            area += dfs(r, c - 1)  # Left
            area += dfs(r, c + 1)  # Right
            return area

        # Iterate over each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell is land, perform DFS to find the area
                if grid[r][c] == 1:
                    current_area = dfs(r, c)
                    # Update max_area if a larger area is found
                    max_area = max(max_area, current_area)

        return max_area

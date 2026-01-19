"""
# Problem: Islands and Treasure (Nearest Treasure Chest)
# [Link](https://neetcode.io/problems/islands-and-treasure/question?list=neetcode150)
#
# Pattern: Multi-Source Breadth-First Search (BFS)
#
# Key Invariant: 
# Every cell in the queue is processed in increasing order of its 
# distance from the nearest source. The first time a 'land' cell 
# is reached, the current path is guaranteed to be its shortest path.
#
# Complexity:
# - Time: O(M * N) where M is rows and N is columns.
# - Space: O(M * N) for the queue in the worst case.
"""
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])

        # Initialize queue for Multi-Source BFS
        # We start with ALL treasure chests as our search 'front'
        q = deque()

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 0:
                    q.append([row, col]) # Enqueue the coordinates of all treasure chests
        
        while q:
            row, col = q.popleft()

            dir = [[0, 1], [-1, 0], [0, -1], [1, 0]]

            for delrow, delcol in dir:
                nrow = row + delrow
                ncol = col + delcol

                # VALIDATION CHECK:
                # 1. Stay within grid boundaries
                # 2. Only visit cells that are currently INF (unvisited land)
                # This check implicitly skips water (-1) and already visited land.
                if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == 2147483647:
                    grid[nrow][ncol] = grid[row][col] + 1 # The distance to the nearest chest is current cell's distance + 1
                    q.append([nrow, ncol]) # Add this new land cell to the queue to find its neighbors

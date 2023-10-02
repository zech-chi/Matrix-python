class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        # possible moves :
        # up   : (-1, 0) 
        # left : (0, 1)
        # down : (1, 0)
        # right: (0, -1)
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
        # count solutions
        count_sol = 0
        # how much empty cell in the grid
        empty_cells = 0
        # start coordinates
        Sr, Sc = 0, 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    empty_cells += 1
                elif grid[r][c] == 1:
                    Sr, Sc = r, c

        def is_possible_move(r, c):
            nonlocal rows
            nonlocal cols
            if r < 0 or r >= rows:
                return False
            if c < 0 or c >= cols:
                return False
            if grid[r][c] == 0 or grid[r][c] == 2:
                return True
            return False

        def Backtrack(r, c, empty_cells):
            nonlocal count_sol
            
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if is_possible_move(nr, nc):
                    if grid[nr][nc] == 2:
                        if empty_cells == 0:
                            count_sol += 1
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = -1
                        Backtrack(nr, nc, empty_cells - 1)
                        grid[nr][nc] = 0
        
        Backtrack(Sr, Sc, empty_cells)
        return count_sol

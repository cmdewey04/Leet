# Last updated: 2/26/2026, 1:36:21 PM
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #We want to runs bfs from the rotting oranges
        ROWS,COLS = len(grid), len(grid[0])
        seen = set()
        q = deque()
        numFresh = 0

        #Add Rotting Oranges to Queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    seen.add((r,c))
                if grid[r][c] == 1:
                    numFresh += 1
        
        #No fresh oranges
        if not numFresh:
            return 0


        def rotOrange(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in seen or grid[r][c] == 0:
                return
            grid[r][c] = 2
            q.append((r,c))
            seen.add((r,c))

        minutes = -1
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                rotOrange(r-1,c)
                rotOrange(r+1,c)
                rotOrange(r,c-1)
                rotOrange(r,c+1)
            minutes+=1

        #Check if any oranges left
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return minutes

        
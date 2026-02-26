# Last updated: 2/26/2026, 1:36:31 PM
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS,COLS = len(rooms), len(rooms[0])
        seen = set()
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append((r,c))
                    seen.add((r,c))
        
        def appendRoom(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in seen or rooms[r][c] == -1:
                return
            queue.append((r,c))
            seen.add((r,c))

        dist = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                appendRoom(r-1,c) #up
                appendRoom(r+1,c) #down
                appendRoom(r,c-1) #left
                appendRoom(r,c+1) #right
                rooms[r][c] = dist
            dist+=1

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.result = False
        path = set()

        r, c = len(board), len(board[0])

        def promising(i, x, y):
            if self.result:
                return False
            # check horizontal bounds
            if x < 0 or x >= c:
                return False
            # check vertical bounds
            if y < 0 or y >= r:
                return False
            # check char
            if board[y][x] != word[i]:
                return False
            # check path
            if (x,y) in path:
                return False
            return True

        def dfs(i, x, y):
            if i >= len(word):
                self.result = True
                return
            if not promising(i, x, y):
                return

            path.add((x, y))

            # four direction
            # up
            dfs(i + 1, x, y - 1)
            # down
            dfs(i + 1, x, y + 1)
            # left
            dfs(i + 1, x - 1, y)
            # right
            dfs(i + 1, x + 1, y)

            path.remove((x,y))

        
        for y in range(r):
            for x in range(c):
                dfs(0, x, y)
    
        return self.result
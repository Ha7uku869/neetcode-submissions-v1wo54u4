class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for r in range(board):
            for c in range(board[0]):
                if board[r][c] == word[0]:
                    def dfs(r, c, i):
                        if i == len(word):
                            return True
                        if (r < 0 or r >= rows or
                            c < 0 or c >= cols or
                            board[r][c] != word[i]):
                            return False

                        tmp = board[r][c]
                        board[r][c] = "#"

                        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            if dfs(r + dr, c + dc, i + 1):
                                return True
                        

                        board[r][c] = tmp
                        return False
                    dfs(r, c, i)

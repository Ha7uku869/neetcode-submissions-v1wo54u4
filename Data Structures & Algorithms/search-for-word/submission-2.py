class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False

            tmp = board[r][c]
            board[r][c] = '#'  # 使用済みマーク

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if dfs(r + dr, c + dc, i + 1):
                    board[r][c] = tmp  # 後片付け
                    return True

            board[r][c] = tmp  # 後片付け
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
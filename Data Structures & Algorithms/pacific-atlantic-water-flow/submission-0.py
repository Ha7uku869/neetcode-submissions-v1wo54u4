from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            visited.add((r, c))

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                # 範囲外ならスキップ
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                # すでに訪問済みならスキップ
                if (nr, nc) in visited:
                    continue

                # 逆向き探索なので「同じ高さ以上」に進める
                if heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

        # Pacific: 上端と左端
        for c in range(cols):
            dfs(0, c, pacific)
        for r in range(rows):
            dfs(r, 0, pacific)

        # Atlantic: 下端と右端
        for c in range(cols):
            dfs(rows - 1, c, atlantic)
        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result
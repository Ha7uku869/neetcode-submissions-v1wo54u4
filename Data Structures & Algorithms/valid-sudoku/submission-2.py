class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_seen = {}
        row_seen = {}
        boxes_seen = {}

        for r in range(9):
            if r == '.':
                continue
            elif c in column_seen:
                return False
            else:
                row_seen[c] == 1

            for c in range(9):
                if c == '.':
                    continue
                elif c in column_seen:
                    return False
                else:
                    column_seen[c] == 1
                


                
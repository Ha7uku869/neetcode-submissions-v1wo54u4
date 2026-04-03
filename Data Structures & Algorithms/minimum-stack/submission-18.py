class MinStack:

    def __init__(self):
        self.stack = []      # メインのスタック
        self.min_stack = []  # 最小値を追跡する補助スタック

    def push(self, val: int) -> None:
        self.stack.append(val)
        # 最小値スタックが空、または現在の値が最小値以下なら追加
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        # もしポップした値が現在の最小値と等しければ、最小値スタックからも削除
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]  # 直接アクセスでOK

    def getMin(self) -> int:
        return self.min_stack[-1]  # O(1) で取得！
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #zipによる2つのリストの要素を順にペアリングしていく
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        stack = []
        for p, s in pair:
            time = (target - p) / s
            stack.append(time)
            
            # Pythonのリストでは、マイナスのインデックスを使うと「後ろから数えた要素」を取得できます。
            # stack[-1]: リストの一番最後の要素。この処理において「今まさにスタックに追加したばかりの要素」を指します。
            # stack[-2]: リストの後ろから2番目の要素。この処理において「1つ前に追加された要素」を指します。
            # Pythonの and 演算子には、「左側が False なら、右側は一切評価せずに判定を終了する」という重要な仕様（短絡評価）があります。
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)
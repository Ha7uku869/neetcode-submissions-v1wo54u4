from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.d[key]) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_key, mid_timestamp = self.d[key][mid]
            if mid_timestamp <= timestamp:
                res = mid_key
                left = mid + 1
            else:
                right = mid - 1
        return res


        

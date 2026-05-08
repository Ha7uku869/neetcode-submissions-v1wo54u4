from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.timemap[key]
        left = 0
        right = len(values) - 1
        res = ""

        while left <= right:
            mid = mid = (left + right) // 2
            mid_time, mid_value = values[mid]
            if mid_time <= timestamp:
                res = mid_value
                left = mid + 1
            else:
                right = mid - 1
        return res

        

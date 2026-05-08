from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(int)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp), value)

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        for t, v in self.timemap[key]:
            if t <= timestamp:
                res = v
            else:
                break
        return res
        
        

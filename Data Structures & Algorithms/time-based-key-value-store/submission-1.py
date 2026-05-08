from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(int)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[timestamp] = [key, value]

    def get(self, key: str, timestamp: int) -> str:
        if self.timemap[key] == 0:
            return ""
        else:
            return self.timemap[key][1]
        

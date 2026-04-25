# filename: find_duplicate.py

def findDuplicate(nums):
    # フェーズ1: サイクル内で出会う
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]           # 1歩
        fast = nums[nums[fast]]     # 2歩
        if slow == fast:
            break

    # フェーズ2: サイクルの入口（= 重複数）を見つける
    slow2 = 0

    while slow != slow2:
        slow  = nums[slow]
        slow2 = nums[slow2]

    return slow


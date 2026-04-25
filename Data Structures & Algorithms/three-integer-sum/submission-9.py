class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = defaultdict(int)
        ans = []
        for num in nums:
            res[num] += 1
        for num1 in res:
            target = 10**6 
            for num2 in res:
                target = 0 - (num1 + num2)
                if target not in res or target in res and res[target] <= 0:
                    continue
                else:
                    if res[num1] > 0:
                        res[num1] -= 1 
                    else:
                        continue
                    if res[num2] > 0:
                        res[num2] -= 1 
                        res[target] -= 1
                    else:
                        continue
                    ans.append([num1, num2, target])
        return ans

                
                    



        
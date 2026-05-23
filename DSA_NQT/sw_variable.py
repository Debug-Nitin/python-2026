from ast import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low , high = 0 , 0
        res = float('inf')
        curr_sum = 0
        while high < len(nums):
            curr_sum += nums[high]
            high += 1
            while curr_sum >= target and low < high:
                res = min(res, high - low)
                curr_sum -= nums[low]
                low +=1
        
        return 0 if res==float('inf') else res
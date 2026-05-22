class Solution:
    def maxSubarraySum(self, arr, k):
        total = sum(arr[:k])
        res = total

        for i in range(k, len(arr)):
            total += arr[i] - arr[i-k]
            res = max(res, total)

        return res
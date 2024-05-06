class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res = 0
        currSum = 0
        pref = {0:1}

        for n in nums:
            currSum += n
            diff = currSum - k

            res += pref.get(diff, 0)
            pref[currSum] = 1 + pref.get(currSum, 0)

        return res
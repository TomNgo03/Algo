class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_elem = max(nums)
        n = len(nums)
        count = 0
        ans = 0
        l = 0

        for r in range(n):
            if nums[r] == max_elem:
                count += 1
            while count >= k:
                if nums[l] == max_elem:
                    count -=1
                l += 1
            
            ans += l
        
        return ans

        # TLE
        # count = 0
        # slow = 0
        # fast = k
        # max_elem = max(nums)

        # while slow < len(nums) and fast <= len(nums):
        #     curr = nums[slow:fast]

        #     if curr.count(max_elem) >= k:
        #         count += 1

        #     fast += 1 
        #     if fast > len(nums):
        #         slow += 1
        #         fast = slow + k
            
        # return counts
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # TLE
        count = 0
        slow = 0
        fast = k
        max_elem = max(nums)

        while slow < len(nums) and fast <= len(nums):
            curr = nums[slow:fast]

            if curr.count(max_elem) >= k:
                count += 1

            fast += 1 
            if fast > len(nums):
                slow += 1
                fast = slow + k
            
        return count
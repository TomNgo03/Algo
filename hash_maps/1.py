def two_sum(self, nums: List[int], target:int) -> List[int]:
    seen = {}
    
    for i, value in enumerate(nums):
        remain = target - nums[i]
        
        if remain in seen:
            return [i, seen[remain]]
        else:
            seen[value] = i
                  
    
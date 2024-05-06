class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        slow = 0
        fast = 1
        currMax = 0

        while slow < len(s) and fast <= len(s):
            curr = s[slow:fast]
            if self.checkNoRepeating(curr):
                currMax = max(len(curr), currMax)
                fast += 1
            else:
                slow += 1
        
        return currMax

    def checkNoRepeating(self, s:str) -> bool:
        return len(list(s)) == len(set(list(s)))
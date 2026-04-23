class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums
        n = len(nums) - 1
        for i in range(len(nums)):
            ans.append(nums[i])
        return ans 
            
        
        
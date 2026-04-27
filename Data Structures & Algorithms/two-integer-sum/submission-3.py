class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums_dict = { number: index for index, number in enumerate(nums)}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    sol_list = [i , j]
                    return sol_list
                
                
                

        
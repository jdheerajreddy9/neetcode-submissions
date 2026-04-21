class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        mem = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                if mem < count:
                    mem = count 
                count = 0
        if count > mem:
            return count
        else:
            return mem
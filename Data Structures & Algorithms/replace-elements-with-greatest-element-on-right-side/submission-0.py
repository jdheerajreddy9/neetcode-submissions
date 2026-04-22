class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        i = 0
        while i < len(arr) - 1: 
            highest = max(arr[i + 1:])
            arr[i] = highest
            i += 1
        arr[i] = -1
        return arr


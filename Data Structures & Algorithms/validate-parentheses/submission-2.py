class Solution:
    def isValid(self, s: str) -> bool:
        values = {"}" : "{", ")" : "(", "]" : "["}
        stack = []
        for i in s:
            if i in values:
                if stack and stack[-1] == values[i]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(i)
        
        if not stack:
            return True
        else: 
            return False
